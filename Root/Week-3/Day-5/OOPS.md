# Object-Oriented Programming (OOP) in Python

## What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into **objects**.

An object contains:

- **Attributes (Data/Properties)**
- **Methods (Functions/Behaviors)**

### Real-World Example

Consider a **Car**.

**Attributes:**

- Brand
- Model
- Color
- Speed

**Methods:**

- Start()
- Stop()
- Accelerate()

In Python, we can represent a car using a class.

---

# Classes and Objects

## What is a Class?

A class is a blueprint for creating objects.

### Syntax

```python
class ClassName:
    pass
```

---

## What is an Object?

An object is an instance of a class.

### Example

```python
class Car:
    pass

car1 = Car()
car2 = Car()

print(type(car1))
```

### Output

```text
<class '__main__.Car'>
```

---

## Creating a Class with Attributes and Methods

```python
class Car:

    def set_details(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand :", self.brand)
        print("Model :", self.model)


car1 = Car()

car1.set_details("Toyota", "Innova")
car1.display()
```

### Output

```text
Brand : Toyota
Model : Innova
```

---

# Constructors and Destructors

## Constructor

A constructor is a special method automatically called when an object is created.

Python constructor:

```python
__init__()
```

### Example

```python
class Employee:

    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def display(self):
        print(f"Employee ID : {self.emp_id}")
        print(f"Name        : {self.name}")


emp = Employee(101, "Rahul")

emp.display()
```

### Output

```text
Employee ID : 101
Name        : Rahul
```

---

## Why Use Constructors?

Instead of:

```python
emp = Employee()

emp.id = 101
emp.name = "Rahul"
```

We can directly initialize values:

```python
emp = Employee(101, "Rahul")
```

Cleaner and safer.

---

## Destructor

Destructor is automatically called when an object is destroyed.

Python destructor:

```python
__del__()
```

### Example

```python
class Demo:

    def __init__(self):
        print("Object Created")

    def __del__(self):
        print("Object Destroyed")


obj = Demo()

del obj
```

### Output

```text
Object Created
Object Destroyed
```

---

## Real-World Use Cases of Destructor

- Closing database connections
- Closing files
- Releasing resources
- Cleaning temporary objects

---

# Inheritance

## What is Inheritance?

Inheritance allows one class to acquire properties and methods of another class.

### Parent Class

```python
class Animal:

    def eat(self):
        print("Animal is eating")
```

### Child Class

```python
class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()
```

### Output

```text
Animal is eating
Dog is barking
```

---

## Types of Inheritance

### Single Inheritance

```python
class A:
    pass

class B(A):
    pass
```

---

### Multilevel Inheritance

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass
```

---

### Multiple Inheritance

```python
class Father:
    pass

class Mother:
    pass

class Child(Father, Mother):
    pass
```

---

# Polymorphism

## What is Polymorphism?

One interface, multiple implementations.

Same method behaves differently for different objects.

---

## Example

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

### Output

```text
Bark
Meow
```

---

## Real-World Example

```python
class Payment:

    def pay(self):
        pass


class CreditCard(Payment):

    def pay(self):
        print("Paid using Credit Card")


class UPI(Payment):

    def pay(self):
        print("Paid using UPI")


payments = [CreditCard(), UPI()]

for p in payments:
    p.pay()
```

### Output

```text
Paid using Credit Card
Paid using UPI
```

---

# Encapsulation

## What is Encapsulation?

Encapsulation means hiding internal data and controlling access.

---

### Example

```python
class BankAccount:

    def __init__(self):
        self.__balance = 10000

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount()

account.deposit(5000)

print(account.get_balance())
```

### Output

```text
15000
```

---

## Attempting Direct Access

```python
print(account.__balance)
```

### Output

```text
AttributeError
```

Because the variable is private.

---

# Abstraction

## What is Abstraction?

Abstraction hides implementation details and exposes only essential functionality.

---

## Example Using Abstract Base Classes

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car Started")


car = Car()
car.start()
```

### Output

```text
Car Started
```

---

## Real-World Example

When driving a car:

- You use steering
- You use brake
- You use accelerator

You do not need to know the engine's internal mechanics.

This is abstraction.

---

# Magic Methods (Dunder Methods)

Magic methods begin and end with double underscores.

```python
__method__
```

Python automatically calls them.

---

# __init__()

Constructor

```python
class Student:

    def __init__(self, name):
        self.name = name


s = Student("John")
```

---

# __str__()

Provides a readable string representation.

### Example

```python
class Employee:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Employee({self.name})"


emp = Employee("Rahul")

print(emp)
```

### Output

```text
Employee(Rahul)
```

Without `__str__()`:

```text
<__main__.Employee object at 0x001>
```

---

# __len__()

```python
class Team:

    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)


team = Team(["A", "B", "C"])

print(len(team))
```

### Output

```text
3
```

---

# __add__()

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)


n1 = Number(10)
n2 = Number(20)

print(n1 + n2)
```

### Output

```text
30
```

---

# Common Magic Methods

| Method | Purpose |
|----------|----------|
| __init__ | Constructor |
| __str__ | String representation |
| __repr__ | Developer representation |
| __len__ | Length |
| __add__ | Addition |
| __sub__ | Subtraction |
| __mul__ | Multiplication |
| __eq__ | Equality |
| __lt__ | Less than |
| __gt__ | Greater than |
| __del__ | Destructor |

---

# Working with Libraries

## What is a Library?

A library is a collection of reusable code.

Python libraries help us perform tasks quickly.

Examples:

```text
NumPy
Pandas
Matplotlib
Scikit-Learn
TensorFlow
PySpark
```

---

# NumPy for Numerical Data Analysis

## What is NumPy?

NumPy stands for:

```text
Numerical Python
```

It is the foundation of:

- Data Analysis
- Data Science
- Machine Learning
- AI
- Scientific Computing

---

## Why NumPy?

Python Lists:

```python
numbers = [1, 2, 3, 4]
```

NumPy Arrays:

```python
import numpy as np

numbers = np.array([1, 2, 3, 4])
```

Advantages:

- Faster
- Less memory
- Vectorized operations
- Mathematical functions
- Multi-dimensional arrays

---

# Creating Arrays

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)
```

Output:

```text
[10 20 30 40]
```

---

# Array Properties

```python
import numpy as np

arr = np.array([[1, 2], [3, 4]])

print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
```

Output:

```text
2
(2, 2)
4
int64
```

---

# Special Arrays

## Zeros

```python
import numpy as np

arr = np.zeros((3, 3))

print(arr)
```

Output:

```text
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
```

---

## Ones

```python
arr = np.ones((2, 2))

print(arr)
```

Output:

```text
[[1. 1.]
 [1. 1.]]
```

---

## Range

```python
arr = np.arange(1, 11)

print(arr)
```

Output:

```text
[1 2 3 4 5 6 7 8 9 10]
```

---

# Vectorized Operations

Without Loop

```python
import numpy as np

sales = np.array([1000, 2000, 3000])

sales = sales * 1.10

print(sales)
```

Output:

```text
[1100. 2200. 3300.]
```

Adding 10% growth to all sales records at once.

---

# Mathematical Operations

```python
import numpy as np

data = np.array([10, 20, 30, 40])

print(np.sum(data))
print(np.mean(data))
print(np.max(data))
print(np.min(data))
```

Output:

```text
100
25.0
40
10
```

---

# Reshaping Arrays

```python
import numpy as np

arr = np.arange(12)

matrix = arr.reshape(3, 4)

print(matrix)
```

Output:

```text
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
```

---

# Real-World Example: Sales Analysis

```python
import numpy as np

sales = np.array([
    10000,
    15000,
    18000,
    20000,
    25000
])

print("Total Sales :", np.sum(sales))
print("Average Sales :", np.mean(sales))
print("Maximum Sales :", np.max(sales))
print("Minimum Sales :", np.min(sales))
```

### Output

```text
Total Sales : 88000
Average Sales : 17600.0
Maximum Sales : 25000
Minimum Sales : 10000
```

---

# OOP + NumPy Example

```python
import numpy as np

class SalesAnalyzer:

    def __init__(self, sales):
        self.sales = np.array(sales)

    def total_sales(self):
        return np.sum(self.sales)

    def average_sales(self):
        return np.mean(self.sales)

    def max_sales(self):
        return np.max(self.sales)


analyzer = SalesAnalyzer(
    [10000, 12000, 15000, 18000]
)

print("Total :", analyzer.total_sales())
print("Average :", analyzer.average_sales())
print("Max :", analyzer.max_sales())
```

### Output

```text
Total : 55000
Average : 13750.0
Max : 18000
```

---

# Interview Questions

### Q1: What is OOP?

A programming paradigm based on classes and objects.

### Q2: Difference between Class and Object?

- Class → Blueprint
- Object → Instance of Class

### Q3: What are the four pillars of OOP?

1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism

### Q4: What is the purpose of __init__()?

It initializes object attributes when an object is created.

### Q5: Why use NumPy instead of Python lists?

- Faster execution
- Less memory usage
- Vectorized operations
- Scientific computing support

### Q6: What is vectorization?

Performing operations on entire arrays without explicit loops.
