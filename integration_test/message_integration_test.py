import requests
from requests.api import request
import json

#indirizzo gateway
url= "127.0.0.1"

#porta gateway
port="9999"
address=url+":"+port+"/"

def test_send_message(text,sender,recipient,media,delivery_date):
    endpoint="message"

    reply=request.get(endpoint)
    assert reply.status_code==200
    
    reply=request.post(
        endpoint,
        data= json.dump({
            "text": text,
            "sender": sender,
            "recipient": recipient,
            "media": media,
            "delivery_date": delivery_date
        })
    )
    assert reply.status_code==200   

def test_mailbox():
    endpoint = address+"message/mailbox"
    reply=request.get(endpoint)
    
    assert reply.status_code ==200

def test_get_message_by_id(msg_id):
    endpoint = address + "message" + str(msg_id)
    reply = requests.get(address)
    assert reply.status_code == 200
    return reply.get_json()

def test_received_messages_metadata():
    endpoint = address + "message/received/metadata"
    reply = requests.get(address)
    assert reply.status_code == 200
    return reply.get_json()

def test_sent_messages_metadata():
    endpoint = address + "message/sent/metadata"
    reply = requests.get(address)
    assert reply.status_code == 200
    return reply.get_json()

def test_retrieve_attachment(msg_id):
    endpoint = address  + "message/" + str(msg_id) + "/attachment"
    reply = requests.get(endpoint)
    assert reply.status_code == 200
    return reply.get_json()

def test_get_day_message(day, month, year):
    endpoint = address + "message/sent/" + str(day) + "/" + str(month)  + "/" + str(year)
    reply = requests.get(endpoint)
    assert reply.status_code == 200
    return reply.get_json()

def test_lottery_delete(msg_id):
    endpoint="lottery/"+msg_id
    reply=request.delete(endpoint)

    #401==Not enough points
    assert reply.status_code==401
    return reply.get_json()

def test_delete_received_message(msg_id):
    endpoint = address + "message/bin/" + str(msg_id)
    reply = endpoint.delete(endpoint)
    assert reply.status_code == 200

def test_render_calendar():
    endpoint = address + "message/calendar"
    reply = requests.get(endpoint)
    assert reply.status_code==200