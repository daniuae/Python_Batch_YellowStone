# Case Study: Transportation Management System (Polymorphism in Python)

## Objective

Design a Transportation Management System where different vehicle types (`Car`, `Bike`, `Bus`, `Truck`, and `Train`) implement a common method called `transport_mode()` to demonstrate **Polymorphism**, **Method Overriding**, and **Abstract Classes** in Python.

---

# Learning Outcomes

By completing this case study, you will learn:

✅ Method Overriding

✅ Runtime Polymorphism

✅ Dynamic Dispatch

✅ Abstract Base Classes (ABC)

✅ Inheritance

✅ Object-Oriented Programming Principles

---

# Step 1: Create a New Python File

Create a file named:

```bash
transportation.py
```

---

# Step 2: Define the Base Class

The base class represents a generic vehicle.

```python
class Vehicle:
    def transport_mode(self):
        raise NotImplementedError(
            "Subclasses must implement this method"
        )
```

### Explanation

* `Vehicle` acts as a parent class.
* `transport_mode()` is a placeholder method.
* Any subclass must provide its own implementation.

---

# Step 3: Define Derived Classes

Create specific vehicle types.

```python
class Car(Vehicle):
    def transport_mode(self):
        return "Car transports people on roads."


class Bike(Vehicle):
    def transport_mode(self):
        return "Bike is used for short-distance travel."


class Bus(Vehicle):
    def transport_mode(self):
        return "Bus transports groups of people on scheduled routes."
```

---

# Class Hierarchy

```text
          Vehicle
             |
    -------------------
    |        |        |
   Car      Bike     Bus
```

---

# Step 4: Create Objects

```python
car = Car()
bike = Bike()
bus = Bus()
```

---

# Step 5: Test transport_mode()

```python
print(car.transport_mode())
print(bike.transport_mode())
print(bus.transport_mode())
```

### Output

```text
Car transports people on roads.
Bike is used for short-distance travel.
Bus transports groups of people on scheduled routes.
```

---

# Understanding Polymorphism

Even though all objects belong to different classes:

```python
car.transport_mode()
bike.transport_mode()
bus.transport_mode()
```

Python automatically calls the correct implementation.

This behavior is known as:

**Runtime Polymorphism**

---

# Step 6: Add a Common Feature

Add another method in the base class.

```python
class Vehicle:

    def transport_mode(self):
        raise NotImplementedError(
            "Subclasses must implement this method"
        )

    def fuel_efficiency(self):
        return "Fuel efficiency varies."
```

---

# Step 7: Override fuel_efficiency()

Each vehicle can provide its own implementation.

```python
class Car(Vehicle):

    def transport_mode(self):
        return "Car transports people on roads."

    def fuel_efficiency(self):
        return "Cars have moderate fuel efficiency."


class Bike(Vehicle):

    def transport_mode(self):
        return "Bike is used for short-distance travel."

    def fuel_efficiency(self):
        return "Bikes have high fuel efficiency."


class Bus(Vehicle):

    def transport_mode(self):
        return "Bus transports groups of people on scheduled routes."

    def fuel_efficiency(self):
        return "Buses are fuel-efficient for mass transportation."
```

---

# Step 8: Test Overridden Methods

```python
print(car.fuel_efficiency())
print(bike.fuel_efficiency())
print(bus.fuel_efficiency())
```

### Output

```text
Cars have moderate fuel efficiency.
Bikes have high fuel efficiency.
Buses are fuel-efficient for mass transportation.
```

---

# Method Overriding Illustration

```text
Vehicle
   |
fuel_efficiency()
   |
-----------------------------------
|               |                |
Car            Bike             Bus
|               |                |
Own Version   Own Version    Own Version
```

---

# Step 9: Dynamic Polymorphism

Create a function that accepts any vehicle.

```python
def describe_vehicle(vehicle):
    print(vehicle.transport_mode())
```

---

# Step 10: Test Runtime Polymorphism

```python
describe_vehicle(car)
describe_vehicle(bike)
describe_vehicle(bus)
```

### Output

```text
Car transports people on roads.
Bike is used for short-distance travel.
Bus transports groups of people on scheduled routes.
```

---

# Why This Works

The function does not care whether the object is:

* Car
* Bike
* Bus

It only expects:

```python
vehicle.transport_mode()
```

Python determines the actual method at runtime.

This is called:

### Dynamic Dispatch

---

# Step 11: Refactor Using main()

```python
def main():

    car = Car()
    bike = Bike()
    bus = Bus()

    describe_vehicle(car)
    describe_vehicle(bike)
    describe_vehicle(bus)


if __name__ == "__main__":
    main()
```

---

# Step 12: Convert to an Abstract Class

Python provides the `abc` module.

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def transport_mode(self):
        pass
```

---

# Why Use Abstract Classes?

Abstract classes:

* Prevent incomplete objects.
* Force subclasses to implement required methods.
* Improve code quality.
* Define a common contract.

---

# Step 13: Test Abstract Class Enforcement

```python
v = Vehicle()
```

### Output

```text
TypeError:
Can't instantiate abstract class Vehicle
with abstract methods transport_mode
```

---

# Step 14: Complete Implementation with ABC

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def transport_mode(self):
        pass

    @abstractmethod
    def fuel_efficiency(self):
        pass


class Car(Vehicle):

    def transport_mode(self):
        return "Car transports people on roads."

    def fuel_efficiency(self):
        return "Cars have moderate fuel efficiency."


class Bike(Vehicle):

    def transport_mode(self):
        return "Bike is used for short-distance travel."

    def fuel_efficiency(self):
        return "Bikes have high fuel efficiency."


class Bus(Vehicle):

    def transport_mode(self):
        return "Bus transports groups of people on scheduled routes."

    def fuel_efficiency(self):
        return "Buses are fuel-efficient for mass transportation."
```

---

# Step 15: Add More Vehicle Types

## Truck

```python
class Truck(Vehicle):

    def transport_mode(self):
        return "Truck transports heavy goods."

    def fuel_efficiency(self):
        return "Trucks consume more fuel due to heavy loads."
```

---

## Train

```python
class Train(Vehicle):

    def transport_mode(self):
        return "Train transports passengers and cargo on railways."

    def fuel_efficiency(self):
        return "Trains are highly efficient for long-distance transport."
```

---

# Enhanced Vehicle Hierarchy

```text
                    Vehicle
                       |
    ------------------------------------------------
    |         |         |          |              |
   Car       Bike      Bus       Truck         Train
```

---

# Step 16: Demonstrate Full Polymorphism

```python
vehicles = [
    Car(),
    Bike(),
    Bus(),
    Truck(),
    Train()
]

for vehicle in vehicles:
    print(vehicle.transport_mode())
    print(vehicle.fuel_efficiency())
    print("-" * 50)
```

---

# Output

```text
Car transports people on roads.
Cars have moderate fuel efficiency.
--------------------------------------------------

Bike is used for short-distance travel.
Bikes have high fuel efficiency.
--------------------------------------------------

Bus transports groups of people on scheduled routes.
Buses are fuel-efficient for mass transportation.
--------------------------------------------------

Truck transports heavy goods.
Trucks consume more fuel due to heavy loads.
--------------------------------------------------

Train transports passengers and cargo on railways.
Trains are highly efficient for long-distance transport.
--------------------------------------------------
```

---

# Real-World Use Case

Transportation companies often manage multiple vehicle types:

| Vehicle Type | Purpose                 |
| ------------ | ----------------------- |
| Car          | Personal transportation |
| Bike         | Quick local travel      |
| Bus          | Public transportation   |
| Truck        | Goods delivery          |
| Train        | Mass transportation     |

A transportation management system can treat all of them as `Vehicle` objects while allowing each to behave differently.

---

# Complete Program

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def transport_mode(self):
        pass

    @abstractmethod
    def fuel_efficiency(self):
        pass


class Car(Vehicle):

    def transport_mode(self):
        return "Car transports people on roads."

    def fuel_efficiency(self):
        return "Cars have moderate fuel efficiency."


class Bike(Vehicle):

    def transport_mode(self):
        return "Bike is used for short-distance travel."

    def fuel_efficiency(self):
        return "Bikes have high fuel efficiency."


class Bus(Vehicle):

    def transport_mode(self):
        return "Bus transports groups of people on scheduled routes."

    def fuel_efficiency(self):
        return "Buses are fuel-efficient for mass transportation."


class Truck(Vehicle):

    def transport_mode(self):
        return "Truck transports heavy goods."

    def fuel_efficiency(self):
        return "Trucks consume more fuel due to heavy loads."


class Train(Vehicle):

    def transport_mode(self):
        return "Train transports passengers and cargo on railways."

    def fuel_efficiency(self):
        return "Trains are highly efficient for long-distance transport."


def describe_vehicle(vehicle):
    print(vehicle.transport_mode())
    print(vehicle.fuel_efficiency())


def main():

    vehicles = [
        Car(),
        Bike(),
        Bus(),
        Truck(),
        Train()
    ]

    for vehicle in vehicles:
        describe_vehicle(vehicle)
        print("-" * 50)


if __name__ == "__main__":
    main()
```

---

# Key Concepts Learned

| Concept           | Description                                 |
| ----------------- | ------------------------------------------- |
| Inheritance       | Child classes inherit from parent class     |
| Method Overriding | Child class provides its own implementation |
| Polymorphism      | Same method behaves differently             |
| Dynamic Dispatch  | Correct method chosen at runtime            |
| Abstract Class    | Cannot be instantiated directly             |
| Abstract Method   | Must be implemented by subclasses           |
| Encapsulation     | Vehicle behavior grouped inside classes     |

---

# Interview Questions

### 1. What is polymorphism?

Polymorphism allows different classes to use the same method name but provide different implementations.

---

### 2. What is method overriding?

Providing a new implementation of a parent class method in a child class.

---

### 3. Why use abstract classes?

To enforce a common interface and prevent incomplete implementations.

---

### 4. What is runtime polymorphism?

Method execution is determined during program execution based on the actual object type.

---

### 5. What happens if an abstract method is not implemented?

Python raises a `TypeError` when attempting to instantiate the subclass.

---
