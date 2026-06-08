# Python Fundamentals - Day 1

## Introduction to Python

Python is a high-level, interpreted, object-oriented, and general-purpose programming language.

### Features of Python

* Easy to Learn
* Easy to Read
* Platform Independent
* Open Source
* Large Community Support
* Rich Library Ecosystem
* Supports Multiple Programming Paradigms

---

## Python Ecosystem

Python is widely used in various domains.

### Data Engineering

| Library    | Purpose                |
| ---------- | ---------------------- |
| Pandas     | Data Analysis          |
| NumPy      | Numerical Computing    |
| PySpark    | Big Data Processing    |
| SQLAlchemy | Database Connectivity  |
| Airflow    | Workflow Orchestration |

### Machine Learning

| Library      | Purpose          |
| ------------ | ---------------- |
| Scikit-Learn | Machine Learning |
| TensorFlow   | Deep Learning    |
| PyTorch      | Deep Learning    |

### Visualization

| Library    | Purpose                   |
| ---------- | ------------------------- |
| Matplotlib | Data Visualization        |
| Seaborn    | Statistical Visualization |
| Plotly     | Interactive Charts        |

### Web Development

| Framework | Purpose                  |
| --------- | ------------------------ |
| Flask     | Lightweight Applications |
| Django    | Enterprise Applications  |
| FastAPI   | REST APIs                |

---

# Installing Python

## Ubuntu Installation

### Check Python Version

```bash
python3 --version
```

Example Output:

```text
Python 3.13.2
```

### Install Python

```bash
sudo apt update
sudo apt install python3
```

### Install Pip

```bash
sudo apt install python3-pip
```

Verify Installation:

```bash
pip3 --version
```

---

# Creating a Virtual Environment

## Install venv

```bash
sudo apt install python3-venv
```

## Create Project Folder

```bash
mkdir PythonTraining
cd PythonTraining
```

## Create Virtual Environment

```bash
python3 -m venv .venv
```

## Activate Environment

```bash
source .venv/bin/activate
```

Output:

```text
(.venv)$
```

## Deactivate Environment

```bash
deactivate
```

---

# Setting Up VS Code

## Install VS Code

Download from:

https://code.visualstudio.com/

### Install Python Extension

1. Open VS Code
2. Click Extensions
3. Search for:

```text
Python
```

4. Install Microsoft Python Extension

---

# Setting Up PyCharm

Download:

https://www.jetbrains.com/pycharm/

Install Community Edition.

---

# Installing Jupyter Notebook

Install:

```bash
pip install notebook
```

Start Notebook:

```bash
jupyter notebook
```

---

# First Python Program

```python
print("Hello World")
```

Output:

```text
Hello World
```

---

# Python Syntax

Python uses indentation instead of braces.

Example:

```python
if 10 > 5:
    print("Ten is greater")
```

Output:

```text
Ten is greater
```

---

# Variables

Variables store data.

```python
name = "John"
age = 25
salary = 45000.50

print(name)
print(age)
print(salary)
```

Output:

```text
John
25
45000.5
```

---

# Variable Naming Rules

## Valid Variables

```python
employee_name = "Rahul"
salary1 = 10000
_age = 30
```

## Invalid Variables

```python
1name = "John"
first-name = "John"
```

---

# Data Types

Python automatically determines data types.

---

## Integer (int)

```python
age = 25

print(age)
print(type(age))
```

Output:

```text
25
<class 'int'>
```

---

## Float

```python
price = 99.99

print(price)
print(type(price))
```

Output:

```text
99.99
<class 'float'>
```

---

## String (str)

```python
city = "Mumbai"

print(city)
print(type(city))
```

Output:

```text
Mumbai
<class 'str'>
```

---

## Boolean

```python
is_active = True

print(is_active)
print(type(is_active))
```

Output:

```text
True
<class 'bool'>
```

---

## List

```python
fruits = ["Apple", "Banana", "Orange"]

print(fruits)
print(type(fruits))
```

Output:

```text
['Apple', 'Banana', 'Orange']
<class 'list'>
```

---

## Accessing List Elements

```python
fruits = ["Apple", "Banana", "Orange"]

print(fruits[0])
print(fruits[1])
```

Output:

```text
Apple
Banana
```

---

# Dynamic Typing

```python
x = 100

print(type(x))

x = "Python"

print(type(x))
```

Output:

```text
<class 'int'>
<class 'str'>
```

---

# Operators

## Arithmetic Operators

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

Output:

```text
13
7
30
3.3333333333
3
1
1000
```

---

## Comparison Operators

```python
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
```

Output:

```text
False
True
False
True
False
True
```

---

## Logical Operators

```python
age = 25
salary = 60000

print(age > 18 and salary > 50000)
print(age > 30 or salary > 50000)
print(not(age > 18))
```

Output:

```text
True
True
False
```

---

## Assignment Operators

```python
x = 10

x += 5
print(x)

x -= 3
print(x)

x *= 2
print(x)
```

Output:

```text
15
12
24
```

---

# Input Operations

## Example 1

```python
name = input("Enter your name: ")

print("Welcome", name)
```

Sample Output:

```text
Enter your name: Ravi
Welcome Ravi
```

---

## Example 2

```python
age = int(input("Enter Age: "))

print(age)
print(type(age))
```

Output:

```text
Enter Age: 25
25
<class 'int'>
```

---

## Example 3 - Addition Program

```python
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

total = num1 + num2

print("Sum =", total)
```

Output:

```text
Enter First Number: 10
Enter Second Number: 20
Sum = 30
```

---

# Output Operations

## Simple Print

```python
print("Python")
```

---

## Multiple Values

```python
name = "Ravi"
age = 25

print(name, age)
```

Output:

```text
Ravi 25
```

---

## f-String Formatting

```python
name = "Ravi"
salary = 75000

print(f"Employee {name} earns {salary}")
```

Output:

```text
Employee Ravi earns 75000
```

---

# Comments

Comments improve readability.

## Single-Line Comment

```python
# This is a single-line comment

name = "John"
```

---

## Multi-Line Comment

```python
"""
This is a multi-line comment.

Used for documentation.
"""
```

---

# Code Documentation Using Docstrings

Docstrings document functions, classes, and modules.

## Example

```python
def add(a, b):
    """
    Adds two numbers and returns the result.
    """

    return a + b


print(add(10, 20))
```

Output:

```text
30
```

---

## Accessing Docstrings

```python
def greet():
    """
    Displays a welcome message.
    """

    print("Hello")


print(greet.__doc__)
```

Output:

```text
Displays a welcome message.
```

---

# Mini Project - Student Information System

```python
name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
marks = float(input("Enter Marks: "))

print("\nStudent Details")
print("----------------")
print(f"Name  : {name}")
print(f"Age   : {age}")
print(f"Marks : {marks}")

if marks >= 35:
    print("Result : PASS")
else:
    print("Result : FAIL")
```

Sample Output:

```text
Enter Student Name: Ravi
Enter Age: 18
Enter Marks: 78.5

Student Details
----------------
Name  : Ravi
Age   : 18
Marks : 78.5
Result : PASS
```

---

# Summary

In this chapter you learned:

* Introduction to Python
* Python Ecosystem
* Installing Python
* Virtual Environments
* VS Code Setup
* PyCharm Setup
* Jupyter Notebook Setup
* Variables
* Data Types
* Operators
* Input and Output
* Comments
* Docstrings
* Mini Project

These concepts form the foundation for learning Python programming, Data Engineering, Automation, Machine Learning, and Software Development.
