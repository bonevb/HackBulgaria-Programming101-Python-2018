import sqlite3
import constants
#from constants import insert_base_user

DB_NAME = "vehicle_management.db"

db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()

#
# insert_base_user = """
# INSERT INTO BASE_USER (user_name, email, phone_number, address)
#  VALUES (:user_name, :email, :phone_number, :address
#  )
# """

# c.execute(insert_base_user, {'user_name': 'dux',
#                              'email': 'dux@abv.bg',
#                              'phone_number': 121,
#                              'address': 'Ruse'})

class Mechanic:
    def __init__(self, user_name, email, phone_number, address, type):
        self.user_name = user_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.type = type


    @classmethod
    def save_to_db(cls, username, email, phone_number, address, type):
        c.execute(constants.insert_base_user,
                  {'user_name': username,
                   'email': email,
                   'phone_number': phone_number,
                   'address': address,
                   'type': type})
        ids = c.execute('SELECT ID FROM BASE_USER WHERE USER_NAME =?',(username,))
        for i in ids.fetchone():
          # print(i)
          c.execute('INSERT INTO MECHANIC  VALUES (?)', (i,))
          c.execute('INSERT INTO MECHANIC_SERVICE (MECHANIC_ID)  VALUES (?)', (i,))
          db.commit()
        db.commit()
        db.commit()

    @classmethod
    def add_service_to_mechanic_id(cls, service_name, mechanic_id):

        service_id = c.execute('SELECT ID FROM SERVICE WHERE NAME=?', (service_name,))
        for i in service_id.fetchone():
            service_id = i
        c.execute('UPDATE MECHANIC_SERVICE SET SERVICE_ID =?  WHERE ID=?', (service_id, mechanic_id))
        db.commit()



