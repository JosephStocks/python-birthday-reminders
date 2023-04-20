from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

def send_sms(message_body):
    client = Client(os.environ.get("TWILIO_ACCOUNT_SID"), os.environ.get("TWILIO_AUTH_TOKEN"))

    return client.messages.create(
        from_=os.environ.get("TWILIO_SENDER_PHONE_NUMBER"),
        body=message_body,
        to=os.environ.get("JOES_PHONE_NUMBER")
    )
