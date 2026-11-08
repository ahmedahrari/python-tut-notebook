
**1- if**

```python
age = 20

if age >= 18:
    print("You are not Teenager")
    
```

	🟠 Indentation is required after the colon (:).
	🟤 The body must be indented (typically by 4 spaces) ==> TAB
	🔴 Python does not use curly braces {}; indentation takes their place.



**2- if & else**

```python
number = int(input("Enter your Number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
    
```


**3- if & elif & else**

```python
score = float(input("Score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your Score: {grade}")

```

⚠️ Order matters! Python checks from top to bottom and stops at the first true condition, ignoring the rest.


**4- Nested if**

```python
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login Success")
    else:
        print("Password Incorrect")
else:
    print("Anonymos User")
```

💡 It is better to use the ( and ) operator instead of nesting (it’s cleaner):

```python
if username == "admin" and password == "1234":
    print("Login Success")
    
```


**5- Comparison Operators**

| Operator | Name      | Example  | Output |
| -------- | --------- | -------- | ------ |
| ==       | Equal     | 10 == 10 | True   |
| !=       | Not-Equal | 12 != 4  | True   |
| >        | Bigger    | 6 > 10   | False  |
| <        | Smaller   | 10 < 6   | False  |
| >=       | B or E    | 5 >= 5   | True   |
| <=       | S or E    | 5 >= 3   | False  |


**6- Logical Operators**

| Operator | Example              | Output             |
| -------- | -------------------- | ------------------ |
| and      | Both are correct     | x > 8  and  x < 10 |
| or       | At least one correct | x < 0 or x > 100   |
| not      | opposite             | Not is active      |
```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can be riding")

if age < 18 or age > 65:
    print("Including VIP percent")

is_weekend = False
if not is_weekend:
    print("Work day")
    
```



**7- Chained Comparison**

```python
x = 15

# Instead of this:
if x > 0 and x < 100:
    print("in this range")

# an be write:
if 0 < x < 100:
    print("ّin this range")

# Even a trilogy:
if 0 < x < 100 < 1000:
    print("All is true")
```



**8- in**

```python
fruits = ["apple", "banana", "cherry"]

if "apple" in fruits:
    print("Apple is vaild")

if "grape" not in fruits:
    print("Grape is invaild")

# On Strings
if "py" in "python":
    print("Including py")

# On dictonary (Check keys)
person = {"name": "Ali", "age": 25}
if "name" in person:
    print("Key name is vaild")
    
```



**9- Counts of Falsy & Truthy**
	🟢 Any value can be used in a condition. These values ​​are considered False

```python
# Falsy variables:
False, None, 0, 0.0, 0j, "", [], (), {}, set()

# another is True:
True, 1, -1, "hello", [0], {"a": 1}

```

```python
name = input("Name: ")

if name:              # Instead of: if name != ""
    print(f"Hi {name}")
else:
    print("Name is Empty!")

items = []
if not items:         # Instead of: if len(items) == 0
    print("List is empty")
```



**10- Ternary conditional operator**
	🔴 For short-term bets

```python
# Struct: value_if_true if condition else value_if_false

age = 20
status = "Adult" if age >= 18 else "Kid"
print(status)    # Adult

# Equal:
if age >= 18:
    status = "Adult"
else:
    status = "Kid"

# Ex
x = 10
result = "Even" if x % 2 == 0 else "Odd"

max_val = a if a > b else b

print("Success" if score >= 50 else "Unsuccessful")
```


**11- match-case**
	💣 For pattern matching

```python
command = input("Syntax: ").lower()

match command:
    case "start":
        print("Started")
    case "stop":
        print("Stopped")
    case "pause" | "hold":       #  | ==> With
        print("Pause")
    case _:                       # default
        print("None Syntax")
        
```

```python
match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case _:
        print("Unknown")

#  --------------------(tuple)----------------
point = (0, 5)
match point:
    case (0, 0):
        print("مبدأ")
    case (0, y):
        print(f" On the Y axis {y}")
    case (x, 0):
        print(f"On the X axis {x}")
    case (x, y):
        print(f"Point ({x}, {y})")

#  --------------------------
match age:
    case n if n < 13:
        print("Kid")
    case n if n < 20:
        print("Teenager")
    case _:
        print("Adult")
        
```



**12- pass --> Empty block**
	🟠 If you do not want the body of the condition.....
```python
if x > 0:
    pass        # Complete Soon
else:
    print("Negative")
     
```





### End This Part
