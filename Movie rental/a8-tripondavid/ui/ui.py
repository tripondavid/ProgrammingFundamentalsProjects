import datetime

class UI:
    def __init__(self, client_service, movie_service, rental_service):
        self._client_service = client_service
        self._movie_service = movie_service
        self._rental_service = rental_service

    def print_menu(self):
        print("1. Manage clients and movies. \n"
              "2. Rent or return a movie. \n"
              "3. Search for clients or movies using any of their fields. \n"
              "4. Create statistics. \n"
              "5. Exit application. ")

    def user_command(self):
        command = input("> ")
        return command

    def run_menu(self):
        while True:
            self.print_menu()
            command = self.user_command()
            if command == "5":
                break
            else:
                self.options_command(command)


    # Manage UI section
    def manage_menu(self):
        print("1. Add. \n"
              "2. Remove. \n"
              "3. Update. \n"
              "4. List.")
        command = self.user_command()
        match command:
            case "1":
                self.manage_add()
            case "2":
                self.manage_remove()
            case "3":
                self.manage_update()
            case "4":
                self.manage_list()
            case _:
                print("Wrong command.")

    def manage_add(self):
        print("1. Clients. \n"
              "2. Movies.")
        command = self.user_command()
        match command:
            case "1":
                self.add_client()
            case "2":
                self.add_movie()
            case _:
                print("Wrong command.")

    def add_client(self):
        client_id_command = int(input("Insert the client id: "))
        client_name_command = input("insert the client name: ")
        self._client_service.add_client(client_id_command, client_name_command)

    def add_movie(self):
        movie_id_command = int(input("Insert the movie id: "))
        movie_title_command = input("Insert the movie title: ")
        movie_description_command = input("Insert the movie description: ")
        movie_genre_command = input("Insert the movie genre: ")
        self._movie_service.add_movie(movie_id_command, movie_title_command, movie_description_command, movie_genre_command)

    def manage_remove(self):
        print("1. Clients. \n"
              "2. Movies.")
        command = self.user_command()
        match command:
            case "1":
                self.remove_client()
            case "2":
                self.remove_movie()
            case _:
                print("Wrong command.")

    def remove_client(self):
        client_id_command = int(input("Insert the client id: "))
        self._client_service.remove_client(client_id_command)

    def remove_movie(self):
        movie_id_command = int(input("Insert the movie id: "))
        self._movie_service.remove_movie(movie_id_command)

    def manage_update(self):
        print("1. Clients. \n"
              "2. Movies.")
        command = self.user_command()
        match command:
            case "1":
                self.update_client()
            case "2":
                self.update_movie()
            case _:
                print("Wrong command.")

    def update_client(self):
        client_id_command = int(input("Insert the client id: "))
        client_name_command = input("Insert the new name: ")
        self._client_service.update_client(client_id_command, client_name_command)

    def update_movie(self):
        movie_id_command = int(input("insert the movied id: "))
        movie_description_command = input("Insert the new description: ")
        self._movie_service.update_movie(movie_id_command, movie_description_command)

    def manage_list(self):
        print("1. Clients. \n"
              "2. Movies.")
        command = self.user_command()
        match command:
            case "1":
                self.list_clients()
            case "2":
                self.list_movies()
            case _:
                print("Wrong command.")

    def list_clients(self):
        print(self._client_service.list_client())

    def list_movies(self):
        print(self._movie_service.list_movie())



    #Rent and return UI section
    def rent_and_return_movie_menu(self):
        print("1. Rent a movie. \n"
              "2. Return a movie. ")
        command = self.user_command()
        match command:
            case "1":
                self.rent_movie_menu()
            case "2":
                self.return_movie_menu()
            case _:
                print("Wrong command.")

    def rent_movie_menu(self):
        rental_id = int(input("Specify the rental id: "))
        movie_id = int(input("Specify the movie id: "))
        client_id = int(input("Specify the client id: "))
        rented_date = input("Specify the rented date(format -> yyyy-mm-dd): ")
        due_date = input("Specify the due date(format -> yyyy-mm-dd): ")
        self._rental_service.add_rental(rental_id, movie_id, client_id, rented_date, due_date)


    def return_movie_menu(self):
        rental_id = int(input("Specify the rental id for return: "))
        self._rental_service.return_rental(rental_id)



    #Search for movies or clients UI section
    def search_menu(self):
        print("1. Search for movie. \n"
              "2. Search for client. ")
        command = self.user_command()
        match command:
            case "1":
                self.search_movie_menu()
            case "2":
                self.search_client_menu()
            case _:
                print("Wrong command.")

    def search_movie_menu(self):
        print("Specify one of the following options: movie_id, title, description or genre: ")
        search_movie_command = self.user_command()
        print(self._movie_service.search_movie(search_movie_command))

    def search_client_menu(self):
        print("Specify the client id or the name: ")
        search_client_command = self.user_command()
        print(self._client_service.search_client(search_client_command))



    #Statistics UI section
    def statistics_menu(self):
        print("1. Most rented movies. \n"
              "2. Most active clients. \n"
              "3. Late rentals. ")
        command = self.user_command()
        match command:
            case "1":
                self.most_rented_statistics_menu()
            case "2":
                self.most_active_clients_statistics_menu()
            case "3":
                self.late_rentals_menu()
            case _:
                print("Wrong command.")

    def most_rented_statistics_menu(self):
        print(self._rental_service.most_rented_movies())

    def most_active_clients_statistics_menu(self):
        print(self._rental_service.most_active_clients())

    def late_rentals_menu(self):
        print(self._rental_service.late_rentals())




    def options_command(self, user_command):
        match user_command:
            case "1":
                self.manage_menu()
            case "2":
                self.rent_and_return_movie_menu()
            case "3":
                self.search_menu()
            case "4":
                self.statistics_menu()
            case _:
                print("Wrong command.")