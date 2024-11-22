from peewee import * 
from datetime import date, time

db = SqliteDatabase("database.db")

class Vehicles(Model):
    car_id = IntegerField(primary_key=True)
    car_make = TextField()
    registration_date = TextField()
    color = TextField()

    class Meta:
        database = db
        db_table = "Vehicles"

class Couriers(Model):
    courier_id = IntegerField(primary_key=True)
    surname = TextField()
    first_name = TextField()
    patronymic = TextField()
    pasport_number = Field()
    birthday_date = DateField()
    hiring_date = DateField()
    work_start_time = TimeField()
    work_end_time = TimeField()
    city = TextField()
    street = IntegerField()
    house_id = IntegerField()
    apartments_id = IntegerField()
    phone_number = TextField()

    class Meta:
        database = db
        db_table = "Couriers"

class Senders(Model):
    sender_id = IntegerField(primary_key=True)
    surname = TextField()
    first_name = TextField()
    patronymic = TextField()
    birthday_date = DateField()
    post_index = IntegerField()
    city = TextField()
    street = IntegerField()
    house_id = IntegerField()
    apartments_id = IntegerField()
    phone_number = TextField()

    class Meta:
        database = db
        db_table = "Senders"

class Recievers(Model):
    reciever_id = IntegerField(primary_key=True)
    surname = TextField()
    first_name = TextField()
    patronymic = TextField()
    birthday_date = DateField()
    post_index = IntegerField()
    city = TextField()
    street = IntegerField()
    house_id = IntegerField()
    apartments_id = IntegerField()
    phone_number = TextField()
        
    class Meta:
        database = db
        db_table = "Recievers"

class Orders(Model):
    order_id = IntegerField(primary_key=True)
    sender_id = ForeignKeyField(Senders, "sender_id")
    reciever_id = ForeignKeyField(Recievers, "reciever_id")
    order_date = DateField()
    delivery_date = DateField()
    price = IntegerField()
    courier = ForeignKeyField(Couriers, "courier_id")
    vehicle = ForeignKeyField(Vehicles, "car_id")

    class Meta:
        database = db
        db_table = "Orders"

def create_tables():
    Senders.create_table()
    Recievers.create_table()
    Orders.create_table()

def add_example_data():
    sender1 = Senders.create(surname = "Ivanov",
                      first_name = "Ivan",
                      patronymic = "Petrovich",
                      birthday_date = date(1990, 12, 10),
                      post_index = 123456,
                      city = "Kaliningrad",
                      street = "Nevskogo",
                      house_id = 123,
                      apartments_id = 456,
                      phone_number = "+71111111111")
    
    sender2 = Senders.create(surname = "Ivanov",
                      first_name = "Ivan",
                      patronymic = "Smirnov",
                      birthday_date = date(1990, 10, 12),
                      post_index = 234567,
                      city = "Kaliningrad",
                      street = "Kuybisheva",
                      house_id = 234,
                      apartments_id = 345,
                      phone_number = "+71111111222")
    
    reciever1 = Recievers.create(surname = "Ivanov",
                      first_name = "Ivan",
                      patronymic = "Smirnov",
                      birthday_date = date(1990, 10, 12),
                      post_index = 234567,
                      city = "Kaliningrad",
                      street = "Kuybisheva",
                      house_id = 234,
                      apartments_id = 345,
                      phone_number = "+71111111222")
    
    reciever2 = Recievers.create(surname = "Ivanov",
                      first_name = "Ivan",
                      patronymic = "Petrovich",
                      birthday_date = date(1990, 12, 10),
                      post_index = 123456,
                      city = "Kaliningrad",
                      street = "Nevskogo",
                      house_id = 123,
                      apartments_id = 456,
                      phone_number = "+71111111111")
    
    order1 = Orders.create(sender_id = sender1,
                           reciever_id = reciever1,
                           order_date = date(2024, 11, 15),
                           delivery_date = date(2024, 11, 20),
                           price = 1200,
                           courier = 1,
                           vehicle = 1)
    
    order2 = Orders.create(sender_id = sender2,
                           reciever_id = reciever2,
                           order_date = date(2024, 11, 10),
                           delivery_date = date(2024, 11, 15),
                           price = 1400,
                           courier = 1,
                           vehicle = 1)
    
    
try:
    create_tables()
    add_example_data()
except Exception as exception:
    print(exception)
