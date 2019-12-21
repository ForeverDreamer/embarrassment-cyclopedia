from django.urls import path

from .views import (
    LikeAPIView,
    CommentAPIView,
    BlockUserAPIView,
    )

urlpatterns = [
    path('like/', LikeAPIView.as_view(), name='like'),
    path('comment/', CommentAPIView.as_view(), name='comment'),
    path('blockuser/', BlockUserAPIView.as_view(), name='blockuser'),
]
