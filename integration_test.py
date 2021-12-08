import integration_test.users_integration_test as itu
import integration_test.message_integration_test as itm
import integration_test.draft_integration_test as dtm
from datetime import datetime, timedelta
import time
import requests

# create request session for cookies
s = requests.Session()

# test rendering the index page
itu.test_home(s)

# test create first user
itu.test_create_user(s, "test1@test1.com", "test1", "test1", "test", "1111-1-1")
# test create second user
itu.test_create_user(s, "test2@test2.com", "test2", "test2", "test", "1111-1-1")

# test login with user test1
itu.test_login_user(s, "test1@test1.com", "test")

# test rendering settings page
itu.test_settings(s)

itu.test_user_change_field(s, "test1.1@test1.com", "test1.1", "test1.1", "1111-1-1")

# test blacklist
# insert user 2 in blacklist
itu.test_add_user_to_blacklist(s, 2)

itu.test_remove_user_from_blacklist(s, 2)

# test change password
itu.test_user_change_password(s, "test", "1test")
itu.test_get_logout(s)
itu.test_login_user(s, "test1.1@test1.com", "1test")

# test report user 2
itu.test_user_report(s, "test2@test2.com")

# test content filter
itu.test_content_filter(s)

# test render the search user page
itu.test_get_search_bar(s)

# test endpoing that retrive all users
reply = itu.test_all_users_list(s)

# test send message
now = datetime.now()
delivery_date = now + timedelta(seconds=62)
itm.test_send_message(s, "hello hello", 2, 1, "", delivery_date.strftime("%Y-%m-%dT%H:%M"))

# waiting for the message to arrive
print("Sleeping for 70 seconds, waiting for the message delivery...")
time.sleep(70)

# get a message by id
reply = itm.test_get_message_by_id(s, 1)
assert reply["text"] == "hello hello"

# retrieve mailbox page
itm.test_mailbox(s)

# get message sent
reply = itm.test_sent_messages_metadata(s)
assert reply[0]["sender"] == 1

# retrieve attachment
reply = itm.test_retrieve_attachment(s, 1)
assert reply["attachment"] == ""

# retrieve message sent in a day
current_day = datetime.now()
year = current_day.year
month = current_day.month
day = current_day.day

reply = itm.test_get_day_message(s, day, month, year)
assert "hello hello" in reply[0]["text"]

# test to delete a message with the lottery bonus without enough points
reply = itm.test_lottery_delete(s, 1)
assert reply["message_id"] == -1

# save a draft
now = datetime.now()
delivery_date = now + timedelta(days=10)
dtm.test_save_message_draft(s, 2, "draft msg", delivery_date.strftime("%Y-%m-%dT%H:%M"))

# get all user draft
reply = dtm.test_get_message_draft(s)
assert reply[0]["sender"] == 1

# delete a draft
dtm.test_delete_message_draft(s, 2)

# logout
itu.test_get_logout(s)

# login with user 2
itu.test_login_user(s, "test2@test2.com", "test")

# get received messages
reply = itm.test_received_messages_metadata(s)
assert len(reply) == 0

# unregister user 2
itu.test_unregister(s, 2)

# login user 1
itu.test_login_user(s, "test1@test1.com", "test1.1")

# unregister user 1
itu.test_unregister(s, 1)


print("\nTests successfull")
