import pymysql as database

# Server Connection or Database Connection:
mysql = database.connect(host="localhost", user="root", passwd="", database="prod-copy")
mycursor = mysql.cursor()

print("{:<15} {:<20}".format("id", "name"))
print("{:<15} {:<20}".format("--", "----"))

try:
    select = "SELECT * FROM brand LEFT JOIN inventory ON brand.id = inventory.id"
    mycursor.execute(select)
    data = mycursor.fetchall()

    for n in data:    # n = tuple
        print("{:<15} {:<20}".format(n[0], n[1]))

except:
    print("Something Went Wrong!")