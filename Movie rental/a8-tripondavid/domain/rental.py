import datetime

class Rental:
    def __init__(self, rental_id :int, movie_id :int, client_id :int, rented_date :datetime, due_date :datetime, returned_date = None):
        self._rental_id =rental_id
        self._movie_id = movie_id
        self._client_id = client_id
        self._rented_date = rented_date
        self._due_date = due_date
        self._returned_date = returned_date

    @property
    def rental_id(self):
        """
        :return: Rental id
        """
        return self._rental_id

    @property
    def movie_id(self):
        """
        :return: Movie id
        """
        return self._movie_id

    @property
    def client_id(self):
        """
        :return: Client id
        """
        return self._client_id

    @property
    def rented_date(self):
        """
        :return: Rented date
        """
        return self._rented_date

    @property
    def due_date(self):
        """
        :return: Due date
        """
        return self._due_date

    @property
    def returned_date(self):
        """
        :return: Returned date
        """
        return self._returned_date

    @returned_date.setter
    def returned_date(self, end: datetime.date):
        """
        Sets the return date
        :param end: End date
        """
        self._returned_date = end
