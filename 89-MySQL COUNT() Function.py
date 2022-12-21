import pymysql as database
mysql = database.connect(host="localhost", user="root", password="", database="testdb")

mycursor = mysql.cursor()

try:
    query = "SELECT COUNT(Salary) FROM testdb"
    mycursor.execute(query)
    mydata = mycursor.fetchall()
    
    for n in mydata:
        print("Total Count: ", n[0])

except:
    print("Something Went Wrong!")