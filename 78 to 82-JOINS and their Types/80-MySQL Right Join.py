import pymysql as database

# Server Connection or Database Connection:
mysql = database.connect(host="localhost", user="root", passwd="", database="prod-copy")
mycursor = mysql.cursor()

try:
    select = "SELECT qty, unit, count FROM brand RIGHT JOIN inventory ON brand.id = inventory.id"
    mycursor.execute(select)
    data = mycursor.fetchall()

    for n in data:    # n = tuple
        print("{:<15} {:<20} {:<15}".format(n[0], n[1], n[2]))

except:
    print("Something Went Wrong!")