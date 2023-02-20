class Movie:
    def __init__(self, movie_id :int, title :str, description :str, genre :str):
        self._movie_id = movie_id
        self._title = title
        self._description = description
        self._genre = genre

    @property
    def get_movie_id(self):
        """
        :return: Movie id
        """
        return self._movie_id

    @property
    def get_title(self):
        """
        :return: Movie title
        """
        return self._title

    @property
    def get_description(self):
        """
        :return: Movie description
        """
        return self._description

    @property
    def get_genre(self):
        """
        :return: Movie genre
        """
        return self._genre

    def __str__(self):
        return str(self._movie_id) + " " + self._title + " " + self._description + " " + self._genre