'''
get into the postgres steps:
psql -U postgres -d postgres  /   psqlpostgres
and tap ur password

some keywords
1. Checking Available Tables in Terminal
1)  \l-- List all databases:

2)  \dt-- List tables inside a database:

3)  \du --This will list all users along with their roles and attributes

4)  \c or \connect- Connect to a database:
e.g. \c database_name;   (\c ) postgres  
您现在已经连接到数据库 "database_name",

5)  \q -- Exit PostgreSQL shell:


'''


'''
Basic PostgreSQL Commands
Operation Command Example Description
1.CREATE DATABASE mydb;(mydb is the name of the database)  ---Creates a new database named mydb .

2.CREATE TABLE users (id SERIAL, name TEXT);  --- Creates a table named 'users ' with an auto incrementing id and a text name .
3.INSERT INTO users (name) VALUES ('Alice');   ---Inserts a new row into the users table with the name "Alice".
4.SELECT * FROM users;  ---Retrieves all columns and rows from the users table.
响应做出的改变

5. UPDATE users SET name = 'Bob' WHERE id = 1;  ---Updates the name to "Bob" for the row where id is 1.

6. DELETE FROM users WHERE id = 1; ---Deletes the row from the users table where id is 1.

7. TRUNCATE TABLE users; ---Removes all rows from the users table

8. DROP TABLE users; --- Completely deletes the users table and its data from the database.

'''