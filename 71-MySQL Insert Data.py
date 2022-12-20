import pymysql as database

mysql = database.connect(host="localhost", user="root", password="", database="testdb")
mycursor = mysql.cursor()

try:
    # ---> Method # 1:
    # db = "INSERT INTO testdb (ID, Name, Email, City) VALUES (1, 'Fakher Zaman', '034851fakherzaman@gmail.com', 'Lahore')"
    # db = "INSERT INTO testdb (ID, Name, Email, City) VALUES (2, 'Hammad Asif', '034928hammadasif@gmail.com', 'Narowal')"
    # db = "INSERT INTO testdb (ID, Name, Email, City) VALUES (3, 'Muhammad Shaban', '034936muhammadshaban@gmail.com', 'Kasur')"
    db = "INSERT INTO testdb (ID, Name, Email, City) VALUES (6, 'Moiz Ali', '034849moizali@gmail.com', 'Lahore')"
    mycursor.execute(db)

    # ---> Method # 2:
    # insert = "INSERT INTO testdb (ID, Name, Email, City) VALUES (%s, %s, %s)"
    # rows = [(7, 'Noman Arif', 'rnanomanarifh@gmail.com', 'Narowal'),
    #         (8, 'Muhammad Ali', 'muhammadalihajvery@gmail.com', 'Kasur')]
    # mycursor.executemany(insert, rows)

    mysql.commit()
    print("Insert Data Successfully!")

except:
    print("Something Went Wrong!")