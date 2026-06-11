# Python Exception Handling and File Handling – Complete Guide

---

# Part 1: Exception Handling

## What is Exception Handling?

An exception is an error that occurs while a program is running.

Without exception handling, the program crashes immediately.

Exception handling allows us to:

- Prevent application crashes
- Display user-friendly messages
- Log errors for troubleshooting
- Continue program execution when possible

---

## Real-World Example

Imagine an ATM machine.

Scenario:

- Customer enters amount
- System checks balance
- If balance is insufficient, ATM should show a message instead of crashing

Exception handling makes this possible.

---

# Try Block

The `try` block contains code that might produce an error.

## Example

```python
number = int(input("Enter a number: "))

print(number)
```

If user enters:

```text
abc
```

Output:

```text
ValueError
```

Program crashes.

---

### Using Try

```python
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")
```

Output:

```text
Enter a number: abc
Invalid Input
```

---

## Flow Diagram

```text
Try Block
    |
    v
Error?
  /   \
No     Yes
 |       |
Execute  Except Block
```

---

# Except Block

Used to catch and handle errors.

---

## Example 1: Division Error

```python
try:
    result = 10 / 0
except:
    print("Cannot divide by zero")
```

Output:

```text
Cannot divide by zero
```

---

## Example 2: Specific Exception

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed")
```

Output:

```text
Division by zero is not allowed
```

---

# Catching Multiple Exceptions

```python
try:
    num = int(input("Enter Number: "))
    result = 100 / num

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Number cannot be zero")
```

---

## Example Outputs

Input:

```text
abc
```

Output:

```text
Please enter a valid number
```

Input:

```text
0
```

Output:

```text
Number cannot be zero
```

---

# Else Block

Runs only if no exception occurs.

```python
try:
    num = int(input("Enter Number: "))
except ValueError:
    print("Invalid Number")
else:
    print("Successfully Entered:", num)
```

---

## Flow

```text
Try
 |
Success?
 /     \
Yes     No
 |       |
Else   Except
```

---

# Finally Block

Always executes whether exception occurs or not.

---

## Real-World Example

Database connection.

Even if error occurs:

- Connection must be closed
- Resources must be released

---

## Example

```python
try:
    file = open("sample.txt")

except FileNotFoundError:
    print("File Not Found")

finally:
    print("Execution Completed")
```

Output:

```text
File Not Found
Execution Completed
```

---

# Complete Example

```python
try:
    number = int(input("Enter Number: "))
    result = 100 / number

except ValueError:
    print("Invalid Input")

except ZeroDivisionError:
    print("Cannot Divide By Zero")

else:
    print("Result =", result)

finally:
    print("Program Finished")
```

---

# Raising Exceptions

Sometimes we create our own errors.

Use:

```python
raise
```

---

## Example

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

Output:

```text
ValueError: Age cannot be negative
```

---

# Custom Exceptions

Used in enterprise applications.

---

## Real-World Example

Bank Account Withdrawal

Rule:

- Withdrawal cannot exceed balance

---

## Creating Custom Exception

```python
class InsufficientBalanceError(Exception):
    pass
```

---

## Using Custom Exception

```python
class InsufficientBalanceError(Exception):
    pass


balance = 500

withdraw_amount = 1000

if withdraw_amount > balance:
    raise InsufficientBalanceError(
        "Not enough balance"
    )
```

Output:

```text
InsufficientBalanceError:
Not enough balance
```

---

# Enterprise Banking Example

```python
class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):

    if amount > balance:
        raise InsufficientBalanceError(
            "Insufficient Funds"
        )

    return balance - amount


try:
    new_balance = withdraw(5000, 7000)

except InsufficientBalanceError as e:
    print(e)
```

Output:

```text
Insufficient Funds
```

---

# Assertions

Assertions help developers verify assumptions.

---

## Syntax

```python
assert condition
```

---

## Example

```python
age = 20

assert age > 0

print("Valid Age")
```

Output:

```text
Valid Age
```

---

## Assertion Failure

```python
age = -5

assert age > 0
```

Output:

```text
AssertionError
```

---

## Assertion with Message

```python
age = -5

assert age > 0, "Age cannot be negative"
```

Output:

```text
AssertionError:
Age cannot be negative
```

---

# Real-World Assertion Example

```python
salary = -10000

assert salary >= 0, \
    "Salary cannot be negative"
```

Useful during development and testing.

---

# Logging

Logging records system activities and errors.

---

## Why Logging?

Instead of:

```python
print("Error")
```

Use logs.

Benefits:

- Audit trail
- Debugging
- Production monitoring

---

# Basic Logging

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Application Started")
```

Output:

```text
INFO:root:Application Started
```

---

# Logging Levels

| Level | Purpose |
|----------|----------|
| DEBUG | Detailed Information |
| INFO | Normal Information |
| WARNING | Potential Issue |
| ERROR | Error Occurred |
| CRITICAL | Serious Failure |

---

## Example

```python
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debug Message")

logging.info("Info Message")

logging.warning("Warning Message")

logging.error("Error Message")

logging.critical("Critical Message")
```

---

# Logging to File

```python
import logging

logging.basicConfig(
    filename="application.log",
    level=logging.INFO
)

logging.info("Program Started")
```

Creates:

```text
application.log
```

---

# Enterprise Logging Example

```python
import logging

logging.basicConfig(
    filename="bank.log",
    level=logging.INFO
)

try:
    result = 10 / 0

except Exception as e:
    logging.error(e)
```

---

# Debugging

Debugging means finding and fixing bugs.

---

## Simple Debugging

```python
a = 10
b = 5

print("a =", a)
print("b =", b)

result = a + b

print(result)
```

---

# Using Logging for Debugging

```python
import logging

logging.basicConfig(level=logging.DEBUG)

salary = 50000
bonus = 10000

logging.debug(
    f"Salary={salary}, Bonus={bonus}"
)

total = salary + bonus

logging.debug(
    f"Total={total}"
)
```

---

# Part 2: File Handling

---

# What is File Handling?

File handling allows programs to:

- Read data
- Write data
- Store information permanently

---

## Real-World Examples

- Employee Records
- Banking Transactions
- Student Databases
- Application Logs

---

# Opening a File

```python
file = open("sample.txt")
```

---

# Reading a File

Assume:

sample.txt

```text
Python
Java
Scala
```

---

## Read Entire File

```python
file = open("sample.txt")

content = file.read()

print(content)

file.close()
```

Output:

```text
Python
Java
Scala
```

---

# Read One Line

```python
file = open("sample.txt")

print(file.readline())

file.close()
```

Output:

```text
Python
```

---

# Read All Lines

```python
file = open("sample.txt")

print(file.readlines())

file.close()
```

Output:

```python
['Python\n', 'Java\n', 'Scala']
```

---

# Writing Files

---

## Write Mode

```python
file = open("employee.txt", "w")

file.write("John")

file.close()
```

Creates file.

---

# Append Mode

```python
file = open("employee.txt", "a")

file.write("\nMike")

file.close()
```

Adds data.

---

# File Modes

| Mode | Description |
|--------|-------------|
| r | Read |
| w | Write |
| a | Append |
| x | Create |
| rb | Read Binary |
| wb | Write Binary |
| r+ | Read + Write |

---

# Context Manager (Recommended)

Avoid:

```python
file = open(...)
file.close()
```

Use:

```python
with open("sample.txt") as file:
    content = file.read()

print(content)
```

Automatically closes file.

---

## Illustration

```text
with open(...)
       |
       v
 Read/Write
       |
       v
Auto Close
```

---

# CSV Files

CSV = Comma Separated Values

---

## Employee Data

```text
id,name,salary
1,John,50000
2,Mike,60000
```

---

# Reading CSV

```python
import csv

with open("employees.csv") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Output:

```python
['id','name','salary']
['1','John','50000']
['2','Mike','60000']
```

---

# Writing CSV

```python
import csv

with open(
    "employees.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow(
        ["id", "name", "salary"]
    )

    writer.writerow(
        [1, "John", 50000]
    )
```

---

# Real-World CSV Example

Sales Report

```python
sales = [
    ["Product", "Revenue"],
    ["Laptop", 100000],
    ["Mobile", 50000]
]
```

Store monthly reports.

---

# JSON Files

JSON = JavaScript Object Notation

Used heavily in:

- APIs
- Cloud Platforms
- Microservices

---

## JSON Example

```json
{
    "id": 101,
    "name": "John",
    "salary": 50000
}
```

---

# Writing JSON

```python
import json

employee = {
    "id": 101,
    "name": "John",
    "salary": 50000
}

with open(
    "employee.json",
    "w"
) as file:

    json.dump(
        employee,
        file,
        indent=4
    )
```

---

# Reading JSON

```python
import json

with open(
    "employee.json"
) as file:

    data = json.load(file)

print(data)
```

Output:

```python
{'id':101,'name':'John','salary':50000}
```

---

# Real-World JSON Example

API Response

```python
{
  "customer_id":101,
  "name":"Ravi",
  "city":"Mumbai"
}
```

---

# XML Files

XML = Extensible Markup Language

Often used in:

- Legacy Systems
- Banking Applications
- Configuration Files

---

## XML Example

```xml
<employee>
    <id>101</id>
    <name>John</name>
</employee>
```

---

# Reading XML

```python
import xml.etree.ElementTree as ET

tree = ET.parse(
    "employee.xml"
)

root = tree.getroot()

for child in root:
    print(
        child.tag,
        child.text
    )
```

Output:

```text
id 101
name John
```

---

# Writing XML

```python
import xml.etree.ElementTree as ET

root = ET.Element("employee")

ET.SubElement(
    root,
    "id"
).text = "101"

ET.SubElement(
    root,
    "name"
).text = "John"

tree = ET.ElementTree(root)

tree.write("employee.xml")
```

---

# Directory Operations

Use module:

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

os.mkdir("reports")
```

---

# Create Nested Directories

```python
os.makedirs(
    "2026/june/reports"
)
```

---

# List Files

```python
import os

print(os.listdir())
```

---

# Rename File

```python
os.rename(
    "old.txt",
    "new.txt"
)
```

---

# Delete File

```python
import os

os.remove("new.txt")
```

---

# Remove Directory

```python
os.rmdir("reports")
```

---

# Enterprise Example

```python
import os

folder = "daily_reports"

if not os.path.exists(folder):
    os.mkdir(folder)

print("Folder Ready")
```

Used in:

- ETL Pipelines
- Data Warehouses
- Reporting Systems

---

# Best Practices

✅ Always use Context Managers

```python
with open(...)
```

✅ Catch Specific Exceptions

```python
except FileNotFoundError
```

✅ Use Logging

```python
logging.error(...)
```

✅ Use Custom Exceptions

```python
class ValidationError(Exception)
```

✅ Validate with Assertions

```python
assert amount > 0
```

✅ Close Resources Properly

```python
finally:
    cleanup()
```

---

# Real-World Applications

| Topic | Real World Usage |
|---------|----------------|
| Exception Handling | Banking Systems |
| Custom Exceptions | Payment Validation |
| Assertions | Unit Testing |
| Logging | Production Monitoring |
| CSV Files | Sales Reports |
| JSON Files | APIs & Microservices |
| XML Files | Legacy Banking Systems |
| File Handling | Data Warehousing |
| Directory Operations | ETL Pipelines |
| Context Managers | Resource Management |

---

# Summary

Exception Handling:
- try
- except
- else
- finally
- raise
- custom exceptions
- assertions
- logging
- debugging

File Handling:
- reading files
- writing files
- CSV
- JSON
- XML
- context managers
- file modes
- directory operations

These concepts form the foundation of production-grade Python applications, ETL pipelines, automation frameworks, data engineering workflows, and enterprise software systems.
