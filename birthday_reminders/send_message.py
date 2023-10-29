import json

import requests

from .load_env import get_env_var


def send_signal_message(message_body: str) -> None:
    SENDER_PHONE_NUMBER = get_env_var("SENDER_PHONE_NUMBER")
    RECIPIENTS_PHONE_NUMBERS_LIST = json.loads(
        get_env_var("RECIPIENTS_PHONE_NUMBERS_LIST")
    )
    ENDPOINT = get_env_var("SIGNAL_SEND_MESSAGE_ENDPOINT")

    data = {
        "message": message_body,
        "number": SENDER_PHONE_NUMBER,
        "recipients": RECIPIENTS_PHONE_NUMBERS_LIST,
    }
    response = requests.post(ENDPOINT, json=data)

    response.raise_for_status()
