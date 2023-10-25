import json
import os

import requests
from dotenv import load_dotenv


def get_env_var(var_name: str) -> str:
    try:
        return os.environ[var_name]
    except KeyError as e:
        raise ValueError(f"Environment variable {e} not set.") from e


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
