import pytest
from posts import Postmanager 

@pytest.fixture
def fake_database():
    return { "4047": {  
      "name": "Testuser",
    "dob": "2006-07-21",
    "gender": "male",
    "hash_password": "paul3553",
    "friends": [],
    "friend_requests": [] ,
    "sent_requests": [],
    "posts": [] }
    }
    
def test_add_post(fake_database):
    user_id="Paul"
    content="Hello world"
    manager=Postmanager(content , "4047" ,  fake_database , "10:55")
    post=manager.add_post(content, "post_db.json")
    print(post)
    assert post["content"]==content
    assert len(fake_database["4047"]["posts"])==1
    assert post["timestamp"] == "10:55"
    assert "posts" in fake_database["4047"]
    assert post in fake_database["4047"]["posts"]
    
def test_show_post(fake_database,capsys):
    content="Hello world"
    manager=Postmanager(content , "4047" ,   fake_database , "13:34:12")
    post=manager.add_post(content, "post_db.json")
    post=manager.show_all_posts( "post_db.json")
    
    captured=capsys.readouterr()
    assert "Hello world" in captured.out
    assert "No posts yet" not in captured.out
                  
         