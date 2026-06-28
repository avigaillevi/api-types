import requests

BASE = "http://localhost:8000"

# GET כל הספרים
print("GET /books ->", requests.get(f"{BASE}/books").json())

# POST ספר חדש
created = requests.post(f"{BASE}/books", json={"title": "Refactoring", "author": "Martin Fowler"})
print("POST /books ->", created.status_code, created.json())
new_id = created.json()["id"]

# GET ספר בודד
print(f"GET /books/{new_id} ->", requests.get(f"{BASE}/books/{new_id}").json())

# PUT עדכון
updated = requests.put(f"{BASE}/books/{new_id}", json={"title": "Refactoring 2nd Ed", "author": "Martin Fowler"})
print(f"PUT /books/{new_id} ->", updated.json())

# DELETE
deleted = requests.delete(f"{BASE}/books/{new_id}")
print(f"DELETE /books/{new_id} -> status", deleted.status_code)