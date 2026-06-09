# Important Python Concepts for Developers and Data Engineers

# Table of Contents

1. Python Memory Management and Garbage Collection (GC)
2. Packing and Unpacking
3. *args and **kwargs
4. Lambda Functions
5. Map, Filter, Reduce
6. List Comprehensions
7. Generators
8. Iterators
9. Decorators
10. Closures
11. Context Managers
12. Deep Copy vs Shallow Copy
13. Mutable vs Immutable Objects
14. Pass by Reference vs Pass by Value
15. Variable Scope (LEGB Rule)
16. Magic Methods (Dunder Methods)
17. Exception Handling
18. Multithreading
19. Multiprocessing
20. Global Interpreter Lock (GIL)
21. Property Decorators
22. Dataclasses
23. Named Tuples
24. Type Hints
25. Python Interview Questions

---

# 1. Garbage Collection (GC)

## What is Garbage Collection?

Garbage Collection automatically frees memory occupied by unused objects.

Python uses:

* Reference Counting
* Generational Garbage Collection

---

## Reference Counting

```python
a = [1, 2, 3]

b = a

c = a
```

Memory:

```text
a ---> [1,2,3]
b ---/
c --/
```

Reference Count = 3

---

## Deleting References

```python
del b
del c
```

Reference Count = 1

---

## When Count Becomes Zero

```python
a = [1, 2, 3]

del a
```

Object removed from memory.

---

## Using gc Module

```python
import gc

print(gc.get_count())

gc.collect()
```

Output

```python
(250, 5, 2)
```

---

# 2. Packing and Unpacking

## Packing

Multiple values packed into one variable.

```python
numbers = 10, 20, 30, 40

print(numbers)
```

Output

```python
(10, 20, 30, 40)
```

---

## Unpacking

```python
a, b, c = (10, 20, 30)

print(a)
print(b)
print(c)
```

Output

```python
10
20
30
```

---

## Extended Unpacking

```python
a, *b, c = [10,20,30,40,50]

print(a)
print(b)
print(c)
```

Output

```python
10
[20,30,40]
50
```

---

# 3. *args and **kwargs

## *args

Accepts multiple positional arguments.

```python
def add(*args):
    return sum(args)

print(add(10,20,30))
```

Output

```python
60
```

---

## **kwargs

Accepts keyword arguments.

```python
def employee(**kwargs):

    for key, value in kwargs.items():
        print(key, value)

employee(
    name="John",
    age=25
)
```

Output

```python
name John
age 25
```

---

# 4. Lambda Functions

Anonymous one-line functions.

```python
square = lambda x: x*x

print(square(5))
```

Output

```python
25
```

---

# 5. Map, Filter, Reduce

## Map

```python
numbers = [1,2,3,4]

result = list(
    map(lambda x:x*2,numbers)
)

print(result)
```

Output

```python
[2,4,6,8]
```

---

## Filter

```python
numbers = [1,2,3,4,5]

result = list(
    filter(
        lambda x:x%2==0,
        numbers
    )
)

print(result)
```

Output

```python
[2,4]
```

---

## Reduce

```python
from functools import reduce

result = reduce(
    lambda x,y:x+y,
    [1,2,3,4]
)

print(result)
```

Output

```python
10
```

---

# 6. List Comprehension

Traditional

```python
squares = []

for i in range(5):
    squares.append(i*i)
```

Comprehension

```python
squares = [i*i for i in range(5)]

print(squares)
```

Output

```python
[0,1,4,9,16]
```

---

# 7. Generators

Generate values one at a time.

```python
def numbers():

    yield 1
    yield 2
    yield 3

for num in numbers():
    print(num)
```

Output

```python
1
2
3
```

---

## Why Generators?

Less memory usage.

```python
def huge():

    for i in range(1000000):
        yield i
```

---

# 8. Iterators

Object implementing:

```python
__iter__()
__next__()
```

Example

```python
nums = iter([1,2,3])

print(next(nums))
print(next(nums))
```

Output

```python
1
2
```

---

# 9. Decorators

Add functionality without modifying original function.

```python
def logger(func):

    def wrapper():
        print("Starting")

        func()

        print("Finished")

    return wrapper
```

Usage

```python
@logger
def hello():
    print("Hello")

hello()
```

Output

```python
Starting
Hello
Finished
```

---

# 10. Closures

Inner function remembers outer variables.

```python
def outer(msg):

    def inner():
        print(msg)

    return inner

func = outer("Hello")

func()
```

Output

```python
Hello
```

---

# 11. Context Managers

Automatic resource management.

```python
with open("sample.txt") as file:
    data = file.read()
```

File automatically closes.

---

## Custom Context Manager

```python
class Database:

    def __enter__(self):
        print("Connected")
        return self

    def __exit__(
        self,
        exc_type,
        exc_val,
        exc_tb
    ):
        print("Closed")
```

Usage

```python
with Database():
    print("Using DB")
```

---

# 12. Deep Copy vs Shallow Copy

```python
import copy
```

---

## Shallow Copy

```python
original = [[1,2],[3,4]]

copy1 = copy.copy(original)

copy1[0][0] = 100

print(original)
```

Output

```python
[[100,2],[3,4]]
```

Original changed.

---

## Deep Copy

```python
copy2 = copy.deepcopy(original)

copy2[0][0] = 999
```

Original unchanged.

---

# 13. Mutable vs Immutable

## Mutable

```python
list
dict
set
```

Example

```python
x = [1,2]

x.append(3)
```

Modified.

---

## Immutable

```python
int
float
tuple
str
```

Example

```python
name = "Python"

name += "3"
```

Creates new object.

---

# 14. Variable Scope (LEGB)

Python searches variables in:

```text
Local
Enclosing
Global
Built-in
```

Example

```python
x = 100

def test():

    x = 10

    print(x)

test()

print(x)
```

Output

```python
10
100
```

---

# 15. Magic Methods

Special methods beginning with __

Example

```python
class Employee:

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

e = Employee("John")

print(e)
```

Output

```python
John
```

---

# 16. Exception Handling

```python
try:
    x = 10 / 0

except ZeroDivisionError:
    print("Cannot divide")

finally:
    print("Always executes")
```

Output

```python
Cannot divide
Always executes
```

---

# 17. Multithreading

Used for I/O tasks.

```python
import threading

def task():
    print("Running")

t1 = threading.Thread(target=task)

t1.start()

t1.join()
```

---

# 18. Multiprocessing

Used for CPU-intensive tasks.

```python
from multiprocessing import Process

def task():
    print("Processing")

p = Process(target=task)

p.start()

p.join()
```

---

# 19. Global Interpreter Lock (GIL)

GIL allows only one thread to execute Python bytecode at a time.

Impacts:

```text
CPU Tasks -> Multiprocessing
I/O Tasks -> Multithreading
```

---

# 20. Property Decorators

Getter and Setter.

```python
class Employee:

    def __init__(self):
        self._salary = 0

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,value):
        self._salary = value
```

Usage

```python
e = Employee()

e.salary = 50000

print(e.salary)
```

---

# 21. Dataclasses

Python 3.7+

```python
from dataclasses import dataclass

@dataclass
class Employee:

    name: str
    age: int

e = Employee(
    "John",
    25
)

print(e)
```

Output

```python
Employee(name='John', age=25)
```

---

# 22. NamedTuple

```python
from collections import namedtuple

Employee = namedtuple(
    "Employee",
    ["name","age"]
)

emp = Employee(
    "John",
    25
)

print(emp.name)
```

Output

```python
John
```

---

# 23. Type Hints

```python
def add(
    a:int,
    b:int
) -> int:

    return a+b
```

Usage

```python
print(add(10,20))
```

Output

```python
30
```

---

# 24. Frequently Asked Interview Questions

### What is GIL?

Global Interpreter Lock allows only one thread to execute Python bytecode at a time.

---

### Difference between List and Tuple?

| List    | Tuple     |
| ------- | --------- |
| Mutable | Immutable |
| []      | ()        |
| Slower  | Faster    |

---

### Difference between Generator and Iterator?

| Generator  | Iterator      |
| ---------- | ------------- |
| Uses yield | Uses **next** |
| Easy       | Manual        |

---

### Difference between Deep Copy and Shallow Copy?

| Deep Copy    | Shallow Copy      |
| ------------ | ----------------- |
| Fully copied | References copied |
| Independent  | Shared objects    |

---

### What are Decorators?

Functions that modify behavior of another function without changing its source code.

---

### What are Closures?

Functions that remember variables from their enclosing scope.

---

### What is Packing and Unpacking?

Packing combines multiple values into one object.

Unpacking extracts values into separate variables.

---

# Summary

Important Python concepts every Software Engineer, Data Engineer, Data Scientist, and Automation Engineer should know:

✔ Garbage Collection (GC)

✔ Packing & Unpacking

✔ *args and **kwargs

✔ Lambda Functions

✔ Map, Filter, Reduce

✔ List Comprehensions

✔ Generators

✔ Iterators

✔ Decorators

✔ Closures

✔ Context Managers

✔ Deep vs Shallow Copy

✔ Mutable vs Immutable

✔ LEGB Scope

✔ Magic Methods

✔ Exception Handling

✔ Multithreading

✔ Multiprocessing

✔ GIL

✔ Property Decorators

✔ Dataclasses

✔ NamedTuple

✔ Type Hints
