# Exception Handling and File Handling in Python

---

# Table of Contents

1. Exception Handling
   - Introduction
   - Try Block
   - Except Block
   - Else Block
   - Finally Block
   - Multiple Exceptions
   - Nested Exception Handling
   - Raising Exceptions
   - Custom Exceptions
   - Assertions
   - Logging
   - Debugging

2. File Handling
   - Introduction
   - Reading Files
   - Writing Files
   - Appending Files
   - File Modes
   - Context Managers
   - CSV Files
   - JSON Files
   - XML Files
   - Directory Operations
   - File Operations

---

# Exception Handling

## What is Exception Handling?

An exception is an error that occurs during program execution.

Without exception handling:

```python
num = int(input("Enter a number: "))
print(100 / num)
```

If user enters:

```text
abc
```

Output:

```text
ValueError
```

Python stops execution immediately.

Exception handling prevents program crashes.

---

# Try Block

Code that may cause an error is placed inside `try`.

```python
try:
    num = int(input("Enter a number: "))
    print(100 / num)
except:
    print("An error occurred")
```

---

# Except Block

Handles specific exceptions.

```python
try:
    num = int(input("Enter a number: "))
    print(100 / num)

except ValueError:
    print("Invalid number entered")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

# Else Block

Runs only when no exception occurs.

```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)
```

Output:

```text
Result: 20.0
```

---

# Finally Block

Always executes.

```python
try:
    file = open("sample.txt")

except FileNotFoundError:
    print("File not found")

finally:
    print("Program completed")
```

Output:

```text
Program completed
```

---

# Complete Try-Except-Else-Finally

```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ValueError:
    print("Enter valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)

finally:
    print("Execution finished")
```

---

# Multiple Exceptions

Handle multiple errors together.

```python
try:
    num = int(input("Enter number: "))
    result = 100 / num

except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)
```

---

# Generic Exception

```python
try:
    x = 10 / 0

except Exception as e:
    print("Error:", e)
```

Output:

```text
division by zero
```

---

# Nested Exception Handling

```python
try:
    try:
        num = int(input("Enter number: "))
        print(100 / num)

    except ZeroDivisionError:
        print("Cannot divide by zero")

except ValueError:
    print("Invalid input")
```

---

# Raising Exceptions

Use `raise` to create exceptions manually.

```python
age = -1

if age < 0:
    raise ValueError("Age cannot be negative")
```

Output:

```text
ValueError: Age cannot be negative
```

---

# Custom Exceptions

Create your own exception class.

```python
class InvalidSalaryError(Exception):
    pass
```

Usage:

```python
salary = -1000

if salary < 0:
    raise InvalidSalaryError("Salary cannot be negative")
```

---

# Custom Exception Example

```python
class InsufficientBalance(Exception):
    pass

balance = 1000
withdraw = 2000

if withdraw > balance:
    raise InsufficientBalance("Insufficient funds")
```

---

# Assertions

Assertions help validate assumptions.

Syntax:

```python
assert condition, "message"
```

Example:

```python
age = 20

assert age >= 18, "Must be adult"

print("Eligible")
```

---

# Assertion Failure

```python
age = 15

assert age >= 18, "Must be adult"
```

Output:

```text
AssertionError: Must be adult
```

---

# Logging

Logging records program events.

---

## Basic Logging

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Program started")
logging.warning("Low memory")
logging.error("File not found")
```

Output:

```text
INFO:root:Program started
WARNING:root:Low memory
ERROR:root:File not found
```

---

# Logging Levels

| Level | Description |
|---------|------------|
| DEBUG | Detailed information |
| INFO | General events |
| WARNING | Potential issue |
| ERROR | Error occurred |
| CRITICAL | Serious failure |

---

# Logging to File

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Application Started")
```

Creates:

```text
app.log
```

---

# Logging Exception Details

```python
import logging

try:
    result = 10 / 0

except Exception as e:
    logging.error(e)
```

---

# Debugging

Debugging helps identify bugs.

---

## Using print()

```python
a = 10
b = 20

print(a)
print(b)

print(a + b)
```

---

## Using breakpoint()

```python
x = 10
y = 20

breakpoint()

z = x + y
```

Execution pauses for inspection.

---

# File Handling

## Introduction

Files allow permanent storage of data.

Examples:

```text
employee.txt
sales.csv
users.json
config.xml
```

---

# Opening Files

Syntax:

```python
file = open("filename", "mode")
```

Example:

```python
file = open("sample.txt", "r")
```

---

# Reading Files

## Read Entire File

```python
file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()
```

---

# Read Specific Characters

```python
file = open("sample.txt", "r")

print(file.read(10))

file.close()
```

---

# Read Line

```python
file = open("sample.txt", "r")

print(file.readline())

file.close()
```

---

# Read All Lines

```python
file = open("sample.txt", "r")

lines = file.readlines()

print(lines)

file.close()
```

---

# Writing Files

## Write Mode

```python
file = open("sample.txt", "w")

file.write("Hello Python")

file.close()
```

Existing content is overwritten.

---

# Append Mode

```python
file = open("sample.txt", "a")

file.write("\nNew Record")

file.close()
```

Adds content to existing file.

---

# File Modes

| Mode | Description |
|--------|------------|
| r | Read |
| w | Write |
| a | Append |
| x | Create |
| rb | Read Binary |
| wb | Write Binary |
| r+ | Read + Write |
| w+ | Write + Read |
| a+ | Append + Read |

---

# Context Managers

Recommended approach.

Automatically closes files.

```python
with open("sample.txt", "r") as file:
    content = file.read()

print(content)
```

No need for:

```python
file.close()
```

---

# CSV Files

CSV = Comma Separated Values

---

## Writing CSV

```python
import csv

with open("employees.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Salary"])
    writer.writerow([1, "John", 50000])
```

---

# Reading CSV

```python
import csv

with open("employees.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Output:

```text
['ID', 'Name', 'Salary']
['1', 'John', '50000']
```

---

# CSV Dictionary Reader

```python
import csv

with open("employees.csv") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row["Name"])
```

---

# JSON Files

JSON is commonly used in APIs.

---

# Writing JSON

```python
import json

employee = {
    "id": 1,
    "name": "John",
    "salary": 50000
}

with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)
```

---

# Reading JSON

```python
import json

with open("employee.json") as file:
    data = json.load(file)

print(data)
```

---

# JSON String Conversion

```python
import json

employee = {"name": "John"}

json_string = json.dumps(employee)

print(json_string)
```

---

# JSON to Dictionary

```python
import json

json_string = '{"name":"John"}'

data = json.loads(json_string)

print(data)
```

---

# XML Files

---

# Writing XML

```python
import xml.etree.ElementTree as ET

root = ET.Element("Employees")

emp = ET.SubElement(root, "Employee")
name = ET.SubElement(emp, "Name")

name.text = "John"

tree = ET.ElementTree(root)

tree.write("employee.xml")
```

---

# Reading XML

```python
import xml.etree.ElementTree as ET

tree = ET.parse("employee.xml")

root = tree.getroot()

for emp in root:
    print(emp.find("Name").text)
```

---

# Directory Operations

```python
import os
```

---

# Current Directory

```python
import os

print(os.getcwd())
```

---

# Create Directory

```python
import os

os.mkdir("data")
```

---

# Create Nested Directories

```python
os.makedirs("project/data/raw")
```

---

# List Files

```python
import os

print(os.listdir())
```

---

# Check File Exists

```python
import os

print(os.path.exists("sample.txt"))
```

---

# Rename File

```python
import os

os.rename(
    "old.txt",
    "new.txt"
)
```

---

# Delete File

```python
import os

os.remove("sample.txt")
```

---

# Remove Directory

```python
os.rmdir("data")
```

---

# Recursive Directory Deletion

```python
import shutil

shutil.rmtree("project")
```

---

# Path Operations

```python
from pathlib import Path

path = Path("data/file.txt")

print(path.exists())
print(path.name)
print(path.suffix)
print(path.parent)
```

---

# Real-World Example:
# Employee Data Processing

```python
import json
import csv
import logging

logging.basicConfig(level=logging.INFO)

try:
    with open("employees.json") as file:
        employees = json.load(file)

    with open("employees.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            ["ID", "Name", "Salary"]
        )

        for emp in employees:

            writer.writerow([
                emp["id"],
                emp["name"],
                emp["salary"]
            ])

    logging.info("CSV created successfully")

except FileNotFoundError:
    logging.error("JSON file missing")

except Exception as e:
    logging.error(e)

finally:
    logging.info("Process completed")
```

---

# Best Practices

### Exception Handling

- Catch specific exceptions
- Avoid bare `except`
- Use custom exceptions for business rules
- Use assertions for development checks
- Log important errors

### File Handling

- Always use `with open()`
- Close files properly
- Validate file existence
- Handle file exceptions
- Use JSON for APIs
- Use CSV for tabular data
- Use XML for legacy integrations
- Prefer `pathlib` over `os.path` for modern Python

---

# Summary

You learned:

✅ Try, Except, Else, Finally

✅ Multiple and Nested Exceptions

✅ Raising Exceptions

✅ Custom Exceptions

✅ Assertions

✅ Logging

✅ Debugging

✅ File Reading and Writing

✅ CSV Processing

✅ JSON Processing

✅ XML Processing

✅ Context Managers

✅ File Modes

✅ Directory Operations

✅ Path Handling

✅ Real-world Data Processing Example
