# Java OOP & Concurrency Complete Guide

> **Interview Preparation Notes with Real-World Examples**

---

# Table of Contents

1. Classes & Objects
2. Constructors
3. Method Overloading
4. Method Overriding
5. Inheritance
6. Abstraction
7. Interfaces vs Abstract Classes
8. Encapsulation
9. Polymorphism
10. `final` Keyword
11. `this` Keyword
12. `super` Keyword
13. Composition vs Inheritance
14. Static Binding vs Dynamic Binding
15. SOLID Principles
16. Concurrency & Multithreading
17. Threads
18. Runnable
19. Executor Framework
20. Future
21. Synchronization
22. Locks
23. Deadlocks
24. Race Conditions
25. Interview Questions
26. Summary

---

# 1. Classes and Objects

## What is a Class?

A **class** is a blueprint or template that defines the properties (fields) and behaviors (methods) of an object.

### Real-World Example

Think of a **building blueprint**.

The blueprint contains:

* Number of rooms
* Floors
* Doors
* Windows

But it is **not** an actual building.

---

## What is an Object?

An object is an **instance of a class**.

Objects occupy memory and can perform actions defined in the class.

### Example

Blueprint → Car

Objects:

* BMW
* Audi
* Tesla

Each is an object created from the Car class.

---

## Java Example

```java
class Car {

    String brand;
    int speed;

    void start() {
        System.out.println(brand + " started.");
    }
}

public class Main {

    public static void main(String[] args) {

        Car car = new Car();

        car.brand = "BMW";
        car.speed = 220;

        car.start();
    }
}
```

---

# 2. Constructors

A constructor initializes an object when it is created.

Constructors:

* Have the same name as the class
* Do not have a return type
* Are automatically called during object creation

---

## Default Constructor

```java
class Student {

    Student() {
        System.out.println("Student Created");
    }
}
```

---

## Parameterized Constructor

```java
class Student {

    String name;

    Student(String name) {
        this.name = name;
    }
}
```

---

## Constructor Overloading

```java
class Employee {

    Employee() {}

    Employee(String name) {}

    Employee(String name, int age) {}
}
```

---

## Real-World Example

Buying a new mobile phone:

* RAM allocated
* Operating system installed
* Battery initialized

Before you use it, initialization occurs.

A constructor performs similar initialization.

---

# 3. Method Overloading

Method overloading means **multiple methods with the same name but different parameter lists**.

It is **Compile-Time Polymorphism**.

---

## Example

```java
class Calculator {

    int add(int a, int b) {
        return a + b;
    }

    int add(int a, int b, int c) {
        return a + b + c;
    }

    double add(double a, double b) {
        return a + b;
    }
}
```

---

## Real-World Example

Google Search supports:

* Text search
* Voice search
* Image search

Same operation, different inputs.

---

# 4. Method Overriding

Method overriding allows a child class to provide its own implementation of a method inherited from the parent class.

It is **Runtime Polymorphism**.

---

## Example

```java
class Animal {

    void sound() {
        System.out.println("Animal Sound");
    }
}

class Dog extends Animal {

    @Override
    void sound() {
        System.out.println("Bark");
    }
}
```

---

## Real-World Example

Animal sounds:

* Dog → Bark
* Cat → Meow
* Cow → Moo

---

# Overloading vs Overriding

| Overloading          | Overriding              |
| -------------------- | ----------------------- |
| Same class           | Parent and child class  |
| Different parameters | Same signature          |
| Compile time         | Runtime                 |
| Faster               | Slight runtime overhead |

---

# 5. Inheritance

Inheritance enables one class to acquire the properties and methods of another class.

---

## Example

```java
class Employee {

    void work() {
        System.out.println("Working");
    }
}

class Manager extends Employee {

    void approveLeave() {
        System.out.println("Leave Approved");
    }
}
```

---

## Real-World Example

Employee

↓

Manager

↓

Project Manager

Every Project Manager is an Employee.

---

## Advantages

* Code reuse
* Reduced duplication
* Easy maintenance
* Extensibility

---

# 6. Abstraction

Abstraction hides implementation details while exposing only essential functionality.

---

## Example

```java
abstract class Vehicle {

    abstract void start();

    void stop() {
        System.out.println("Vehicle Stopped");
    }
}

class Car extends Vehicle {

    void start() {
        System.out.println("Car Started");
    }
}
```

---

## Real-World Example

ATM Machine

User presses:

Withdraw Money

↓

Gets Cash

Hidden details:

* Banking Server
* Database
* Encryption
* Transaction Processing

---

# 7. Interface vs Abstract Class

| Interface                     | Abstract Class             |
| ----------------------------- | -------------------------- |
| Contract                      | Partial implementation     |
| Multiple inheritance          | Single inheritance         |
| No constructors               | Constructors allowed       |
| Public static final variables | Instance variables allowed |
| Used for capability           | Used for common behavior   |

---

## Interface Example

```java
interface Flyable {

    void fly();
}

class Bird implements Flyable {

    public void fly() {
        System.out.println("Bird Flying");
    }
}
```

---

## Real-World Example

### Interface

Human can:

* Walk
* Swim
* Drive

These are capabilities.

---

### Abstract Class

Vehicle

Common features:

* Engine
* Wheels

Specific behavior:

* Bike
* Car
* Bus

---

# 8. Encapsulation

Encapsulation wraps data and methods into one unit while restricting direct access to data.

---

## Example

```java
class Account {

    private double balance;

    public void deposit(double amount) {
        balance += amount;
    }

    public double getBalance() {
        return balance;
    }
}
```

---

## Real-World Example

Bank Account

Balance is private.

Only methods like:

* Deposit
* Withdraw

can modify it.

---

# 9. Polymorphism

One interface.

Many implementations.

---

## Example

```java
class Payment {

    void pay() {
        System.out.println("Generic Payment");
    }
}

class UPI extends Payment {

    @Override
    void pay() {
        System.out.println("UPI Payment");
    }
}
```

---

## Real-World Example

Payment options:

* UPI
* Credit Card
* Debit Card
* Net Banking

All perform payment differently.

---

# 10. final Keyword

Used to restrict modification.

---

## Final Variable

```java
final int MAX_USERS = 100;
```

Cannot be changed.

---

## Final Method

```java
final void display() {}
```

Cannot be overridden.

---

## Final Class

```java
final class Utility {}
```

Cannot be inherited.

---

## Real-World Example

Government-issued Aadhaar Number

It cannot be modified once issued.

---

# 11. this Keyword

Refers to the current object.

---

## Uses

Current object variable

```java
this.name = name;
```

Current method

```java
this.display();
```

Current constructor

```java
this();
```

---

## Real-World Example

"I am Dani."

The word **I** refers to the current person.

---

# 12. super Keyword

Refers to the parent class.

---

## Uses

Call parent constructor

```java
super();
```

Access parent variable

```java
super.name;
```

Call parent method

```java
super.display();
```

---

## Real-World Example

Child says:

"My father owns this house."

Accessing the parent's property.

---

# 13. Composition vs Inheritance

## Inheritance

Represents an **IS-A** relationship.

Example

Dog **IS-A** Animal.

---

## Composition

Represents a **HAS-A** relationship.

Example

Car **HAS-A** Engine.

---

## Java Example

```java
class Engine {}

class Car {

    Engine engine = new Engine();
}
```

---

## Real-World Example

Laptop has:

* CPU
* RAM
* SSD

Laptop does not inherit from CPU.

---

# 14. Static Binding vs Dynamic Binding

## Static Binding

Occurs at compile time.

Applicable to:

* static methods
* final methods
* private methods

---

## Dynamic Binding

Occurs at runtime.

Method overriding uses dynamic binding.

---

## Example

```java
Animal animal = new Dog();

animal.sound();
```

The JVM decides at runtime which implementation to execute.

---

## Real-World Example

Customer Support IVR

Press:

1 → Sales

2 → Billing

The system determines the destination during execution.

---

# 15. SOLID Principles

---

## S - Single Responsibility Principle

A class should have only one responsibility.

Example:

Employee class should not generate reports and send emails.

---

## O - Open/Closed Principle

Open for extension.

Closed for modification.

Use interfaces or inheritance to extend behavior.

---

## L - Liskov Substitution Principle

A child object should replace the parent object without breaking functionality.

---

## I - Interface Segregation Principle

Avoid forcing classes to implement unnecessary methods.

---

## D - Dependency Inversion Principle

Depend on abstractions rather than concrete implementations.

---

## Real-World Example

A mobile phone charges with any compatible USB-C charger because it depends on a standard interface, not a specific charger brand.

---

# 16. Concurrency & Multithreading

Concurrency allows multiple tasks to make progress during overlapping periods.

Multithreading enables multiple threads to execute within the same process.

---

## Real-World Example

Restaurant

* Chef cooks
* Waiter serves
* Cashier bills

Tasks happen simultaneously.

---

# 17. Threads

A thread is the smallest unit of execution inside a process.

---

## Example

```java
class MyThread extends Thread {

    public void run() {
        System.out.println("Thread Running");
    }
}
```

---

# 18. Runnable

Preferred way of creating threads.

```java
class Task implements Runnable {

    public void run() {
        System.out.println("Task Running");
    }
}
```

---

# Thread vs Runnable

| Thread                      | Runnable                 |
| --------------------------- | ------------------------ |
| Extends Thread              | Implements Runnable      |
| Cannot extend another class | Can extend another class |
| Less flexible               | Preferred                |

---

# 19. Executor Framework

Instead of creating threads manually, use thread pools.

---

## Example

```java
ExecutorService executor =
        Executors.newFixedThreadPool(3);

executor.submit(() -> {
    System.out.println("Executing Task");
});

executor.shutdown();
```

---

## Real-World Example

Restaurant hires five waiters instead of hiring a new waiter for every customer.

---

# 20. Future

Represents the result of an asynchronous computation.

---

## Example

```java
Future<Integer> future =
executor.submit(() -> 100 + 200);

System.out.println(future.get());
```

---

## Real-World Example

Ordering food online.

You place the order now and receive the meal later.

---

# 21. Synchronization

Synchronization allows only one thread to access a shared resource at a time.

---

## Example

```java
class Counter {

    int count;

    synchronized void increment() {
        count++;
    }
}
```

---

## Real-World Example

Only one customer can use an ATM at a time.

---

# 22. Locks

Provides advanced synchronization features.

---

## Example

```java
Lock lock = new ReentrantLock();

lock.lock();

try {

    System.out.println("Critical Section");

} finally {

    lock.unlock();
}
```

---

## Real-World Example

Meeting Room

Take the key

↓

Use room

↓

Return key

---

# synchronized vs Lock

| synchronized     | Lock                         |
| ---------------- | ---------------------------- |
| JVM managed      | API managed                  |
| Automatic unlock | Manual unlock                |
| Simple           | Flexible                     |
| Limited features | tryLock(), timeout, fairness |

---

# 23. Race Conditions

A race condition occurs when multiple threads update shared data simultaneously without proper synchronization.

---

## Example

```java
class Counter {

    int count = 0;

    void increment() {
        count++;
    }
}
```

Two threads executing `increment()` simultaneously may produce an incorrect final count.

---

## Real-World Example

Shared Bank Account

Balance = ₹1000

Thread A withdraws ₹500

Thread B withdraws ₹700

If both read the balance before either updates it, the final balance becomes incorrect.

---

## Prevention

* synchronized
* ReentrantLock
* AtomicInteger
* Concurrent Collections

---

# 24. Deadlocks

Deadlock occurs when two or more threads wait indefinitely for each other to release resources.

---

## Example

```
Thread A

Lock Resource 1

Waiting for Resource 2

----------------------------

Thread B

Lock Resource 2

Waiting for Resource 1
```

Both threads wait forever.

---

## Real-World Example

Two cars enter a one-lane bridge from opposite directions.

Neither can move until the other backs up.

---

## Prevention

* Acquire locks in the same order.
* Keep lock duration short.
* Use tryLock().
* Avoid nested locks.

---

# Common Interview Questions

1. What is the difference between a class and an object?
2. What is a constructor?
3. Explain constructor overloading.
4. Difference between overloading and overriding.
5. What is abstraction?
6. Explain encapsulation with an example.
7. Interface vs abstract class.
8. Explain compile-time and runtime polymorphism.
9. What is inheritance?
10. Explain composition vs inheritance.
11. What is the purpose of `this` and `super`?
12. What is the `final` keyword?
13. What are SOLID principles?
14. What is multithreading?
15. Thread vs Runnable.
16. What is ExecutorService?
17. What is Future?
18. What is synchronization?
19. synchronized vs Lock.
20. What is a race condition?
21. What is deadlock?
22. How do you prevent deadlocks?
23. What are concurrent collections?
24. What is AtomicInteger?
25. What is the difference between concurrency and parallelism?

---

# Quick Revision Sheet

| Topic           | Key Point                              |
| --------------- | -------------------------------------- |
| Class           | Blueprint                              |
| Object          | Instance of Class                      |
| Constructor     | Initializes Objects                    |
| Overloading     | Compile-Time Polymorphism              |
| Overriding      | Runtime Polymorphism                   |
| Inheritance     | IS-A Relationship                      |
| Composition     | HAS-A Relationship                     |
| Encapsulation   | Data Hiding                            |
| Abstraction     | Hide Implementation                    |
| Interface       | Contract                               |
| Abstract Class  | Partial Implementation                 |
| Polymorphism    | One Interface, Many Forms              |
| final           | Prevent Modification                   |
| this            | Current Object                         |
| super           | Parent Object                          |
| Static Binding  | Compile Time                           |
| Dynamic Binding | Runtime                                |
| Thread          | Smallest Unit of Execution             |
| Runnable        | Preferred Thread Creation              |
| ExecutorService | Thread Pool                            |
| Future          | Asynchronous Result                    |
| Synchronization | Thread Safety                          |
| Lock            | Advanced Synchronization               |
| Race Condition  | Unsafe Shared Data Access              |
| Deadlock        | Threads Waiting Forever                |
| SOLID           | Five Object-Oriented Design Principles |

---

# Conclusion

Mastering Java Object-Oriented Programming (OOP) and Concurrency is essential for building scalable, maintainable, and high-performance applications. Understanding concepts such as classes, inheritance, polymorphism, encapsulation, abstraction, composition, SOLID principles, and Java's concurrency utilities enables developers to write clean, reusable, and thread-safe code. These topics are frequently tested in Java, Spring Boot, and enterprise application interviews and form the foundation of professional Java development.
