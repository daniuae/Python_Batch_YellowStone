# Python Exception Handling and File Handling – Complete Guide

---

# Table of Contents

1. Exception Handling
   - Try Block
   - Except Block
   - Else Block
   - Finally Block
   - Multiple Exceptions
   - Nested Exception Handling
   - Raising Exceptions
   - Custom Exceptions
   - Assertions

2. Logging and Debugging
   - Logging Levels
   - Logging to File
   - Exception Logging
   - Debugging Techniques

3. File Handling
   - Reading Files
   - Writing Files
   - Appending Files
   - File Modes
   - Context Managers

4. CSV Files
   - Read CSV
   - Write CSV
   - DictReader
   - DictWriter

5. JSON Files
   - Read JSON
   - Write JSON
   - Pretty Printing

6. XML Files
   - Read XML
   - Write XML

7. Directory and File Operations
   - Create Directory
   - Rename Directory
   - Delete Directory
   - List Files
   - Walk Directory Structure

8. Real-World Combined Examples

---

# 1. Exception Handling

Exception handling allows a program to continue running even when errors occur.

---

## Basic Try and Except

### Example

```python
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Invalid input. Please enter a number.")
```

### Output

```text
Enter a number: abc
Invalid input. Please enter a number.
```

---

## Try, Except and Else

Else executes only if no exception occurs.

```python
try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid Number")
else:
    print("Square =", num ** 2)
```

---

## Try, Except and Finally

Finally always executes.

```python
try:
    file = open("sample.txt")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution completed")
```

---

## Multiple Exceptions

```python
try:
    result = 10 / int(input("Enter divisor: "))
except ValueError:
    print("Please enter a valid integer")
except ZeroDivisionError:
    print("Division by zero not allowed")
```

---

## Single Except for Multiple Errors

```python
try:
    result = 10 / int(input("Enter divisor: "))
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)
```

---

## Generic Exception

```python
try:
    x = 10 / 0
except Exception as e:
    print("Unexpected Error:", e)
```

---

## Nested Exception Handling

```python
try:
    try:
        num = int(input("Enter number: "))
        result = 10 / num
    except ZeroDivisionError:
        print("Cannot divide by zero")
except ValueError:
    print("Invalid number")
```

---

## Raise Exception Manually

```python
age = 15

if age < 18:
    raise ValueError("Age must be 18 or above")
```

---

# 2. Custom Exceptions

Custom exceptions help create business-specific validations.

---

## Basic Custom Exception

```python
class InvalidSalaryError(Exception):
    pass

salary = -5000

if salary < 0:
    raise InvalidSalaryError("Salary cannot be negative")
```

---

## Real World Example

```python
class InsufficientBalanceError(Exception):
    pass

balance = 1000
withdraw = 2000

if withdraw > balance:
    raise InsufficientBalanceError(
        "Insufficient balance"
    )
```

---

# 3. Assertions

Assertions validate assumptions.

---

## Basic Assertion

```python
age = 25

assert age >= 18

print("Eligible")
```

---

## Failed Assertion

```python
marks = -5

assert marks >= 0, "Marks cannot be negative"
```

Output

```text
AssertionError: Marks cannot be negative
```

---

# 4. Logging and Debugging

Logging records application events.

---

## Logging Levels

| Level | Purpose |
|---------|----------|
| DEBUG | Detailed Information |
| INFO | Normal Information |
| WARNING | Warning Messages |
| ERROR | Error Messages |
| CRITICAL | Serious Errors |

---

## Basic Logging

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Program Started")
logging.warning("Low Disk Space")
logging.error("Database Connection Failed")
```

---

## Logging to File

```python
import logging

logging.basicConfig(
    filename="application.log",
    level=logging.INFO
)

logging.info("Application Started")
```

---

## Logging Exceptions

```python
import logging

logging.basicConfig(level=logging.ERROR)

try:
    result = 10 / 0
except Exception:
    logging.exception("Exception occurred")
```

---

## Debug Logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)

name = "John"

logging.debug(f"Processing {name}")
```

---

# 5. File Handling

---

## Opening a File

```python
file = open("sample.txt", "r")
```

---

## Reading Entire File

```python
file = open("sample.txt", "r")

data = file.read()

print(data)

file.close()
```

---

## Read One Line

```python
file = open("sample.txt", "r")

line = file.readline()

print(line)

file.close()
```

---

## Read All Lines

```python
file = open("sample.txt", "r")

lines = file.readlines()

print(lines)

file.close()
```

---

## Writing File

```python
file = open("sample.txt", "w")

file.write("Welcome to Python")

file.close()
```

---

## Appending Data

```python
file = open("sample.txt", "a")

file.write("\nNew Record")

file.close()
```

---

# 6. File Modes

| Mode | Description |
|--------|------------|
| r | Read |
| w | Write |
| a | Append |
| x | Create New File |
| r+ | Read + Write |
| w+ | Write + Read |
| a+ | Append + Read |
| rb | Read Binary |
| wb | Write Binary |

---

## Example r+

```python
file = open("sample.txt", "r+")

print(file.read())

file.write("Extra Data")

file.close()
```

---

## Binary File

```python
file = open("image.jpg", "rb")

content = file.read()

file.close()
```

---

# 7. Context Managers

Recommended approach.

---

## Basic Example

```python
with open("sample.txt", "r") as file:
    data = file.read()

print(data)
```

Advantages:

- Automatic file closing
- Cleaner code
- Safer resource handling

---

## Writing with Context Manager

```python
with open("sample.txt", "w") as file:
    file.write("Python Training")
```

---

# 8. Working with CSV Files

CSV = Comma Separated Values

---

## Read CSV

employees.csv

```csv
id,name,salary
1,John,50000
2,Alice,60000
```

Python

```python
import csv

with open("employees.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

---

## Write CSV

```python
import csv

with open(
    "employees.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow(["id", "name", "salary"])
    writer.writerow([1, "John", 50000])
```

---

## CSV DictReader

```python
import csv

with open("employees.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"])
```

---

## CSV DictWriter

```python
import csv

with open(
    "employees.csv",
    "w",
    newline=""
) as file:

    fields = ["id", "name"]

    writer = csv.DictWriter(
        file,
        fieldnames=fields
    )

    writer.writeheader()

    writer.writerow({
        "id":1,
        "name":"John"
    })
```

---

# 9. Working with JSON

JSON = JavaScript Object Notation

---

## Python Dictionary to JSON

```python
import json

employee = {
    "id": 1,
    "name": "John",
    "salary": 50000
}

with open("employee.json", "w") as file:
    json.dump(employee, file)
```

---

## Read JSON

```python
import json

with open("employee.json") as file:
    data = json.load(file)

print(data)
```

---

## Pretty Print JSON

```python
import json

employee = {
    "name": "John",
    "salary": 50000
}

print(
    json.dumps(
        employee,
        indent=4
    )
)
```

---

# 10. Working with XML

---

## Read XML

employees.xml

```xml
<employees>
    <employee>
        <name>John</name>
        <salary>50000</salary>
    </employee>
</employees>
```

Python

```python
import xml.etree.ElementTree as ET

tree = ET.parse("employees.xml")

root = tree.getroot()

for emp in root.findall("employee"):
    print(emp.find("name").text)
```

---

## Write XML

```python
import xml.etree.ElementTree as ET

root = ET.Element("employees")

employee = ET.SubElement(
    root,
    "employee"
)

name = ET.SubElement(
    employee,
    "name"
)

name.text = "John"

tree = ET.ElementTree(root)

tree.write("employees.xml")
```

---

# 11. Directory Operations

---

## Create Directory

```python
import os

os.mkdir("reports")
```

---

## Create Nested Directory

```python
import os

os.makedirs(
    "project/data/input"
)
```

---

## Remove Directory

```python
import os

os.rmdir("reports")
```

---

## Rename Directory

```python
import os

os.rename(
    "reports",
    "monthly_reports"
)
```

---

## Check File Exists

```python
import os

if os.path.exists("sample.txt"):
    print("File Exists")
```

---

# 12. File Operations

---

## Delete File

```python
import os

os.remove("sample.txt")
```

---

## File Information

```python
import os

print(
    os.path.getsize(
        "sample.txt"
    )
)

print(
    os.path.abspath(
        "sample.txt"
    )
)
```

---

## List Files

```python
import os

files = os.listdir()

for file in files:
    print(file)
```

---

## Traverse Directory Tree

```python
import os

for root, dirs, files in os.walk("."):
    print(root)

    for file in files:
        print(file)
```

---

# 13. Combined Real-World Example

Employee Data Processing System

Features:

- Read employee CSV
- Validate salary
- Handle exceptions
- Log errors
- Save output to JSON

```python
import csv
import json
import logging

logging.basicConfig(
    filename="errors.log",
    level=logging.ERROR
)

employees = []

try:
    with open("employees.csv") as file:

        reader = csv.DictReader(file)

        for row in reader:

            salary = float(row["salary"])

            assert salary > 0

            employees.append(row)

    with open(
        "employees.json",
        "w"
    ) as outfile:

        json.dump(
            employees,
            outfile,
            indent=4
        )

except AssertionError:
    logging.error(
        "Invalid salary found"
    )

except FileNotFoundError:
    logging.error(
        "CSV file missing"
    )

except Exception as e:
    logging.exception(e)

finally:
    print(
        "Employee processing completed"
    )
```

---

# Key Interview Questions

1. Difference between Exception and Error?
2. What is the purpose of finally block?
3. Difference between raise and assert?
4. Why use custom exceptions?
5. Difference between read(), readline(), readlines()?
6. Difference between JSON and XML?
7. What are context managers?
8. Why use with open()?
9. Difference between logging and print()?
10. Explain file modes r, w, a, r+, w+, a+.
11. How do you read large CSV files efficiently?
12. Difference between os and pathlib modules?
13. How does os.walk() work?
14. When should assertions be used?
15. How do you log exceptions in production applications?

---
