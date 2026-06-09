# Packing and Unpacking in Python

Packing and unpacking are powerful Python features that make it easy to work with multiple values, function arguments, collections, and data structures.

---

# 1. What is Packing?

**Packing** means placing multiple values into a single variable (usually a tuple).

## Example 1: Tuple Packing

```python
data = 10, 20, 30

print(data)
print(type(data))
```

### Output

```text
(10, 20, 30)
<class 'tuple'>
```

Python automatically packs the values into a tuple.

---

## Example 2: Packing Different Data Types

```python
employee = 101, "John", 50000.50, True

print(employee)
```

### Output

```text
(101, 'John', 50000.5, True)
```

---

# 2. What is Unpacking?

**Unpacking** means extracting values from a collection into individual variables.

## Example 1: Tuple Unpacking

```python
data = (10, 20, 30)

a, b, c = data

print(a)
print(b)
print(c)
```

### Output

```text
10
20
30
```

---

## Example 2: List Unpacking

```python
numbers = [100, 200, 300]

x, y, z = numbers

print(x, y, z)
```

### Output

```text
100 200 300
```

---

# 3. Packing and Unpacking Together

```python
employee = 101, "Raj", "Developer"

emp_id, name, designation = employee

print(emp_id)
print(name)
print(designation)
```

### Output

```text
101
Raj
Developer
```

---

# 4. Extended Unpacking Using *

The `*` operator collects multiple values.

## Example 1

```python
numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print(first)
print(middle)
print(last)
```

### Output

```text
10
[20, 30, 40]
50
```

---

## Example 2

```python
a, *b = [1, 2, 3, 4, 5]

print(a)
print(b)
```

### Output

```text
1
[2, 3, 4, 5]
```

---

## Example 3

```python
*a, b = [1, 2, 3, 4, 5]

print(a)
print(b)
```

### Output

```text
[1, 2, 3, 4]
5
```

---

# 5. Packing Function Arguments (*args)

`*args` packs multiple positional arguments into a tuple.

## Example 1

```python
def display(*args):
    print(args)

display(10, 20, 30)
```

### Output

```text
(10, 20, 30)
```

---

## Example 2

```python
def total(*numbers):
    print(sum(numbers))

total(10, 20, 30)
total(1, 2, 3, 4, 5)
```

### Output

```text
60
15
```

---

# 6. Unpacking Function Arguments

The `*` operator unpacks a sequence when calling a function.

## Example

```python
def add(a, b, c):
    print(a + b + c)

numbers = [10, 20, 30]

add(*numbers)
```

### Output

```text
60
```

---

# 7. Packing Keyword Arguments (**kwargs)

`**kwargs` packs keyword arguments into a dictionary.

## Example 1

```python
def employee_info(**kwargs):
    print(kwargs)

employee_info(id=101, name="John", salary=50000)
```

### Output

```text
{'id': 101, 'name': 'John', 'salary': 50000}
```

---

## Example 2

```python
def details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

details(name="Raj", city="Chennai", age=30)
```

### Output

```text
name : Raj
city : Chennai
age : 30
```

---

# 8. Unpacking Dictionary Arguments

The `**` operator unpacks dictionary key-value pairs.

```python
def employee(id, name, salary):
    print(id, name, salary)

data = {
    "id": 101,
    "name": "John",
    "salary": 50000
}

employee(**data)
```

### Output

```text
101 John 50000
```

---

# 9. Using *args and **kwargs Together

```python
def process_data(name, *skills, **details):
    print("Name:", name)
    print("Skills:", skills)
    print("Details:", details)

process_data(
    "John",
    "Python",
    "SQL",
    city="Chennai",
    experience=5
)
```

### Output

```text
Name: John
Skills: ('Python', 'SQL')
Details: {'city': 'Chennai', 'experience': 5}
```

---

# 10. Swapping Variables Using Unpacking

```python
a = 10
b = 20

a, b = b, a

print(a, b)
```

### Output

```text
20 10
```

---

# 11. Ignoring Values During Unpacking

```python
data = (10, 20, 30)

a, _, c = data

print(a)
print(c)
```

### Output

```text
10
30
```

---

# 12. Nested Unpacking

```python
employee = ("John", (101, "Developer"))

name, (emp_id, role) = employee

print(name)
print(emp_id)
print(role)
```

### Output

```text
John
101
Developer
```

---

# 13. List Merging Using *

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged = [*list1, *list2]

print(merged)
```

### Output

```text
[1, 2, 3, 4, 5, 6]
```

---

# 14. Dictionary Merging Using **

```python
emp = {"id": 101}
info = {"name": "John"}

result = {**emp, **info}

print(result)
```

### Output

```text
{'id': 101, 'name': 'John'}
```

---

# 15. Real-World Data Engineering Examples

## Example 1: ETL Configuration

```python
config = {
    "source": "mysql",
    "target": "snowflake",
    "batch_size": 1000
}

source, target, batch_size = config.values()

print(source)
print(target)
print(batch_size)
```

### Output

```text
mysql
snowflake
1000
```

---

## Example 2: Dynamic SQL Builder

```python
columns = ["id", "name", "salary"]

query = "SELECT {} FROM employee".format(
    ", ".join(columns)
)

print(query)
```

### Output

```text
SELECT id, name, salary FROM employee
```

---

## Example 3: Processing Multiple Files

```python
def process_files(*files):
    for file in files:
        print("Processing:", file)

process_files(
    "customers.csv",
    "orders.csv",
    "products.csv"
)
```

### Output

```text
Processing: customers.csv
Processing: orders.csv
Processing: products.csv
```

---

# 16. Advanced Examples

## Example 1: Returning Multiple Values

```python
def get_employee():
    return 101, "John", 50000

emp_id, name, salary = get_employee()

print(emp_id)
print(name)
print(salary)
```

### Output

```text
101
John
50000
```

---

## Example 2: Multiple Assignment

```python
a, b, c = 10, 20, 30

print(a, b, c)
```

### Output

```text
10 20 30
```

---

## Example 3: Unpacking Strings

```python
a, b, c = "CAT"

print(a)
print(b)
print(c)
```

### Output

```text
C
A
T
```

---

## Example 4: Unpacking Sets

```python
numbers = {10, 20, 30}

a, b, c = numbers

print(a, b, c)
```

> Note: Sets are unordered. Output order may vary.

---

# Common Errors

## Error 1: Too Many Values

```python
a, b = [1, 2, 3]
```

### Output

```text
ValueError: too many values to unpack (expected 2)
```

---

## Error 2: Not Enough Values

```python
a, b, c = [1, 2]
```

### Output

```text
ValueError: not enough values to unpack (expected 3, got 2)
```

---

# Interview Questions

## Q1. What is Packing?

Packing is the process of collecting multiple values into a single variable.

```python
data = 1, 2, 3
```

---

## Q2. What is Unpacking?

Unpacking is the process of assigning elements from a collection into multiple variables.

```python
a, b, c = data
```

---

## Q3. Difference Between *args and **kwargs

| Feature | *args | **kwargs |
|----------|--------|-----------|
| Type | Tuple | Dictionary |
| Accepts | Positional Arguments | Keyword Arguments |
| Symbol | * | ** |

---

## Q4. Why Use Packing and Unpacking?

Benefits:

- Cleaner code
- Flexible functions
- Dynamic parameter handling
- Commonly used in APIs
- Useful in ETL pipelines
- Simplifies data processing

---

# Cheat Sheet

```python
# Packing
data = 1, 2, 3

# Unpacking
a, b, c = data

# Extended unpacking
a, *b = [1, 2, 3, 4]

# Packing positional arguments
def f(*args):
    pass

# Unpacking positional arguments
f(*[1, 2, 3])

# Packing keyword arguments
def g(**kwargs):
    pass

# Unpacking keyword arguments
g(**{"name": "John"})

# Merge lists
[*list1, *list2]

# Merge dictionaries
{**d1, **d2}

# Swap variables
a, b = b, a

# Ignore values
a, _, c = data
```

---

# Key Takeaways

- **Packing** → Multiple values → One variable
- **Unpacking** → One collection → Multiple variables
- `*args` → Packs positional arguments into a tuple
- `**kwargs` → Packs keyword arguments into a dictionary
- `*` → Unpacks iterables
- `**` → Unpacks dictionaries
- Extensively used in Python APIs, ETL pipelines, Data Engineering, Spark applications, and automation scripts.
