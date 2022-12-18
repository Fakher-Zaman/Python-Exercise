# Insert Query - SQLite
import sqlite3
conn = sqlite3.connect("sqlite.db")

insert = '''
INSERT INTO Persons (PersonID, LastName, FirstName, Address, City)
VALUES (552, 'Shaban', 'Muhammad', 'Khudian', 'Kasur')
'''
conn.execute(insert)
conn.commit()
conn.close()
# INSERT INTO Persons (PersonID, LastName, FirstName, Address, City)
# VALUES (578, 'Zaman', 'Fakhar', 'Rachna Town', 'Lahore')