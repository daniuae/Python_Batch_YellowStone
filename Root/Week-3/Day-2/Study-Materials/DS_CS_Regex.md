# Python Data Structures, Control Structures & Regular Expressions

---

# 1. Data Structures

Data structures are used to store and organize data efficiently.

## Types Covered

1. Lists
2. Tuples

---

# Lists

A List is an ordered, mutable (changeable) collection.

### Creating a List

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits)
```

Output:

```text
['Apple', 'Banana', 'Mango']
```

---

## Accessing Elements

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[1])
```

Output:

```text
Apple
Banana
```

---

## Negative Indexing

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[-1])
```

Output:

```text
Mango
```

---

## Modifying List

```python
fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)
```

Output:

```text
['Apple', 'Orange', 'Mango']
```

---

## Adding Elements

### append()

```python
fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)
```

Output:

```text
['Apple', 'Banana', 'Mango']
```

---

### insert()

```python
fruits = ["Apple", "Mango"]

fruits.insert(1, "Banana")

print(fruits)
```

Output:

```text
['Apple', 'Banana', 'Mango']
```

---

## Removing Elements

### remove()

```python
fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)
```

Output:

```text
['Apple', 'Mango']
```

---

### pop()

```python
fruits = ["Apple", "Banana", "Mango"]

removed = fruits.pop()

print(removed)
print(fruits)
```

Output:

```text
Mango
['Apple', 'Banana']
```

---

## List Slicing

```python
numbers = [10,20,30,40,50]

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

---

## Iterating Through List

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

Output:

```text
Apple
Banana
Mango
```

---

## Real World Example

```python
employees = ["Rahul", "Priya", "Amit"]

employees.append("Kiran")

for emp in employees:
    print(emp)
```

Output:

```text
Rahul
Priya
Amit
Kiran
```

---

# Tuples

A Tuple is an ordered and immutable collection.

---

## Creating Tuple

```python
colors = ("Red", "Green", "Blue")

print(colors)
```

Output:

```text
('Red', 'Green', 'Blue')
```

---

## Access Tuple Elements

```python
colors = ("Red", "Green", "Blue")

print(colors[0])
```

Output:

```text
Red
```

---

## Tuple Cannot Be Modified

```python
colors = ("Red", "Green", "Blue")

colors[0] = "Black"
```

Output:

```text
TypeError
```

---

## Tuple Unpacking

```python
name, age, city = ("Rahul", 25, "Mumbai")

print(name)
print(age)
print(city)
```

Output:

```text
Rahul
25
Mumbai
```

---

## Real World Example

Employee record should not change.

```python
employee = (101, "Rahul", "Developer")

print(employee)
```

Output:

```text
(101, 'Rahul', 'Developer')
```

---

# 2. Control Structures

Control structures decide how code executes.

---

# Conditional Statements

---

## if Statement

```python
age = 18

if age >= 18:
    print("Eligible to vote")
```

Output:

```text
Eligible to vote
```

---

## if-else Statement

```python
age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

Output:

```text
Not Eligible
```

---

## if-elif-else Statement

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

Output:

```text
Grade B
```

---

## Nested if

```python
age = 25
salary = 50000

if age > 18:
    if salary > 30000:
        print("Loan Approved")
```

Output:

```text
Loan Approved
```

---

# Loops

Loops repeat a block of code.

---

# For Loop

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

---

## Loop Through String

```python
name = "Python"

for ch in name:
    print(ch)
```

Output:

```text
P
y
t
h
o
n
```

---

## Loop Through List

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

---

# While Loop

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
```

---

# Infinite Loop Example

```python
while True:
    print("Running")
```

Use carefully!

---

# Loop Control Statements

---

## break

Stops the loop immediately.

```python
for i in range(10):

    if i == 5:
        break

    print(i)
```

Output:

```text
0
1
2
3
4
```

---

## continue

Skips current iteration.

```python
for i in range(5):

    if i == 2:
        continue

    print(i)
```

Output:

```text
0
1
3
4
```

---

## pass

Placeholder for future code.

```python
for i in range(5):

    if i == 3:
        pass

    print(i)
```

Output:

```text
0
1
2
3
4
```

---

# Real World Example

Finding first failed student.

```python
marks = [80, 90, 45, 70, 85]

for mark in marks:

    if mark < 50:
        print("Failed Student Found")
        break
```

Output:

```text
Failed Student Found
```

---

# 3. Comprehensions

Comprehensions create collections in a single line.

---

# List Comprehension

Traditional way:

```python
squares = []

for i in range(1,6):
    squares.append(i*i)

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

---

Using List Comprehension

```python
squares = [i*i for i in range(1,6)]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

---

## With Condition

```python
even_numbers = [i for i in range(10) if i % 2 == 0]

print(even_numbers)
```

Output:

```text
[0, 2, 4, 6, 8]
```

---

# Dictionary Comprehension

```python
square_dict = {x: x*x for x in range(1,6)}

print(square_dict)
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

# Set Comprehension

```python
square_set = {x*x for x in range(1,6)}

print(square_set)
```

Output:

```text
{1, 4, 9, 16, 25}
```

---

## Real World Example

Convert names to uppercase.

```python
employees = ["rahul", "priya", "amit"]

result = [emp.upper() for emp in employees]

print(result)
```

Output:

```text
['RAHUL', 'PRIYA', 'AMIT']
```

---

# 4. Regular Expressions (Regex)

Regular Expressions are used to search, validate, extract, and replace patterns in text.

---

## Import Regex Module

```python
import re
```

---

# re.search()

Find first match.

```python
import re

text = "Python is easy"

result = re.search("easy", text)

print(result)
```

Output:

```text
<re.Match object>
```

---

# re.findall()

Returns all matches.

```python
import re

text = "Cat Bat Rat"

result = re.findall(r"\w+at", text)

print(result)
```

Output:

```text
['Cat', 'Bat', 'Rat']
```

---

# re.match()

Checks from beginning.

```python
import re

text = "Python"

result = re.match("Py", text)

print(result)
```

Output:

```text
<re.Match object>
```

---

# re.sub()

Replace text.

```python
import re

text = "I like Java"

result = re.sub("Java", "Python", text)

print(result)
```

Output:

```text
I like Python
```

---

# Common Regex Patterns

| Pattern | Meaning |
|----------|----------|
| . | Any character |
| \d | Digit |
| \D | Non-digit |
| \w | Word character |
| \W | Non-word character |
| \s | Space |
| \S | Non-space |
| ^ | Start of string |
| $ | End of string |
| * | Zero or more |
| + | One or more |
| ? | Optional |

---

# Extract Phone Numbers

```python
import re

text = "Call me at 9876543210"

phone = re.findall(r"\d{10}", text)

print(phone)
```

Output:

```text
['9876543210']
```

---

# Extract Email Address

```python
import re

text = "Email: rahul@gmail.com"

email = re.findall(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    text
)

print(email)
```

Output:

```text
['rahul@gmail.com']
```

---

# Validate PAN Number

Indian PAN Format:

ABCDE1234F

```python
import re

pan = "ABCDE1234F"

pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]$"

if re.match(pattern, pan):
    print("Valid PAN")
else:
    print("Invalid PAN")
```

Output:

```text
Valid PAN
```

---

# Validate Aadhaar Number

```python
import re

aadhaar = "123412341234"

pattern = r"^\d{12}$"

if re.match(pattern, aadhaar):
    print("Valid Aadhaar")
else:
    print("Invalid Aadhaar")
```

Output:

```text
Valid Aadhaar
```

---

# Real World ETL Example

Extract all customer IDs from a log file.

```python
import re

log = """
CustomerID:1001
CustomerID:1002
CustomerID:1003
"""

ids = re.findall(r"CustomerID:(\d+)", log)

print(ids)
```

Output:

```text
['1001', '1002', '1003']
```

---

# Interview Questions

### Q1. Difference between List and Tuple?

| List | Tuple |
|--------|--------|
| Mutable | Immutable |
| Uses [] | Uses () |
| Slower | Faster |
| More memory | Less memory |

---

### Q2. Difference between break and continue?

| break | continue |
|---------|-----------|
| Exits loop | Skips current iteration |
| Loop stops | Loop continues |

---

### Q3. Why use Comprehensions?

- Cleaner code
- Faster execution
- Less memory usage
- Easy filtering and transformations

---

### Q4. Why use Regex?

- Data Validation
- Data Extraction
- Data Cleaning
- Log Analysis
- ETL Pipelines
- Web Scraping

---

# Summary

✔ Lists (Create, Update, Delete, Iterate)

✔ Tuples (Immutable Collections)

✔ Conditional Statements (if, elif, else)

✔ Loops (for, while)

✔ Loop Controls (break, continue, pass)

✔ List, Dictionary and Set Comprehensions

✔ Regular Expressions (search, match, findall, sub)

✔ Real-world ETL and Data Engineering examples

✔ Interview Questions and Best Practices
