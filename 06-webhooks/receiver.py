from fastapi import FastAPI, Request
import hmac, hashlib

app = FastAPI(title="Webhook Receiver")
SECRET = b"my-shared-secret"

@app.post("/webhook")
async def receive_webhook(request: Request):
    body = await request.body()
    signature = request.headers.get("X-Signature", "")

    # אימות חתימה - מוודא שהאירוע באמת הגיע מהמקור הצפוי
    expected = hmac.new(SECRET, body, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, signature):
        return {"status": "rejected", "reason": "invalid signature"}

    event = await request.json()
    print(f"Received event: {event['type']} -> {event['data']}")
    return {"status": "received"}