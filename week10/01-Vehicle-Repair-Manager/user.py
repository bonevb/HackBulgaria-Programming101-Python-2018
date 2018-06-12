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

class User:
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
          c.execute('INSERT INTO CLIENT  VALUES (?)', (i,))
          db.commit()
        db.commit()

    @classmethod
    def get_client_id(cls, username):
      ids = c.execute('SELECT ID FROM BASE_USER WHERE USER_NAME =?',(username,))
      for i in ids.fetchone():
        return i


    # @classmethod
    # def save_to_client(cls, username):
    #     ids = c.execute('SELECT ID FROM BASE_USER WHERE USER_NAME =?',(username,))
    #     for i in ids.fetchone():
    #       print(i)
    #       c.execute('INSERT INTO CLIENT  VALUES (?)', (i,))
    #       db.commit()

    @classmethod
    def check_user(cls, username, password):

        c.execute('SELECT USER_NAME, TYPE FROM BASE_USER WHERE USER_NAME=?',
                 (username,))
        try:
            for i in c.fetchone():
                return i
        except Exception:
            return None

    @classmethod
    def check_type(cls, username):

        c.execute('SELECT TYPE FROM BASE_USER WHERE USER_NAME=?',
                 (username,))
        try:
            for i in c.fetchone():
                return i
        except Exception:
            return None


#
# # User.save_to_db('dux', 'dux@abv.bg', 98765, 'Sofia')
# t = ('sadfas',)
# c.execute('SELECT USER_NAME FROM BASE_USER WHERE USER_NAME=?', t)
# try:
#     for i in c.fetchone():
#         print(i)
# except Exception:
#     print('Never')

# User.save_to_client('dany')
