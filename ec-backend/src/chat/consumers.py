from urllib.parse import parse_qs

from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib.auth.models import User

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async

from .models import PrivateChat, PrivateChatMsg, GroupChat, GroupChatMsg, ChannelName


class GroupChatConsumer(AsyncJsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        self.group_name = 'chat_%s' % self.group_name
        GroupChatConsumer.groups = [self.group_name]

    async def connect(self):
        if not self.scope['user'].is_authenticated:
            await super().close()
            print('未授权用户，禁止进入房间')
            return
        await super().connect()
        print(self.scope['user'].username + ' 进入房间')

    async def disconnect(self, close_code):
        print('连接断开 ' + str(close_code))

    # Receive message from WebSocket
    async def receive_json(self, json_data):
        message = json_data['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send_json({'message': message})

    # @database_sync_to_async
    # def get_name(self):
    #     return User.objects.all()[0].name


class PrivateChatConsumer(AsyncJsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = self.scope['user']
        self.other_user_id = parse_qs(self.scope["query_string"].decode("utf8"))["other_user"][0]

    async def connect(self):
        if not self.scope['user'].is_authenticated:
            print('未授权用户，禁止发送消息')
            await super().close()
            return
        try:
            self.chat, created = await self.get_or_new_chat()
            await self.save_channel_name()
        except (ValidationError, ObjectDoesNotExist) as e:
            # await self.send_json({'message': str(e)})
            # log记录日志
            print(e)
        await super().connect()
        # print(self.scope['user'].username + ' 进入房间')

    async def disconnect(self, close_code):
        print('连接断开 ' + str(close_code))
        await self.delete_channel_name()

    # Receive message from WebSocket
    async def receive_json(self, json_data):
        message = json_data['message']
        await self.save_msg(self.chat, self.user, message)
        # Send message to other_user
        try:
            channel_name = await self.other_user_channel_name()
            await self.channel_layer.send(channel_name, {
                "type": "chat.message",
                "message": message,
            })
            # 同一个用户多端登录应该需要加入group, 使用group_send发送消息
            # channel_name_list = await self.other_user_channel_name()
            # for item in channel_name_list:
            #     await self.channel_layer.send(item.channel_name, {
            #         "type": "chat.message",
            #         "message": message,
            #     })
        except ObjectDoesNotExist as e:
            await self.send_json({'message': str(e)})

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send_json({'message': message})

    @database_sync_to_async
    def get_or_new_chat(self):
        return PrivateChat.objects.get_or_new(self.user, self.other_user_id)

    @database_sync_to_async
    def save_channel_name(self):
        ChannelName.objects.create(user=self.user, channel_name=self.channel_name)
        print('用户' + self.user.username + '上线, 创建channel_name: ' + self.channel_name)
        # qs = ChannelName.objects.filter(user=self.user)
        # if not qs.exists():
        #     ChannelName.objects.create(user=self.user, channel_name=self.channel_name)
        #     print('用户' + self.user.username + '上线, 创建channel_name: ' + self.channel_name)

    @database_sync_to_async
    def delete_channel_name(self):
        ChannelName.objects.filter(channel_name=self.channel_name).delete()
        print('用户离线删除channel_name')

    @database_sync_to_async
    def save_msg(self, chat, sender, msg):
        PrivateChatMsg.objects.create(chat=chat, sender=sender, msg=msg)
        print('保存私聊消息')

    @database_sync_to_async
    def other_user_channel_name(self):
        qs = User.objects.filter(id=self.other_user_id)
        if not qs.exists():
            raise ObjectDoesNotExist('用户不存在')
        qs = ChannelName.objects.filter(user=qs.first())
        if not qs.exists():
            raise ObjectDoesNotExist('用户不在线')
        return qs.first().channel_name
        # channel_name_list = []
        # for channel_name in qs:
        #     channel_name_list.append(channel_name)
        # return channel_name_list
