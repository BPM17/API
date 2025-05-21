import sqlite3
import json
import os.path
import time
from typing import List
from generateToken import Token
from timeit import default_timer as timer

class ApiDb ():
    def __init__(self):
        self.apiDb = "ApiDb.db"
        try:
            self.conn = sqlite3.connect(self.apiDb, check_same_thread=False)
            print("Connection stablished")
        except:
            print("Something went wrong")
        self.cursor = self.conn.cursor()
        self.dict = {}
        self.table = []
        self.token = Token()
        self.init = float
        self.CheckDB()
        

    def CheckDB(self):
        try:
            if os.path.isfile("ApiDb.db"):
                print("The file exist")
                try:
                    self.GetTable(0)
                except Exception as e:
                    self.RunTableLines()
                    print("The tables do not exist in the DB")
                    print(f'caught{type(e)}: e{e}')
        except Exception as e:
            print("File not found")
            print(f'caught{type(e)}: e{e}')
            self.CreeateDB()

    def RunTableLines(self):
        print("Creating table lines")
        # Create CarTable
        self.table.append(""" CREATE TABLE IF NOT EXISTS CARS(
            id INTEGER PRIMARY KEY,
            Brand VARCHAR(255) NOT NULL,
            Model VARCHAR(255) NOT NULL,
            Color VARCHAR(255) NOT NULL,
            Year INTEGER NOT NULL,
            Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        ) """)
        # Create UserTable
        self.table.append("""CREATE TABLE IF NOT EXISTS USERS(
            id INTEGER PRIMARY KEY,
            Name VARCHAR(100) NOT NULL,
            LastName VARCHAR(100) NOT NULL,
            Email VARCHAR(100) NOT NULL,
            Password VARCHAR(100) NOT NULL,
            Position VARCHAR(100) NOT NULL,
            Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )""")
        # Create ChangesTable
        self.table.append(""" CREATE TABLE IF NOT EXISTS CHANGES(
            id INTEGER PRIMARY KEY,
            userId INTEGER,
            carId INTEGER,
            Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        ) """)
        self.CreateTable()
        # db.GetItem("2")

    def CreeateDB(self):
        try:
            print(f"API DB is already created as {self.apiDb}")
        except:
            print(f"Something went wrong")

    def CreateTable(self):
        for item in self.table:
            self.cursor.execute(item)
        print("The table has been created correctly")

    def GetTable(self, int):
        if int == 0:
            self.cursor.execute("""SELECT * FROM Cars""")
            data = self.cursor.fetchall()
        elif int == 1:
            self.cursor.execute("""SELECT * FROM Users""")
            data = self.cursor.fetchall()    
        return data
    
    def GetItem(self, int, str):
        if int == 0:
            self.cursor.execute("""SELECT *
                                    FROM Cars
                                    WHERE id = {}""".format(str))
            data = self.cursor.fetchall()
            print(data)
        elif int == 1:
            self.cursor.execute("""SELECT *
                                    FROM Users
                                    WHERE id = {}""".format(str))
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
        self.instruction = '''INSERT INTO USERS(Name, LastName, Email, Password, Position) VALUES(?,?,?,?)'''
        self.fields = (self.dict["name"], self.dict["lastName"], self.dict["email"], self.dict["password"], self.dict["position"])

    def SetInstructionAndFieldsChanges(self):
        self.instruction = '''INSERT INTO CHANGES(UserId, CarId) VALUES(?,?)'''
        self.fields = (self.dict["userId"], self.dict["carId"])

    def ProcessToCarTable(self):
        self.SetInstructionAndFieldsCar()
        self.AddToTable()

    def ProcessToUserTable(self):
        self.SetInstructionAndFieldsUser()
        self.AddToTable()

    def ProcessToRegister(self):
        self.SetInstructionAndFieldsChanges()
        self.AddToTable()

    def LogIn(self):
        data = self.GetUser()
        data = self.AutenticateUser(data)
        return data
    
    def GetUser(self):
        self.instruction = """SELECT id, Name, password FROM USERS WHERE Email = \"{}\" AND Password = \"{}\";""".format(self.dict["email"], self.dict["password"])
        self.cursor.execute(self.instruction)
        data = self.cursor.fetchall()
        return data
    
    def AutenticateUser(self, data):
        if len(data) != 0:
            self.token = self.token.GetToken()
            self.init = timer()
            self.StartCounting(timer())
            return "Autenticated"
        else:
            return "Credentials wrong or user do not exist"
        
    def StartCounting(self, end):
        try:
            self.timing = end - self.init
            print("This is the timing {} and token {}".format(self.timing, self.token))
        except Exception as e:
            print(e)
            
    def CompareTiming(self):
        if self.timing > 60.0:
            print(self.timing, self.timing>60.0)
            print("The token has expire please logIn again")
        else:
            print(self.timing, self.timing>60.0)
            print("The token remains useful")

# The __main__ function will be used to create the DB thats why there wasn't registers after 
# reactivate the API
if __name__ == "__main__":
    db = ApiDb()