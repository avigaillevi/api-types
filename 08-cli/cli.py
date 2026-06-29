import typer
import requests

app = typer.Typer(help="CLI שעוטף קריאות REST ל-API ציבורי")

BASE = "https://jsonplaceholder.typicode.com"

@app.command()
def get_post(post_id: int):
    """שליפת post לפי מזהה - מתרגם פקודת CLI לקריאת GET."""
    resp = requests.get(f"{BASE}/posts/{post_id}")
    data = resp.json()
    typer.echo(f"Title: {data['title']}")

@app.command()
def list_users():
    """רשימת משתמשים - מתרגם פקודת CLI לקריאת GET."""
    users = requests.get(f"{BASE}/users").json()
    for u in users:
        typer.echo(f"{u['id']}: {u['name']} ({u['email']})")

if __name__ == "__main__":
    app()