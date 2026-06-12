# Python OOP and NumPy Training Guide
## Beginner to Advanced with Real-World Examples

---

## Recommended Learning Sequence

Use this sequence:

```text
Real World Example
       ↓
Class Design
       ↓
Python Code
       ↓
Object Creation
       ↓
Visualization
       ↓
Hands-On Exercise
```

Example:

```text
Employee Management System
       ↓
Employee Class
       ↓
Create Employees
       ↓
Perform Operations
       ↓
Explain OOP Concepts
```

This approach makes learning easier.

---

# PART 1: OBJECT ORIENTED PROGRAMMING (OOP)

---

# What is OOP?

Object-Oriented Programming is a programming style that organizes code into objects.

Real World:

```text
Employee
Car
Bank Account
Student
Product
Hospital Patient
```

All these are objects.

---

# OOP Pillars

```text
1. Class
2. Object
3. Encapsulation
4. Inheritance
5. Polymorphism
6. Abstraction
```

---

# 1. Classes and Objects

---

## Real World Example

Think of a Car.

Every car has:

```text
Brand
Model
Color
Speed
```

These are attributes.

A car can:

```text
Start
Stop
Accelerate
```

These are behaviors.

---

## Class Diagram

```text
+------------------+
|       Car        |
+------------------+
| brand            |
| color            |
| speed            |
+------------------+
| start()          |
| stop()           |
+------------------+
```

---

## Example 1

```python
class Car:

    def start(self):
        print("Car Started")

car1 = Car()

car1.start()
```

Output

```text
Car Started
```

---

## Example 2

```python
class Employee:

    def display(self):
        print("Employee Details")

emp = Employee()

emp.display()
```

---

# Exercise

Create:

```text
Student
Product
Customer
HospitalPatient
```

Classes and objects.

---

# 2. Constructors (__init__)

---

## What is Constructor?

Constructor initializes an object.

Runs automatically when object is created.

---

## Real World Example

When a new employee joins:

```text
ID
Name
Salary
```

must be assigned immediately.

---

## Example

```python
class Employee:

    def __init__(self, emp_id, name):

        self.emp_id = emp_id
        self.name = name

emp = Employee(101, "Raj")

print(emp.emp_id)
print(emp.name)
```

Output

```text
101
Raj
```

---

## Illustration

```text
Employee(101, Raj)
        |
        v
 __init__()
        |
        v
Object Created
```

---

# Multiple Attributes Example

```python
class Employee:

    def __init__(self, emp_id, name, salary):

        self.emp_id = emp_id
        self.name = name
        self.salary = salary

emp = Employee(1001, "John", 85000)

print(emp.salary)
```

---

# Exercise

Create constructor for:

```text
Student
Book
Product
Hospital Patient
```

---

# 3. Destructor (__del__)

---

## What is Destructor?

Called when object is destroyed.

---

## Example

```python
class Employee:

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} object deleted")

emp = Employee("John")

del emp
```

Output

```text
John object deleted
```

---

## Real World Example

```text
Database Connection Closed
File Closed
Socket Closed
```

---

# 4. Encapsulation

---

## Definition

Protecting data from direct access.

---

## Real World Example

ATM Machine

```text
Balance is hidden
User only sees:
Deposit()
Withdraw()
CheckBalance()
```

---

## Without Encapsulation

```python
class BankAccount:

    def __init__(self):
        self.balance = 10000

account = BankAccount()

account.balance = -50000

print(account.balance)
```

Problem:

```text
Invalid Balance
```

---

## With Encapsulation

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

Output

```text
15000
```

---

# Illustration

```text
User
 |
 v
Deposit()
Withdraw()
 |
 v
Private Data
```

---

# 5. Inheritance

---

## Definition

Child class acquires properties from Parent class.

---

## Real World Example

```text
Vehicle
  |
  +---- Car
  |
  +---- Bike
  |
  +---- Bus
```

---

## Example

```python
class Vehicle:

    def move(self):
        print("Vehicle Moving")

class Car(Vehicle):
    pass

car = Car()

car.move()
```

Output

```text
Vehicle Moving
```

---

# Illustration

```text
Vehicle
   |
   +--- Car
   |
   +--- Bike
```

---

# Exercise

Create:

```text
Animal
   |
   + Dog
   + Cat
```

---

# 6. Polymorphism

---

## Definition

Same method behaves differently.

---

## Real World Example

```text
Dog -> Sound()
Cat -> Sound()
Bird -> Sound()
```

Same method.

Different output.

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

Output

```text
Bark
Meow
```

---

# Illustration

```text
sound()
   |
   +--- Dog → Bark
   |
   +--- Cat → Meow
```

---

# 7. Abstraction

---

## Definition

Show essential information.

Hide implementation.

---

## Real World Example

```text
Car Start Button

User:
Press Button

Hidden:
Fuel System
Battery
Engine
```

---

## Example

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):

    def move(self):
        print("Car Moving")

car = Car()

car.move()
```

---

# 8. Magic Methods

---

# __init__()

Constructor

```python
class Student:

    def __init__(self,name):
        self.name=name
```

---

# __str__()

Controls object printing.

Without __str__

```python
class Student:
    pass

s=Student()

print(s)
```

Output

```text
<__main__.Student object at 0x100>
```

---

With __str__

```python
class Student:

    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f"Student({self.name})"

s=Student("Raj")

print(s)
```

Output

```text
Student(Raj)
```

---

# __len__()

```python
class Team:

    def __len__(self):
        return 25

team=Team()

print(len(team))
```

Output

```text
25
```

---

# __add__()

```python
class Employee:

    def __init__(self,salary):
        self.salary=salary

    def __add__(self,other):
        return self.salary+other.salary

e1=Employee(50000)
e2=Employee(60000)

print(e1+e2)
```

Output

```text
110000
```

---

# PART 2 : NUMPY

---

# What is NumPy?

NumPy = Numerical Python

Used for:

```text
Data Analytics
Machine Learning
Artificial Intelligence
Scientific Computing
ETL Processing
```

---

# Why NumPy?

Python List Problems:

```text
Slow
Consumes More Memory
Limited Mathematical Operations
```

NumPy Solves:

```text
Fast
Efficient
Vectorized Operations
```

---

# Illustration

```text
Python List
      |
      v
Slow Processing

NumPy Array
      |
      v
Fast Processing
```

---

# Import NumPy

```python
import numpy as np
```

---

# Create Array

```python
arr = np.array([10,20,30,40])

print(arr)
```

Output

```text
[10 20 30 40]
```

---

# Array Properties

```python
arr=np.array([10,20,30])

print(arr.ndim)
print(arr.size)
print(arr.shape)
```

Output

```text
1
3
(3,)
```

---

# 2D Array

```python
arr=np.array([
    [1,2],
    [3,4]
])

print(arr)
```

Output

```text
[[1 2]
 [3 4]]
```

---

# Real World Example

Sales Data

```python
sales=np.array([
    [100,200,300],
    [150,250,350]
])

print(sales)
```

---

# Mathematical Operations

```python
a=np.array([10,20,30])

print(a+10)
print(a*2)
```

Output

```text
[20 30 40]
[20 40 60]
```

---

# Aggregate Functions

```python
sales=np.array([100,200,300,400])

print(np.sum(sales))
print(np.mean(sales))
print(np.max(sales))
print(np.min(sales))
```

Output

```text
1000
250
400
100
```

---

# Reshaping

```python
arr=np.arange(12)

print(arr.reshape(3,4))
```

Output

```text
[[ 0 1 2 3]
 [ 4 5 6 7]
 [ 8 9 10 11]]
```

---

# Filtering

```python
sales=np.array([100,200,300,400])

print(sales[sales>200])
```

Output

```text
[300 400]
```

---

# Real World ETL Example

```python
sales=np.array([
    100,
    250,
    300,
    50,
    600
])

high_sales=sales[sales>200]

print(high_sales)
```

Output

```text
[250 300 600]
```

---

# Random Data Generation

```python
np.random.randint(
    1,
    100,
    10
)
```

Output

```text
Random 10 numbers
```

---

# Data Engineering Example

Daily Pipeline Runtime

```python
runtime=np.array([
    30,
    45,
    28,
    35,
    40
])

print("Average:",np.mean(runtime))
print("Max:",np.max(runtime))
print("Min:",np.min(runtime))
```

---

# Mini Project

## Employee Salary Analytics

```python
import numpy as np

salary=np.array([
    50000,
    60000,
    70000,
    80000,
    90000
])

print("Average Salary:",np.mean(salary))
print("Maximum Salary:",np.max(salary))
print("Minimum Salary:",np.min(salary))
print("Total Salary:",np.sum(salary))
```

---

# Training Tips for Freshers

## Day 1

```text
Class
Object
Constructor
```

Employee Example

---

## Day 2

```text
Encapsulation
Inheritance
Polymorphism
```

Vehicle Example

---

## Day 3

```text
Magic Methods
Abstraction
```

Bank Example

---

## Day 4

```text
NumPy Arrays
Operations
Filtering
Aggregation
```

Sales Example

---

## Day 5

```text
Mini Projects

Employee System
Bank System
Sales Analytics
ETL Monitoring Dashboard
```

This progression helps trainees understand OOP and NumPy through practical business scenarios instead of memorizing theory.
