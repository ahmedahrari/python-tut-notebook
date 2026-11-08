
**1- What is variables**
	🌏 A variable in Python is a name that points to an object in memory. Unlike languages ​​like C or Java, in Python there is no need to declare the type of the variable and the type is automatically detected (Dynamic Typing).

```python

name = "Ahmed"      # String
age = 20          # int
height = 1.90     # Float
is_student = True # Boolean

```

**Variable naming rules**
	🌎 Can be including letters, numbers and etc....
	🔱 Don't start with number
	👻 Can not be keywords  ==>   if, else, for & etc.......
	🌐  Case sensitive (age ≠ Age)
	🏀 Convention: use snake_case   →   user_name

```python

# TRUE

user_name = "Sara"
_private = 10
count2 = 5

# FALSE
 2count = 5
 user-name = "Sara"
 class = 10

```


**2- Main data types**

	2-1 ==> Numbers

	🏛️ int
```python
a = 10
b = -25
c = 1_000_000      # Slicing for readable
d = 0b1010         # Binary
e = 0o17           # Octal
f = 0xFF           # Hexadecimal

print(type(a))     # <class 'int'>

```

	🔥 Float
```python
x = 3.14
y = -0.001
z = 2.5e3          # Scientific symbol → 2500.0
w = float('inf')   # Unlimited

print(0.1 + 0.2)   # 0.30000000000000004 (Floating path error)

```

	💫 Use the decimal module for high precision.


	✳️ Complex
```python
z = 3 + 4j
print(z.real)      # 3.0
print(z.imag)      # 4.0
print(abs(z))      # 5.0

```


	2-1 ==> String
		🌍 Strings is immutable

```python
s1 = 'Hello'
s2 = "World"
s3 = '''Multi line
string'''
s4 = """Ahmed
Ahrari"""

# f-string (The best way)
name = "Ahmedoo"
age = 25
print(f"{name} is {age} years old")   # Ali is 25 years old

# Operation
print("Hi" + " " + "there")   # Past
print("ab" * 3)                # ababab
print(len("Python"))           # 6
print("Python"[0])             # P (Index)
print("Python"[-1])            # n
print("Python"[1:4])           # yth (Cut)

# Important Methods
s = "  Hello World  "
print(s.strip())          # "Hello World"
print(s.upper())          # "  HELLO WORLD  "
print(s.lower())
print(s.replace("World", "Python"))
print(s.split())          # ['Hello', 'World']
print("-".join(["a", "b", "c"]))   # a-b-c
print("Hello".startswith("He"))    # True
print("Hello".find("ll"))          # 2

```


	2-2 ==> Bool
		❄️ Just have two value ( True or False )
```python
a = True
b = False
print(type(a))         # <class 'bool'>
print(True + True)  

```

		🌊 Falsy variables ==> These values ​​are considered False in conditions
```python
False, None, 0, 0.0, "", [], (), {}, set()

```


	2-4 ==> NoneType
		👽 Just have one value = None (NULL)
```python
x = None
print(type(x))     # <class 'NoneType'>
print(x is None)   # True

```


	2-5 ==> List
		🌕 An organized and changeable collection of items.
```python
fruits = ["apple", "banana", "cherry"]
mixed = [1, "two", 3.0, True, None]
nested = [[1, 2], [3, 4]]

# Access and Cut
print(fruits[0])       # apple
print(fruits[-1])      # cherry
print(fruits[0:2])     # ['apple', 'banana']

# Change
fruits[1] = "orange"

# Important Methods
fruits.append("date")          # Add to end
fruits.insert(1, "kiwi")       # Add in index
fruits.remove("apple")         # Remove with value
fruits.pop()                   # Remove endless
fruits.extend(["fig", "grape"])
fruits.sort()                  # In-place sorting
fruits.reverse()
print(fruits.index("kiwi"))
print(fruits.count("kiwi"))

```


	2-6 ==> Tuple
		💧 Like a list but immutable
```python
point = (3, 5)
single = (42,)          
empty = ()

print(point[0])         # 3
# point[0] = 10         # TypeError!

# unpacking
x, y = point
print(x, y)             # 3 5

# Methods
print(point.count(3))   # 1
print(point.index(5))   # 1

```


	2-7 ==> Set
		🫐 A collection without order and without repeating elements.
```python
s = {1, 2, 3, 3, 2}
print(s)               # {1, 2, 3}

s.add(4)
s.remove(1)
s.discard(100)         # Without error if nothing

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)           # Union {1, 2, 3, 4, 5}
print(a & b)           # Subscription {3}
print(a - b)           # difference {1,2}
print(a ^ b)           # Symmetric difference {1,2,4,5}

```
		🌶️ Immutable version
```python
fs = frozenset([1, 2, 3])
```


	2-7 ==> Dictonary
		🍅 A collection of key-value pairs.
```python
person = {
    "name": "Ali",
    "age": 25,
    "city": "Tehran"
}

# Access
print(person["name"])           # Ahmed
print(person.get("job"))        # None (Without Error)
print(person.get("job", "N/A")) # N/A

# Change
person["age"] = 26
person["job"] = "Engineer"

# Remove
del person["city"]
person.pop("job")

# Methods
print(person.keys())      # dict_keys(['name', 'age'])
print(person.values())    # dict_values(['Ali', 26])
print(person.items())     # dict_items([...])

# Navigation
for key, value in person.items():
    print(f"{key}: {value}")

# Merge
d1 = {"a": 1}
d2 = {"b": 2}
merged = d1 | d2          # {'a': 1, 'b': 2}

```




**3- Type Casting**

```python
# Explicit conversion
int("42")          # 42
int(3.99)          # 3 
float("3.14")      # 3.14
float(10)          # 10.0
str(123)           # "123"
bool(0)            # False
bool("hello")      # True
list("abc")        # ['a', 'b', 'c']
tuple([1, 2])      # (1, 2)
set([1, 2, 2])     # {1, 2}
dict([("a", 1)])   # {'a': 1}
```



**4- Check type**

```python
x = 10

print(type(x))              # <class 'int'>
print(isinstance(x, int))   # True
print(isinstance(x, (int, float)))  # True

```



**5- Mutable VS Immutable**

| **Mutable** | **Immutable**       |
| ----------- | ------------------- |
| List        | Complex, Float, int |
| Dict        | str                 |
| set         | tuple               |
| Bytearray   | None, bool          |
| ........... | Frozenset           |
	🐅 Important Point : Refrence

```python
# List (Immutable) → Refrence Copied
a = [1, 2, 3]
b = a
b.append(4)
print(a)      # [1, 2, 3, 4] ← 

# کپی صحیح
c = a.copy()      # list(a) or a[:]
c.append(5)
print(a)          # [1, 2, 3, 4]
print(c)          # [1, 2, 3, 4, 5]

# Surface Copy vs Deep Copy
import copy
deep = copy.deepcopy(a)
```




**6- Storage & ID**

```python
x = 10
y = 10
print(id(x) == id(y))   # True (for little numbers، caching)

a = [1, 2]
b = [1, 2]
print(a == b)           # True  (equal value)
print(a is b)           # False (diffrent object)
```




**7- Operators on data types**

```python
# محاسباتی
print(10 / 3)     # 3.333... (Divide float)
print(10 // 3)    # 3 (Divide round)
print(10 % 3)     # 1 (remaining)
print(2 ** 10)    # 1024 (Pow)

# comparative
==  !=  <  >  <=  >=

# Logical
and  or  not

# Membership
"a" in "cat"      # True
3 in [1, 2, 3]    # True
"key" in {"key": 1}  # True
```



### **End of Lesson**

