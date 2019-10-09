from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.exceptions import ValidationError

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status


from .serializers import UserSerializer, ProfileSerializer, UserCodeLoginSerializer
from .models import Profile
from .utils import is_phone


# 发送验证码
class SendCodeAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, *args, **kwargs):
        data = self.request.data
        mobile_phone = data.get('mobile_phone')
        # 验证手机号码合法性
        if not is_phone(mobile_phone):
            return Response({"msg": "发送验证码， 请输入正确的电话号码！", 'error_code': '9997'}, status=status.HTTP_400_BAD_REQUEST)
        print('data', data)
        # 检查验证码缓存缓存
        print('cache: [{}]-> {}'.format(mobile_phone, cache.get(mobile_phone)))
        if cache.get(mobile_phone):
            return Response({"msg": "您操作太频繁，请稍后再试！", 'error_code': '9999'}, status=status.HTTP_400_BAD_REQUEST)
        # 调用短信服务商接口发送验证码给用户
        # print('data: ', data)
        cache.set(mobile_phone, '1314', 10)

        return Response({"msg": "发送成功", 'error_code': '10000'}, status=status.HTTP_200_OK)


# 验证码注册或登录
class CodeRegOrLoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, *args, **kwargs):
        data = self.request.data
        print('data', data)
        mobile_phone = data.get('mobile_phone')
        # 验证手机号码合法性
        if not is_phone(mobile_phone):
            return Response({"msg": "验证码注册或登录， 请输入正确的电话号码！", 'error_code': '9997'}, status=status.HTTP_400_BAD_REQUEST)
        # 缓存检查验证码是否一致
        print('cache: [{}]-> {}'.format(mobile_phone, cache.get(mobile_phone)))
        if cache.get(mobile_phone) != data.get('veri_code'):
            return Response({"msg": "验证码错误", 'error_code': '9999'}, status=status.HTTP_400_BAD_REQUEST)
        # gender = data.get('gender')
        # age = data.get('age')
        # emotion = data.get('emotion')
        # birthday = data.get('birthday')
        # hometown = data.get('hometown')
        qs = Profile.objects.all().filter(mobile_phone=mobile_phone)
        if qs.exists():
            # 用户登录
            # return Response({"msg": "用户已存在", 'error_code': '10001'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"msg": "登录成功", 'error_code': '10002'}, status=status.HTTP_200_OK)
        else:
            # 创建并关联用户
            profile = Profile.objects.create(mobile_phone=mobile_phone)
            user = User.objects.create_user(username='user_' + mobile_phone)
            # profile[0].owner = user
            profile.owner = user
            profile.save()
            # user = User(username='user_' + mobile_phone)
            # profile = Profile(mobile_phone=mobile_phone, owner=user)
            # try:
            #     profile.full_clean()
            # except ValidationError as e:
            #     print(e)
            #     # Do something when validation is not passing
            #     return Response({"msg": "数据库写入错误，请输入正确的电话号码！", 'error_code': '9997'},
            #                     status=status.HTTP_400_BAD_REQUEST)
            # else:
            #     # Validation is ok we will save the instance
            #     profile.save()
            #     user.save()

            return Response({"msg": "注册成功", 'error_code': '10001'}, status=status.HTTP_200_OK)


# 验证码注册或登录
# class CodeRegOrLoginAPIView(generics.CreateAPIView):
#     permission_classes = [permissions.AllowAny]
#     serializer_class = UserCodeLoginSerializer
#
#     def perform_create(self, serializer):
#         # 缓存检查验证码是否一致
#         data = self.request.data
#         veri_code = data.get('veri_code')
#         if True:
#             mobile_phone = data.get('mobile_phone')
#             qs = Profile.objects.all().filter(mobile_phone=mobile_phone)
#             if qs.exists():
#                 # 用户登录
#                 return Response({"msg": "登录成功", 'error_code': '10002'}, status=status.HTTP_200_OK)
#             else:
#                 serializer.save()
#                 return Response({"msg": "注册成功", 'error_code': '10001'}, status=status.HTTP_200_OK)


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
