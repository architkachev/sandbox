import json

a = {"zsv": "asdv"}
b = {"c" : None}

a = json.dumps(a)
print a
b["c"] = a
a = json.loads(a)
b["c"] = a
print json.dumps(b)