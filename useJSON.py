import json

x = '{"name":"John", "age": 30, "city":"New York"}'

y = json.loads(x)

print(type(y))
print(y["age"])

a = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

b = json.dumps(a)

print(type(b))
print(b)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.16))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))