import datetime
from domain.rental import Rental

class RentalService:
    def __init__(self, rental_repo, movie_repo, client_repo):
        self._rental_repo = rental_repo
        self._movie_repo = movie_repo
        self._client_repo = client_repo

    def get_all_rentals(self):
        """
        Accesses the rental repo in order to get all current rentals
        :return: Dict of current rentals
        """
        return self._rental_repo.get_all_rentals()

    def movie_available(self, movie):
        """
        Accesses the rental repo in order to check if a movie is available
        :param movie: Movie
        :return: True if the movie is available, False otherwise
        """
        list_of_rentals = self.get_all_rentals().copy()
        if movie.movie_id not in self._movie_repo.get_all_movies():
            #print("primul if")
            return False
        for obj in list_of_rentals:
            if movie.movie_id == list_of_rentals[obj].movie_id:
                if list_of_rentals[obj].returned_date is None:
                    #print("al doilea if")
                    return False
                if datetime.datetime.strptime(str(movie.rented_date), '%Y-%m-%d').date() < datetime.datetime.strptime(str(list_of_rentals[obj].returned_date), '%Y-%m-%d').date():
                    #print(datetime.datetime.strptime(str(movie.rented_date), '%Y-%m-%d').date())
                    #print(datetime.datetime.strptime(str(list_of_rentals[obj].returned_date), '%Y-%m-%d').date())
                    #print("al treilea if")
                    return False
                if datetime.datetime.strptime(str(movie.due_date), '%Y-%m-%d').date() < datetime.datetime.strptime(str(list_of_rentals[obj].rented_date), '%Y-%m-%d').date():
                    #print("al patrulea if")
                    return False
        return True

    def client_registered(self, client_id):
        """
        Accesses the client repo in order to check if the client is registered
        :param client_id: Client id
        :return: True if client is registered, False otherwise
        """
        if client_id not in self._client_repo.get_all_clients():
            return False
        return True

    def add_rental(self, rental_id: int, movie_id: int, client_id: int, rented_date: datetime, due_date: datetime):
        """
        Accesses the rental repo in order to add a new rental
        :param rental_id: Rental id
        :param movie_id: Movie id
        :param client_id: Client id
        :param rented_date: Renting start date
        :param due_date: Renting end date
        """
        new_rental = Rental(rental_id, movie_id, client_id, rented_date, due_date)

        all_movies = self._movie_repo.get_all_movies().copy()
        all_clients = self._client_repo.get_all_clients().copy()
        movie_name = None
        client_name = None
        for obj in all_movies:
            if all_movies[obj].get_movie_id == movie_id:
                movie_name = all_movies[obj].get_title
                break
        for obj in all_clients:
            if all_clients[obj].client_id == client_id:
                client_name = all_clients[obj].client_name
                break


        if (self.movie_available(new_rental) is True) and (self.client_registered(client_id) is True) and movie_name != None and client_name != None:
            self._rental_repo.add_rental(new_rental, movie_name, client_name)
        else:
            print("Not available for renting.")

    def return_rental(self, rental_id: int):
        self._rental_repo.return_rental(rental_id)


    #Statistics section
    def get_rentals_by_times(self):
        """
        Accesses the rental repo in order to get rental by number of times rented
        :return: Dict of rental by number of times
        """
        return self._rental_repo.get_rentals_by_times()

    def get_number_of_clients(self):
        """
        Accesses the rental repo in order to get the number of clients that have rented at least a movie
        :return: Length(int) of the number of total clients
        """
        return self._rental_repo.get_number_of_clients()

    def most_rented_movies(self):
        """
        Calculates top 3 most rented movies
        :return: List of top 3 most rented movies in descending order
        """
        list_of_rentals = self.get_rentals_by_times().copy()
        most_rented_movies = []
        first_movie_int = 0
        second_movie_int = 0
        third_movie_int = 0
        for obj in list_of_rentals:
            if list_of_rentals[obj] >= first_movie_int:
                third_movie_int = second_movie_int
                second_movie_int = first_movie_int
                first_movie_int = list_of_rentals[obj]
            elif list_of_rentals[obj] >= second_movie_int:
                third_movie_int = second_movie_int
                second_movie_int = list_of_rentals[obj]
            elif list_of_rentals[obj] >= third_movie_int:
                third_movie_int = list_of_rentals[obj]

        for obj in list_of_rentals:
            if list_of_rentals[obj] == first_movie_int and (obj not in most_rented_movies):
                most_rented_movies.append(obj)
                break

        for obj in list_of_rentals:
            if list_of_rentals[obj] == second_movie_int and (obj not in most_rented_movies):
                most_rented_movies.append(obj)
                break

        for obj in list_of_rentals:
            if list_of_rentals[obj] == third_movie_int and (obj not in most_rented_movies):
                most_rented_movies.append(obj)
                break

        return most_rented_movies


    def most_active_clients(self):
        """
        Calculates top 3 most active clients
        :return: List of top 3 most active clients in descending order
        """
        list_of_clients = self.get_number_of_clients()
        most_active_clients = []
        first_client_int = 0
        second_client_int = 0
        third_client_int = 0
        for obj in list_of_clients:
            if list_of_clients[obj] >= first_client_int:
                third_client_int = second_client_int
                second_client_int = first_client_int
                first_client_int = list_of_clients[obj]
            elif list_of_clients[obj] >= second_client_int:
                third_client_int = second_client_int
                second_client_int = list_of_clients[obj]
            elif list_of_clients[obj] >= third_client_int:
                third_client_int = list_of_clients[obj]

        for obj in list_of_clients:
            if list_of_clients[obj] == first_client_int and (obj not in most_active_clients):
                most_active_clients.append(obj)
                break

        for obj in list_of_clients:
            if list_of_clients[obj] == second_client_int and (obj not in most_active_clients):
                most_active_clients.append(obj)
                break

        for obj in list_of_clients:
            if list_of_clients[obj] == third_client_int and (obj not in most_active_clients):
                most_active_clients.append(obj)
                break

        return most_active_clients

    def late_rentals(self):
        """
        Calculates late rentals
        :return: List of late rentals in descending order
        """
        list_of_rentals = self.get_all_rentals().copy()
        list_of_late_rentals = []
        list_difference_rentals = []
        for obj in list_of_rentals:
            if (list_of_rentals[obj].returned_date is None) and (datetime.datetime.strptime(str(list_of_rentals[obj].due_date), '%Y-%m-%d').date() < datetime.datetime.today().date()):
                list_of_late_rentals.append(list_of_rentals[obj])

        for obj in list_of_late_rentals:
            d1 = datetime.datetime.strptime(str(obj.due_date), '%Y-%m-%d').date()
            d2 = datetime.datetime.today().date()
            list_difference_rentals.append(d2-d1)

        for i in range(len(list_difference_rentals)):
            for j in range(i+1, len(list_difference_rentals)):
                if list_difference_rentals[i] < list_difference_rentals[j]:
                    list_difference_rentals[i], list_difference_rentals[j] = list_difference_rentals[j], list_difference_rentals[i]
                    list_of_late_rentals[i], list_of_late_rentals[j] = list_of_late_rentals[j], list_of_late_rentals[i]

        return list_of_late_rentals


