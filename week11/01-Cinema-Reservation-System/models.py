from connector import Connector
from queries import CREATE_MOVIE_TABLE, LIST_MOVIES, GET_MOVIE_IN_PROJECTIONS, CREATE_MOVIE
import sqlite3
conn = sqlite3.connect("cinema.db")
cursor = conn.cursor()
import hashlib
import uuid
from settings import matrix



class MovieModel:
    def __init__(self):
        self.conn = Connector()

    def create(self, name, rating):
        query = CREATE_MOVIE
        self.conn.execute_query(query, (name, rating))

    def list(self):
        query = LIST_MOVIES
        return self.conn.all(query)

    @classmethod
    def get_movie_id(self, id):
        query = GET_MOVIE_IN_PROJECTIONS
        a = conn.execute(query, (id,))
        result = []
        for i in a.fetchall():
            result.append(i)
        # print(result)
        return result


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

    @staticmethod
    def calculate_free_seats(projection_id):
        a = 0
        result = conn.execute('SELECT COUNT(*) FROM RESERVATIONS WHERE PROJECTION_ID=?', (projection_id, ))
        for i in result.fetchone():
            a = i

        return 100 - a

    def get_reservations(self, projection_id, matrix):
        a = conn.execute('''SELECT ROW, COL FROM RESERVATIONS WHERE PROJECTION_ID=?''', (projection_id,))
        result = []
        for i in a.fetchall():
            result.append(i)

        for i in result:
            row, col = i
            matrix[row][col] = 'X'
        return matrix

    def make_reservation(self, username, row, col, id):
        cursor.execute('INSERT INTO RESERVATIONS (user_id, projection_id, row, col )  VALUES (?, ?, ?, ?)', (username, id, row, col))


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

    @classmethod
    def get_pass(cls, username):
        try:
            result = cursor.execute('SELECT PASSWORD FROM USERS WHERE USERNAME=?', (username,))
            for i in result.fetchone():
                return i
        except Exception:
            return None

    @classmethod
    def check_user(cls, username, password):
        passwd = cls.get_pass(username)
        if cls.check_password(passwd, password):
            a = cursor.execute('SELECT USERNAME FROM USERS WHERE USERNAME=?',
                     (username, ))
            try:
                for i in a.fetchone():
                    return i
            except Exception:
                return None
        else:
            return None

    @classmethod
    def register_user(cls, username, password):
        cursor.execute('INSERT INTO USERS (USERNAME, PASSWORD) VALUES (?, ?)', (username, password))
        conn.commit()

    @classmethod
    def login_user(cls, username):
        cursor.execute('UPDATE USERS SET IS_ACTIVE = 1 WHERE USERNAME=?', (username,))
        conn.commit()

    @classmethod
    def loged_in(cls, username):
        result = cursor.execute('SELECT IS_ACTIVE FROM USERS WHERE USERNAME=?', (username,))
        for i in result.fetchone():
            return i
        conn.commit()


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
