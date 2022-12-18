import json

# json type data:
jsonData = '{"course-namae": "python", "fee": 10000, "duration": "3-month"}'

file = open("write.json", "w")
getData = file.write(jsonData)
finalData = json.dumps(getData)

print(finalData)
print(type(finalData))

for n in finalData:
    print(n)