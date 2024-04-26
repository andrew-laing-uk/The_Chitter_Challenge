# Makers Model and Repository Classes Design 


## 1. Design and create the Table

```
# EXAMPLE

Table: makers
id: SERIAL
full_name: text
username: text
user_email: text
user_password: text
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
# Table name: makers

# Model class
# (in lib/maker.py)
class Maker


# Repository class
# (in lib/maker_repository.py)
class MakerRepository

```

## 4. Implement the Model class


```python
# EXAMPLE
# Table name: makers

# Model class
# (in lib/maker.py)

class Maker:
    def __init__(self):
        self.id = 0
        self.full_name= ""
        self.username = ""
        self.user_email = ""
        self.user_password = ""


```

*You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.*

## 5. Define the Repository Class interface


```python
# Table name: makers

# Repository class
# (in lib/maker_repository.py)

class MakerRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, full_name, username, user_email, user_password FROM makers;

        # Returns an array of Maker objects.

        # Gets a single record by its ID
        # One argument: the id (number)
    def find(id):
        # Executes the SQL query:
        # SELECT id, null_name, username, user_email, user_password FROM makers WHERE id = $1;

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

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# 1
# Get all makers

repo = MakerRepository()

makers = repo.all()

len(makers) # =>  3

makers[0].id # =>  1
makers[0].full_name # =>  'John Jones'
makers[0].username # =>  'jonesy'
makers[0].user_email # =>  'jjones@email.com'
makers[0].user_password # =>  'password123'

makers[1].id # =>  2
makers[1].full_name # =>  'Sarah Connor'
makers[1].username # =>  'sconnor'
makers[1].user_email # =>  'sarahc123@email.com'
makers[1].user_password # =>  'password456'

makers[2].id # =>  3
makers[2].full_name # =>  'Soirse Flaherty'
makers[2].username # =>  'saucyf'
makers[2].user_email # =>  'soirsef@email.com'
makers[2].user_password # =>  'qwertyuiop'
# 2
# Get a single maker

repo = makerRepository()

maker = repo.find(1)

maker.id # =>  1
maker.full_name # =>  'John Jones'
maker.username # =>  'jonesy'
maker.user_email # =>  'jjones@email.com'
maker.user_password # =>  'password123'

# Add more examples for each method
```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
