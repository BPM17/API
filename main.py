from fastapi import FastAPI

from apiDb import ApiDb
from Car import Car

app = FastAPI()

items = []
cars = []

@app.get("/")
def root():
    return{"Title: This API is intended to consume movies data, from a DB created in mongoDB{}".format(items)}

@app.post("/items")
def createItem(item: str):
    items.append(item)
    return items

@app.get("/items/{itemId}")
def getItem(itemId : int) -> str:
    try:
        item = items[itemId]
        return item
    except Exception as e:
        print(e.msg)

@app.get("/getItems")
def getItems():
    print("The items are{}".format(items))
    return items

# Car is the object created from Car.py it used BaseModel to be created
@app.put("/Car/{Car}")
async def PostCar(car : Car):
    cars.append({"Car" : car})
    db = ApiDb()
    db.dict = car
    db.ProcessToTable()
    return cars