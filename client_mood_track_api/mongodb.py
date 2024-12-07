import json


class MongoDBHandler:
    def __init__(self, data):
        self.data = data

    def get_client_info(self):
        user_name = self.data.get("userName")
        user_id = self.data.get("userId")
        # implement mongodb

        with open("mock_client_data.json", "r") as file:
            complete_data = json.load(file)

        print(f"Getting client {user_name} data by id {user_id}...")

        self.save_client_comment()

        return complete_data

    def save_client_comment(self):
        print("Saving user comment...")
