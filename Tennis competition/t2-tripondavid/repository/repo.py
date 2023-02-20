from domain.player import Player

class Repo:
    def __init__(self):
        self._data = {}
        try:
            self._data = read_text_file("proba.txt")
            print("File accessed.")
        except ValueError:
            print("Can't access file.")

    def get_all_players(self):
        """
        :return: Returns the values which contain all players.
        """
        return self._data.values()

    def remove_player(self, id):
        """
        Removes a player from dict.
        :param id: Id of the player that needs to be eliminated.
        """
        self._data.pop(id)




def read_text_file(file_name):
    """
    Tries to open and take the elements of a file(reading mode).
    :param file_name: Name of the file needed to be used.
    :return: The elements from the file if it can be opened, ValueError otherwise.
    """
    try:
        result = {}
        f = open(file_name, "r")
        line = f.readline().strip()
        while len(line) > 0:
            line = line.split(",")
            player = Player(int(line[0]), line[1], int(line[2]))
            result[player.id] = player
            line = f.readline().strip()
        f.close()
        return result
    except ValueError:
        print("Can't access file.")