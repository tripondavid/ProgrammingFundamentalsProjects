class ClientRepository:
    def __init__(self):
        self.client_data = {}

    def get_all_clients(self):
        """
        :return: Dict of all clients
        """
        return self.client_data

    def add_client(self, new_client):
        """
        Add a client to the client repo
        :param new_client: New client
        """
        if new_client.client_id in self.client_data:
            raise ValueError("Client already in repo.")
        self.client_data[new_client.client_id] = new_client

    def remove_client(self, client_id):
        """
        Remove client from client repo
        :param client_id: Client id
        """
        self.client_data.pop(client_id)

    def update_client(self, client_id, updated_client):
        """
        Update client name
        :param client_id: Client id
        :param updated_client: Updated client
        """
        self.client_data[client_id] = updated_client
