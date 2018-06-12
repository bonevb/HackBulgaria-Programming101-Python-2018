from collections import namedtuple
import sqlite3
from prettytable import PrettyTable
import constants



DB_NAME = "vehicle_management.db"

db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()

class RepairHour:
    def __init__(self, date, start_hour, vehicle=None, bill=None, mechanic_service=None):
        self.date = date
        self.start_hour = start_hour
        self.vehicle = vehicle
        self.bill = bill
        self.mechanic_service = mechanic_service

    @classmethod
    def get_free_hours(cls):
        x = PrettyTable()
        x.field_names = ['date', 'start hour']
        for i in c.execute('SELECT id, date, start_hour FROM REPAIR_HOURS WHERE VEHICLE IS NULL'):
            x.add_row([i[1], i[2]])
        print(x)

    @classmethod
    def get_free_hours_date(cls, date):
        x = PrettyTable()
        x.field_names = ['date', 'start hour']
        for i in c.execute('SELECT id, date, start_hour FROM REPAIR_HOURS WHERE VEHICLE IS NULL AND DATE=?', (date,)):
            x.add_row([i[1], i[2]])
        print(x)

    @classmethod
    def save_repair_hour_by_id(cls, vehicle, service, free_hour_id):
        c.execute(constants.save_repair_hour,(vehicle, service, free_hour_id))
        db.commit()

    @classmethod
    def get_saved_repair_hour(cls,user_id):
        x = PrettyTable()
        x.field_names = ['date', 'start hour']
        user_id = str(user_id)
        # vehicle_id = c.execute('SELECT id FROM VEHICLE WHERE OWNER=?')
        # for i in c.execute('SELECT * FROM REPAIR_HOURS WHERE ID=(SELECT ID FROM VEHICLE JOIN CLIENT WHERE (SELECT id FROM VEHICLE WHERE OWNER=?)=CLIENT.BASE_ID)', user_id):
        for i in c.execute('SELECT * FROM REPAIR_HOURS WHERE VEHICLE = (SELECT ID FROM VEHICLE JOIN CLIENT ON ? = CLIENT.BASE_ID)', user_id):
            x.add_row([i[1], i[2]])
        print(x)

    @classmethod
    def delete_repair_hour_by_id(cls,id):
        # x = PrettyTable()
        # x.field_names = ['date', 'start hour']
        # user_id = str(user_id)
        # # vehicle_id = c.execute('SELECT id FROM VEHICLE WHERE OWNER=?')
        c.execute('DELETE FROM REPAIR_HOURS WHERE ID=?', id)
        db.commit()

    @classmethod
    def all_busy_hours(cls):
        c.execute('SELECT id, date, start_hour FROM REPAIR_HOURS WHERE VEHICLE IS NOT NULL')

    @classmethod
    def all_busy_hours_date(cls, date):
        c.execute('SELECT id, date, start_hour FROM REPAIR_HOURS WHERE VEHICLE IS NOT NULL AND DATE=?', date)

    @classmethod
    def add_new_repair_hour_date(cls, time, date):
        c.execute('INSERT INTO REPAIR_HOURS (START_HOUR, DATE) VALUES (?, ?)', (time, date))


# print(RepairHour.get_saved_repair_hour(5))
