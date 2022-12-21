# Equi Join similar to the Inner Join but Syntax Changed:
import pymysql as database

# Server Connection or Database Connection:
mysql = database.connect(host="localhost", user="root", passwd="", database="prod-copy")
mycursor = mysql.cursor()

try:
    select = "SELECT * FROM invertory AS i1, inventory AS i2 WHERE i1.id = i2.id"
    mycursor.execute(select)
    data = mycursor.fetchall()

    for n in data:    # n = tuple
        print(n)

except:
    print("Something Went Wrong!")