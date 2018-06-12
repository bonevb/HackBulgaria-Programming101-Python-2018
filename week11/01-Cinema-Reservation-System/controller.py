from movie_controller import MovieController
from reservation import Reservation



class Controller:

    @classmethod
    def create_movie(cls, name, rating):
        # Check user is logged in
        return MovieController.create(name, rating)

    @classmethod
    def show_movies(cls):
        # Check user is logged in
        return MovieController.show_all_movies()

    @classmethod
    def show_movie_projections(cls, id):
        return MovieController.show_movies_by_id(id)

    @classmethod
    def get_user_id(cls, username):
        pass

    @classmethod
    def make_reservation(cls):
        return Reservation.make_reservation()
