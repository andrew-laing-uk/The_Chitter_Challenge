from lib.maker import Maker

"""
Maker constructs with an id, title, release_year and artist_id
"""
def test_makers_construct():
    maker = Maker(1, "Test Name", "Test Username", 
                  "test@email.com", "password123")
    assert maker.id == 1
    assert maker.full_name == "Test Name"
    assert maker.username == "Test Username"
    assert maker.user_email == "test@email.com"
    assert maker.user_password == "password123"

"""
We can format makers to strings nicely
"""
def test_makers_format_nicely():
    maker = Maker(1, "Test Name", "Test Username", 
                  "test@email.com", "password123")
    assert str(maker) == "Maker(1, Test Name, Test Username, test@email.com, password123)"


"""
We can compare two identical makers
And have them be equal
"""
def test_makers_are_equal():
    maker_1 = Maker(1, "Test Name", "Test Username", 
                  "test@email.com", "password123")
    maker_2 = Maker(1, "Test Name", "Test Username", 
                  "test@email.com", "password123")
    assert maker_1 == maker_2

"""
An instance can be validated
"""
def test_artist_validity():
    assert Maker(1, "", "", "", "").is_valid() == False
    assert Maker(1, "", "sdfffs", "sdfsdf", "sdfdf").is_valid() == False
    assert Maker(1, "dfsdf", "", "sdfsdf", "sdfsdf").is_valid() == False
    assert Maker(1, "sdfsdf", "sdfsdf", "", "sdfsdf").is_valid() == False
    assert Maker(1, "sdfsdf", "sdfsdf", "sdfsdf", "").is_valid() == False
    assert Maker(1, None, "sdfffs", "sdfsdf", "sdfdf").is_valid() == False
    assert Maker(1, "dfsdf", None, "sdfsdf", "sdfsdf").is_valid() == False
    assert Maker(1, "sdfsdf", "sdfsdf", None, "sdfsdf").is_valid() == False
    assert Maker(1, "sdfsdf", "sdfsdf", "sdfsdf", None).is_valid() == False

    assert Maker(1, "Test Name",  "Test Username", "test@email.com", 
                 "password123").is_valid() == True
    assert Maker(None, "Test Name", "Test Username", "test@email.com", 
                 "password123").is_valid() == True

"""
We can generate errors for an invalid Maker
"""
def test_maker_errors():
    assert Maker(1, "", "", "", "").generate_errors() == "Full Name can't be blank, Username can't be blank, Email can't be blank, Password can't be blank"
    assert Maker(1, "", "sdfffs", "sdfsdf", "sdfdf").generate_errors() == "Full Name can't be blank"
    assert Maker(1, "dfsdf", "", "sdfsdf", "sdfsdf").generate_errors() == "Username can't be blank"
    assert Maker(1, "sdfsdf", "sdfsdf", "", "sdfsdf").generate_errors() == "Email can't be blank"
    assert Maker(1, "sdfsdf", "sdfsdf", "sdfsdf", "").generate_errors() == "Password can't be blank"
    assert Maker(1, None, "sdfffs", "sdfsdf", "sdfdf").generate_errors() == "Full Name can't be blank"
    assert Maker(1, "dfsdf", None, "sdfsdf", "sdfsdf").generate_errors() == "Username can't be blank"
    assert Maker(1, "sdfsdf", "sdfsdf", None, "sdfsdf").generate_errors() == "Email can't be blank"
    assert Maker(1, "sdfsdf", "sdfsdf", "sdfsdf", None).generate_errors() == "Password can't be blank"

    assert Maker(1, "Test Name", 
                 "Test Username", "test@email.com", 
                 "password123").generate_errors() == None
    assert Maker(None, "Test Name", 
                 "Test Username", "test@email.com", 
                 "password123").generate_errors() == None

"""
User can log in
"""  
def test_log_in():
    maker = Maker(1, "Test Name", "Test Username", 
                  "test@email.com", "password123")
    maker.log_in()
    assert maker.logged_in == True


"""
User can log out
"""  
def test_log_out():
    maker = Maker(1, "Test Name", "Test Username", 
                  "test@email.com", "password123")
    maker.log_out()
    assert maker.logged_in == False