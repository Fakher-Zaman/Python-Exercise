import json

# json type data:
jsonData = '{"course-namae": "python", "fee": 10000, "duration": "3-month"}'

dictData = json.loads(jsonData)
print(dictData)
print(type(dictData))

for n in dictData:
    print(n, dictData[n])
