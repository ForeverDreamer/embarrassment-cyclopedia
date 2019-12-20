from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('group/', views.group_chat, name='group-chat'),
    path('private/', views.private_chat, name='private-chat'),
]
