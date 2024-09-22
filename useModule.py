import mymodule
import mymodule as mx
import platform
from mymodule import person1

mymodule.greeting("Jonathan")
a = mymodule.person1['age']
print(a)

b = mx.person1['name']
print(b)

x = platform.system()
print(x)

y = dir(platform)
print(y)

print(person1["age"])