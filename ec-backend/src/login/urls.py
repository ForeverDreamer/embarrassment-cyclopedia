from django.urls import path

from .views import (
    SendCodeAPIView,
    CodeRegOrLoginAPIView,
    EmailRegAPIView,
    AccountLoginAPIView,
    ThirdLoginAPIView,
    ThirdBindPhoneAPIView,
    LogoutAPIView,
)

urlpatterns = [
    path('sendcode/', SendCodeAPIView.as_view(), name='sendcode'),
    path('coderegorlogin/', CodeRegOrLoginAPIView.as_view(), name='code_regorlogin'),
    path('emailreg/', EmailRegAPIView.as_view(), name='email_reg'),
    path('accountlogin/', AccountLoginAPIView.as_view(), name='account_login'),
    path('thirdlogin/', ThirdLoginAPIView.as_view(), name='third_login'),
    path('thirdbindphone/', ThirdBindPhoneAPIView.as_view(), name='third_bind_phone'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]
