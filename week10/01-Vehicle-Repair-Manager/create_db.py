import sqlite3

DB_NAME = "vehicle_management.db"

db = sqlite3.connect(DB_NAME)
#db.row_factory = sqlite3.Row
c = db.cursor()

drop_base_user = """DROP TABLE IF EXISTS BASE_USER"""
c.execute(drop_base_user)
db.commit()

create_base_user_tabe = """
CREATE TABLE IF NOT EXISTS BASE_USER(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
USER_NAME TEXT NOT NULL,
EMAIL TEXT NOT NULL,
PHONE_NUMBER INTEGER NOT NULL,
ADDRESS TEXT,
TYPE TEXT
)
"""

c.execute(create_base_user_tabe)
db.commit()

drop_mechanic = """DROP TABLE IF EXISTS MECHANIC"""
c.execute(drop_mechanic)
db.commit()

create_table_mechanic = """
CREATE TABLE IF NOT EXISTS MECHANIC(
BASE_ID INTEGER PRIMARY KEY NOT NULL,
FOREIGN KEY (BASE_ID) REFERENCES BASE_USER(ID)
)
"""

c.execute(create_table_mechanic)
db.commit()

drop_client = """DROP TABLE IF EXISTS CLIENT"""
c.execute(drop_client)
db.commit()

create_table_client = """
CREATE TABLE IF NOT EXISTS CLIENT(
BASE_ID INTEGER PRIMARY KEY NOT NULL,
FOREIGN KEY (BASE_ID) REFERENCES BASE_USER(ID)
)
"""

c.execute(create_table_client)
db.commit()

drop_vehicle = """DROP TABLE IF EXISTS VEHICLE"""
c.execute(drop_vehicle)
db.commit()

create_table_vehicle = """
CREATE TABLE IF NOT EXISTS VEHICLE(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
CATEGORY TEXT NOT NULL,
MAKE TEXT NOT NULL,
MODEL TEXT NOT NULL,
REGISTER_NUMBER TEXT NOT NULL,
GEAR_BOX TEXT,
OWNER TEXT NOT NULL,
FOREIGN KEY (OWNER) REFERENCES CLIENT(BASE_ID)
)
"""
c.execute(create_table_vehicle)
db.commit()

drop_repair_hours = """DROP TABLE IF EXISTS REPAIR_HOURS"""
c.execute(drop_repair_hours)
db.commit()

create_table_repair_hours = """
CREATE TABLE IF NOT EXISTS REPAIR_HOURS(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
DATE TEXT NOT NULL,
START_HOUR INTEGER NOT NULL,
VEHICLE  INTEGER ,
BILL REAL ,
MECHANIC_SERVICE INTEGER ,
FOREIGN KEY (MECHANIC_SERVICE) REFERENCES MECHANIC_SERVICE(ID)
FOREIGN KEY (VEHICLE) REFERENCES VEHICLE(ID)
)
"""
c.execute(create_table_repair_hours)
db.commit()

insert_into_repair_hour = """
INSERT INTO REPAIR_HOURS (date, start_hour)
VALUES (:date, :start_hour)
"""
c.execute(insert_into_repair_hour, {
                                    'date': "25-05-2018",
                                    'start_hour': '10:00'
})
c.execute(insert_into_repair_hour, {
                                    'date': "25-05-2018",
                                    'start_hour': '11:00'
})
c.execute(insert_into_repair_hour, {
                                    'date': "26-05-2018",
                                    'start_hour': '12:00'
})

drop_mechanic_service = """DROP TABLE IF EXISTS MECHANIC_SERVICE"""
c.execute(drop_mechanic_service)
db.commit()

create_table_mechanic_service = """
CREATE TABLE IF NOT EXISTS MECHANIC_SERVICE(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
MECHANIC_ID INTEGER NOT NULL,
SERVICE_ID INTEGER ,
FOREIGN KEY (MECHANIC_ID) REFERENCES MECHANIC(BASE_ID)
FOREIGN KEY (SERVICE_ID) REFERENCES SERVICE(ID)
)
"""

c.execute(create_table_mechanic_service)
db.commit()

drop_service = """DROP TABLE IF EXISTS SERVICE"""
c.execute(drop_service)
db.commit()

create_table_service = """
CREATE TABLE IF NOT EXISTS SERVICE(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
NAME TEXT NOT NULL
)
"""
c.execute(create_table_service)
db.commit()

insert_base_user = """
INSERT INTO BASE_USER (user_name, email, phone_number, address)
 VALUES (:user_name, :email, :phone_number, :address
 )
"""

insert_into_repair_hour = """
INSERT INTO REPAIR_HOURS ()
"""

# c.execute(insert_base_user, {'user_name': 'Boby',
#                              'email': 'test@abv.bg',
#                              'phone_number': 87654321,
#                              'address': 'Sofia'})


# c.execute(insert_base_user, {'user_name': 'Ivan',
#                              'email': 'ivan@abv.bg',
#                              'phone_number': 1234,
#                              'address': 'Varna'})

# c.execute(insert_base_user, {'user_name': 'Pesho',
#                              'email': 'Pesho@abv.bg',
#                              'phone_number': 7654,
#                              'address': 'Plovdiv'})

insert_service = """
INSERT INTO SERVICE (name) VALUES (:name)
"""

c.execute(insert_service, {'name': 'Oil Change'})

db.commit()

db.close()
