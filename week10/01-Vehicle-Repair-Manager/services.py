import sqlite3
from prettytable import PrettyTable


DB_NAME = "vehicle_management.db"

db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()

class Service:
    def __init__(self, name):
        self.name = name

    @classmethod
    def print_service(cls):
        x = PrettyTable()
        x.field_names = ['id', 'name']
        row = c.execute('SELECT * FROM SERVICE')
        a = row.fetchone()
        x.add_row([a[0], a[1]])
        print(x)

    @classmethod
    def create_service(cls, name):
        c.execute('INSERT INTO SERVICE (name) VALUES (?)', (name, ))
        db.commit()
