import sqlite3
from db import DB, db_client

class Car:
    table_name = "cars"
    
    def __init__(self, id, vin, brand, model, status, price, location):
        self.id = id
        self.vin = vin
        self.brand = brand
        self.model = model
        self.status = status
        self.price = price
        self.location = location

    def __dict__(self):
        # Convert object to a dictionary
        return {
            "id": self.id,
            "vin": self.vin,
            "brand": self.brand,
            "model": self.model,
            "status": self.status,
            "price": self.price,
            "location": self.location,
        }

    def print_data(self):
        for key, value in self.__dict__().items():
            print(f"{key}: {value}")

    @classmethod
    def get_cars(cls, db_client: DB):
        return db_client.fetch_all(f"SELECT * from {cls.table_name}")

    @classmethod
    def update_car_status(self):
        # db_client.update("Status", "pending", car_id = 1) TODO TODO
        pass

    def sell_car(self):
        pass

    def repair_car(self):
        pass
