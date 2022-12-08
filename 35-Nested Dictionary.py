# A collection of dictionaries into one single dictionary called Nested Dictionary.

# Created a Nested Dictionary
course = {
    'python': {'duration': '2 Months', 'fee': 15000},
    'c++': {'duration': '2 Months', 'fee': 15000},
    'java': {'duration': '2 Months', 'fee': 15000}
}
print(course)
course['python']['fee'] = 20000
print(course['c++']['fee'])
print("----------------------------------------------\n")

for n in course:
    print("Key: ", n)
    print("Value: ", course[n])
print("----------------------------------------------\n")

for n, m in course.items():
    print(n, m['duration'], m['fee'])
