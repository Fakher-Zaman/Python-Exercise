import pymysql as database

# Server Connection or Database Connection:
mysql = database.connect(host="localhost", user="root", passwd="", database="testdb")
mycursor = mysql.cursor()

print("{:<5} {:<20} {:<25} {:<10}".format("ID", "Name", "Email", "City"))

try:
    select = "SELECT * FROM testdb ORDER BY ID DESC LIMIT 0,2"
    mycursor.execute(select)
    data = mycursor.fetchall()

    for n in data:    # n = tuple
        print(n)

except:
    print("Something Went Wrong!")