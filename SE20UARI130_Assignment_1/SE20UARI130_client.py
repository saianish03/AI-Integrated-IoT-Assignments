import websockets
import asyncio

async def hello():
    url = "ws://64.227.144.150:2003"
    async with websockets.connect(url) as websocket:
        while True:
            name = input("Enter your name: ")
            await websocket.send(name)
            print(f"Client sent: {name}")

            greeting = await websocket.recv()
            print(f"Client recieved : {greeting}")
            print("-"*30)
            await asyncio.sleep(3)

if __name__=="__main__":
    asyncio.run(hello())