from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, update
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import matrix
from models import User as usr


# A class that maps to a table, inherits from Base
Base = declarative_base()


class Movie(Base):
    __tablename__ = 'Movies'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(Float)


class Projection(Base):
    __tablename__ = 'Projections'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('Movies.id'))
    type = Column(String)
    date = Column(String)
    time = Column(String)

class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    is_active = Column(Integer, default=0)


class Reservation(Base):
    __tablename__ = 'Reservations'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    projection_id = Column(Integer, ForeignKey('Projections.id'))
    row = Column(Integer)
    col = Column(Integer)

engine = create_engine('sqlite:///movies.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()
session.add_all([
    Movie(name='The Hunger Games: Catching Fire', rating=7.9),
    Movie(name='Wreck-It Ralph', rating=7.8),
    Movie(name='Her', rating=8.3),
    Projection(movie_id=1, type='3D', date='2014-04-01', time='19:10'),
    Projection(movie_id=1, type='2D', date='2014-04-01', time='19:00'),
    Projection(movie_id=1, type='4DX', date='2014-04-02', time='21:00'),
    Projection(movie_id=3, type='2D', date='2014-04-05', time='20:20'),
    Projection(movie_id=2, type='3D', date='2014-04-02', time='22:00'),
    Projection(movie_id=3, type='2D', date='2014-04-02', time='19:30'),
    Reservation(user_id=3, projection_id=1, row=2, col=1),
    Reservation(user_id=3, projection_id=1, row=3, col=5),
    Reservation(user_id=3, projection_id=1, row=7, col=8),
    Reservation(user_id=2, projection_id=3, row=1, col=1),
    Reservation(user_id=2, projection_id=3, row=1, col=2),
    Reservation(user_id=5, projection_id=5, row=2, col=3),
    Reservation(user_id=5, projection_id=5, row=2, col=4)
    ])
session.commit()

session.add_all([User(username='Ivo', password='Boby')])

class Controller_Alchemy:

    @classmethod
    def list(cls):
        movies  = session.query(Movie.id, Movie.name, Movie.rating).all()
        print(movies)
        # for movie in movies:
        #     print(movie)

    @classmethod
    def get_movie_id(cls, id):
        result = session.query(Movie, Projection).filter(Movie.id==Projection.movie_id)
        # return result
        for row in result:
            print('{} {} {} {} - {} spots available'.format(row[1].id, row[0].name, row[1].date, row[1].time, cls.calculate_free_seats(row[1].id)))
        # movie = session.query(Projection.id).filter(Projection.id==ids.id).all()
        # return movie.name

    @classmethod
    def calculate_free_seats(cls, projection_id):
        seats = session.query(Reservation).filter(Reservation.projection_id==projection_id).count()
        # for i in seats:
            # print(i.id)
        return 100 - seats

    @classmethod
    def get_reservations(cls, projection_id, matrix):
        result = session.query(Reservation.row, Reservation.col).filter(Reservation.projection_id==projection_id).all()
        for i in result:
            row, col = i
            matrix[row][col] = 'X'
        return matrix

    @classmethod
    def make_reservation(self, username, id, rows, cols):
        session.add_all([
            Reservation(user_id=username, projection_id=id, row=rows, col=cols)
            ])

    @classmethod
    def get_pass(cls, user_name):
        result = session.query(User).filter(User.username==user_name)
        try:
            return result[0].password
        except Exception:
            print('No user found')

    @classmethod
    def check_user(cls, user_name, password):
        passwd = cls.get_pass(user_name)
        if usr.check_password(passwd, password):
            return user_name
        else:
            return None

    @classmethod
    def register_user(cls, username, password):
        # cursor.execute('INSERT INTO USERS (USERNAME, PASSWORD) VALUES (?, ?)', (username, password))
        # conn.commit()
        session.add_all([User(username=username, password=password)])
        session.commit()

    @classmethod
    def login_user(cls, user_name):
        result = session.query(User).filter(User.username==user_name).update({'is_active': 1})
        # result.is_active = 1
        session.commit()

    @classmethod
    def loged_in(cls, user_name):
        result = session.query(User.is_active).filter(User.username==user_name)
        session.commit()
        return result[0].is_active

    @classmethod
    def finalize(cls):
        session.commit()



# print(session.query(Movie, Projection).filter(Movie.id==1).filter(Projection.movie_id==1).all())

# print(Controller_Alchemy.get_movie_id(1))
# print(Controller_Alchemy.calculate_free_seats(1))
# print(Controller_Alchemy.get_movie_id(1))
# Controller_Alchemy.login_user('Ivo')
# Controller_Alchemy.make_reservation(1, 1, 1, 1)
# print(Controller_Alchemy.loged_in('Ivo'))
# session.commit()
#
# print(Controller_Alchemy.get_pass('adf'))
# result = session.query(User).filter(User.username=='Ivo')
# print(result[0].username)
# q = session.query(Movie, Projection).filter(Movie.id==Projection.movie_id)
# for row in q:
#     print(row[1].id, row[0].name, row[1].date, row[1].time )
# session.commit()
# print(session.query(Reservation).filter(Reservation.projection_id==1).count())
# print(Controller_Alchemy.check_user('tedi', 'tedi'))
# q = session.query(User.username).filter(User.username=='ivan').one()
# print(q[0])
