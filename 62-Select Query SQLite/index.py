# Select Query, Order By & Limit
import sqlite3

conn = sqlite3.connect("sqlite.db")
data = conn.execute("SELECT * FROM Persons LIMIT 1, 4")

for n in data:
    print(n)