from lib.peep_repository import PeepRepository
from lib.peep import Peep

"""
When we call PeepRepository#all
We get a list of Maker objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/chitter_tables.sql") # Seed our database with some test data
    repository = PeepRepository(db_connection) # Create a new ArtistRepository

    peeps = repository.all() # Get all artists

    # Assert on the results
    print("PEEPS ======= ", peeps)
    assert peeps == [
        Peep(1, 'John Jones ready to connect', '2024-04-26 15:36:38', ['hello', 'greeting'], 1),
        Peep(2, 'Where is ma shotgun?', '2024-04-26 12:15:45', ['funny', 'sarah'], 2),
        Peep(3, 'Hi Folks! Wanna see my lunch?', '2024-04-21 11:22:13', ['greeting', 'lunch'], 3)
    ]

"""
When we call MakerRepository#find
We get a single Maker object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/chitter_tables.sql") # Seed our database with some test data
    repository = PeepRepository(db_connection) # Create a new ArtistRepository

    peep = repository.find(1)
    assert peep ==  Peep(1, 'John Jones ready to connect', '2024-04-26 15:36:38', ['hello', 'greeting'], 1)