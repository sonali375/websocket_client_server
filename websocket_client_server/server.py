import asyncio
import websockets


async def server(websocket, path):
    # Handle incoming messages from the client
    async for user_message in websocket:
        print(f"Received message from client: {user_message}")

        # Send a response back to the client
        response = f"Server received: {user_message}"
        await websocket.send(response)


start_server = websockets.serve(server, 'localhost', 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
