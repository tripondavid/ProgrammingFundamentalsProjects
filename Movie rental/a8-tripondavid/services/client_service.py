from domain.client import Client

class ClientService:
    def __init__(self, client_repo, validator):
        self._client_repo = client_repo
        self._validator = validator

    def add_client(self, client_id :int, name :str):
        """
        Accesses the client repo in order to add a client
        :param client_id: Client id
        :param name: Name of the client
        """
        new_client = Client(client_id, name)
        self._client_repo.add_client(new_client)

    def remove_client(self, client_id :int):
        """
        Accesses the client repo in order to remove a client
        :param client_id: Client id
        """
        client_list = self.list_client().copy()

        for obj in client_list:
            if client_list[obj].client_id == client_id:
                self._client_repo.remove_client(obj)


    def update_client(self, client_id :int, new_name :str):
        """
        Accesses the client repo in order to update the name of a client
        :param client_id: Client id
        :param new_name: New name of the client
        """
        client_list = self.list_client().copy()

        for obj in client_list:
            if client_list[obj].client_id == client_id:
                client_list[obj].client_name = new_name
                new_client = client_list[obj]
                self._client_repo.update_client(obj, new_client)

    def list_client(self):
        """
        Accesses the client repo in order to list the clients
        :return: Dict of clients
        """
        return self._client_repo.get_all_clients()

    def search_client(self, parameter: str):
        """
        Accesses the client repo in order to search for a specific client
        :param parameter: User input
        :return: List that matched the parameter(case-insensitive, partial string matching)
        """
        client_list = self.list_client().copy()
        match_list = []

        if parameter.isnumeric():
            for obj in client_list:
                if parameter in str(client_list[obj].client_id):
                    match_list.append(client_list[obj])
        else:
            for obj in client_list:
                if (parameter.lower()) in client_list[obj].client_name.lower():
                    match_list.append(client_list[obj])

        return match_list

