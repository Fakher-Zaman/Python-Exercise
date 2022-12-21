import pymysql as database
mysql = database.connect(host="localhost", user="root", password="", database="school")

mycursor = mysql.cursor()
print("{:<20} {:<20} {:<20}".format("Count", "Name", "Class"))
print("{:<20} {:<20} {:<20}".format("-----", "----", "-----"))

try:
    query = "SELECT COUNT(*), Name, Class FROM students GROUP BY Class"
    mycursor.execute(query)
    mydata = mycursor.fetchall()
    
    for n in mydata:
        print("{:<20} {:<20} {:<20}".format(n[0], n[1], n[2]))

except:
    print("Something Went Wrong!")