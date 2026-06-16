# Python Exception Handling, File Handling, Testing & Deployment

## Table of Contents

1. Exception Handling
   - Try, Except, Else, Finally
   - Custom Exceptions
   - Assertions
   - Logging
   - Debugging
2. File Handling
   - Reading and Writing Files
   - File Modes
   - Context Managers
   - CSV Files
   - JSON Files
   - XML Files
   - Directory and File Operations
3. Testing and Deployment
   - Unit Testing with unittest
   - Unit Testing with pytest
4. Mini Project Example

---

# 1. Exception Handling

Exception handling allows a program to continue running even when errors occur.

## Common Exceptions

| Exception | Description |
|------------|-------------|
| ValueError | Invalid value provided |
| TypeError | Wrong data type used |
| ZeroDivisionError | Division by zero |
| FileNotFoundError | File does not exist |
| KeyError | Dictionary key not found |
| IndexError | Invalid list index |

---

## Try and Except

### Example

```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter a valid number")
```

### Flow

```
TRY
 |
 |-- Error?
 |     |
 |    Yes ---> EXCEPT
 |     |
 |    No ----> Continue
```

---

## Try, Except, Else, Finally

```python
try:
    num = int(input("Enter number: "))

except ValueError:
    print("Invalid Input")

else:
    print("Square =", num ** 2)

finally:
    print("Program Finished")
```

### Output

```
Enter number: 5
Square = 25
Program Finished
```

---

# Custom Exceptions

Custom exceptions help enforce business rules.

## Example: Bank Withdrawal

```python
class InsufficientBalanceError(Exception):
    pass
```

```python
class InsufficientBalanceError(Exception):
    pass

balance = 5000
withdraw_amount = 7000

try:
    if withdraw_amount > balance:
        raise InsufficientBalanceError(
            "Insufficient Balance"
        )

except InsufficientBalanceError as e:
    print(e)
```

### Output

```
Insufficient Balance
```

---

# Assertions

Assertions validate assumptions during development.

## Syntax

```python
assert condition, "message"
```

## Example

```python
age = 20

assert age >= 18, "Age must be at least 18"

print("Eligible")
```

### Output

```
Eligible
```

## Failed Assertion

```python
age = 15

assert age >= 18, "Age must be at least 18"
```

### Output

```
AssertionError: Age must be at least 18
```

---

# Logging

Logging records events and errors.

## Basic Logging

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Application Started")
logging.warning("Low Disk Space")
logging.error("Database Connection Failed")
```

### Output

```
INFO:root:Application Started
WARNING:root:Low Disk Space
ERROR:root:Database Connection Failed
```

---

## Logging to File

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Application Started")
logging.error("An error occurred")
```

Generated file:

```
app.log
```

---

## Logging Levels

| Level | Purpose |
|---------|----------|
| DEBUG | Detailed diagnostics |
| INFO | General information |
| WARNING | Warning messages |
| ERROR | Error messages |
| CRITICAL | Severe failures |

---

# Debugging

## Print Debugging

```python
a = 10
b = 20

print("a =", a)
print("b =", b)
print(a + b)
```

---

## Logging Debugging

```python
import logging

logging.basicConfig(level=logging.DEBUG)

a = 10
b = 20

logging.debug(f"a={a}")
logging.debug(f"b={b}")
```

---

## Python Debugger (pdb)

```python
import pdb

x = 10
y = 20

pdb.set_trace()

z = x + y

print(z)
```

Useful commands:

```
n  -> next line
c  -> continue
p  -> print variable
q  -> quit
```

---

# 2. File Handling

Files provide permanent storage.

---

# File Modes

| Mode | Description |
|--------|------------|
| r | Read |
| w | Write (overwrite) |
| a | Append |
| x | Create new file |
| r+ | Read and Write |
| rb | Read binary |
| wb | Write binary |

---

# Writing Files

```python
file = open("data.txt", "w")

file.write("Hello Python")

file.close()
```

File content:

```
Hello Python
```

---

# Reading Files

```python
file = open("data.txt", "r")

content = file.read()

print(content)

file.close()
```

---

# Reading Line by Line

```python
with open("data.txt") as file:

    for line in file:
        print(line.strip())
```

---

# Context Managers

Recommended approach.

```python
with open("data.txt", "r") as file:
    content = file.read()

print(content)
```

### Benefits

- Automatically closes files
- Cleaner code
- Safer resource management

---

# Working with CSV Files

CSV = Comma Separated Values

Example:

```csv
id,name,salary
1,John,50000
2,Mary,60000
```

---

## Read CSV

```python
import csv

with open("employees.csv") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Output:

```python
['id', 'name', 'salary']
['1', 'John', '50000']
['2', 'Mary', '60000']
```

---

## Read CSV as Dictionary

```python
import csv

with open("employees.csv") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"])
```

Output:

```
John
Mary
```

---

## Write CSV

```python
import csv

data = [
    ["ID", "Name", "Salary"],
    [1, "John", 50000],
    [2, "Mary", 60000]
]

with open(
    "employees.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerows(data)
```

---

# Working with JSON

## Write JSON

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

Generated file:

```json
{
    "id": 1,
    "name": "John",
    "salary": 50000
}
```

---

## Read JSON

```python
import json

with open("employee.json") as file:
    data = json.load(file)

print(data["name"])
```

Output:

```
John
```

---

# Working with XML

Example XML:

```xml
<employee>
    <id>1</id>
    <name>John</name>
</employee>
```

---

## Read XML

```python
import xml.etree.ElementTree as ET

tree = ET.parse("employee.xml")

root = tree.getroot()

for child in root:
    print(child.tag, child.text)
```

Output:

```
id 1
name John
```

---

## Write XML

```python
import xml.etree.ElementTree as ET

employee = ET.Element("employee")

name = ET.SubElement(employee, "name")
name.text = "John"

tree = ET.ElementTree(employee)

tree.write("employee.xml")
```

---

# Directory and File Operations

## Current Directory

```python
import os

print(os.getcwd())
```

---

## Create Directory

```python
import os

os.mkdir("Reports")
```

---

## Create Nested Directories

```python
import os

os.makedirs(
    "2026/June/Reports",
    exist_ok=True
)
```

---

## List Files

```python
import os

print(os.listdir())
```

---

## Rename File

```python
import os

os.rename(
    "old.txt",
    "new.txt"
)
```

---

## Delete File

```python
import os

os.remove("data.txt")
```

---

## Delete Directory

```python
import os

os.rmdir("Reports")
```

---

## Check File Exists

```python
import os

if os.path.exists("data.txt"):
    print("Exists")
```

---

# 3. Testing and Deployment

Testing ensures code behaves as expected.

---

# Unit Testing with unittest

## Application Code

### calculator.py

```python
def add(a, b):
    return a + b
```

---

## Test Code

### test_calculator.py

```python
import unittest
from calculator import add

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(
            add(2, 3),
            5
        )

if __name__ == "__main__":
    unittest.main()
```

Run:

```bash
python test_calculator.py
```

Output:

```
.
----------------------------------------------------------------
Ran 1 test

OK
```

---

## Common Assertions

```python
self.assertEqual(a, b)
self.assertTrue(condition)
self.assertFalse(condition)
self.assertIn(item, collection)
self.assertRaises(Exception)
```

---

# Unit Testing with pytest

Install:

```bash
pip install pytest
```

---

## Application Code

```python
def multiply(a, b):
    return a * b
```

---

## Test File

```python
from calculator import multiply

def test_multiply():
    assert multiply(2, 3) == 6
```

Run:

```bash
pytest
```

Output:

```
1 passed
```

---

## Parametrized Tests

```python
import pytest

@pytest.mark.parametrize(
    "a,b,result",
    [
        (2,3,6),
        (4,5,20),
        (10,2,20)
    ]
)
def test_multiply(a,b,result):
    assert a*b == result
```

---

# Project Structure

```
project/
│
├── app.py
├── calculator.py
├── employees.csv
├── employee.json
│
├── tests/
│   └── test_calculator.py
│
├── logs/
│   └── app.log
│
└── reports/
```

---

# 4. Mini Project: CSV to JSON Converter

## converter.py

```python
import csv
import json
import logging

logging.basicConfig(
    filename="converter.log",
    level=logging.INFO
)

def csv_to_json(csv_file, json_file):

    data = []

    with open(csv_file) as file:

        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    with open(json_file, "w") as file:

        json.dump(data, file, indent=4)

    logging.info(
        f"{csv_file} converted successfully"
    )
```

---

## test_converter.py

```python
from converter import csv_to_json

def test_function_exists():
    assert callable(csv_to_json)
```

Run:

```bash
pytest
```

---

# Summary

This guide covered:

- Exception Handling
  - try
  - except
  - else
  - finally
  - custom exceptions
- Assertions
- Logging
- Debugging
- File Handling
- CSV Processing
- JSON Processing
- XML Processing
- Directory Operations
- Unit Testing with unittest
- Unit Testing with pytest
- Mini Production-Style Project

These concepts form the foundation of Python backend development, automation, ETL pipelines, data engineering, API development, and production applications.
