import json
import os

import requests
from dotenv import load_dotenv


def send_signal_message(message_body: str) -> None:
    try:
        SENDER_PHONE_NUMBER = os.environ["SENDER_PHONE_NUMBER"]
        RECIPIENTS_PHONE_NUMBERS_LIST = json.loads(
            os.environ["RECIPIENTS_PHONE_NUMBERS_LIST"]
        )
        ENDPOINT = os.environ["SIGNAL_SEND_MESSAGE_ENDPOINT"]
    except KeyError as e:
        raise ValueError(f"Environment variable {e} not set.") from e

    data = {
        "message": message_body,
        "number": SENDER_PHONE_NUMBER,
        "recipients": RECIPIENTS_PHONE_NUMBERS_LIST,
    }
    response = requests.post(ENDPOINT, json=data)

    response.raise_for_status()
