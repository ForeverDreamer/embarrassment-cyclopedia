# chat/routing.py
from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    path('ws/chat/group', consumers.GroupChatConsumer, name='group-chat'),
    re_path(r'ws/chat/private/$', consumers.PrivateChatConsumer, name='private-chat'),
]
