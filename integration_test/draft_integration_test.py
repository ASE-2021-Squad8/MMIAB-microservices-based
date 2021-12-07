import requests
from requests.api import request
import io
import json

from requests.models import encode_multipart_formdata

# indirizzo gateway
url = "127.0.0.1"

# porta gateway
port = "80"
address = "http://" + url + ":" + port + "/"


def test_get_message_draft():
    endpoint = "message/draft"
    reply = requests.get(endpoint)
    assert reply.status_code == 200
    return reply.json()


def test_save_message_draft(recipient, text, delivery_date):
    endpoint = "message/draft"
    reply = requests.post(
        endpoint,
        json={
                "recipient": recipient,
                "text": text,
                "delivery_date": delivery_date,
                "attachment": (
                    io.BytesIO(b"This is a JPG file, I swear!"),
                    "test.jpg",
                ),
                "draft_id": "",
            },
    )
    assert reply.status_code == 302


def test_delete_message_draft(msg_id):
    endpoint = "message/draft/" + msg_id
    reply = requests.delete(endpoint)

    assert reply.status_code == 200
