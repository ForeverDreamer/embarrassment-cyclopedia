from django.urls import path

from .views import (
    SendCodeAPIView,
    CodeRegOrLoginAPIView,
)

urlpatterns = [
    path('sendcode/', SendCodeAPIView.as_view(), name='sendcode'),
    # 放在video-detail前面，注意url匹配顺序，否则会把create当slug匹配
    path('CodeRegOrLogin/', CodeRegOrLoginAPIView.as_view(), name='CodeRegOrLogin'),
]
