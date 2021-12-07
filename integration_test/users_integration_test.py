import requests
from requests.api import request
import json

#indirizzo gateway
url= "127.0.0.1"

#porta gateway
port="9999"
address=url+":"+port+"/"

def test_home():
    reply = requests.get(address)
    assert reply.status_code == 200
    return reply

def test_settings():
    endpoind = address + "settings"
    reply = requests.get(endpoind)
    assert reply.status_code == 200
    return reply

def test_create_user(email, firstname, lastname, password, dateofbirth):
    #test get method that render the create_user html page
    endpoint = address + "create_user"
    reply = requests.get(endpoint)
    assert reply.status_code == 302
    
    #test post method that create a new user
    reply=requests.post(
            endpoint,
            data=dict(
                email = email,
                firstname = firstname,
                lastname = lastname,
                password = password,
                dateofbirth = dateofbirth,
            ),
            follow_redirects=True,
        )
    assert reply.status_code == 302
    return reply

def test_login_user(email, password):
    #test get method that render the login html page
    endpoint = address + "login"
    reply = requests.get(endpoint)
    assert reply.status_code == 200

    #test post method which allows the user to login by entering credentials
    #test login with invalid credentials
    reply=requests.post(
            endpoint,
            data=dict(
                email="error@error.com",
                password="error",
            ),
            follow_redirects=True,
        )
    assert reply.status_code == 200
    
    #test correct login
    reply=requests.post(
            endpoint,
            data=dict(
                email=email,
                password=password,
            ),
            follow_redirects=True,
        )
    assert reply.status_code == 302
    return reply
def test_get_logout():
    endpoint = address + "logout"
    reply = requests.get(endpoint)
    assert reply.status_code == 302
    return reply

def test_user_change_field(newemail, newfirstname, newlastname, newdateofbirth):
    #test get method that render the profile template of current user
    endpoint = address + "user"
    reply = requests.get(endpoint)
    assert reply.status_codes == 200
    
    #test post method which allows a user to update his profile information
    reply = request.post(
        endpoint,
        data = json.dumps({
                "email": newemail,
                "firstname": newfirstname,
                "lastname": newlastname,
                "dateofbirth": newdateofbirth
                })
        )
    assert reply.status_code == 200
    return reply

def test_unregister(id):
    endpoint= address + "unregister" +"/" +id
    reply= request.get(endpoint)
    assert reply.status_code==302
    return reply

def test_add_user_to_blacklist(id):
    endpoint = address + "user/blacklist"

    reply=request.post(
            endpoint,
            data=json.dumps({"op": "add", "users": [id]}),
            content_type="application/json",
        )
    assert reply.status_code == 200
    return reply.get_json()

def test_remove_user_from_blacklist(id):
    endpoint = address + "user/blacklist"

    reply=request.post(
            endpoint,
            data=json.dumps({"op": "delete", "users": [id]}),
            content_type="application/json",
        )
    assert reply.status_code == 200
    return reply.get_json()
    
def test_get_users_list():
    endpoint = address + "users"
    reply = requests.get(endpoint)
    assert reply.status_code == 200
    return reply

def test_user_change_password(_currentpassword, _newpassword):
   
    endpoint=address+"user/password"
    reply= request.post(
            endpoint,
            data=dict(
                currentpassword=_currentpassword,
                newpassword=_newpassword,
                confirmpassword=_newpassword,
            ),
            follow_redirects=True,
        )
    assert reply.status_code == 200
    return reply



def test_user_report(user_email_to_report):
    endpoint = address + "user/report"

    #test get method that render report page
    reply = requests.get(endpoint)
    assert reply.status_code == 200
    
    #test post method through which it is possible to make a report to a user
    reply = requests.post(endpoint,
                data=dict(
                useremail="test_user_not_exists@test.com",
            ),
        )
    assert reply.status_code == 200

def test_content_filter():
    endpoint=address+"/user/content_filter"

    #test get method that render the content filter page
    reply = requests.get(endpoint)
    assert reply.status_code == 200

    #test post method that allow to activate or deactivate content filter
    reply = requests.post(
        endpoint, data=dict(filter="true"), follow_redirects=True
    )
    assert reply.status_code ==200

def test_get_search_bar():
    endpoint = address + "/user/search_bar"
    reply = request.get(endpoint)
    assert reply.status_code == 200

    

def test_all_users_list():
    endpoint = address + "/user/list"
    reply = request.get(address)
    assert reply.status_code == 200
    return reply.get_json()
    
    