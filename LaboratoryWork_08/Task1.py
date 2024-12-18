import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

def create_tables(cursor : sqlite3.Cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS Vehicles(
               car_id INTEGER PRIMARY KEY AUTOINCREMENT,
               car_make TEXT NOT NULL,
               registration_date TEXT NOT NULL,
               color TEXT NOT NULL)
               """)
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS Couriers(
                courier_id INTEGER PRIMARY KEY AUTOINCREMENT,
                surname TEXT NOT NULL,
                first_name TEXT NOT NULL,
                patronymic TEXT NOT NULL,
                pasport_number INTEGER NOT NULL,
                birthday_date DATE NOT NULL,
                hiring_date DATE NOT NULL,
                work_start_time TIME NOT NULL,
                work_end_time TIME NOT NULL,
                city TEXT NOT NULL,
                street TEXT NOT NULL,
                house_id INTEGER NOT NULL,
                apartments_id INTEGER NOT NULL,
                phone_number TEXT NOT NULL
               )
               """)

def add_data(cursor : sqlite3.Cursor):
    vehicle_to_add = ("Ladaa", "01.02.2023", "Red")
    courier_to_add = ("Ivanovich", "Ivan", "Ivanov", "123456", 
                      "01-01-2000", "01-01-2024", "08:00:00", "18:00:00", "Kaliningrad",
                      "Nevskogo", "1", "2", "+71234567890")
    cursor.execute("INSERT INTO Vehicles(car_make, registration_date, color) VALUES(?, ?, ?)", vehicle_to_add)
    cursor.execute("""INSERT INTO Couriers(surname, first_name, patronymic, pasport_number, 
                   birthday_date, hiring_date, work_start_time, 
                   work_end_time, city, street, house_id, apartments_id, phone_number) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                   """, courier_to_add)

def modify_data(cursor : sqlite3.Cursor):
    new_vehicle_data = ("Lada", "01.02.2023", "Red", 1)
    cursor.execute("""UPDATE Vehicles
                   SET car_make = ?, registration_date = ?, color = ?
                   WHERE car_id = ?
                   """, new_vehicle_data)
    


try:
    create_tables(cursor)
    connection.commit()
    add_data(cursor)
    modify_data(cursor)
    connection.commit()
except Exception as ex:
    print(ex)













