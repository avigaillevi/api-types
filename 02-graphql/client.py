import requests

URL = "http://localhost:8001/graphql"

# query שמבקש רק title - לא מקבלים author ולא id (פתרון over-fetching)
query_titles_only = {"query": "{ books { title } }"}
print("Titles only ->", requests.post(URL, json=query_titles_only).json())

# query שמבקש את כל השדות של ספר ספציפי
query_full = {"query": "{ book(id: 1) { id title author } }"}
print("Full book ->", requests.post(URL, json=query_full).json())

# mutation שמוסיף ספר
mutation = {"query": 'mutation { addBook(title: "Domain-Driven Design", author: "Eric Evans") { id title } }'}
print("Mutation ->", requests.post(URL, json=mutation).json())