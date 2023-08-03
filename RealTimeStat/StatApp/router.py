from django.urls import path
from .consumer import RealTimeConsumer

ws_urlpatterns = [
    path('ws/realtime/', RealTimeConsumer.as_asgi()),
]