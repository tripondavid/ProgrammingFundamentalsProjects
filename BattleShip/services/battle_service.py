import random


class ComputerService:
    def __init__(self, data):
        self._player_data = data

    @staticmethod
    def random_attack():
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        return row, col

    def targeted_attack(self, row, col):
        if (row - 1 > 0) and (self._player_data.get_visibility(row - 1, col) is False) and (self._player_data.get_symbol(row - 1, col) == "x"):
            return row - 1, col
        elif (row + 1 < 10) and (self._player_data.get_visibility(row + 1, col) is False) and (self._player_data.get_symbol(row + 1, col) == "x"):
            return row + 1, col
        elif (col - 1 > 0) and (self._player_data.get_visibility(row, col - 1) is False) and (self._player_data.get_symbol(row, col - 1) == "x"):
            return row, col - 1
        elif (col + 1 > 0) and (self._player_data.get_visibility(row, col + 1) is False) and (self._player_data.get_symbol(row, col + 1) == "x"):
            return row, col + 1
        else:
            return -1, -1


class BattleService:
    def __init__(self, player_battlefield, computer_battlefield, computer_service):
        self._player_battlefield = player_battlefield
        self._player_score = 0
        self._computer_score = 0
        self._computer_battlefield = computer_battlefield
        self._computer_service = computer_service

    def zone_attacked_by_computer(self, row, col, last_attack: bool):
        visibility = self._player_battlefield.get_visibility(row, col)
        if visibility is True:
            self._computer_service.random_attack()
        else:
            symbol = self._player_battlefield.get_symbol(row, col)
            self._player_battlefield.set_visibility_true(row, col)
            if symbol == "x":
                if self.increase_computer_score() is True:
                    return True
            else:
                self._player_battlefield.set_symbol(row, col, "o")
        return False

    def zone_attacked_by_player(self, row, col):
        visibility = self._computer_battlefield.get_visibility(row, col)
        if visibility is True:
            print("Zone already attacked.")
        else:
            symbol = self._computer_battlefield.get_symbol(row, col)
            self._computer_battlefield.set_visibility_true(row, col)
            if symbol == "x":
                if self.increase_player_score() is True:
                    return True
            else:
                self._computer_battlefield.set_symbol(row, col, "o")
        return False

    def increase_player_score(self):
        self._player_score += 1
        if self._player_score == 17:
            return True
        return False

    def increase_computer_score(self):
        self._computer_score += 1
        if self._computer_score == 17:
            return True
        return False

    def check_ship_position_player(self, row, col, direction, length):
        try:
            i = row
            j = col
            if direction == "l":
                number = length
                while number != 0:
                    number -= 1
                    if j < 0:
                        return False
                    if self._player_battlefield.get_symbol(row, j) == "x":
                        return False
                    j -= 1
                return True
            elif direction == "r":
                number = length
                while number != 0:
                    number -= 1
                    if j >= 10:
                        return False
                    if self._player_battlefield.get_symbol(row, j) == "x":
                        return False
                    j += 1
                return True
            elif direction == "u":
                number = length
                while number != 0:
                    number -= 1
                    if i < 0:
                        return False
                    if self._player_battlefield.get_symbol(i, col) == "x":
                        return False
                    i -= 1
                return True
            elif direction == "d":
                number = length
                while number != 0:
                    number -= 1
                    if i >= 10:
                        return False
                    if self._player_battlefield.get_symbol(i, col) == "x":
                        return False
                    i += 1
                return True
        except ValueError:
            print("Incorrect direction.")

    def check_ship_position_computer(self, row, col, direction, length):
        try:
            i = row
            j = col
            if direction == "l":
                number = length
                while number != 0:
                    number -= 1
                    if j < 0:
                        return False
                    if self._computer_battlefield.get_symbol(row, j) == "x":
                        return False
                    j -= 1
                return True
            elif direction == "r":
                number = length
                while number != 0:
                    number -= 1
                    if j >= 10:
                        return False
                    if self._computer_battlefield.get_symbol(row, j) == "x":
                        return False
                    j += 1
                return True
            elif direction == "u":
                number = length
                while number != 0:
                    number -= 1
                    if i < 0:
                        return False
                    if self._computer_battlefield.get_symbol(i, col) == "x":
                        return False
                    i -= 1
                return True
            elif direction == "d":
                number = length
                while number != 0:
                    number -= 1
                    if i >= 10:
                        return False
                    if self._computer_battlefield.get_symbol(i, col) == "x":
                        return False
                    i += 1
                return True
        except ValueError:
            return False

    def set_player_ship(self, row, col, direction, length):
        i = row
        j = col
        if direction == "l":
            while length != 0:
                length -= 1
                self._player_battlefield.set_symbol(row, j, "x")
                j -= 1
        elif direction == "r":
            while length != 0:
                length -= 1
                self._player_battlefield.set_symbol(row, j, "x")
                j += 1
        elif direction == "u":
            while length != 0:
                length -= 1
                self._player_battlefield.set_symbol(i, col, "x")
                i -= 1
        elif direction == "d":
            while length != 0:
                length -= 1
                self._player_battlefield.set_symbol(i, col, "x")
                i += 1

    def set_computer_ship(self, row, col, direction, length):
        i = row
        j = col
        if direction == "l":
            while length != 0:
                length -= 1
                self._computer_battlefield.set_symbol(row, j, "x")
                j -= 1
        elif direction == "r":
            while length != 0:
                length -= 1
                self._computer_battlefield.set_symbol(row, j, "x")
                j += 1
        elif direction == "u":
            while length != 0:
                length -= 1
                self._computer_battlefield.set_symbol(i, col, "x")
                i -= 1
        elif direction == "d":
            while length != 0:
                length -= 1
                self._computer_battlefield.set_symbol(i, col, "x")
                i += 1

    def generate_random_ships_computer(self):
        number_of_ships_to_insert = 5
        ok1 = 0

        while number_of_ships_to_insert != 0:
            if number_of_ships_to_insert == 5:
                ok = False
                while ok is False:
                    position_row = random.randint(0, 9)
                    position_col = random.randint(0, 9)
                    direction_letters = ["l", "r", "u", "d"]
                    direction_number = random.randint(0, 3)
                    if self.check_ship_position_computer(position_row, position_col, direction_letters[direction_number], 5) is True:
                        self.set_computer_ship(position_row, position_col, direction_letters[direction_number], 5)
                        ok = True
            elif number_of_ships_to_insert == 4:
                ok = False
                while ok is False:
                    position_row = random.randint(0, 9)
                    position_col = random.randint(0, 9)
                    direction_letters = ["l", "r", "u", "d"]
                    direction_number = random.randint(0, 3)
                    if self.check_ship_position_computer(position_row, position_col, direction_letters[direction_number], 4) is True:
                        self.set_computer_ship(position_row, position_col, direction_letters[direction_number], 4)
                        ok = True
            elif number_of_ships_to_insert == 3 and ok1 == 1:
                ok = False
                while ok is False:
                    position_row = random.randint(0, 9)
                    position_col = random.randint(0, 9)
                    direction_letters = ["l", "r", "u", "d"]
                    direction_number = random.randint(0, 3)
                    if self.check_ship_position_computer(position_row, position_col, direction_letters[direction_number], 3) is True:
                        self.set_computer_ship(position_row, position_col, direction_letters[direction_number], 3)
                        ok = True
            elif number_of_ships_to_insert == 3 and ok1 == 0:
                ok = False
                while ok is False:
                    position_row = random.randint(0, 9)
                    position_col = random.randint(0, 9)
                    direction_letters = ["l", "r", "u", "d"]
                    direction_number = random.randint(0, 3)
                    if self.check_ship_position_computer(position_row, position_col, direction_letters[direction_number], 3) is True:
                        self.set_computer_ship(position_row, position_col, direction_letters[direction_number], 3)
                        ok = True
                        ok1 = 1
                        number_of_ships_to_insert += 1
            elif number_of_ships_to_insert == 2:
                ok = False
                while ok is False:
                    position_row = random.randint(0, 9)
                    position_col = random.randint(0, 9)
                    direction_letters = ["l", "r", "u", "d"]
                    direction_number = random.randint(0, 3)
                    if self.check_ship_position_computer(position_row, position_col, direction_letters[direction_number], 2) is True:
                        self.set_computer_ship(position_row, position_col, direction_letters[direction_number], 2)
                        ok = True
                        number_of_ships_to_insert = 1

            number_of_ships_to_insert -= 1

    def return_battlefield_computer(self):
        return str(self._computer_battlefield)

    def return_battlefield_player(self):
        return str(self._player_battlefield)