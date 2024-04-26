from lib.maker_repository import MakerRepository
from lib.maker import Maker

"""
When we call MakerRepository#all
We get a list of Maker objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/chitter_tables.sql") # Seed our database with some test data
    repository = MakerRepository(db_connection) # Create a new ArtistRepository

    makers = repository.all() # Get all artists

    # Assert on the results
    assert makers == [
        Maker(1, 'John Jones', 'jonesy', 'jjones@email.com', 'password123'),
        Maker(2, 'Sarah Connor', 'sconnor', 'sarahc123@email.com', 'password456'),
        Maker(3, 'Soirse Flaherty', 'saucyf', 'soirsef@email.com', 'qwertyuiop')
    ]

"""
When we call MakerRepository#find
We get a single Maker object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/chitter_tables.sql") # Seed our database with some test data
    repository = MakerRepository(db_connection) # Create a new ArtistRepository

    maker = repository.find(1)
    assert maker == Maker(1, 'John Jones', 'jonesy', 'jjones@email.com', 'password123')


"""
We can check if a username is unique
"""
def test_unique_username(db_connection):
    db_connection.seed("seeds/chitter_tables.sql") # Seed our database with some test data
    repository = MakerRepository(db_connection) # Create a new ArtistRepository

    assert repository.username_is_unique('uniquesusername') == True

"""
We can check if a username already exists
"""
def test_duplicate_username(db_connection):
    db_connection.seed("seeds/chitter_tables.sql") # Seed our database with some test data
    repository = MakerRepository(db_connection) # Create a new ArtistRepository

    assert repository.username_is_unique('jonesy') == False

"""
We can check if an email is unique
"""
def test_unique_email(db_connection):
    db_connection.seed("seeds/chitter_tables.sql") # Seed our database with some test data
    repository = MakerRepository(db_connection) # Create a new ArtistRepository

    assert repository.email_is_unique('powwow@email.com') == True

"""
We can check if an email already exists
"""
def test_duplicate_email(db_connection):
    db_connection.seed("seeds/chitter_tables.sql") # Seed our database with some test data
    repository = MakerRepository(db_connection) # Create a new ArtistRepository

    assert repository.email_is_unique('jjones@email.com') == False