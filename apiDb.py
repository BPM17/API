import sqlite3
import json


class ApiDb ():
    def __init__(self):
        self.apiDb = "ApiDb.db"
        try:
            self.conn = sqlite3.connect(self.apiDb)
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

    def AddToTable(self):
        self.cursor.execute(self.table)
        print("Data have been added correctly")
        self.conn.commit()

    def SeeRow(self):
        data = self.cursor.execute('''SELECT * FROM Cars''')
        for row in data:
            print(row)

    def ProcessToTable(self):
        print(self.dict)
        self.table = ""
        self.SeparetingIntoTable()
        self.CreateSentenceDB()
        self.AddToTable()

    def SeparetingIntoTable(self):
        for key, value in self.dict:
            table =[]
            table.append(value)
            self.table = self.table +"'"+ str(value)+"',"
            print(f"This is what is going to be saved in the table {self.table}")

    def CreateSentenceDB(self):
        l = list(self.table)
        del(l[len(self.table)-1])
        self.table = "".join(l)
        self.table =f"INSERT INTO CARS VALUES({self.table})"
        print("Se han procesado los valores correctamente")

if __name__ == "__main__":
    db = ApiDb()
    db.table = """ CREATE TABLE IF NOT EXISTS CARS(
        Brand VARCHAR(255) NOT NULL,
        Model VARCHAR(255) NOT NULL,
        Color VARCHAR(255) NOT NULL,
        Year INTEGER
    ) """
    db.CreateTable()