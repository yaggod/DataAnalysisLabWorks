from peewee import * 
from datetime import date, time

db = SqliteDatabase("database.db")

class Vehicles(Model):
    car_id = IntegerField(primary_key=True)
    car_make = TextField()
    registration_date = TextField()
    color = TextField()

    def add_item(car_make, registration_date, color):
        Vehicles.create(car_make=car_make, registration_date=registration_date, color=color)

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

    def add_item(surname,
                 first_name,
                 patronymic,
                 pasport_number,
                 birthday_date,
                 hiring_date,
                 work_start_time,
                 work_end_time,
                 city,
                 street,
                 house_id,
                 apartments_id,
                 phone_number):
        Couriers.create(surname=surname,
                        first_name=first_name,
                        patronymic=patronymic,
                        pasport_number=pasport_number,
                        birthday_date=birthday_date,
                        hiring_date=hiring_date,
                        work_start_time=work_start_time,
                        work_end_time=work_end_time,
                        city=city,
                        street=street,
                        house_id=house_id,
                        apartments_id=apartments_id,
                        phone_number=phone_number)

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

    def add_item(surname,
                 first_name,
                 patronymic,
                 birthday_date,
                 post_index,
                 city,
                 street,
                 house_id,
                 apartments_id,
                 phone_number):
        Senders.create(surname=surname,
                       first_name=first_name,
                       patronymic=patronymic,
                       birthday_date=birthday_date,
                       post_index=post_index,
                       city=city,
                       street=street,
                       house_id=house_id,
                       apartments_id=apartments_id,
                       phone_number=phone_number)

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

    def add_item(surname,
                 first_name,
                 patronymic,
                 birthday_date,
                 post_index,
                 city,
                 street,
                 house_id,
                 apartments_id,
                 phone_number):
        Recievers.add_item()
        

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
    
    def add_item(order_id,
                 sender_id,
                 reciever_id,
                 order_date,
                 delivery_date,
                 price,
                 courier,
                 vehicle):
        Orders.create(
                 order_id=order_id,
                 sender_id=sender_id,
                 reciever_id=reciever_id,
                 order_date=order_date,
                 delivery_date=delivery_date,
                 price=price,
                 courier=courier,
                 vehicle=vehicle)

    class Meta:
        database = db
        db_table = "Orders"

def create_tables():
    Senders.create_table()
    Recievers.create_table()
    Orders.create_table()


try:
    create_tables()
except Exception as exception:
    print(exception)
