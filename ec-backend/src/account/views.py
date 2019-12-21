import requests

from django.contrib.auth.models import User
from django.core.cache import cache
from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    UserSerializer,
    ProfileSerializer,
    CodeRegOrLoginSerializer,
    EmailRegSerializer,
    AccountLoginSerializer,
    ThirdLoginSerializer,
    ThirdBindPhoneSerializer,
    ChangePasswordSerializer,
)
from .models import Profile, ThirdLoginInfo
from .utils import is_phone, get_tokens_for_user
from ec import config
from ec.permissions import IsBindPhone, IsOwnerOrReadOnly
from . import error_code


# 通过手机验证码修改密码
class ChangePasswordAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsBindPhone]

    def post(self, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=self.request.data)
        if not serializer.is_valid(raise_exception=False):
            # print(serializer.errors)
            return Response({'error_code': '3000', "msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        user = self.request.user
        data = serializer.validated_data
        mobile_phone = user.username
        # 缓存检查验证码是否一致
        if cache.get(mobile_phone) != data.get('veri_code'):
            return Response({"msg": "验证码错误", 'error_code': '9999'}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(data.get('password'))
        user.save()
        return Response({'error_code': '10002', "msg": "密码重置成功"}, status=status.HTTP_200_OK)


# 退出登录
class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsBindPhone]

    def post(self, *args, **kwargs):
        # data = self.request.data
        # print('data', data)
        user = self.request.user
        # print('user: ', self.request.user)
        # if user.username == config.TEMP_USER_INFO.get('username'):
        #     return Response({"msg": "未绑定手机用户，前端处理登出就行！"}, status=status.HTTP_200_OK)
        user.profile.logout = True
        user.profile.save()
        # logout_type = data.get('logout_type')
        # if logout_type == config.LOGOUT_TYPE.get('phone_or_email'):
        #     user.profile.logout = True
        #     user.save()
        # elif logout_type == config.LOGOUT_TYPE.get('third'):
        #     user.third.logout = True
        #     user.save()
        # else:
        #     return Response({"msg": "参数错误！"}, status=status.HTTP_400_BAD_REQUEST)

        # data = {'username': user.username, 'password': user.password}
        # 刷新token，让原token失效
        # requests.post(config.BASE_URL + '/api/auth/token/', data=data)
        # token = get_tokens_for_user(self.request.user)
        # print(token)

        return Response({"msg": "退出登录成功！"}, status=status.HTTP_200_OK)


# 第三方登录
class ThirdLoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, *args, **kwargs):
        serializer = ThirdLoginSerializer(data=self.request.data)
        if not serializer.is_valid(raise_exception=False):
            # print(serializer.errors)
            return Response({'error_code': '3000', "msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        data = self.request.data
        # 先要向第三方官方发送请求，验证openid的有效性
        # 第三方信息是否已存在
        qs = ThirdLoginInfo.objects.filter(openid__exact=data.get('openid'))
        if qs.exists():
            third_login_info = qs.first()
            user = third_login_info.owner
            # # 用户是否绑定手机
            # if not user:
            #     return Response({"msg": "用户未绑定手机，仅有游客权限!"}, status=status.HTTP_200_OK)
            # 用户是否被禁用
            if not user.is_active:
                return Response({"msg": "用户被禁用!"}, status=status.HTTP_403_FORBIDDEN)
            token = get_tokens_for_user(user)
            return Response({'error_code': '10002', "msg": "第三方登录成功", 'data': {'token': token}},
                            status=status.HTTP_200_OK)
        else:
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'error_code': '10002', "msg": "第三方登录创建成功", 'data': {'token': token}},
                            status=status.HTTP_201_CREATED)


# 第三方登录绑定手机号
class ThirdBindPhoneAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, *args, **kwargs):
        serializer = ThirdBindPhoneSerializer(data=self.request.data)
        if not serializer.is_valid(raise_exception=False):
            # print(serializer.errors)
            return Response({'error_code': '3000', "msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        data = self.request.data
        mobile_phone = data.get('mobile_phone')
        # 缓存检查验证码是否一致
        print('cache: [{}]-> {}'.format(mobile_phone, cache.get(mobile_phone)))
        if cache.get(mobile_phone) != data.get('veri_code'):
            return Response({"msg": "验证码错误", 'error_code': '9999'}, status=status.HTTP_400_BAD_REQUEST)
        # 第三方登录信息是否存在
        third_qs = ThirdLoginInfo.objects.filter(openid__exact=data.get('openid'))
        if not third_qs.exists():
            return Response({'error_code': '3000', "msg": '第三方信息不存在'}, status=status.HTTP_400_BAD_REQUEST)
        third_login_info = third_qs.first()
        # 用户是否已存在
        user_qs = User.objects.filter(username__exact=mobile_phone)
        if user_qs.exists():
            user = user_qs.first()
            # 用户是否被禁用
            if not user.is_active:
                return Response({"msg": "用户被禁用!"}, status=status.HTTP_403_FORBIDDEN)
            # 该手机是否已绑定第三方信息
            # 绑定第三方信息
            third_login_info.owner = user
            third_login_info.save()
            token = get_tokens_for_user(user)
            return Response({'error_code': '10002', "msg": "手机号绑定成功", 'data': {'token': token}},
                            status=status.HTTP_200_OK)
        else:
            # 创建用户
            user = User.objects.create_user(username=mobile_phone, password=config.DEFALT_PASSWORD)
            # 创建用户信息
            Profile.objects.create(owner=user, mobile_phone=mobile_phone)
            # 绑定第三方信息
            third_login_info.owner = user
            third_login_info.save()
            return Response({"msg": "创建并绑定成功！", 'error_code': '10001'}, status=status.HTTP_201_CREATED)


# 邮箱注册
class EmailRegAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = EmailRegSerializer

    def create(self, request, *args, **kwargs):
        # user = self.request.user
        # if user.is_authenticated:
        #     user.profile.logout = False
        #     user.profile.save()
        #     return Response({'error_code': '10002', "msg": "邮箱登录成功"}, status=status.HTTP_200_OK)
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            print(serializer.errors)
            return Response({"msg": "用户名或密码格式错误!"}, status=status.HTTP_400_BAD_REQUEST)

        data = self.request.data
        print('data', data)
        email = data.get('email')
        password = data.get('password')
        qs = User.objects.all().filter(email=email)
        if qs.exists():
            user = qs.first()
            # 用户是否被禁用
            if not user.is_active:
                print('用户被禁用!')
                return Response({"msg": "用户被禁用!"}, status=status.HTTP_403_FORBIDDEN)
            # 比对密码，用户登录操作
            if not user.check_password(password):
                print('用户名或密码错误!')
                return Response({"msg": "用户名或密码错误", 'error_code': '10002'}, status=status.HTTP_400_BAD_REQUEST)
            # 创建token返回给客户端
            # headers = {'Content-Type': 'application/json'}
            # data = {'username': user.username, 'password': password}
            # # token = requests.post(config.BASE_URL+'/api/auth/token/', headers=headers, data=data)
            # token = requests.post(config.BASE_URL + '/api/auth/token/', data=data).json()
            token = get_tokens_for_user()
            print(token)
            return Response({'error_code': '10002', "msg": "邮箱登录成功", 'data': {'token': token}}, status=status.HTTP_200_OK)
        else:
            # 发送验证邮件
            # serializer.save()
            return Response({"msg": "验证邮件已发送，请登录邮箱点击验证链接！", 'error_code': '10001'}, status=status.HTTP_200_OK)


# 账号登录(手机/邮箱)
class AccountLoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, *args, **kwargs):
        serializer = AccountLoginSerializer(data=self.request.data)
        if not serializer.is_valid(raise_exception=False):
            # print(serializer.errors)
            return Response({"msg": "用户名或密码格式错误!"}, status=status.HTTP_400_BAD_REQUEST)
        data = self.request.data
        if data.get('mobile_phone'):
            qs = User.objects.filter(username__exact=data.get('mobile_phone'))
        else:
            qs = User.objects.filter(email__exact=data.get('email'))
        if qs.exists():
            user = qs.first()
            # 用户是否被禁用
            if not user.is_active:
                return Response({"msg": "用户被禁用!"}, status=status.HTTP_403_FORBIDDEN)
            # 比对密码，用户登录操作
            password = data.get('password')
            if password == config.DEFALT_PASSWORD:
                return Response({"msg": "用户名或密码错误", 'error_code': '10001'}, status=status.HTTP_400_BAD_REQUEST)
            if not user.check_password(password):
                return Response({"msg": "用户名或密码错误", 'error_code': '10002'}, status=status.HTTP_400_BAD_REQUEST)
            # 创建token返回给客户端
            # headers = {'Content-Type': 'application/json'}
            # data = {'username': user.username, 'password': password}
            # # token = requests.post(config.BASE_URL+'/api/auth/token/', headers=headers, data=data)
            # token = requests.post(config.BASE_URL + '/api/auth/token/', data=data).json()
            token = get_tokens_for_user(user)
            return Response({'error_code': '10002', "msg": "账号登录成功", 'data': {'token': token}},
                            status=status.HTTP_200_OK)
        else:
            return Response({"msg": "用户不存在，请先注册！", 'error_code': '10001'}, status=status.HTTP_200_OK)


# 发送验证码
class SendCodeAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, *args, **kwargs):
        data = self.request.data
        mobile_phone = data.get('mobile_phone')
        # 验证手机号码格式
        if not is_phone(mobile_phone):
            return Response(error_code.VERI_CODE.get('phone_format'), status=status.HTTP_400_BAD_REQUEST)
        # print('data', data)
        # # 检查验证码缓存缓存
        # print('cache: [{}]-> {}'.format(mobile_phone, cache.get(mobile_phone)))
        if cache.get(mobile_phone):
            return Response(error_code.VERI_CODE.get('too_often'), status=status.HTTP_400_BAD_REQUEST)
        # 调用短信服务商接口发送验证码给用户
        # print('data: ', data)
        cache.set(mobile_phone, '131452', 300)

        return Response(error_code.VERI_CODE.get('success'), status=status.HTTP_200_OK)


class CodeRegOrLoginAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CodeRegOrLoginSerializer

    def create(self, *args, **kwargs):
        # user = self.request.user
        # if user.is_authenticated:
        #     user.profile.logout = False
        #     user.profile.save()
        #     return Response({'error_code': '10002', "msg": "手机验证码登录成功"}, status=status.HTTP_200_OK)
        serializer = self.get_serializer(data=self.request.data)
        if not serializer.is_valid():
            # print(serializer.errors)
            return Response({"msg": "手机号或验证码格式错误!"}, status=status.HTTP_400_BAD_REQUEST)
        data = serializer.validated_data
        # print('data', data)
        mobile_phone = data.get('mobile_phone')
        # 缓存检查验证码是否一致
        # print('cache: [{}]-> {}'.format(mobile_phone, cache.get(mobile_phone)))
        if cache.get(mobile_phone) != data.get('veri_code'):
            return Response({"msg": "验证码错误", 'error_code': '9999'}, status=status.HTTP_400_BAD_REQUEST)
        qs = User.objects.filter(username=mobile_phone)
        if qs.exists():
            user = qs.first()
            # 用户是否被禁用
            if not user.is_active:
                return Response({"msg": "用户被禁用!"}, status=status.HTTP_403_FORBIDDEN)
            # 创建token返回给客户端
            # data = {'username': user.username, 'password': config.DEFALT_PASSWORD}
            # print('data', data)
            # token = requests.post(config.BASE_URL + '/api/auth/token/', data=data).json()
            token = get_tokens_for_user(user)
            # print(token)
            user.profile.logout = False
            user.profile.save()
            return Response({'error_code': '10002', "msg": "手机验证码登录成功", 'data': {'token': token}},
                            status=status.HTTP_200_OK)
        else:
            user = serializer.save()
            token = get_tokens_for_user(user)
            # print(token)
            return Response({'error_code': '10002', "msg": "手机验证码注册成功", 'data': {'token': token}},
                            status=status.HTTP_201_CREATED)


class ProfileUpdateAPIView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsBindPhone, IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer

    # For partial update - PATCH http method
    # For full update - PUT http method

    def get_object(self):
        qs = self.get_queryset()
        user = self.request.user

        obj = get_object_or_404(qs, owner=user)
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_update(self, serializer):
        serializer.save()
        # serializer.data.update(dict({'msg': '资料更新成功', 'data': dict(serializer.data)}))
        # serializer.data['item'] = 'test'


class UserListAPIView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
