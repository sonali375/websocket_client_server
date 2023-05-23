import asyncio
import websockets


async def client():
    async with websockets.connect('ws://localhost:8000') as websocket:
        user_message = input("enter a message:- ")
        await websocket.send(user_message)
        print(f"Sent message to server: {user_message}")

        # Receive and print the response from the server
        response = await websocket.recv()
        print(f"Received response from server: {response}")

asyncio.get_event_loop().run_until_complete(client())

