import json
x = '''[{"name": "John", "divorced": "false", "cars": [{"mpg": 27.5, "model": "BMW 230"},
	{"mpg": 24.1, "model": "Ford Edge"}], "age": 30, "married": "true", "pets": "null", "children": ["Ann", "Billy"]}]'''
y = json.loads(x)
print (y)