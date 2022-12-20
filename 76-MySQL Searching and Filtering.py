import pymysql as database

# Server Connection or Database Connection:
mysql = database.connect(host="localhost", user="root",
                         passwd="", database="testdb")
mycursor = mysql.cursor()

print("{:<5} {:<20} {:<25} {:<10}".format("ID", "Name", "Email", "City"))

try:
    name = input("Enter the Name: ")
    select = "SELECT * FROM testdb WHERE Name LIKE '%" + name + "%'"
    mycursor.execute(select)
    data = mycursor.fetchall()

    for n in data:    # n = tuple
        print(n)

except:
    print("Something Went Wrong!")
