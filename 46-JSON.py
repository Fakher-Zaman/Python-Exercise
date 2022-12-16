'''
JSON supports mainly 6 data types:
1. string
2. number
3. boolean
4. null
5. object
6. array

In Python, JSON exists as a string. For Example:
p = '{"name":"abc", "lang":["python", "java"]}'
'''

import json

# dictionary type data:
dictData = {
    'course_name':'python',
    'duration':'3-months'
}

jsonData = json.dumps(dictData)
print(jsonData)
print(type(jsonData))
