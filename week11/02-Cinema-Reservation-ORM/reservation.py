from models import User, Cinema, matrix
# from movie_controller import MovieController
from controller_alchemy import Controller_Alchemy
import sys
import getpass
import uuid
import hashlib


class Reservation:
    controller=Controller_Alchemy()


    @classmethod
    def make_reservation(cls):
        username = input('Hello!\nProvide your user_name:\n>>> ')
        password =  input('password: ')
        hash_pass = User.hash_password(password)
        user = cls.controller.check_user(username, password)
        # print('User', user)

        if user:
            cls.controller.login_user(username)

        else:
            print('Unknown user!\n Would you like to create new user?')
            create_new = input('>>> ')
            if create_new.lower() in ['y', 'yes']:
                username = input('username: ')
                password = input('password ')
                hash_pass = User.hash_password(password)
                cls.controller.register_user(username, hash_pass)
                cls.controller.login_user(username)
        if cls.controller.loged_in(username) == 1:
            print('Hello, {}'.format(username))
            while True:
                tickests = int(input('Step 1 (User): Choose number of tickets> '))
                print('Current movies:')
                cls.controller.list()
                movie_id = int(input('Step 2 (Movie): Choose a movie> '))
                cls.controller.get_movie_id(movie_id)

                projection_id = input('Step 3 (Projections: Choose a projection> )')
                whole = matrix
                my_cinema = Cinema(whole)
                cls.controller.get_reservations(projection_id, whole)
                my_cinema.print_matrix()

                for i in range(tickests):
                    while True:
                        seats = input("Step 4 (Seats): Choose seat {}> ".format(i+1))
                        row, col = seats.split(',')
                        row = int(row)
                        col = int(col)
                        print(row, col)
                        if my_cinema.check_borders(row, col):
                            whole[row][col] = 'X'
                            cls.controller.make_reservation(username, row, col, projection_id )
                            break
                        else:
                            continue
                finalize = input("Step 5 (Confirm - type 'finalize') >")
                if finalize == 'finalize':
                    cls.controller.finalize()
                    print('Thanks')
                    break
















# Reservation.make_reservation()
