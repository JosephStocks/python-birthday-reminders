import logging

import requests

from config import config


def send_signal_message(message_body: str) -> None:
    try:
        SENDER_PHONE_NUMBER = config["SENDER_PHONE_NUMBER"]
        RECIPIENTS_PHONE_NUMBERS_LIST = config["RECIPIENTS_PHONE_NUMBERS_LIST"]
        ENDPOINT = f"{config['SIGNAL_MESSAGING_REST_API_BASE_URL']}{config['SIGNAL_SEND_MESSAGE_RELATIVE_ENDPOINT']}"

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
