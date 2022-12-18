import json

file = open("post.json", "r")
getData = file.read()
finalData = json.loads(getData)

print(finalData)
print(type(finalData))

for n in finalData:
    print(n)