import pymysql as database

# Imp points for database connection (Passing 3 Arguments):
# 1 - Server Name: localhost
# 2 - User Name: root
# 3 = Password: ''

myobj = database.connect(host="localhost", user="root", password="")
cursorObj = myobj.cursor()

try:
    db = "CREATE DATABASE testDB;"
    cursorObj.execute(db)
    print("Database created successfully!")

except:
    print("Something went wrong with database!")