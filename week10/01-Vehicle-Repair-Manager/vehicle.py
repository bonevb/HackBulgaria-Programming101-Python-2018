import sqlite3
import constants
from prettytable import PrettyTable
# from constants import insert_base_user

DB_NAME = "vehicle_management.db"

db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()


class Vehicle:
    def __init__(self, category, make, model, register_number,
                 gera_box, owner):
        self.category = category
        self.make = make
        self.model = model
        self.register_number = register_number
        self.gera_box = gera_box
        self.owner = owner

    @classmethod
    def save_vehicle_to_db(cls, category, make, model, register_number, gear_box, owner):
        c.execute(constants.insert_vehicle,{'category': category, 'make': make, 'model': model,'register_number': register_number,'gear_box' : gear_box,'owner': owner})
        db.commit()

    @classmethod
    def list_vehicle(cls, ids):
        x = PrettyTable()
        car_details = []
        x.field_names = ['id','category', 'make', 'model' ,'reg number', 'gear_box']
        row =  c.execute('SELECT * FROM VEHICLE WHERE OWNER = ?', (ids,))
        a = row.fetchall()

        for i in a:
            x.add_row([i[0], i[1], i[2], i[3], i[4], i[5]])
        print(x)

    @classmethod
    def update_vehicle_in_db(cls, id, category, make, model, register_number, gear_box, owner):
        c.execute('UPDATE VEHICLE SET category=?, make=?, model=?, register_number=?, gear_box=?, owner=? WHERE id=?', (category, make, model, register_number, gear_box, owner, id))
        db.commit()

    @classmethod
    def remove_from_db(cls, id, owner):
        c.execute('DELETE FROM VEHICLE WHERE ID=? AND OWNER=?', (id, owner))
        db.commit()


#     @classmethod
#     def list_vehicle_by_user_id(cls, ids):
#         x = PrettyTable()
#         cars = []
#         x.field_names = ['id','category', 'make', 'model' ,'reg number', 'gear_box']
#         row = c.execute('SELECT id FROM VEHICLE WHERE OWNER = ?', (ids,))
#         a = row.fetchall()
#
#         for i in a:
#             cars.append(i[0])
#         return cars
#
#
# print(Vehicle.list_vehicle_by_user_id(4))
