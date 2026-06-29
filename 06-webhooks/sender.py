import hashlib
import hmac
import json

import requests

SECRET = b"my-shared-secret"
event = {"type": "payment.succeeded", "data": {"amount": 250, "currency": "ILS"}}

# הצד השולח חותם על ה-payload לפני השליחה
body = json.dumps(event).encode()
signature = hmac.new(SECRET, body, hashlib.sha256).hexdigest()

resp = requests.post(
    "http://localhost:8004/webhook",
    data=body,
    headers={"Content-Type": "application/json", "X-Signature": signature},
)
print("Receiver responded:", resp.json())
