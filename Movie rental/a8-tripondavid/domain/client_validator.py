class ClientValidator:
    def validate(self, client):
        if client.client_name.isnumeric():
            raise ValueError("Incorrect name.")
        if len(client.client_name) < 2:
            raise ValueError("Name too short.")
        