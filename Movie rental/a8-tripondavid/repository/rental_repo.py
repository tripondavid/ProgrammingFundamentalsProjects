import datetime


class RentalRepository:
    def __init__(self):
        self.rental_data = {}
        self.movie_rental_times = {}
        self.client_rental_times = {}

    def get_all_rentals(self):
        """
        :return: Dict of all rentals
        """
        return self.rental_data

    def get_rentals_by_times(self):
        """
        :return:Dict of all rentals by times
        """
        return self.movie_rental_times

    def return_rental(self, rental_id: int):
        """
        Return date of the given rental is set to today
        :param rental_id: Rental id
        """
        self.rental_data[rental_id].returned_date = datetime.date.today()

    def add_rental(self, new_rental, name_of_movie: str, client_name: str):
        """
        Add rental in rental repo
        :param new_rental: New rental
        :param name_of_movie: Name of movie
        :param client_name: Client name
        """
        if new_rental.rental_id in self.rental_data:
            raise ValueError("Rental already in repo.")
        self.rental_data[new_rental.rental_id] = new_rental
        if name_of_movie in self.movie_rental_times:
            self.movie_rental_times[name_of_movie] += 1
            self.client_rental_times[client_name] += 1
        else:
            self.movie_rental_times[name_of_movie] = 1
            self.client_rental_times[client_name] = 1

    #Statistics section
    def get_number_of_rentals(self):
        """
        :return: Number of rentals(int)
        """
        return len(self.rental_data)

    def get_number_of_clients(self):
        """
        :return: Dict of number of clients
        """
        return self.client_rental_times



