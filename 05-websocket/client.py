import asyncio
import websockets

async def main():
    async with websockets.connect("ws://localhost:8003/ws") as ws:
        print("Server:", await ws.recv())          # הודעת קבלת פנים
        for msg in ["hello", "real-time", "bye"]:
            await ws.send(msg)
            print("Server:", await ws.recv())       # echo מהשרת

asyncio.run(main())