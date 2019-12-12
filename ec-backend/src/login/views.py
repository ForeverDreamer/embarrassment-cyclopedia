import requests

from django.contrib.auth.models import User
from django.core.cache import cache
from django.db.models import Q

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
)
from .models import Profile, ThirdLoginInfo
from .utils import is_phone, get_tokens_for_user
from ec import config
from .permissions import IsLogin
from . import error_code


# 退出登录
class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsLogin]

    def post(self, *args, **kwargs):
        # data = self.request.data
        # print('data', data)
        user = self.request.user
        print('user: ', self.request.user)
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
        qs = ThirdLoginInfo.objects.filter(openid__exact=data.get('openid'))
        if qs.exists():
            third_login_info = qs.first()
            user = third_login_info.owner
            # 用户是否绑定手机
            if not user:
                return Response({"msg": "用户未绑定手机，仅有游客权限!"}, status=status.HTTP_200_OK)
            # 用户是否被禁用
            if not user.is_active:
                return Response({"msg": "用户被禁用!"}, status=status.HTTP_403_FORBIDDEN)
            token = get_tokens_for_user(user)
            return Response({'error_code': '10002', "msg": "账号登录成功", 'data': {'token': token}},
                            status=status.HTTP_200_OK)
        else:
            serializer.save()
            return Response({"msg": "第三方登录成功，请绑定手机号！", 'error_code': '10001'}, status=status.HTTP_201_CREATED)


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
        print('data', data)
        # 检查验证码缓存缓存
        print('cache: [{}]-> {}'.format(mobile_phone, cache.get(mobile_phone)))
        if cache.get(mobile_phone):
            return Response(error_code.VERI_CODE.get('too_often'), status=status.HTTP_400_BAD_REQUEST)
        # 调用短信服务商接口发送验证码给用户
        # print('data: ', data)
        cache.set(mobile_phone, '1314', 300)

        return Response(error_code.VERI_CODE.get('success'), status=status.HTTP_200_OK)


class CodeRegOrLoginAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CodeRegOrLoginSerializer

    def create(self, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            user.profile.logout = False
            user.profile.save()
            return Response({'error_code': '10002', "msg": "手机验证码登录成功"}, status=status.HTTP_200_OK)
        serializer = self.get_serializer(data=self.request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({"msg": "手机号或验证码格式错误!"}, status=status.HTTP_400_BAD_REQUEST)
        data = self.request.data
        print('data', data)
        mobile_phone = data.get('mobile_phone')
        # 缓存检查验证码是否一致
        print('cache: [{}]-> {}'.format(mobile_phone, cache.get(mobile_phone)))
        if cache.get(mobile_phone) != data.get('veri_code'):
            return Response({"msg": "验证码错误", 'error_code': '9999'}, status=status.HTTP_400_BAD_REQUEST)
        qs = User.objects.all().filter(username=mobile_phone)
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
            print(token)
            user.profile.logout = False
            user.profile.save()
            return Response({'error_code': '10002', "msg": "手机验证码登录成功", 'data': {'token': token}},
                            status=status.HTTP_200_OK)
        else:
            user = serializer.save()
            token = get_tokens_for_user(user)
            print(token)
            return Response({'error_code': '10002', "msg": "手机验证码注册成功", 'data': {'token': token}},
                            status=status.HTTP_201_CREATED)


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    #
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


# 验证码注册或登录
# class CodeRegOrLoginAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         print('data', data)
#         mobile_phone = data.get('mobile_phone')
#         # 验证手机号码合法性
#         if not is_phone(mobile_phone):
#             return Response({"msg": "验证码注册或登录， 请输入正确的电话号码！", 'error_code': '9997'}, status=status.HTTP_400_BAD_REQUEST)
#         # 缓存检查验证码是否一致
#         print('cache: [{}]-> {}'.format(mobile_phone, cache.get(mobile_phone)))
#         if cache.get(mobile_phone) != data.get('veri_code'):
#             return Response({"msg": "验证码错误", 'error_code': '9999'}, status=status.HTTP_400_BAD_REQUEST)
#         # gender = data.get('gender')
#         # age = data.get('age')
#         # emotion = data.get('emotion')
#         # birthday = data.get('birthday')
#         # hometown = data.get('hometown')
#         qs = Profile.objects.all().filter(mobile_phone=mobile_phone)
#         if qs.exists():
#             # 用户登录
#             # return Response({"msg": "用户已存在", 'error_code': '10001'}, status=status.HTTP_400_BAD_REQUEST)
#             return Response({"msg": "手机验证码登录成功", 'error_code': '10002'}, status=status.HTTP_200_OK)
#         else:
#             # 创建并关联用户
#             profile = Profile.objects.create(mobile_phone=mobile_phone)
#             user = User.objects.create_user(username='user_' + mobile_phone)
#             # profile[0].owner = user
#             profile.owner = user
#             profile.save()
#             # user = User(username='user_' + mobile_phone)
#             # profile = Profile(mobile_phone=mobile_phone, owner=user)
#             # try:
#             #     profile.full_clean()
#             # except ValidationError as e:
#             #     print(e)
#             #     # Do something when validation is not passing
#             #     return Response({"msg": "数据库写入错误，请输入正确的电话号码！", 'error_code': '9997'},
#             #                     status=status.HTTP_400_BAD_REQUEST)
#             # else:
#             #     # Validation is ok we will save the instance
#             #     profile.save()
#             #     user.save()
#
#             return Response({"msg": "手机验证码注册成功", 'error_code': '10001'}, status=status.HTTP_200_OK)