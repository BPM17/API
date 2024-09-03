import sqlite3
import json
from typing import List

class ApiDb ():
    def __init__(self):
        self.apiDb = "ApiDb.db"
        try:
            self.conn = sqlite3.connect(self.apiDb, check_same_thread=False)
            print("connection stablished")
        except:
            print("something went wrong")
        self.cursor = self.conn.cursor()
        self.dict = {}
        self.table = ""

    def CreateDB(self):
        try:
            print(f"API DB is already created as {self.apiDb}")
        except:
            print(f"Something went wrong")

    def CreateTable(self):
        self.cursor.execute(self.table)
        print("The table has been created correctly")

    def GetTable(self, int):
        if int == 0:
            self.cursor.execute("""SELECT * FROM Cars""")
            data = self.cursor.fetchall()
        elif int == 1:
            self.cursor.execute("""SELECT * FROM Users""")
            data = self.cursor.fetchall()    
        return data
    
    def GetItem(self, carId):
        print("Hola mundo ", type(carId))
        self.cursor.execute("""SELECT *
                                FROM Cars
                                WHERE id = {}""".format(carId))
        data = self.cursor.fetchall()
        print(data)
        return data

    def AddToTable(self):
        try:
            self.cursor.execute(self.instruction, self.fields)
            print("Data have been added correctly")
            self.conn.commit()
        except Exception as e:
            print("There is an error {}".format(e))

    def SeeRow(self):
        data = self.cursor.execute('''SELECT * FROM Cars''')
        for row in data:
            print(row)

    def SetInstructionAndFieldsCar(self):
        self.instruction = '''INSERT INTO CARS(Brand, Model, Color, Year) VALUES(?,?,?,?)'''
        self.fields = (self.dict["brand"], self.dict["model"], self.dict["color"], int(self.dict["year"]))

    def SetInstructionAndFieldsUser(self):
        self.instruction = '''INSERT INTO USERS(Name, LastName, Position) VALUES(?,?,?)'''
        self.fields = (self.dict["name"], self.dict["lastName"], self.dict["position"])

    def ProcessToCarTable(self):
        self.SetInstructionAndFieldsCar()
        self.AddToTable()

    def ProcessToUserTable(self):
        self.SetInstructionAndFieldsUser()
        self.AddToTable()
    
        

if __name__ == "__main__":
    db = ApiDb()
    # Create CarTable
    db.table = """ CREATE TABLE IF NOT EXISTS CARS(
        id INTEGER PRIMARY KEY,
        Brand VARCHAR(255) NOT NULL,
        Model VARCHAR(255) NOT NULL,
        Color VARCHAR(255) NOT NULL,
        Year INTEGER NOT NULL,
        Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    ) """
    # Create UserTable
    # db.table = """CREATE TABLE IF NOT EXISTS USERS(
    #     id INTEGER PRIMARY KEY,
    #     Name VARCHAR(100) NOT NULL,
    #     LastName VARCHAR(100) NOT NULL,
    #     Position VARCHAR(100) NOT NULL,
    #     Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    # )"""
    db.CreateTable()
    # db.GetItem("2")