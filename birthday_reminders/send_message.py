import requests
from dotenv import load_dotenv

load_dotenv()


def send_signal_message(message_body: str):
    data = {
        "message": message_body,
        "number": "+19035203470",
        "recipients": ["+19035203470"],
    }
    response = requests.post("http://192.168.55.32:8080/v2/send", json=data)
    print(response.status_code)
    print(response.text)
