

<span style="font-size: 2em; font-weight: 700;">PEP20</span>
<hr style="border: 3px solid var(--text-normal); border-radius: 2px; margin: 24px 0;">
1-  Beautiful is Better than ugly.
2- Explicit is better than implicit.
3- Simple is better than complex.
4- Complex is better than complicated.
5- Flat is better than nested.
6- Sparse is better than dense.
7- Readability counts.
8- Special cases are not special enough to break the rules.
9- Although practicality beats purity.
10- Errors should never pass silently.
11- Unless explicitly.
12- In the face of ambiguity, refuse the temptation to guess.
13- There should be one-- and preferably only one --obvious way to do it.
14- Although that way may not be obvious at first unless you're Dutch.
15- Now is better than never.
16- Although never is often better than right now.
17- if the implementation is hard to explain, it's a bad idea.
18- If the implementation is easy to explain, it may be a good idea.
19- Namespace are one honking great idea -- let's do more of those !
20-      ?

___


<span style="font-size: 2em; font-weight: 700;">PEP8 (Clean Code)</span>
<hr style="border: 3px solid var(--text-normal); border-radius: 2px; margin: 24px 0;">
**1- Indentation and Spacing**
	👻 Don't use tabs unless the project you are contributing to requires it.

```python
# Good ✅

def great():
	print("4HME2")

# Bad ❌

def great():
  print("4HME2")
```


1-2 => Line continuation
	👹 To continue a line, either align with the opening parenthesis or use a hanging indent with an extra 4 spaces

```python
# Good ✅

	# Aligned with the opening parenthesis
	result = some_func(arr_one,
	                   arr_two)
                   
                   
	# HANGING INDENT
	result = some_funk(
		arr_one,
		arr_two,
	)
	
	
# Bad ❌

result = some_function(argument_one,
    argument_two)
```


1-3 => Closing Brackets/braces on a new line
	👺 If you break a line, the closing parenthesis should be on the same line as the last content line or on a new line with proper alignment

```python
# Good ✅

my_list = [
	1, 2, 3
	4, 5, 6
]
```


**2- Line Length**
	🤖 Maximum code line length: 79 characters
	💥 Maximum comment & docstring line length: 72 characters

	💫 If a line becomes too long, use parenthesis and line breaks

```python
# Good ✅

income = (
    gross_wages
    + taxable_interest
    + dividends
    - qualified_dividend
    - ira_deduction
)


# Bad ❌

income = (gross_wages + taxable_interest + dividends - qualified_dividend -ira_deduction)
```


**3- Blank Lines**
	👽 Tow blank lines before and after top-level classes and functions
	💀 One blank line between methods inside a class
	😈 Inside functions, use blank lines sparingly & purposefully
	☠️ You may use one blank line between logical groups of code inside a function

```python

# Good ✅

import os


class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"


def main():
    user = User("Ali")
    print(user.greet())
```


**4- Imports**

4-1 => One import per line

```python
# Good ✅

import os
import sys


# Bad ❌

import os, sys
```

4-2 => Import order
	A- Standard library
	B- Third-party libraries
	3- Local project imports

	😎 Separate each group with one blank line

```python
# Good ✅

import os
import sys

import requests

from myproject import utils

```


4-3 => Imports at the top of the file
	🍋‍🟩 Imports should come after the module docstring and comments, and before global variables.

4-4 => Avoid  ( import * )

```python
# Good ✅

from math import sqrt

# Bad ❌

from math import *

```

4-5 => Prefer absolute imports

```python
# Better ✅

from package.subpackage import module

# Explicit relative imports are also acceptable:

from . import module

```



**5- Spacing in Expressions and  Statements

5-1 => One space after a comma

```python
# Good ✅

values = [1, 2, 3]

# Bad ❌

values = [1,2,3]

```

5-2 => Put spaces around operators

```python
# Good ✅

x = 1 + 2

# Bad ❌

x=1+2

```

5-3 => Don't put a space before a comma, semicolon, or colon

```python
# Good ✅

if x == 1:
    pass
    
    
# Bad ❌

if x == 1 :
    pass

```

5-4 => Don't put a space before the parenthesis in a function call

```python
# Good ✅

print("Hello")


# Bad ❌

print ("Hello")

```

5-5 => Don't put spaces around = for keyword arguments & default values

```python
# Good ✅

def greet(name="Ali"):
    print(name)

greet(name="Sara")


# Bad ❌

def greet(name = "Ali"):
    print(name)

greet(name = "Sara")

```

	✴️ However, if you have an annotation, PEP8 says to put spaces around =:

```python
# Good ✅

def greet(name: str = "Ali") -> None:
    print(name)
    
```

5-6 => Slicing
	❇️ For simple slices, Don't put spaces around the colon

```python
# Good ✅

ham[lower:upper]
ham[lower:upper:]
ham[lower::step]
ham[::step]

```

	✳️ If the expressions are complex, symmetric spacing is allowed:
```python
# Good ✅

ham[lower + offset : upper + offset]
ham[: upper_fn(x) : step_fn(x)]

```



**6- Comments**

5-1 => Write complete and clear comments

```python
# Good ✅

x = x + 1  # Increase retry count after a failed request.

# Bad ❌

x = x + 1  # increment

```

6-2 => Use inline comments sparingly
	🔱 If used, put at least two spaces before ( # ) and one space after it.
	
```python
# Good ✅

timeout = 30  # seconds

```

6-3 => Block comments
	⚜️ Each line should start with ( # ) and one space.

```python
# Good ✅

# Calculate the total price.
# Tax is applied after discount.
total = price * quantity

```

6-4 => Avoid useless comments

```python
# Bad ❌

i = i + 1  # add one to i
```



**7- Docstring**
	🌏 Write docstrings for functions, classes and modules ( PEP8 refers to PEP257 )

```python
# Good ✅

def calculate_area(width: float, height: float) -> float:
    """Return the area of a rectangle.

    Args:
        width: The width of the rectangle.
        height: The height of the rectangle.

    Returns:
        The area as a float.
    """
    return width * height

```

🌐 Use triple double quotes ( """ )
🌍 The first line should be a short summary
🌎 If the docstring is multi-line, the first line should be separate, followed by the description


**8- Naming**


| Item               | Style              | Example         |
| ------------------ | ------------------ | --------------- |
| Variables          | snake_case         | user_name       |
| Functions          | snake_case         | calc_total      |
| Method             | snake_case         | get_name        |
| Class              | PascalCase         | UserProfile     |
| Constant           | UPPER_CASE         | MAX_RETRIES     |
| Module             | Short & snake      | utils.py        |
| Package            | Lowercase          | mypackage       |
| Exception          | PascalCase         | ValidError      |
| Protected variable | One leading ( _ )  | _internal_value |
| Private Variable   | Two leading ( __ ) | __private_value |
|                    | camelCase          |                 |
|                    | fUcKtHeCaSe        |                 |

8-1 => Avoid ambiguous single-character names

```python
# Good ✅

line_count = 1

# Bad ❌

l = 1
O = 0
I = 1

```

8-2 => ### Use descriptive names

```python
# Good ✅

def double(value):
    return value * 2
    
# Bad ❌

def f(x):
    return x * 2
    
```



**9- Strings**
	🌕 Single quotes and double quotes are equivalent in Python.
	🌑 Keep one style consistent throughout the project.
	⭐ Use `"""` for docstrings.

```python
# Good ✅

name = "Ali"
message = 'Hello'

# Good ✅

def greet() -> None:
    """Print a greeting."""
    print("Hello")
    
```




**10-  Compound Statements**
	🌟 Avoid multiple statements on one line

```python
# Good ✅

if x:
    print(x)
    
    
# Bad ❌

if x: print(x)


# Bad ❌

a = 1; b = 2


# Good ✅

a = 1
b = 2

```



**11. Comparisons and Programming Recommendations**

11-1 => Comparing with  (None )
	🏛️ Use ( is ) and ( is not )

```python
# Good ✅

if x is None:
    pass

# Bad ❌

if x == None:
	pass
	
```

11-2 => Comparing With ( True ) and ( False )

```python
# Good ✅

if is_valid:
    pass
    
# Bad ❌

if is_valid == True:
    pass
    
```

11.3 => Checking whether a sequence is empty

```python
# Good ✅

if not items:
    pass
    
# Bad ❌

if len(items) == 0:
    pass
    
```

 11.4 => Type checking

```python
# Good ✅

if isinstance(x, int):
    pass
    

# Bad ❌

if type(x) is int:
    pass
    
```

11-5 => Using ( not )

```python
# Good ✅

if x is not None:
    pass
    
    
# Bad ❌

if not x is None:
    pass
    
```

11-6 => Using ( with ) for resources

```python
# Good ✅

with open("file.txt", encoding="utf-8") as f:
    data = f.read()
    
# Bad ❌

f = open("file.txt")
data = f.read()
f.close()

```

11-7 => Using ( enumerate )

```python
# Good ✅

for index, item in enumerate(items):
    print(index, item)
    
    
# Bad ❌

for i in range(len(items)):
    print(i, items[i])
    
```

11-8 => Using ( zip )

```python
# Good ✅

for name, age in zip(names, ages):
    print(name, age)
    
    
# Bad ❌

for i in range(len(names)):
    print(names[i], ages[i])
    
```

11-9 => Use ( def ) instead of assigning a ( lambda )

```python
# Good ✅

def double(x):
    return x * 2
    
    
# Bad ❌

double = lambda x: x * 2

```

11.10 Use string methods to check prefixes/suffixes

```python
# Good ✅

if text.startswith("Hello"):
    pass

    
# Bad ❌

if text[:5] == "Hello":
    pass
    
 
```




**12- Breaking Long Lines & Operators**
	☁️ PEP8 prefers the binary operator at the beginning of the new line

```python
# Good ✅

total = (
    first_value
    + second_value
    + third_value
)

# Good ✅

if (
    user_is_active
    and user_has_permission
    and not user_is_blocked
):
    allow_access()
    
```



**13- Trailing Commas**
	⚡ In multi-line structures, trailing commas are useful and make diffs cleaner

```python
# Good ✅

colors = [
    "red",
    "green",
    "blue",
]


# Good ✅

def create_user(
    name: str,
    age: int,
    email: str,
) -> None:
    ...


# For a one-element tuple, a comma is required:
# Good ✅

single = (1,)

```




**14- Annotations**

```python
# Good ✅

def greet(name: str) -> str:
    return f"Hello {name}"
    
```

	🔥 One space after the colon in an annotation.
	❄️ Spaces around `->`.
	☄️ In a default value with an annotation, put spaces around `=`.

```python
# Good ✅

def connect(host: str = "localhost") -> None:
    ...
    
```




**15- File Encoding**
	🌊 In Python 3, source files are UTF-8 by default. The following line is not needed unless there is a special reason:

```python

# -*- coding: utf-8 -*-

```



**16- A Few Complete Example**

```python
# Good ✅

import os
import sys


class User:
    def __init__(self, name: str, age: int = 0) -> None:
        self.name = name
        self.age = age

    def greet(self) -> None:
        if self.name is not None:
            print(f"Hello {self.name}")
            
            
            
# Bad ❌

import os,sys
class user:
  def __init__(self,name,age=0):
    self.name=name;self.age=age
  def greet(self):
    if self.name!=None: print("Hello "+self.name)
   
```




**17- Automated Tools for PEP8 Compliance**
	🧭  **pycodestyle** ==> checks PEP8 style
	⚽ **flake8** ==> combines pycodestyle + pyflakes + mccabe
	🏀 **ruff** ==> fast linter and formatter
	🏐 **black** ==> automatic code formatter
	🏈 **autopep8** ==> automatically fixes some PEP8 issues
	🥎 **isort** ==> sorts imports

```python

pip install flake8 black isort
flake8 .
black .
isort .

```





### END THIS LESSON
