from django.urls import path

from .views import (
    CategoryListView,
    CategoryDetailView,
    TopicListView,
    TopicDetailView,
    PostDetailView,
    PostCreateView,
    PostUploadFileView,
    )

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('topic/', TopicListView.as_view(), name='topic-list'),
    path('topic/<str:pk>/', TopicDetailView.as_view(), name='topic-detail'),
    path('post/', TopicListView.as_view(), name='post-list'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/uploadfile/', PostUploadFileView.as_view(), name='post-uploadfile'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post-detail'),

]
