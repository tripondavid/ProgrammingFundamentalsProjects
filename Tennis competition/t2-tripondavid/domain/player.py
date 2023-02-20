class Player:
    def __init__(self, id: int, name: str, strength: int):
        self._id = id
        self._name =name
        self._strength = strength

    @property
    def id(self):
        """
        :return: Returns the id of the player.
        """
        return self._id

    @property
    def name(self):
        """
        :return: Returns the name of the player.
        """
        return self._name

    @property
    def strength(self):
        """
        :return: Returns the strength of the player.
        """
        return self._strength

    @strength.setter
    def strength(self, value):
        """
        Changes the value of the playing strength of a player.
        :param value: The value that will be changed.
        """
        self._strength = value

    def __str__(self):
        return str(self._id) + " " + self._name + " " + str(self._strength)