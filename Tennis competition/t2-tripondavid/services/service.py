class Service:
    def __init__(self, repo):
        self._repo = repo

    def get_all_players(self):
        """
        Accesses the repo in order to get all the current players.
        :return: All players from the competition.
        """
        return self._repo.get_all_players()

    def order_descending(self):
        """
        Orders the players in descending order based on their playing strength.
        :return: Descending ordered list of players.
        """
        list_of_players = list(self.get_all_players())
        list_of_players.sort(key=lambda player: player.strength, reverse=True)

        return list_of_players

    def increase_player_strength(self, player, strength):
        """
       Increases the strength of a player with a certain amount.
        """
        #Time complexity O(n)
        list_of_players = self.get_all_players()
        for players in list_of_players:
            if players.id == player:
                players.strength += strength


    def remove_player(self, player):
        """
        Removes from repo a certain player.
        :param player: The player that needs to be removed.
        """
        self._repo.remove_player(player.id)



    def power_two(self, number):
        """
        Checks if a number is power of two.
        :param number: The number needed to be checked.
        :return: True if number is power of two, False otherwise.
        """
        if number % 2 == 1:
            return False
        if number == 0:
            return False
        if number == 1:
            return True
        while number % 2 == 0:
            number = number / 2
        if number == 1:
            return True
        return False


