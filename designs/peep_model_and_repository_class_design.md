# Makers Model and Repository Classes Design 


## 1. Design and create the Table

```
# EXAMPLE

Table: peeps
id: SERIAL
content: text
time_of_post: time
tags: text
maker_id: int
```

## 2. Create Test SQL seeds

```sql
-- see chitter_tables.sql
```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 The_Chitter_Challenge < chitter_tables.sql
```

## 3. Define the class names


```python
# Table name: peeps

# Model class
# (in lib/peep.py)
class Peep


# Repository class
# (in lib/peep_repository.py)
class PeepRepository

```

## 4. Implement the Model class


```python
# EXAMPLE
# Table name: peeps

# Model class
# (in lib/peep.py)

class Peep:
    def __init__(self):
        self.id = 0
        self.content= ""
        self.time_of_post = ""
        self.tags = "" or None
        self.maker_id = None


```

*You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.*

## 5. Define the Repository Class interface


```python
# Table name: peeps

# Repository class
# (in lib/peep_repository.py)

class PeepRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, content, time_of_post, tags, maker_id FROM peeps;

        # Returns an array of Peep objects.

        # Gets a single record by its ID
        # One argument: the id (number)
    def find(id):
        # Executes the SQL query:
        # SELECT id, content, time_of_post, tags, maker_id FROM peeps WHERE id = $1;

        # Returns a single Maker object.

        # Add more methods below for each operation you'd like to implement.

    # def create(maker)
    # 

    # def update(maker)
    # 

    # def delete(maker)
    # 

```

## 6. Write Test Examples

```python
# EXAMPLES

# 1
# Get all peeps

repo = PeepRepository()

peeps = repo.all()

len(peeps) # =>  3

peeps[0].id # =>  1
peeps[0].content # => 'John Jones ready to connect :)'
peeps[0].time_of_post # => '2024-04-26 15:36:38'
peeps[0].tags # => ['hello', greeting']
peeps[0].maker_id # => 1

peeps[1].id # =>  2
peeps[1].content # => 'Where is ma shotgun?'
peeps[1].time_of_post # => '2024-04-26 12:15:45'
peeps[1].tags # => ['funny', 'sarah']
peeps[1].maker_id # => 2

peeps[2].id # =>  3
peeps[2].content # => 'Hi Folks! Wanna see my lunch?'
peeps[2].time_of_post # => '2024-04-21 11:22:13'
peeps[2].tags # => ['greeting', 'lunch']
peeps[2].maker_id # => 3
# 2
# Get a single maker

repo = PeepRepository()

peep = repo.find(1)

peep.id # =>  1
peep.content # => 'John Jones ready to connect :)'
peep.time_of_post # => '2024-04-26 15:36:38'
peep.tags # => ['hello', greeting']
peep.maker_id # => 1


# Add more examples for each method
```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
