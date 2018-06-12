from user import User
from mechanic import Mechanic
from repair_hours import  RepairHour
from vehicle import Vehicle
from services import Service


class Controller:

    # @classmethod
    # def find_all_by_username(cls, username):
    #     result = .execute("SELECT * FROM VEHICLE WHERE OWNER=username")
    #     return cls.build_vehicle(result)
    #
    # @classmethod
    # def build_vehicle(cls, row):
    #     return Vehicle(row)

    @classmethod
    def create_user(cls, *params):
        return User(*params).save_to_db(*params)

    @classmethod
    def create_mechanic(cls, *params):
        return Mechanic(*params).save_to_db(*params)

    @classmethod
    def check_if_user_exists(cls, username):
        return User.check_user(username)

    def check_type_of_user(cls, username):
        return User.check_type(username)

    @classmethod
    def list_all_free_hours(cls):
        return RepairHour.get_free_hours()

    @classmethod
    def get_free_hours_by_date(cls, date):
        return RepairHour.get_free_hours_date(date)

    @classmethod
    def get_id_of_username(cls, username):
        return User.get_client_id(username)

    @classmethod
    def add_vehicle(cls, *params):
        return Vehicle(*params).save_vehicle_to_db(*params)

    @classmethod
    def list_vehicle_by_username(cls, username):
        user_name = User.get_client_id(username)
        return Vehicle.list_vehicle(user_name)

    @classmethod
    def list_services(cls):
        return Service.print_service()

    @classmethod
    def save_repair_hour(id, car_id, service_id):
        return RepairHour.save_repair_hour_by_id()

    @classmethod
    def update_vehicle(cls, id, *params):
        return Vehicle(*params).update_vehicle_in_db(id, *params)

    @classmethod
    def delete_vehicle(cls, id, owner):
        return Vehicle.remove_from_db(id, owner)

    @classmethod
    def save_repair_hour_id(cls,vehicle, service, free_hour_id):
        return RepairHour.save_repair_hour_by_id(vehicle, service, free_hour_id)

    @classmethod
    def list_saved_repair_hours(cls, client_id):
        return RepairHour.get_saved_repair_hour(client_id)

    @classmethod
    def delete_repair_hour(cls, id):
        return RepairHour.delete_repair_hour_by_id(id)

    @classmethod
    def get_all_busy_hours(cls):
        return RepairHour.all_busy_hours()


    @classmethod
    def get_all_busy_hours_date(cls, date):
        return RepairHour.all_busy_hours(date)

    @classmethod
    def add_new_repair_hour(cls, time, date):
        return RepairHour.add_new_repair_hour_date(time, date)

    @classmethod
    def create_new_service(cls, name):
        return Service.create_service(name)

    @classmethod
    def add_service_to_mechanic(cls, service_name, mechanic_id):
        return Mechanic.add_service_to_mechanic_id(service_name, mechanic_id)




# Controller.list_vehicle_by_username('tedi')
# Controller.create_new_service('test2')
# Controller.list_services()
# print(Controller.add_service_to_mechanic('test2', 1))
