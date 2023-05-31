import asyncio
import websockets
import json


async def chat_client():
    uri = "ws://localhost:5000/ws"
    async with websockets.connect(uri) as websocket:
        # Sending message
        data = {
            "user_id": 4,
            "user_name": "UserTestC",
            "message": "This is a test message from me",
        }
        json_data = json.dumps(data)
        await websocket.send(json_data)

        # Receiving and printing messages
        response = await websocket.recv()
        print(f"{response}")


asyncio.get_event_loop().run_until_complete(chat_client())
