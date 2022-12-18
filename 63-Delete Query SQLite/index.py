# Delete Query:
import sqlite3

conn = sqlite3.connect("sqlite.db")
PID = input("Enter the Person ID: ")
conn.execute("DELETE FROM Persons WHERE PersonID=" + PID)
conn.commit()
conn.close()