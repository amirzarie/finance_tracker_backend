from fastapi import FastAPI

app = FastAPI()

users = []


@app.get("/users")
async def root():
    return users


@app.post("/users")
async def create_user(user):
    users.append(user)
    return "Success"
