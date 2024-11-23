import sqlite3

class DB:
    pass

    def __init__(self,db_name="project.db") -> None:
        self.db_name = db_name
        self.connection = None

    def connect(self):
        if not self.connection:
            self.connection = sqlite3.connect(self.db_name)
        
        self.connection.row_factory = sqlite3.Row       # dictionary object
        return self.connection

    @property
    def cursor(self):
        return self.connect().cursor()

    def execute(self, query: str, params = ()):
        cursor = self.cursor
        cursor.execute(query, params)
        if "INSERT" or "UPDATE" or "DELETE" in query:
            self.connection.commit()
        return cursor
    
    def fetch_all(self, query:str):
        cursor = self.cursor
        
        res = cursor.execute(query)
        return res.fetchall()

    def fetch_one(self,query:str):
        cursor = self.cursor

        cursor.execute(query)
        return cursor.fetchone()

    def create_table(self, table_name: str, schema : dict):
        # cur.execute("CREATE TABLE movie(id INTEGER PRIMARY KEY, year, score)")
        columns = ", ".join(f"{col} {d_type}" for col, d_type in schema.items())
        query = f"CREATE TABLE {table_name} ({columns})"
        print(query)
        self.execute(query)
    
    # {"id":1, "vin": "AB2313AC"}
    def insert(self, table_name: str, data: dict):
        columns = ",".join(data.keys())           # "id,vin" 
        questions = ",".join("?" for i in data)   # "?,?"        
        values = tuple(data.values())             # "1,"AB2313AC"

        # INSERT INTO cars  (id,vin) VALUES (?,?)
        query = f"INSERT INTO {table_name}  ({columns}) VALUES ({questions})"
        self.execute(query, values)
    

    def update(self):
        pass

    def delete(self):
        pass

    def join(self):
        pass


"""
1. Dynamic queries  --> proffessional type
2. class Car ()         def insert_to_db():
"""


# from schemas import cars
db_client = DB()

