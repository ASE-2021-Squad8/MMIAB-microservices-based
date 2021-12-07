import requests
import json

# indirizzo gateway
url = "127.0.0.1"

# porta gateway
port = "80"
address = "http://" + url + ":" + port + "/"


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
    # test get method that render the create_user html page
    endpoint = address + "create_user"
    reply = requests.get(endpoint)
    assert reply.status_code == 200

    # test post method that create a new user
    reply = requests.post(
        endpoint,
        data=dict(
            email=email,
            firstname=firstname,
            lastname=lastname,
            password=password,
            dateofbirth=dateofbirth,
        ),
        allow_redirects = True
    )
    assert reply.status_code == 200
    return reply


def test_login_user(email, password):
    # test get method that render the login html page
    endpoint = address + "login"
    reply = requests.get(endpoint)
    assert reply.status_code == 200

    # test post method which allows the user to login by entering credentials
    # test login with invalid credentials
    reply = requests.post(
        endpoint,
        json=dict(
            email="error@error.com",
            password="error",
        ),
        allow_redirects = True
    )
    assert reply.status_code == 200

    # test correct login
    reply = requests.post(
        endpoint,
        json=dict(
            email=email,
            password=password,
        ),
        allow_redirects = True
    )
    assert reply.status_code == 200
    return reply


def test_get_logout():
    endpoint = address + "logout"
    reply = requests.get(endpoint, allow_redirects = True)
    assert reply.status_code == 200
    return reply


def test_user_change_field(newemail, newfirstname, newlastname, newdateofbirth):
    # test get method that render the profile template of current user
    endpoint = address + "user/edit_profile"
    reply = requests.get(endpoint)
    assert reply.status_code == 200

    # test post method which allows a user to update his profile information
    reply = requests.post(
        endpoint,
        data=dict(
                email=newemail,
                firstname=newfirstname,
                lastname=newlastname,
                dateofbirth=newdateofbirth,
        ),
        allow_redirects = True
    )
    assert reply.status_code == 200
    return reply


def test_unregister(id):
    endpoint = address + "unregister/" + id
    reply = requests.get(endpoint, allow_redirects = True)
    print("CODE", reply.status_code)
    assert reply.status_code == 200
    return reply


def test_add_user_to_blacklist(id):
    endpoint = address + "blacklist"

    reply = requests.post(
        endpoint,
        json={"op": "add", "users": [id]},
    )
    assert reply.status_code == 200


def test_remove_user_from_blacklist(id):
    endpoint = address + "blacklist"

    reply = requests.post(
        endpoint,
        json={"op": "delete", "users": [id]},
    )
    assert reply.status_code == 200


def test_get_users_list():
    endpoint = address + "users"
    reply = requests.get(endpoint)
    assert reply.status_code == 200
    return reply


def test_user_change_password(_currentpassword, _newpassword):
    endpoint = address + "password"
    reply = requests.post(
        endpoint,
        data=dict(
            currentpassword=_currentpassword,
            newpassword=_newpassword,
            confirmpassword=_newpassword,
        ),
        allow_redirects = True
    )
    assert reply.status_code == 200
    return reply


def test_user_report(user_email_to_report):
    endpoint = address + "report"

    # test get method that render report page
    reply = requests.get(endpoint)
    assert reply.status_code == 200

    # test post method through which it is possible to make a report to a user
    reply = requests.post(
        endpoint,
        data=dict(
            useremail=user_email_to_report,
        ),
    )
    assert reply.status_code == 200


def test_content_filter():
    endpoint = address + "content_filter"

    # test get method that render the content filter page
    reply = requests.get(endpoint)
    assert reply.status_code == 200

    # test post method that allow to activate or deactivate content filter
    reply = requests.post(endpoint, data=dict(filter="true"), allow_redirects = True)
    assert reply.status_code == 200


def test_get_search_bar():
    endpoint = address + "search_bar"
    reply = requests.get(endpoint)
    assert reply.status_code == 200


def test_all_users_list():
    endpoint = address + "users"
    reply = requests.get(endpoint)
    assert reply.status_code == 200
