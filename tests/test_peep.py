from lib.peep import Peep

"""
Peep constructs with an id, content, time_of_post, 
                        tags and maker_id
"""
def test_peeps_construct():
    peep = Peep(1, "Test Content", "2024-04-26 15:36:38", 
                  ["tag1", "tag2"], 1)
    assert peep.id == 1
    assert peep.content == "Test Content"
    assert peep.time_of_post == "2024-04-26 15:36:38"
    assert peep.tags == ["tag1", "tag2"]
    assert peep.maker_id== 1

"""
We can format Peeps to strings nicely
"""
def test_Peeps_format_nicely():
    peep = Peep(1, "Test Content", "2024-04-26 15:36:38", 
                  ["tag1", "tag2"], 1)
    assert str(peep) == "Peep(1, Test Content, 2024-04-26 15:36:38, ['tag1', 'tag2'], 1)"


"""
We can compare two identical Peeps
And have them be equal
"""
def test_Peeps_are_equal():
    peep_1 = Peep(1, "Test Content", "2024-04-26 15:36:38", 
                  ["tag1", "tag2"], 1)
    peep_2 = Peep(1, "Test Content", "2024-04-26 15:36:38", 
                  ["tag1", "tag2"], 1)
    assert peep_1 == peep_2