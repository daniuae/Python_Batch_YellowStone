# Python Collections, Iterators, Generators, Threading & Concurrency

---

# 1. Sets

## What is a Set?

A **Set** is an unordered collection of unique elements.

### Characteristics

- No duplicate values
- Mutable (can add/remove items)
- Unordered
- Fast lookup operations

```python
fruits = {"apple", "banana", "mango"}

print(fruits)
```

**Output**

```python
{'apple', 'banana', 'mango'}
```

---

## Creating Sets

```python
numbers = {1, 2, 3, 4}

colors = set(["red", "green", "blue"])

print(numbers)
print(colors)
```

---

## Adding Elements

```python
fruits = {"apple", "banana"}

fruits.add("orange")

print(fruits)
```

---

## Removing Elements

### remove()

```python
fruits.remove("banana")
```

### discard()

```python
fruits.discard("grapes")
```

> No error occurs if the element doesn't exist.

---

## Set Operations

### Union

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)
```

**Output**

```python
{1, 2, 3, 4, 5}
```

---

### Intersection

```python
print(A & B)
```

**Output**

```python
{3}
```

---

### Difference

```python
print(A - B)
```

**Output**

```python
{1, 2}
```

---

### Symmetric Difference

```python
print(A ^ B)
```

**Output**

```python
{1, 2, 4, 5}
```

---

## Real-World Example

Finding unique website visitors.

```python
visitors = [
    "John",
    "Mary",
    "John",
    "David",
    "Mary"
]

unique_visitors = set(visitors)

print(unique_visitors)
```

---

# 2. Dictionaries

## What is a Dictionary?

A dictionary stores data as key-value pairs.

```python
student = {
    "id": 101,
    "name": "Rahul",
    "marks": 95
}

print(student)
```

---

## Accessing Values

```python
print(student["name"])
```

**Output**

```python
Rahul
```

---

## Using get()

```python
print(student.get("marks"))
```

**Output**

```python
95
```

---

## Adding a New Key

```python
student["city"] = "Mumbai"

print(student)
```

---

## Updating Values

```python
student["marks"] = 98
```

---

## Removing Values

```python
student.pop("city")
```

---

## Looping Through a Dictionary

```python
for key, value in student.items():
    print(key, value)
```

---

## Dictionary Comprehension

```python
squares = {
    x: x * x
    for x in range(1, 6)
}

print(squares)
```

**Output**

```python
{
    1:1,
    2:4,
    3:9,
    4:16,
    5:25
}
```

---

## Real-World Example

Employee Information System

```python
employee = {
    "emp_id": 101,
    "name": "Amit",
    "department": "IT",
    "salary": 80000
}

print(employee["department"])
```

---

# 3. Nested Structures

Nested structures combine lists, dictionaries, tuples, and sets.

---

## List Inside Dictionary

```python
student = {
    "name": "Rahul",
    "subjects": [
        "Math",
        "Physics",
        "Chemistry"
    ]
}

print(student["subjects"][0])
```

**Output**

```python
Math
```

---

## Dictionary Inside Dictionary

```python
employee = {
    "id": 101,
    "personal": {
        "name": "John",
        "city": "Mumbai"
    }
}

print(employee["personal"]["city"])
```

**Output**

```python
Mumbai
```

---

## List of Dictionaries

```python
employees = [
    {"id": 1, "name": "Amit"},
    {"id": 2, "name": "Priya"},
    {"id": 3, "name": "Rahul"}
]

print(employees[1]["name"])
```

**Output**

```python
Priya
```

---

## Real-World Example

E-Commerce Orders

```python
orders = [
    {
        "order_id": 1001,
        "customer": "Rahul",
        "items": [
            "Laptop",
            "Mouse"
        ]
    },
    {
        "order_id": 1002,
        "customer": "Priya",
        "items": [
            "Keyboard",
            "Monitor"
        ]
    }
]

print(orders[0]["items"])
```

---

# 4. Iteration and Manipulation

## Iterating Through a List

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

---

## Using enumerate()

```python
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

**Output**

```python
0 Apple
1 Banana
2 Mango
```

---

## Iterating Through Dictionary

```python
student = {
    "name": "Rahul",
    "marks": 90
}

for key, value in student.items():
    print(key, value)
```

---

## List Comprehension

### Traditional Approach

```python
squares = []

for i in range(5):
    squares.append(i * i)
```

### Pythonic Approach

```python
squares = [i * i for i in range(5)]

print(squares)
```

**Output**

```python
[0, 1, 4, 9, 16]
```

---

## Filtering Data

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    n
    for n in numbers
    if n % 2 == 0
]

print(even_numbers)
```

**Output**

```python
[2, 4, 6]
```

---

# 5. Iterators and Generators

## Iterator

An iterator remembers its current position and returns one item at a time.

### Creating an Iterator

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

**Output**

```python
10
20
30
```

---

## Custom Iterator Example

```python
class Counter:

    def __init__(self, max_value):
        self.current = 1
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):

        if self.current > self.max_value:
            raise StopIteration

        value = self.current
        self.current += 1

        return value


counter = Counter(5)

for num in counter:
    print(num)
```

**Output**

```python
1
2
3
4
5
```

---

# Generators

Generators produce values lazily using the `yield` keyword.

### Benefits

- Memory efficient
- Faster for large datasets
- Lazy evaluation

---

## Generator Function

```python
def generate_numbers():

    yield 1
    yield 2
    yield 3

g = generate_numbers()

print(next(g))
print(next(g))
print(next(g))
```

**Output**

```python
1
2
3
```

---

## Generator with Loop

```python
def even_numbers(limit):

    for i in range(limit):

        if i % 2 == 0:
            yield i


for num in even_numbers(10):
    print(num)
```

**Output**

```python
0
2
4
6
8
```

---

## Real-World Example

Reading a Large File

```python
def read_file(file_name):

    with open(file_name) as file:

        for line in file:
            yield line


for line in read_file("sales.txt"):
    print(line)
```

This is memory efficient because only one line is loaded at a time.

---

# 6. Threading and Concurrency

## What is Threading?

Threading allows multiple tasks to execute concurrently.

### Common Use Cases

- API calls
- File downloads
- Database operations
- ETL jobs
- Network requests

---

## Single Thread Example

```python
import time

def task():

    for i in range(5):
        print(i)
        time.sleep(1)

task()
```

Approximate execution time:

```python
5 seconds
```

---

## Multi-Thread Example

```python
import threading
import time

def task(name):

    for i in range(3):
        print(name, i)
        time.sleep(1)


t1 = threading.Thread(
    target=task,
    args=("Thread-1",)
)

t2 = threading.Thread(
    target=task,
    args=("Thread-2",)
)

t1.start()
t2.start()

t1.join()
t2.join()

print("Completed")
```

---

## ThreadPoolExecutor Example

```python
from concurrent.futures import ThreadPoolExecutor
import time

def process_order(order):

    time.sleep(2)

    return f"Processed {order}"


orders = [
    "Laptop",
    "Mouse",
    "Keyboard"
]

with ThreadPoolExecutor(max_workers=3) as executor:

    results = executor.map(
        process_order,
        orders
    )

    for result in results:
        print(result)
```

**Output**

```python
Processed Laptop
Processed Mouse
Processed Keyboard
```

---

## Multiprocessing Example

```python
from multiprocessing import Process

def task():
    print("Running Process")

p1 = Process(target=task)
p2 = Process(target=task)

p1.start()
p2.start()

p1.join()
p2.join()
```

---

# Concurrency vs Parallelism

| Feature | Concurrency | Parallelism |
|----------|------------|------------|
| Meaning | Multiple tasks in progress | Multiple tasks run simultaneously |
| CPU Usage | Single or Multiple CPU | Multiple CPUs/Cores |
| Goal | Better resource utilization | Faster execution |
| Example | Threading | Multiprocessing |

---

# Data Engineering Example

Parallel File Processing

```python
from concurrent.futures import ThreadPoolExecutor

files = [
    "sales.csv",
    "orders.csv",
    "customers.csv"
]

def process_file(file):
    print(f"Processing {file}")

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(
        process_file,
        files
    )
```

### Benefits

- Faster ETL processing
- Improved resource utilization
- Parallel ingestion
- Reduced execution time

---

# Quick Revision Cheat Sheet

| Topic | Purpose |
|---------|----------|
| Set | Store unique values |
| Dictionary | Store key-value pairs |
| Nested Structures | Represent complex data |
| Iteration | Traverse collections |
| Iterator | Sequential access using `next()` |
| Generator | Lazy value generation using `yield` |
| Threading | Concurrent execution |
| ThreadPoolExecutor | Manage thread pools |
| Multiprocessing | True parallel execution |
| Concurrency | Multiple tasks progressing together |
| Parallelism | Multiple tasks executing simultaneously |
