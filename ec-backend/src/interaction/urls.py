from django.urls import path

from .views import (
    LikeAPIView,
    CommentAPIView,
    BlockUserAPIView,
    FollowUserAPIView,
    FriendListAPIView,
    FansListAPIView,
    FollowListAPIView,
    )

urlpatterns = [
    path('like/', LikeAPIView.as_view(), name='like'),
    path('comment/', CommentAPIView.as_view(), name='comment'),
    path('blockuser/', BlockUserAPIView.as_view(), name='blockuser'),
    path('followuser/', FollowUserAPIView.as_view(), name='followuser'),
    path('friends/', FriendListAPIView.as_view(), name='friends'),
    path('fans/', FansListAPIView.as_view(), name='fans'),
    path('follows/', FollowListAPIView.as_view(), name='follows'),
]
