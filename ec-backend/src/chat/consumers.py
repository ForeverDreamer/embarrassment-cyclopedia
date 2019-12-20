# chat/consumers.py
from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json


class ChatConsumer(AsyncJsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        ChatConsumer.groups = [self.room_group_name]

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
