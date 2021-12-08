# gateway
url = "127.0.0.1"
port = "80"
address = "http://" + url + ":" + port + "/"


def test_home(s):
    reply = s.get(address)
    assert reply.status_code == 200
    return reply


def test_settings(s):
    endpoind = address + "settings"
    reply = s.get(endpoind)
    assert reply.status_code == 200
    return reply


def test_create_user(s, email, firstname, lastname, password, dateofbirth):
    # test get method that render the create_user html page
    endpoint = address + "create_user"
    reply = s.get(endpoint)
    assert reply.status_code == 200

    # test post method that create a new user
    reply = s.post(
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


def test_login_user(s, email, password):
    # test get method that render the login html page
    endpoint = address + "login"
    reply = s.get(endpoint)
    assert reply.status_code == 200

    # test post method which allows the user to login by entering credentials
    # test login with invalid credentials
    reply = s.post(
        endpoint,
        json=dict(
            email="error@error.com",
            password="error",
        ),
        allow_redirects = True
    )
    assert reply.status_code == 200

    # test correct login
    reply = s.post(
        endpoint,
        json=dict(
            email=email,
            password=password,
        ),
        allow_redirects = True
    )
    assert reply.status_code == 200
    return reply


def test_get_logout(s):
    endpoint = address + "logout"
    reply = s.get(endpoint, allow_redirects = True)
    assert reply.status_code == 200
    return reply


def test_user_change_field(s, newemail, newfirstname, newlastname, newdateofbirth):
    # test get method that render the profile template of current user
    endpoint = address + "user/edit_profile"
    reply = s.get(endpoint)
    assert reply.status_code == 200

    # test post method which allows a user to update his profile information
    reply = s.post(
        endpoint,
        data=dict(
            textemail=newemail,
            textfirstname=newfirstname,
            textlastname=newlastname,
            textbirth=newdateofbirth,
        ),
        allow_redirects = True
    )
    assert reply.status_code == 200
    return reply


def test_unregister(s, id):
    endpoint = address + "unregister"
    reply = s.get(endpoint, allow_redirects = True)
    assert reply.status_code == 200
    return reply


def test_add_user_to_blacklist(s, id):
    endpoint = address + "blacklist"
    reply = s.post(
        endpoint,
        json={"op": "add", "users": [id]},
    )
    assert reply.status_code == 200


def test_remove_user_from_blacklist(s, id):
    endpoint = address + "blacklist"
    reply = s.post(
        endpoint,
        json={"op": "delete", "users": [id]},
    )
    assert reply.status_code == 200


def test_get_users_list(s):
    endpoint = address + "users"
    reply = s.get(endpoint)
    assert reply.status_code == 200
    return reply


def test_user_change_password(s, _currentpassword, _newpassword):
    endpoint = address + "password"
    reply = s.post(
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


def test_user_report(s, user_email_to_report):
    endpoint = address + "report"

    # test get method that render report page
    reply = s.get(endpoint)
    assert reply.status_code == 200

    # test post method through which it is possible to make a report to a user
    reply = s.post(
        endpoint,
        data=dict(
            useremail=user_email_to_report,
        ),
    )
    assert reply.status_code == 200


def test_content_filter(s):
    endpoint = address + "content_filter"

    # test get method that render the content filter page
    reply = s.get(endpoint)
    assert reply.status_code == 200

    # test post method that allow to activate or deactivate content filter
    reply = s.post(endpoint, data=dict(filter="1"), allow_redirects = True)
    assert reply.status_code == 200


def test_get_search_bar(s):
    endpoint = address + "search_bar"
    reply = s.get(endpoint)
    assert reply.status_code == 200


def test_all_users_list(s):
    endpoint = address + "users"
    reply = s.get(endpoint)
    assert reply.status_code == 200
