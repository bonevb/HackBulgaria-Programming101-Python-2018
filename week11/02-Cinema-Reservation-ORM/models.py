
# from queries import CREATE_MOVIE_TABLE, LIST_MOVIES, GET_MOVIE_IN_PROJECTIONS, CREATE_MOVIE
import sqlite3
conn = sqlite3.connect("cinema.db")
cursor = conn.cursor()
import hashlib
import uuid
from settings import matrix



class MovieModel:
    def __init__(self):
        self.conn = Connector()

class Cinema:
    def __init__(self, matrix):
        self.matrix = matrix

    def print_matrix(self):
        n = len(self.matrix)
        m = len(self.matrix[0])

        for i in range(0, n):
            print()
            for j in range(0, m):
                print(self.matrix[i][j], end="")

    def  check_borders(self, col, row):
        if col > len(self.matrix) or row > len(self.matrix[0]):
            print("Lol ... No!")
            return False
        elif self.matrix[col][row] == 'X':
            print("This is already taken")
            return False
        else:
            print("This is your reservation")
            return True



    def finalize(self):
        conn.commit()


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


    @classmethod
    def hash_password(cls, password):
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    @staticmethod
    def check_password(hashed_password, user_password):
        try:
            password, salt = hashed_password.split(':')
            return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
        except Exception:
            return None

   
# cinema = Cinema()
# cinema.create_cinema()
# print(Cinema.calculate_free_seats(1))
# a = MovieModel.get_movie_id(1)
# for i in a:
#     print(i)
# User.register_user('pesho', 'cisco')
# print(User.check_user('ivan', 'ivan'))
# print(Cinema.get_reservations(1))
# passwd = User.get_pass('ivan')
# print(User.check_password(passwd, 'ivan'))
# print(User.check_user('ivan', 'ivan'))
