from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI(title="WebSocket Demo")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("מחובר לשרת. כל הודעה שתישלח תחזור כ-echo.")
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"השרת קיבל: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")