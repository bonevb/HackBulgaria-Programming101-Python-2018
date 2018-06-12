from models import MovieModel



class MovieController:
    movie = MovieModel()

    @classmethod
    def create(cls, name, rating):
        if int(rating) < 0:
            raise ValueError("Rating must be positive number")
        # all_movies_names = MovieModel.list(values_list='name')

        cls.movie.create(name, rating)

    @classmethod
    def show_all_movies(cls):
        print(cls.movie.list())

    @classmethod
    def show_movies_by_id(cls, id):
        return MovieModel.get_movie_id(id)

    @classmethod
    def show_projections(cls, id):
        pass



# print(MovieController.show_movies_by_id(1))
# print(MovieController.show_all_movies())
