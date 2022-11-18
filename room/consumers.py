import json
from datetime import datetime as dt

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from django.contrib.auth.models import User
from .models import Message, Room

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
            )

        await self.accept()

        await self.increment_users_online(self.room_name)

    async def disconnect(self, text):
        
        await self.channel_layer.group_discard(
            self.room_group_name, 
            self.channel_name
            )

        await self.decrement_users_online(self.room_name)
    
    async def receive(self, text_data):
        data = json.loads(text_data)

        message = data["message"]
        username = data["username"]
        room = data["room"]

        await self.save_message(username, room, message)

        await self.channel_layer.group_send(
            self.room_group_name, 
            {
                "type": "chat_message",
                "message": message,
                "username": username,
                "room": room,
                "date": dt.now().strftime("%d-%b-%Y %I.%M %p")
            }
        )
    
    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        room = event["room"]

        await self.send(text_data=json.dumps({
            "message": message,
            "username": username,
            "room": room,
            "date": dt.now().strftime("%d-%b-%Y %I.%M %p"),
        }))

    @sync_to_async
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)

        Message.objects.create(user = user, room = room, content = message, 
                            date = dt.now().strftime("%d-%b-%Y %I.%M %p"))

    @sync_to_async
    def increment_users_online(self, slug):
        room = Room.objects.get(slug=slug)
        room.users_online += 1
        room.save()

    @sync_to_async
    def decrement_users_online(self, slug):
        room = Room.objects.get(slug=slug)
        room.users_online -= 1
        room.save()
