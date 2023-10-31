import json
import logging

import requests

from .load_env import get_env_var


def send_signal_message(message_body: str) -> None:
    try:
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
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
    else:
        logging.info("Signal message sent successfully")
