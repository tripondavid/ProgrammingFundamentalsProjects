class Client:
    def __init__(self, client_id :int, name :str):
        self._client_id = client_id
        self._name = name

    @property
    def client_id(self):
        """
        :return: Client id
        """
        return self._client_id

    @property
    def client_name(self):
        """
        :return: Client name
        """
        return self._name

    @client_name.setter
    def client_name(self, new_name :str):
        """
        Changes the client name
        :param new_name: New name
        """
        self._name = new_name


    def __str__(self):
        return str(self._client_id) + " " + self._name