import sqlite3


class ApiDb ():
    def __init__(self):
        self.apiDb = "ApiDb.db"
        try:
            self.conn = sqlite3.connect(self.apiDb)
            print("connection stablished")
        except:
            print("something went wrong")
        self.cursor = self.conn.cursor()
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
        print(self.table)
        self.cursor.execute(self.table)
        print("Data have been added correctly")
        self.conn.commit()

    def SeeRow(self):
        data = self.cursor.execute('''SELECT * FROM Cars''')
        for row in data:
            print(row)


db = ApiDb()

db.table = """INSERT INTO CARS VALUES('Ford', 'Mustang', 'Red', '1995')"""

db.AddToTable()
db.SeeRow()
db.conn.close()