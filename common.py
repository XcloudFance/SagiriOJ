import json
fs=open("title.json","r")
a=fs.read()
a=json.loads(a)
fs.close()
print(a)
