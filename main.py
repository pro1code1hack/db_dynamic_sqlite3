from db import db_client
from cars import Car

# TODO statuses as enums

# car2 = Car(id = 2, vin = "TESTVIN",brand ="BMW",model = "M5",status = "SOLD",price = "50000",location = "Germany")
# car3 = Car(id = 3, vin = "NEW_TEST",brand ="TOYOTA",model = "SUPRA",status = "ON_HOLD",price = "75000",location = "Japan")
# car4 = Car(id = 4, vin = "VINTEST",brand ="Rolls Royce",model = "Ghost",status = "CONTRACTED",price = "500000",location = "GB")

# # db_client.insert(
# #     car4.table_name, car4.__dict__()
# # )

cars = Car.get_cars(db_client)

# {'id': 3, 'vin': 'NEW_TEST', 'brand': 'TOYOTA', 'status': 'ON_HOLD', 'model': 'SUPRA', 'price': 75000.0, 'location': 'Japan'}
for car in cars:
    car_dict = dict(car) 
    print(car_dict)