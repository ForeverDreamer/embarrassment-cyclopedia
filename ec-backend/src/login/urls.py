from django.urls import path

from .views import (
    SendCodeAPIView,
    CodeRegOrLoginAPIView,
    EmailRegOrLoginAPIView,
    ThirdRegOrLoginAPIView,
    LogoutAPIView,
)

urlpatterns = [
    path('sendcode/', SendCodeAPIView.as_view(), name='sendcode'),
    path('coderegorlogin/', CodeRegOrLoginAPIView.as_view(), name='code'),
    path('emailregorLogin/', EmailRegOrLoginAPIView.as_view(), name='email'),
    path('thirdparty/', ThirdRegOrLoginAPIView.as_view(), name='third'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]
