"""
The format() method formats the specified value(s) and insert them inside the string`s placeholder:
The placeholder is defined using curly brackets: {}. Read more about the placeholder in the Placeholder
section below.
"""

# Named Indexes:
txt1 = "Welcome to {} {}".format("Python", "Language")
print(txt1)

txt2 = "{0} in the {1} {2}".format("Hello", "Natural", "World!")
print(txt2)

txt3 = "Sum of {a:5} and {b:10} is equal to {r:15}!".format(a=10, b=20, r="result")
print(txt3)
# It means that:
"""
    a:5 means ___10
    b:10 means ________20
    r:15 means _________result
"""

txt4 = "Sum of {a:^6} and {b:<10} is equal to {r:>15}!".format(a=10, b=20, r="result")
print(txt4)
# It means that:
"""
    a:^6 means __10__
    b:<10 means 20________
    r:>15 means _________result
"""