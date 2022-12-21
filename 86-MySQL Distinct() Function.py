import pymysql as database
mysql = database.connect(host="localhost", user="root", password="", database="school")

mycursor = mysql.cursor()
print("{:<20}".format("Class"))
print("{:<20}".format("-----"))

try:
    query = "SELECT DISTINCT(Class) FROM students"
    mycursor.execute(query)
    mydata = mycursor.fetchall()
    
    for n in mydata:
        print("{:<20}".format(n[0]))

except:
    print("Something Went Wrong!")