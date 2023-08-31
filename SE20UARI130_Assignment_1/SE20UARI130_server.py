import websockets
import asyncio

print("Server listening on port " + str(2003))
async def hello(websocket):
    while True:
        name = await websocket.recv()
        print(f"Server received: {name}")
        greeting = f"Hello {name}"
        await websocket.send(greeting)
        print(f"Server sent: {greeting}")
        print("-"*30)
        await asyncio.sleep(3)

async def main():
    async with websockets.serve(hello, "64.227.144.150", 2003):
        await asyncio.Future()

if __name__=="__main__":
    asyncio.run(main())