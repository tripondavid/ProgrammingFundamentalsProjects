class MovieValidator:
    def validate(self, movie):
            if movie.get_genre.isnumeric():
                raise ValueError("Incorrect genre.")
            if movie.get_description.isnumeric():
                raise ValueError("Incorrect description.")