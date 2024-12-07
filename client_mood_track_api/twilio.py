from client_mood_track_api.mongodb import MongoDBHandler


class TwilioHandler:

    def __init__(self):
        pass

    def send_confirmation_message(self, data):
        mongo_db = MongoDBHandler(data)
        client_data = mongo_db.get_client_info()
        phone_number = client_data.get("phoneNumber")
        client_name = client_data.get("name")
        print(f"Message for {client_name} sent at {phone_number}")
