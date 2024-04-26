-- File: chitter_tables.sql

DROP TABLE IF EXISTS makers CASCADE;
DROP SEQUENCE IF EXISTS makers_id_seq;
DROP TABLE IF EXISTS peeps;
DROP SEQUENCE IF EXISTS peeps_id_seq;


CREATE SEQUENCE IF NOT EXISTS makers_id_seq;
CREATE TABLE makers (
  id SERIAL PRIMARY KEY,
  full_name text,
  username text,
  user_email text,
  user_password text
);


CREATE SEQUENCE IF NOT EXISTS peeps_id_seq;
CREATE TABLE peeps (
  id SERIAL PRIMARY KEY,
  content text,
  time_of_post timestamp,
  tags text,
-- The foreign key
  maker_id int,
  constraint fk_maker foreign key(maker_id)
    references makers(id)
    on delete cascade
);

INSERT INTO makers (full_name, username, user_email, user_password) 
     VALUES ('John Jones', 'jonesy', 'jjones@email.com', 'password123');
INSERT INTO makers (full_name, username, user_email, user_password) 
     VALUES ('Sarah Connor', 'sconnor', 'sarahc123@email.com', 'password456');
INSERT INTO makers (full_name, username, user_email, user_password) 
     VALUES ('Soirse Flaherty', 'saucyf', 'soirsef@email.com', 'qwertyuiop');


INSERT INTO peeps (content, time_of_post, tags, maker_id) 
     VALUES ('John Jones ready to connect', '2024-04-26 15:36:38', 'hello, greeting', 1);
INSERT INTO peeps (content, time_of_post, tags, maker_id) 
     VALUES ('Where is ma shotgun?', '2024-04-26 12:15:45', 'funny, sarah', 2);
INSERT INTO peeps (content, time_of_post, tags, maker_id) 
     VALUES ('Hi Folks! Wanna see my lunch?', '2024-04-21 11:22:13', 'greeting, lunch', 3);
