import pymysql as db

mysql = db.connect(host="localhost", user="root", password="", database="testdb")
pointer = mysql.cursor()
id = input("Enter the ID you want to update: ")

update = "UPDATE testdb SET Name=%s, Email=%s, City=%s WHERE ID=%s"
data = ("Ahad Raza", "ahadrazamir@gmail.com", "Karachi", id)

try:
    pointer.execute(update, data)
    mysql.commit()
    print("Update Data Successfully!")

except:
    print("Something Went Wrong!")