import os

import requests
from dotenv import load_dotenv

load_dotenv()


def send_signal_message(message_body: str) -> None:
    try:
        PHONE_NUMBER = os.environ["JOES_PHONE_NUMBER"]
        ENDPOINT = os.environ["SIGNAL_SEND_MESSAGE_ENDPOINT"]
    except KeyError as e:
        raise ValueError(f"Environment variable {e} not set.") from e

    data = {
        "message": message_body,
        "number": PHONE_NUMBER,
        "recipients": [PHONE_NUMBER],
    }
    response = requests.post(ENDPOINT, json=data)

    response.raise_for_status()
