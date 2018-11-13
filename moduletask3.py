import json

x = [{
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}]

# convert into JSON:
y = json.dumps(x, indent = 2, sort_keys = True)
print y

#JSON string to python:
new = json.loads(y)
print new
