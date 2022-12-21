import pymysql as database
mysql = database.connect(host="localhost", user="root", password="", database="testdb")

mycursor = mysql.cursor()
print("{:<15} {:<15}".format("Name", "City"))
print("{:<15} {:<15}".format("----", "----"))

try:
    query = "SELECT Name, City FROM testdb WHERE ID BETWEEN 1 and 3"
    mycursor.execute(query)
    mydata = mycursor.fetchall()
    
    for n in mydata:
        print("{:<15} {:<20}".format(n[0], n[1]))

except:
    print("Something Went Wrong!")