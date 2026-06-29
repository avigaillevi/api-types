import requests

# stream=True שומר על החיבור פתוח ומאפשר לקרוא שורה-שורה ככל שמגיעה
with requests.get("http://localhost:8005/stream", stream=True) as resp:
    for line in resp.iter_lines():
        if line:
            print(line.decode())
