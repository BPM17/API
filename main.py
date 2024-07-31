from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/")
def root():
    return{"Title: This API is intended to consume movies data, from a DB created in mongoDB"}

@app.post("/items")
def createItem(item: str):
    items.append(item)
    return items

@app.get("/items/{itemId}")
def getItem(itemId : int) -> str:
    print(type(items))
    item = items[itemId]
    return item