# Imports
from fastapi import FastAPI

from apiDb import ApiDb
from Car import Car
from User import User

#Objects and Variables
app = FastAPI()
items = []
users = []
cars = []
db = ApiDb()

@app.get("/")
def root():
    return{"Title: This API is intended to consume vehicle data, from a DB created in from SQLite3"}

@app.put("/User/{User}")
async def PutUser(user : User):
    users.append({"User" : user})
    db.dict = dict(user)
    db.ProcessToUserTable()
    return "The User has been added correctly"

@app.get("/Users")
async def GetUsers():
    data = db.GetTable(1)
    return data

# Car is the object created from Car.py it used BaseModel to be created
@app.put("/Car/{Car}")
async def PostCar(car : Car):
    cars.append({"Car" : car})
    db.dict = dict(car)
    db.ProcessToCarTable()
    return "The Car has been added correctly"

# This request should response all the objects stored in the DB
@app.get("/Car")
async def GetCars():
    data = db.GetTable(0)
    return data

# This request is to get a car with an specific Id
@app.get("/Car/{carId}")
def GetCar(carId:str):
    data = db.GetItem(carId)
    return data