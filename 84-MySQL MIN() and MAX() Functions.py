import pymysql as database
mysql = database.connect(host="localhost", user="root", password="", database="testdb")

mycursor = mysql.cursor()
print("{:<20}".format("Salary"))
print("{:<20}".format("----"))

try:
    # query = "SELECT MIN(Salary) FROM testdb"
    query = "SELECT MAX(Salary) FROM testdb"
    mycursor.execute(query)
    mydata = mycursor.fetchall()
    
    for n in mydata:
        print("{:<20}".format(n[0]))

except:
    print("Something Went Wrong!")