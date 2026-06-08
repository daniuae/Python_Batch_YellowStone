# Functions and Modules in Python

## Learning Objectives

By the end of this chapter, you will be able to:

* Define and call functions
* Understand arguments and return values
* Use lambda functions
* Implement recursion
* Create and use modules
* Create packages
* Import and use built-in and third-party libraries

---

# What is a Function?

A function is a reusable block of code that performs a specific task.

## Benefits of Functions

* Code Reusability
* Better Readability
* Easier Maintenance
* Reduced Code Duplication
* Modular Programming

---

# Defining a Function

Functions are defined using the `def` keyword.

## Syntax

```python
def function_name():
    # Function Body
    pass
```

---

# Simple Function Example

```python
def greet():
    print("Welcome to Python")


greet()
```

## Output

```text
Welcome to Python
```

---

# Calling a Function Multiple Times

```python
def greet():
    print("Hello User")


greet()
greet()
greet()
```

## Output

```text
Hello User
Hello User
Hello User
```

---

# Function with Parameters

Parameters allow data to be passed into functions.

```python
def greet(name):
    print("Welcome", name)


greet("Rahul")
greet("Priya")
```

## Output

```text
Welcome Rahul
Welcome Priya
```

---

# Multiple Parameters

```python
def employee_details(name, salary):
    print("Employee:", name)
    print("Salary:", salary)


employee_details("Ravi", 75000)
```

## Output

```text
Employee: Ravi
Salary: 75000
```

---

# Arguments and Return Values

Functions can return values using the `return` keyword.

```python
def add(a, b):
    return a + b


result = add(10, 20)

print(result)
```

## Output

```text
30
```

---

# Why Return Values?

Without return:

```python
def add(a, b):
    print(a + b)


result = add(10, 20)

print(result)
```

Output:

```text
30
None
```

With return:

```python
def add(a, b):
    return a + b


result = add(10, 20)

print(result)
```

Output:

```text
30
```

---

# Default Arguments

```python
def greet(name="Guest"):
    print("Welcome", name)


greet()
greet("Ravi")
```

## Output

```text
Welcome Guest
Welcome Ravi
```

---

# Keyword Arguments

```python
def employee(name, age):
    print(name)
    print(age)


employee(age=30, name="Ravi")
```

## Output

```text
Ravi
30
```

---

# Variable-Length Arguments (*args)

Used when the number of arguments is unknown.

```python
def total_marks(*marks):
    print(sum(marks))


total_marks(10, 20)
total_marks(10, 20, 30)
total_marks(10, 20, 30, 40)
```

## Output

```text
30
60
100
```

---

# Keyword Variable-Length Arguments (**kwargs)

```python
def employee_info(**details):
    print(details)


employee_info(
    name="Rahul",
    age=28,
    city="Mumbai"
)
```

## Output

```text
{'name': 'Rahul', 'age': 28, 'city': 'Mumbai'}
```

---

# Real-World Example: Salary Calculation

```python
def calculate_salary(
    basic,
    hra,
    allowance
):
    return basic + hra + allowance


salary = calculate_salary(
    50000,
    15000,
    5000
)

print("Total Salary:", salary)
```

## Output

```text
Total Salary: 70000
```

---

# Lambda Functions

## What is a Lambda Function?

A lambda function is a small anonymous function.

### Syntax

```python
lambda arguments: expression
```

---

# Normal Function vs Lambda

## Normal Function

```python
def square(x):
    return x * x


print(square(5))
```

Output:

```text
25
```

---

## Lambda Function

```python
square = lambda x: x * x

print(square(5))
```

Output:

```text
25
```

---

# Lambda with Multiple Arguments

```python
add = lambda a, b: a + b

print(add(10, 20))
```

## Output

```text
30
```

---

# Lambda with Sorting

```python
employees = [
    ("Ravi", 50000),
    ("Priya", 70000),
    ("John", 60000)
]

employees.sort(
    key=lambda emp: emp[1]
)

print(employees)
```

## Output

```text
[
 ('Ravi', 50000),
 ('John', 60000),
 ('Priya', 70000)
]
```

---

# Recursion

## What is Recursion?

Recursion is a technique where a function calls itself.

---

# Factorial Using Recursion

Mathematical Formula:

```text
5! = 5 × 4 × 3 × 2 × 1
```

---

## Code

```python
def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))
```

## Output

```text
120
```

---

# How Recursion Works

```text
factorial(5)

5 * factorial(4)

5 * 4 * factorial(3)

5 * 4 * 3 * factorial(2)

5 * 4 * 3 * 2 * factorial(1)

5 * 4 * 3 * 2 * 1

120
```

---

# Fibonacci Series Using Recursion

```python
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(10):
    print(fibonacci(i))
```

## Output

```text
0
1
1
2
3
5
8
13
21
34
```

---

# When to Use Recursion?

Use recursion when solving:

* Tree Traversal
* Graph Algorithms
* Directory Navigation
* Divide and Conquer Problems
* Dynamic Programming

---

# Modules

## What is a Module?

A module is a Python file containing functions, variables, and classes.

Example:

```text
math_operations.py
```

---

# Creating a Module

## File: math_operations.py

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
```

---

# Using a Module

## File: main.py

```python
import math_operations

print(
    math_operations.add(10, 20)
)

print(
    math_operations.subtract(20, 10)
)
```

## Output

```text
30
10
```

---

# Import Specific Functions

```python
from math_operations import add

print(add(10, 20))
```

Output:

```text
30
```

---

# Import with Alias

```python
import math_operations as mo

print(
    mo.add(10, 20)
)
```

Output:

```text
30
```

---

# Built-in Modules

Python provides many built-in modules.

---

# math Module

```python
import math

print(math.sqrt(25))
print(math.pi)
```

Output:

```text
5.0
3.141592653589793
```

---

# random Module

```python
import random

print(
    random.randint(1, 100)
)
```

Sample Output:

```text
67
```

---

# datetime Module

```python
from datetime import datetime

print(
    datetime.now()
)
```

Sample Output:

```text
2026-01-01 12:30:45
```

---

# os Module

```python
import os

print(os.getcwd())
```

Output:

```text
/current/directory/path
```

---

# Packages

## What is a Package?

A package is a collection of related modules.

Example Structure:

```text
project/

│
├── main.py
│
└── utilities/
    │
    ├── __init__.py
    ├── math_utils.py
    └── string_utils.py
```

---

# Creating a Package

## math_utils.py

```python
def add(a, b):
    return a + b
```

---

## string_utils.py

```python
def uppercase(text):
    return text.upper()
```

---

## main.py

```python
from utilities.math_utils import add
from utilities.string_utils import uppercase

print(add(10, 20))
print(
    uppercase("python")
)
```

## Output

```text
30
PYTHON
```

---

# Installing Third-Party Libraries

Python packages can be installed using pip.

## Install Requests Library

```bash
pip install requests
```

---

# Using Requests Library

```python
import requests

response = requests.get(
    "https://api.github.com"
)

print(response.status_code)
```

Output:

```text
200
```

---

# Listing Installed Packages

```bash
pip list
```

---

# Generating Requirements File

```bash
pip freeze > requirements.txt
```

Example:

```text
numpy==2.2.0
pandas==2.2.3
requests==2.32.0
```

---

# Virtual Environment Best Practice

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

Install packages:

```bash
pip install pandas
pip install requests
```

Generate requirements:

```bash
pip freeze > requirements.txt
```

---

# Mini Project: Employee Bonus Calculator

```python
def calculate_bonus(
    salary,
    percentage
):
    return salary * percentage / 100


salary = float(
    input("Enter Salary: ")
)

bonus = calculate_bonus(
    salary,
    10
)

print(
    f"Bonus Amount = {bonus}"
)
```

### Sample Output

```text
Enter Salary: 50000
Bonus Amount = 5000.0
```

---

# Summary

In this chapter, you learned:

* Defining Functions
* Calling Functions
* Parameters and Arguments
* Return Values
* Default Arguments
* *args and **kwargs
* Lambda Functions
* Recursion
* Modules
* Packages
* Import Statements
* Built-in Libraries
* Third-Party Libraries
* Virtual Environments
* Requirements File Management

These concepts are the foundation of reusable, maintainable, and modular Python application development.
