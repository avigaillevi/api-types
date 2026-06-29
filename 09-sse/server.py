import asyncio
from fastapi import FastAPI
from sse_starlette.sse import EventSourceResponse

app = FastAPI(title="SSE Demo")

@app.get("/stream")
async def stream():
    async def event_generator():
        for i in range(1, 6):
            await asyncio.sleep(1)              # מדמה עיבוד מתמשך
            yield {"data": f"עדכון מספר {i}"}
    return EventSourceResponse(event_generator())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8005)