# Link: https://www.sqlshack.com/different-approaches-to-sql-join-multiple-tables/

import sqlite3
conn = sqlite3.connect("join.db")
# conn.execute('''
# CREATE TABLE Employees (
#     Employee_id int, 
#     Employee_name varchar(250), 
#     Employee_DOB date, 
#     Department_ID int
# );
# ''')

# conn.execute('''
# CREATE TABLE Departments (
#     Department_id int, 
#     Department_Name varchar(250)
# );
# ''')

# insert = '''
# INSERT INTO Departments (Department_id,Department_Name)
# VALUES (1,'Human Resources'), (2,'Development'), (3,'Sales'), (4, 'Technical Support')
# '''

# insert = '''
# INSERT INTO Employees(Employee_id,Employee_name, Employee_DOB,Department_ID)
# VALUES (1,'Alan Smith','19890101',1),
#        (2,'Sultan Nader','19920101',1),
#        (3,'Mohd Rasheed','19990101',2),
#        (4,'Brian Wallace','19790101',3),
#        (5,'Peter Hilton','19860101',NULL)
# '''
# conn.execute(insert)

# ----------> Inner Join Product
# data = conn.execute('''
# SELECT Employee_id,Employee_name, Employee_DOB, Department_Name
# FROM Departments INNER JOIN Employees
# ON Departments.Department_id = Employees.Department_ID
# ''')

# ----------> Left Join Product
data = conn.execute('''
SELECT Employee_id,Employee_name, Employee_DOB, Department_Name
FROM Employees LEFT JOIN Departments
ON Departments.Department_id = Employees.Department_ID
''')

# ----------> Right Join Product
# data = conn.execute('''
# SELECT Employee_id,Employee_name, Employee_DOB, Department_Name
# FROM Employees RIGHT JOIN Departments
# ON Departments.Department_id = Employees.Department_ID
# ''')

for n in data:
    print(n)