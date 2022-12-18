# Searching Query:
import sqlite3

name = input("Enter the First Name of Person: ")
conn = sqlite3.connect("sqlite.db")
# data = conn.execute("SELECT * FROM Persons WHERE FirstName='"+name+"'")
data = conn.execute("SELECT * FROM Persons WHERE FirstName LIKE '%"+name+"%'")
for n in data:
    print(n)