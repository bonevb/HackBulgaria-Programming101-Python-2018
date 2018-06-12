from models import User, Cinema, matrix
from movie_controller import MovieController
import sys
import getpass
import uuid
import hashlib



class Reservation:


    @classmethod
    def make_reservation(cls):
        username = input('Hello!\nProvide your user_name:\n>>> ')
        password =  getpass.getpass('password: ')
        hash_pass = User.hash_password(password)
        user = User.check_user(username, password)
        # print('User', user)

        if user:
            User.login_user(username)

        else:
            print('Unknown user!\n Would you like to create new user?')
            create_new = input('>>> ')
            if create_new.lower() in ['y', 'yes']:
                username = input('username: ')
                password = getpass.getpass('password ')
                hash_pass = User.hash_password(password)
                User.register_user(username, hash_pass)
                User.login_user(username)
        if User.loged_in(username) == 1:
            print('Hello, {}'.format(username))
            while True:
                tickests = int(input('Step 1 (User): Choose number of tickets> '))
                print('Current movies:')
                MovieController.show_all_movies()
                movie_id = int(input('Step 2 (Movie): Choose a movie> '))
                result = MovieController.show_movies_by_id(movie_id)

                for i in result:
                    argument = i[0]
                    print('{} {} {} {} - {} spots available'.format(i[0], i[1], i[2], i[3], Cinema.calculate_free_seats(argument)))
                projection_id = input('Step 3 (Projections: Choose a projection> )')
                whole = matrix
                my_cinema = Cinema(whole)
                my_cinema.get_reservations(projection_id, whole)
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
                            my_cinema.make_reservation(username, row, col, projection_id )
                            break
                        else:
                            continue
                finalize = input("Step 5 (Confirm - type 'finalize') >")
                if finalize == 'finalize':
                    my_cinema.finalize()
                    print('Thanks')
                    break
















Reservation.make_reservation()
