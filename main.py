# Imports
from fastapi import FastAPI

from apiDb import ApiDb
from Car import Car

#Objects and Variables
app = FastAPI()
items = []
cars = []
db = ApiDb()

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
    db.dict = car
    db.ProcessToTable()
    return "The Car has been added correctly"

# This request should response all the objects stored in the DB
@app.get("/Car")
async def GetCars():
    data = db.GetTable()
    return data

# This request is to get a car with an specific Id
@app.get("/Car/{carId}")
def GetCar(carId:str):
    data = db.GetItem(carId)
    return data