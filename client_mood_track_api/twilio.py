from client_mood_track_api.mongodb import MongoDBHandler
from client_mood_track_api.config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_CONTENT_SID,
    TWILIO_FROM_WHATSAPP,
)
from twilio.rest import Client


class TwilioHandler:

    def __init__(self):
        pass

    def get_client_data_to_message(self, data):
        mongo_db = MongoDBHandler(data)
        client_data = mongo_db.get_client_info()
        return client_data.get("phoneNumber"), client_data.get("name")

    def send_confirmation_message(self, data):
        phone_number, client_name = self.get_client_data_to_message(data)
        TO_PHONE_NUMBER = f"whatsapp:{phone_number}"
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # Message with template
        # message = client.messages.create(
        # from_= TWILIO_FROM_WHATSAPP,
        # content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
        # content_variables='{"1":"12/1","2":"3pm"}',
        # to=TO_PHONE_NUMBER
        # )

        # Send Whatsapp Message
        message = client.messages.create(
            from_=TWILIO_FROM_WHATSAPP,
            body=f"{client_name}, thank you for your feedback! We have received your evaluation and appreciate your input.",
            to=TO_PHONE_NUMBER,
        )

        # Send Sms
        client.api.account.messages.create(
            to=TO_PHONE_NUMBER,
            from_=TWILIO_FROM_WHATSAPP,
            body=f"{client_name}, thank you for your feedback! We have received your evaluation and appreciate your input.",
        )

        print(f"Message for {client_name} sent at {phone_number}")
        print(f"Message Sid: {message.sid}")
