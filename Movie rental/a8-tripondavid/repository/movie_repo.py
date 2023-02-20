class MovieRepository:
    def __init__(self):
        self.movie_data = {}

    def get_all_movies(self):
        """
        :return: Dict of all movies
        """
        return self.movie_data

    def add_movie(self, new_movie):
        """
        Add a movie to the movie repo
        :param new_movie: New movie
        """
        if new_movie.get_movie_id in self.movie_data:
            raise ValueError("Movie already in repo.")
        self.movie_data[new_movie.get_movie_id] = new_movie

    def remove_movie(self, movie_id :int):
        """
        Remove movie from movie repo
        :param movie_id: Movie id
        """
        self.movie_data.pop(movie_id)

    def update_movie(self, movie_id :int, updated_movie :str):
        """
        Update a movie description
        :param movie_id: Movie id
        :param updated_movie: Updated movie
        """
        self.movie_data[movie_id] = updated_movie