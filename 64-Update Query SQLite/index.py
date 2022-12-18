# Update Query:
import sqlite3

conn = sqlite3.connect("sqlite.db")
conn.execute('''
UPDATE Persons SET LastName='Fakhar', City='Lahore' WHERE PersonID=582
''')

conn.commit()
conn.close()