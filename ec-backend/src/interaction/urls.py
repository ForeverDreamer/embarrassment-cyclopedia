from django.urls import path

from .views import (
    LikeAPIView,
    CommentAPIView,
    )

urlpatterns = [
    path('like/', LikeAPIView.as_view(), name='like'),
    path('comment/', CommentAPIView.as_view(), name='comment'),
]
