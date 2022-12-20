import pymysql as database

# Server Connection or Database Connection:
mysql = database.connect(host="localhost", user="root", passwd="", database="testdb")
mycursor = mysql.cursor()
id = input("Enter the ID you want to delete: ")

delete = "DELETE FROM testdb WHERE ID=%s"
try:
    mycursor.execute(delete, id)
    mysql.commit()
    print("Delete data successfully!")
except:
    print("Something Went Wrong!")