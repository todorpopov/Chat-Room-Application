from django.urls import path, re_path
from . import consumers
from chat_project.settings import hosting_variable

if hosting_variable:
    websocket_urlpatterns = [
        re_path(r'^ws/(?P<room_name>[-\w]+)/$', consumers.ChatConsumer.as_asgi()),
        #path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
    ]
else:
    websocket_urlpatterns = [
        #re_path(r'^ws/(?P<room_name>[-\w]+)/$', consumers.ChatConsumer.as_asgi()),
        path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
    ]