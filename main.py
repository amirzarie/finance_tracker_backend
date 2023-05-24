# run the following code in the terminal to start your app (on default port 8000): uvicorn main:app --reload
# On the web app, navigate to localhost:8000/docs to send requests and test out your paths.

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/")
async def post():
    return {"message": "Hello from the post route"}


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}


fake_items_dv = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get('/items')
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_dv[skip: skip + limit]


@app.get("/item/{item_id}")
async def get_item(item_id: int, q: str = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
