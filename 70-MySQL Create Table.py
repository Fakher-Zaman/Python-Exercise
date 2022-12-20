import pymysql as database

myobj = database.connect(host="localhost", user="root", password="", database="testdb")
cursorObj = myobj.cursor()

try:
    db = '''
    CREATE TABLE testdb (
        ID int PRIMARY KEY,
        Name varchar(255),
        Email varchar(255),
        City varchar(255)
    );
    '''
    cursorObj.execute(db)

except:
    print("Table created successfully!")