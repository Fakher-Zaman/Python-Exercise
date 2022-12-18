# Python - SQLite (DB Create and Connection)

import sqlite3
conn = sqlite3.connect("sqlite.db")
conn.execute('''
CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
''')
conn.close