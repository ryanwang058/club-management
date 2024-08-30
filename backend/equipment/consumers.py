# equipment/consumers.py

from channels.generic.websocket import AsyncWebsocketConsumer
import json

class EquipmentConsumer(AsyncWebsocketConsumer):
  async def connect(self):
    # Join a group named 'equipment_updates'
    await self.channel_layer.group_add("equipment_updates", self.channel_name)
    await self.accept()

  async def disconnect(self, close_code):
    # Leave the group when the connection is closed
    await self.channel_layer.group_discard("equipment_updates", self.channel_name)

  # Receive message from the group
  async def equipment_update(self, event):
    # Forward the message to the WebSocket client
    await self.send(text_data=json.dumps(event['message']))