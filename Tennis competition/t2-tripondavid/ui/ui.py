import random


class UI:
    def __init__(self, service):
        self._service = service

    def print_menu(self):
        print("Choose an option: \n"
              "1. Display all players sorted descending by their strength. \n"
              "2. Play the tournament. \n"
              "3. Exit application.")

    def user_command(self):
        command = int(input("> "))

        return command

    def run_menu(self):
        while True:
            self.print_menu()
            command = self.user_command()
            if command == 3:
                break
            else:
                self.options_command(command)

    def options_command(self, command):
        match command:
            case 1:
                self.display_players()
            case 2:
                self.tournament()
            case _:
                print("Wrong input.")

    def display_players(self):
        list_of_players = list(self._service.order_descending())

        for player in list_of_players:
            print(player)

    def tournament(self):
        """
        Tournament: we run the tournament here because we need user input and output.
        Every functionality of the program is still in service.
        """
        list_of_players = self._service.order_descending()
        number_of_total_players = len(list_of_players)

        if self._service.power_two(number_of_total_players) is True:
            print("Tournament rounds!")
            print("Last " + str(number_of_total_players))

            number_of_current_players = len(list_of_players)
            number_of_final_players = 1

            while number_of_current_players != number_of_final_players:
                #We use random in order to search for two players
                player_one = random.randint(number_of_final_players - 1, number_of_current_players - 1)
                player_two = random.randint(number_of_final_players - 1, number_of_current_players - 1)

                if player_one != player_two:
                    eliminated_player = self.request_input_for_tournament(list_of_players[player_one], list_of_players[player_two])

                    if eliminated_player != list_of_players[player_one]:

                        self._service.increase_player_strength(list_of_players[player_one].id, 1)
                    if eliminated_player != list_of_players[player_two]:
                        self._service.increase_player_strength(list_of_players[player_two].id, 1)

                    self._service.remove_player(eliminated_player)
                    number_of_current_players -= 1
                    list_of_players = self._service.order_descending()

            for player in list_of_players:
                print(str(player) + " is winner!")


        elif self._service.power_two(number_of_total_players) is False:
            print("Qualifying rounds!")
            print("Last " + str(number_of_total_players))

            number_of_current_players = len(list_of_players)
            number_of_rounds = 0

            while number_of_current_players > 0:
                if self._service.power_two(number_of_current_players) is False:
                    number_of_rounds += 1
                    number_of_current_players -= 1
                else:
                    break

            number_of_current_players = len(list_of_players)
            number_of_final_players = number_of_current_players - number_of_rounds

            while number_of_current_players != number_of_final_players:
                player_one = random.randint(number_of_final_players - 1, number_of_current_players - 1)
                player_two = random.randint(number_of_final_players - 1, number_of_current_players - 1)

                if player_one != player_two:
                    eliminated_player = self.request_input_for_tournament(list_of_players[player_one],
                                                                          list_of_players[player_two])

                    if eliminated_player != list_of_players[player_one]:
                        self._service.increase_player_strength(list_of_players[player_one].id, 1)
                    if eliminated_player != list_of_players[player_two]:
                        self._service.increase_player_strength(list_of_players[player_two].id, 1)

                    self._service.remove_player(eliminated_player)
                    number_of_current_players -= 1
                    list_of_players = self._service.order_descending()

            return self.tournament()

    def request_input_for_tournament(self, player_one, player_two):
        command = int(input("Insert the winner from the following players: " + str(player_one) + "(1) or  " + str(player_two) + "(2) "))

        if command == 1:
            return player_two
        elif command == 2:
            return player_one
        else:
            print("Wrong input.")
            return self.request_input_for_tournament(player_one, player_two)

