import integration_test.users_integration_test as itu
import integration_test.message_integration_test as itm
import integration_test.draft_integration_test as dtm
from datetime import datetime, timedelta
import time

# test rendering the index page
itu.test_home()

# test create first user
itu.test_create_user("test1@test1.com", "test1", "test1", "test", "1111-1-1")
# test create second user
itu.test_create_user("test2@test2.com", "test2", "test2", "test", "1111-1-1")

# test login wituh user test1
itu.test_login_user("test1@test1.com", "test")

# test rendering settings page
itu.test_settings()

itu.test_user_change_field("test1.1@test1.com", "test1.1", "test1.1", "1111-1-1")

# test blacklist
# insert user 2 in blacklist
itu.test_add_user_to_blacklist(2)

itu.test_remove_user_from_blacklist(2)

# test change password
itu.test_user_change_password("test1", "1test")
itu.test_get_logout()
itu.test_login_user("test1@test1.com", "1test")

# test report user 2
itu.test_user_report("test2@test2.com")

# test content filter
itu.test_content_filter()

# test render the search user page
itu.test_get_search_bar()

# test endpoing that retrive all users
reply = itu.test_all_users_list()

# test send message
now = datetime.now()
delivery_date = now + timedelta(seconds=62)
itm.test_send_message("hello hello", 2, 1, "", delivery_date.strftime("%Y-%m-%dT%H:%M"))

# waiting for the message to arrive
print("Sleeping for 70 seconds, waiting for the message delivery...")
time.sleep(70)

# get a message by id
reply = itm.test_get_message_by_id(1)
assert reply["text"] == "hello hello"

# retrieve mailbox page
itm.test_mailbox()

# get message sent
reply = itm.test_sent_messages_metadata()
assert reply[0]["sender"] == 1

# retrieve attachment
reply = itm.test_retrieve_attachment(1)
assert reply["attachment"] == None

# retrieve message sent in a day
current_day = datetime.now()
year = current_day.year
month = current_day.month
day = current_day.day

reply = itm.test_get_day_message(day, month, year)
assert "hello hello" in reply[0]["text"]

# test to delete a message with the lottery bonus without enought points
itm.test_lottery_delete(1)

# save a draft
now = datetime.now()
delivery_date = now + timedelta(days=10)
dtm.test_save_message_draft(2, "draft msg", delivery_date)


# get all user draft
reply = dtm.test_get_message_draft()

assert reply[0]["sender"] == 1

# delete a draft
dtm.test_delete_message_draft(2)


# logout
itu.test_get_logout()

# login with user 2
itu.test_login_user("test2@test2.com", "test2")


# get received message
reply = itm.test_received_messages_metadata()
assert reply[0]["sender"] == 0

# unregister user 2
itu.test_unregister(2)

# login user 1
itu.test_login_user("test1@test1.com", "test1.1")

# unregister user 1
itu.test_unregister(1)
