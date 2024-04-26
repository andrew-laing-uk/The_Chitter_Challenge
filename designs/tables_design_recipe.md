# Tables Design

## 1. Extract nouns from the user stories or specification

```
# USER STORIES:

As a Maker
So that I can let people know what I am doing
I want to post a message (peep) to chitter

As a maker
So that I can see what others are saying
I want to see all peeps in reverse chronological order

As a Maker
So that I can better appreciate the context of a peep
I want to see the time at which it was made

As a Maker
So that I can post messages on Chitter as me
I want to sign up for Chitter

As a Maker
So that only I can post messages on Chitter as me
I want to log in to Chitter

As a Maker
So that I can avoid others posting messages on Chitter as me
I want to log out of Chitter

As a Maker
So that I can stay constantly tapped in to the shouty box of Chitter
I want to receive an email if I am tagged in a Peep
```

```
Nouns:

maker, full name, username, email, password
peep, content, time of posting, tags, maker id
```

## 2. Infer the Table Name and Columns

| Record         | Properties                            |
| -------------- | ------------------------------------- |
| maker          | full name, username, email, password
| peep           | content, time of post, tags, maker id

1. Name of the first table (always plural): `makers` 

    Column names: `full_name`, `username`, `user_email`, `user_password`

2. Name of the second table (always plural): `peeps` 

    Column names: `content`, `time_of_post`, `tags`, `maker_id`

## 3. Decide the column types

```
# EXAMPLE:

Table: makers
id: SERIAL
full_name: text
username: text
user_email: text
user_password: text


Table: peeps
id: SERIAL
content: text
time_of_post: timestamp
tags: text
maker_id: int
```

## 4. Decide on The Tables Relationship

```
1. Can one maker have many peeps? YES
2. Can one peep have many makers? NO

-> Therefore,
-> An maker HAS MANY peeps
-> A peep BELONGS TO a maker

-> Therefore, the foreign key is on the peeps table.
```

## 5. Write the SQL

```sql
-- file: chitter_tables.sql

-- Create the table without the foreign key first.
CREATE TABLE makers (
  id SERIAL PRIMARY KEY,
  full_name text,
  username text,
  user_email text,
  user_password text
);

-- Then the table with the foreign key second.
CREATE TABLE peeps (
  id SERIAL PRIMARY KEY,
  content text,
  time_of_post time,
  tags text,
-- The foreign key
  maker_id int,
  constraint fk_maker foreign key(maker_id)
    references makers(id)
    on delete cascade
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 The_Chitter_Challenge < chitter_tables.sql
```
