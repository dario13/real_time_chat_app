from quart import websocket
from src.services.chat_service import ChatService
from src.domain.entities import Chatroom, Message, User
import json


class WebSocketAdapter:
    def __init__(self, chat_service: ChatService):
        self._chat_service = chat_service

    async def receive_message(self):
        while True:
            json_data = await websocket.receive()
            data = json.loads(json_data)

            # Extract the username and message from the JSON data
            user_id = data.get("user_id")
            username = data.get("user_name")
            message_content = data.get("message")

            if username and message_content:
                user = User(user_id, username)
                message = Message(user, message_content)
                chatroom = Chatroom(1, "General")
                self._chat_service.send_message(chatroom, message)
                # Send a confirmation response
                response_data = {"message": "Message received successfully"}
                await websocket.send(json.dumps(response_data))

            else:
                # If the JSON data is invalid, return an error response
                response_data = {"error": "Invalid JSON payload"}
                await websocket.send(json.dumps(response_data))
