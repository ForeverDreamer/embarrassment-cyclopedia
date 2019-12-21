from django.urls import path

from .views import (
    SendCodeAPIView,
    CodeRegOrLoginAPIView,
    EmailRegAPIView,
    AccountLoginAPIView,
    ThirdLoginAPIView,
    ThirdBindPhoneAPIView,
    LogoutAPIView,
    ProfileUpdateAPIView,
    ChangePasswordAPIView,
    UserListAPIView,
)

urlpatterns = [
    path('userlist/', UserListAPIView.as_view(), name='userlist'),
    path('sendcode/', SendCodeAPIView.as_view(), name='sendcode'),
    path('coderegorlogin/', CodeRegOrLoginAPIView.as_view(), name='code_regorlogin'),
    path('emailreg/', EmailRegAPIView.as_view(), name='email_reg'),
    path('passwdlogin/', AccountLoginAPIView.as_view(), name='passwd_login'),
    path('thirdlogin/', ThirdLoginAPIView.as_view(), name='third_login'),
    path('thirdbindphone/', ThirdBindPhoneAPIView.as_view(), name='third_bind_phone'),
    path('profileupdate/', ProfileUpdateAPIView.as_view(), name='profileupdate'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('changepassword/', ChangePasswordAPIView.as_view(), name='changepassword'),
]
