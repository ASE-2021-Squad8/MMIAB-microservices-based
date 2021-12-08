# gateway 
url = "127.0.0.1"
port = "80"
address = "http://" + url + ":" + port + "/"


def test_send_message(s, text, sender, recipient, media, delivery_date):
    endpoint = address + "message"

    reply = s.get(endpoint)
    assert reply.status_code == 200

    msg = dict(
        text=text,
        sender=sender,
        recipient=[recipient],
        attachment=media,
        delivery_date=delivery_date,
        timezone="+01:00",
        draft_id=""
    )
    reply = s.post(
        endpoint,
        data=msg,
    )
    assert reply.status_code == 200


def test_mailbox(s):
    endpoint = address + "message/mailbox"
    reply = s.get(endpoint)
    assert reply.status_code == 200


def test_get_message_by_id(s, msg_id):
    endpoint = address + "message/" + str(msg_id)
    reply = s.get(endpoint)
    assert reply.status_code == 200
    return reply.json()


def test_get_messages_metadata(s):
    endpoint = address + "received/metadata"
    reply = s.get(endpoint)
    assert reply.status_code == 200
    return reply.json()


def test_retrieve_attachment(s, msg_id):
    endpoint = address + "message/" + str(msg_id) + "/attachment"
    reply = s.get(endpoint)
    assert reply.status_code == 200
    return reply.json()


def test_get_day_message(s, day, month, year):
    endpoint = address + "api/calendar/" + str(day) + "/" + str(month) + "/" + str(year)
    reply = s.get(endpoint)
    assert reply.status_code == 200
    return reply.json()


def test_lottery_delete(s, msg_id):
    endpoint = address + "lottery/" + str(msg_id)
    reply = s.delete(endpoint)
    return reply.json()


def test_delete_received_message(s, msg_id):
    endpoint = address + "message/bin/" + str(msg_id)
    reply = s.delete(endpoint)
    assert reply.status_code == 200


def test_render_calendar(s):
    endpoint = address + "message/calendar"
    reply = s.get(endpoint)
    assert reply.status_code == 200


def test_received_messages_metadata(s):
    endpoint = address + "received/metadata"
    reply = s.get(endpoint)
    assert reply.status_code == 200
    return reply.json()


def test_sent_messages_metadata(s):
    endpoint = address + "sent/metadata"
    reply = s.get(endpoint)
    assert reply.status_code == 200
    return reply.json()
