import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class Book:
    id: int
    title: str
    author: str


books = [
    Book(id=1, title="Clean Code", author="Robert Martin"),
    Book(id=2, title="The Pragmatic Programmer", author="Hunt & Thomas"),
]


@strawberry.type
class Query:
    @strawberry.field
    def books(self) -> list[Book]:
        return books

    @strawberry.field
    def book(self, id: int) -> Book | None:
        return next((b for b in books if b.id == id), None)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str) -> Book:
        new = Book(id=max(b.id for b in books) + 1, title=title, author=author)
        books.append(new)
        return new


schema = strawberry.Schema(query=Query, mutation=Mutation)

app = FastAPI(title="GraphQL Demo")
app.include_router(GraphQLRouter(schema), prefix="/graphql")
