import pymysql as database
mysql = database.connect(host="localhost", user="root", password="", database="testdb")

mycursor = mysql.cursor()

try:
    query = "SELECT Name, CITY FROM testdb WHERE id IN(1, 2)"
    # query = "SELECT Name, City FROM testdb WHERE id NOT IN(1, 2)"
    mycursor.execute(query)
    mydata = mycursor.fetchall()
    
    for n in mydata:
        print(n[0])

except:
    print("Something Went Wrong!")