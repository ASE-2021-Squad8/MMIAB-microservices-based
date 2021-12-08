import io

# gateway
url = "127.0.0.1"
port = "80"
address = "http://" + url + ":" + port + "/"


def test_get_message_draft(s):
    endpoint = address + "message/draft"
    reply = s.get(endpoint)
    assert reply.status_code == 200
    return reply.json()


def test_save_message_draft(s, recipient, text, delivery_date):
    endpoint = address + "message/draft"
    reply = s.post(
        endpoint,
        data=dict(
            recipient= recipient,
            text= text,
            delivery_date= delivery_date,
            attachment= "",
            draft_id= "",
        ),
        allow_redirects = True
    )
    assert reply.status_code == 200


def test_delete_message_draft(s, msg_id):
    endpoint = address + "api/message/draft/" + str(msg_id)
    reply = s.delete(endpoint)
    assert reply.status_code == 200
