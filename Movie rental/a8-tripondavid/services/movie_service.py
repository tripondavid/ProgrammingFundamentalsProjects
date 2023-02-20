from domain.movie import Movie

class MovieService:
    def __init__(self, movie_repo, validator):
        self._movie_repo = movie_repo
        self._validator = validator

    def add_movie(self, movie_id :int, title :str, description :str, genre :str):
        """
        Accesses the movie repo in order to add a new movie
        :param movie_id: Movie id
        :param title: Movie title
        :param description: Movie description
        :param genre: Movie genre
        """
        new_movie = Movie(movie_id, title, description, genre)
        self._validator.validate(new_movie)
        self._movie_repo.add_movie(new_movie)

    def list_movie(self):
        """
        Accesses the movie repo in order to list all current movies
        :return: Dict of current movies
        """
        return self._movie_repo.get_all_movies()

    def remove_movie(self, movie_id :int):
        """
        Accesses the movie repo in order to remove a movie
        :param movie_id: Movie id
        """
        movie_list = self.list_movie().copy()

        for obj in movie_list:
            if movie_list[obj].get_movie_id == movie_id:
                self._movie_repo.remove_movie(obj)

    def update_movie(self, movie_id :int, new_description :str):
        """
        Accesses the movie repo in order to update the description of a movie
        :param movie_id: Movie id
        :param new_description: New movie description
        """
        movie_list = self.list_movie().copy()

        for obj in movie_list:
            if movie_list[obj].get_movie_id == movie_id:
                movie_list[obj].movie_description = new_description
                new_movie = movie_list[obj]
                self._movie_repo.update_movie(obj, new_movie)

    def search_movie(self, parameter: str):
        """
        Accesses the movie repo in order to search for a specific movie
        :param parameter: User input
        :return: List that matched the parameter(case-insensitive, partial string matching)
        """
        movie_list = self.list_movie().copy()
        match_list = []

        if parameter.isnumeric():
            for obj in movie_list:
                if parameter in str(movie_list[obj].get_movie_id):
                    match_list.append(movie_list[obj])
        else:
            for obj in movie_list:
                if (parameter.lower() in movie_list[obj].get_title.lower()) or (parameter.lower() in movie_list[obj].get_description.lower()) or (parameter.lower() in movie_list[obj].get_genre.lower()):
                    match_list.append(movie_list[obj])

        return match_list

