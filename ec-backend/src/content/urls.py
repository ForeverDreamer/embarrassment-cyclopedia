from django.urls import path

from .views import (
    CategoryListView,
    CategoryDetailView,
    TopicListView,
    TopicDetailView,
    PostUploadImageView,
    PostUploadVideoView,
    )

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('topic/', TopicListView.as_view(), name='topic-list'),
    path('topic/<str:slug>/', TopicDetailView.as_view(), name='topic-detail'),
    path('post/', TopicListView.as_view(), name='post-list'),
    path('post/uploadimage/', PostUploadImageView.as_view(), name='post-uploadimage'),
    path('post/uploadvideo/', PostUploadVideoView.as_view(), name='post-uploadvideo'),
    path('post/<str:slug>/', TopicDetailView.as_view(), name='post-detail'),

]
