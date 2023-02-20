class UI:
    def __init__(self, service, computer):
        self._service = service
        self._computer = computer
        print("!Battleship!")

    def start(self):
        self.insert_ships()
        print()
        print("Let the fight begin!")
        print()
        self.start_war()

    @staticmethod
    def direction_input():
        print("Choose a command from the following ones in order to set the direction: left/right/up/down")
        direction = input("> ")
        direction = direction.lower()
        direction = direction.strip()

        match direction:
            case "left":
                return "l"
            case "right":
                return "r"
            case "up":
                return "u"
            case "down":
                return "d"
            case _:
                print("Wrong input for direction.")
                return -1

    @staticmethod
    def position_input():
        print("Choose a position by using a combination of the following format: A-J + 1-10. \n"
              "Example: A8.")
        position = input("> ")
        position = position.strip()

        if len(position) != 2 and len(position) != 3:
            print("Wrong input.")
            return -1, -1

        if position[0].upper() not in [chr(65+i) for i in range(10)]:
            print("Invalid position for row.")
            return -1, -1

        row = ord(position[0].upper()) - 65

        try:
            col = int(position[1:]) - 1
        except ValueError:
            print("Invalid position for column.")
            return -1, -1

        if col not in list(range(10)):
            print("Invalid position for column.")
            return -1, -1

        return row, col

    def insert_ships(self):
        number_of_ships_to_insert = 5
        ok1 = 0
        self._service.generate_random_ships_computer()

        while number_of_ships_to_insert != 0:
            if number_of_ships_to_insert == 5:
                ok = False
                while ok is False:
                    print("Choose where the Carrier will be: ")
                    position_row, position_col = self.position_input()
                    direction = self.direction_input()
                    if self._service.check_ship_position_player(position_row, position_col, direction, 5) is True:
                        print("Carrier set.")
                        self._service.set_player_ship(position_row, position_col, direction, 5)
                        ok = True
                    else:
                        print("Can't set Carrier here. Try again.")

            elif number_of_ships_to_insert == 4:
                ok = False
                while ok is False:
                    print("Choose where the Battleship will be: ")
                    position_row, position_col = self.position_input()
                    direction = self.direction_input()
                    if self._service.check_ship_position_player(position_row, position_col, direction, 4) is True:
                        print("Battleship set.")
                        self._service.set_player_ship(position_row, position_col, direction, 4)
                        ok = True
                    else:
                        print("Can't set Battleship here. Try again.")

            elif number_of_ships_to_insert == 3 and ok1 == 1:
                ok = False
                while ok is False:
                    print("Choose where the Submarine will be: ")
                    position_row, position_col = self.position_input()
                    direction = self.direction_input()
                    if self._service.check_ship_position_player(position_row, position_col, direction, 3) is True:
                        print("Submarine set.")
                        self._service.set_player_ship(position_row, position_col, direction, 3)
                        ok = True
                    else:
                        print("Can't set Submarine here. Try again.")

            elif number_of_ships_to_insert == 3 and ok1 == 0:
                ok1 = 1
                ok = False
                while ok is False:
                    print("Choose where the Destroyer will be: ")
                    position_row, position_col = self.position_input()
                    direction = self.direction_input()
                    if self._service.check_ship_position_player(position_row, position_col, direction, 3) is True:
                        print("Destroyer set.")
                        self._service.set_player_ship(position_row, position_col, direction, 3)
                        number_of_ships_to_insert += 1
                        ok = True
                    else:
                        print("Can't set Destroyer here. Try again.")

            elif number_of_ships_to_insert == 2:
                ok = False
                while ok is False:
                    print("Choose where the Patrol Boat will be: ")
                    position_row, position_col = self.position_input()
                    direction = self.direction_input()
                    if self._service.check_ship_position_player(position_row, position_col, direction, 2) is True:
                        print("Patrol Boat set.")
                        self._service.set_player_ship(position_row, position_col, direction, 2)
                        ok = True
                        number_of_ships_to_insert = 1
                    else:
                        print("Can't set Patrol Boat here. Try again.")

            number_of_ships_to_insert -= 1

    def start_war(self):
        winner = False
        last_attack = False

        while winner is False:
            row, col = self.position_input()
            if self._service.zone_attacked_by_player(row, col) is True:
                winner = True
                print("Player won!")
                break
            print("__Computer board__")
            print(self._service.return_battlefield_computer())
            print("__Computer board__")
            row, col = self._computer.random_attack()
            win_computer = self._service.zone_attacked_by_computer(row, col, last_attack)
            if win_computer is True:
                winner = True
                print("Computer won!")
                break
            print("__Player board__")
            print(self._service.return_battlefield_player())
            print("__Player board__")

