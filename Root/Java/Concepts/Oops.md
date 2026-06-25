# Encapsulation vs Abstraction in Object-Oriented Programming (OOP)

## Learning Objectives

By the end of this lesson, you will be able to:

- Understand Encapsulation and Abstraction
- Differentiate between them
- Implement both concepts in Java
- Identify real-world examples
- Answer interview questions confidently

---

# What is Encapsulation?

## Definition

**Encapsulation** is the process of **bundling data (variables) and methods (functions) into a single unit (class)** while **restricting direct access** to the data.

It protects an object's internal state by allowing access only through controlled methods.

### Formula

```
Data + Methods = Class
```

---

## Why Encapsulation?

Without encapsulation:

- Anyone can modify object data.
- Invalid values may be assigned.
- Data becomes inconsistent.

With encapsulation:

- Data is secure.
- Validation is possible.
- Better maintainability.
- Better modularity.

---

# Real-Life Analogy: Medicine Capsule

Imagine a medicine capsule.

```
+-------------------+
|                   |
|   Medicine        |
|   (Hidden)        |
|                   |
+-------------------+
```

- You cannot directly touch the medicine.
- You consume it through the capsule.

Similarly,

- Data is hidden.
- Users access it through methods.

This is **Encapsulation**.

---

# Java Example: Encapsulation

```java
class Employee {

    private String name;
    private double salary;

    public void setSalary(double salary) {

        if (salary > 0) {
            this.salary = salary;
        }
    }

    public double getSalary() {
        return salary;
    }
}
```

Main Class

```java
public class Main {

    public static void main(String[] args) {

        Employee emp = new Employee();

        emp.setSalary(50000);

        System.out.println(emp.getSalary());
    }
}
```

### Output

```
50000.0
```

---

## Why is this Encapsulation?

```
salary
   ↓
private
   ↓
Cannot access directly

Only through

setSalary()

getSalary()
```

---

# Without Encapsulation

```java
class Employee {

    public double salary;
}
```

Now,

```java
Employee emp = new Employee();

emp.salary = -100000;
```

Output

```
Invalid Salary
```

No validation exists.

---

# Advantages of Encapsulation

- Data Security
- Controlled Access
- Validation
- Flexibility
- Easy Maintenance
- Better Testing

---

# What is Abstraction?

## Definition

**Abstraction** is the process of **hiding implementation details** and exposing only the essential functionality.

Users know **what** to do.

They don't know **how** it works internally.

---

# Real-Life Analogy: Driving a Car

You know

- Steering
- Brake
- Accelerator

You do **not** know

- Engine timing
- Fuel injection
- ECU programming
- Gear synchronization

The complex implementation is hidden.

This is **Abstraction**.

---

# Java Abstraction using Abstract Class

```java
abstract class Shape {

    abstract void draw();
}
```

Implementation

```java
class Circle extends Shape {

    @Override
    void draw() {

        System.out.println("Drawing Circle");
    }
}

class Rectangle extends Shape {

    @Override
    void draw() {

        System.out.println("Drawing Rectangle");
    }
}
```

Main

```java
public class Main {

    public static void main(String[] args) {

        Shape shape = new Circle();

        shape.draw();
    }
}
```

Output

```
Drawing Circle
```

The user simply writes

```java
shape.draw();
```

They don't know how drawing is implemented.

---

# Abstraction using Interface

```java
interface Payment {

    void pay(double amount);
}
```

Implementation

```java
class CreditCardPayment implements Payment {

    @Override
    public void pay(double amount) {

        System.out.println("Paid using Credit Card");
    }
}

class UpiPayment implements Payment {

    @Override
    public void pay(double amount) {

        System.out.println("Paid using UPI");
    }
}
```

Main

```java
public class Main {

    public static void main(String[] args) {

        Payment payment = new UpiPayment();

        payment.pay(1000);
    }
}
```

Output

```
Paid using UPI
```

---

# Visual Illustration

## Encapsulation

```
+----------------------------------+
|          Employee                |
|----------------------------------|
| - name (private)                 |
| - salary (private)               |
|----------------------------------|
| + getSalary()                    |
| + setSalary()                    |
+----------------------------------+

Direct Access Not Allowed
```

---

## Abstraction

```
           Payment
               |
    ---------------------
    |                   |
Credit Card          UPI

User

payment.pay()

Doesn't know
how payment works.
```

---

# Encapsulation vs Abstraction

| Feature | Encapsulation | Abstraction |
|----------|--------------|-------------|
| Definition | Hides data by restricting access | Hides implementation details |
| Focus | Data Protection | Simplicity |
| Purpose | Secure object data | Reduce complexity |
| Achieved Using | Private variables, Getters, Setters | Abstract classes, Interfaces |
| Question Answered | How to protect data? | What functionality should be exposed? |
| Level | Class Level | Design Level |
| Example | Bank Account Balance | ATM Machine |

---

# Key Difference

## Encapsulation hides **Data**

```
private int salary;
```

Users cannot access it directly.

---

## Abstraction hides **Implementation**

```
payment.pay();
```

Users don't know how the payment is processed.

---

# ATM Example

## Encapsulation

```
Cash Storage
PIN Database

Hidden from user
```

---

## Abstraction

User sees

```
Insert Card

↓

Enter PIN

↓

Withdraw Cash
```

Internal processing remains hidden.

---

# Mobile Phone Example

## Encapsulation

Hidden

```
Battery
Processor
Memory
Sensors
```

---

## Abstraction

Visible

```
Camera

Gallery

Phone

Messages
```

Users don't need to know the internal implementation.

---

# Relationship Between Them

```
                  OOP
                   |
        -----------------------
        |                     |
 Encapsulation          Abstraction
        |                     |
Hide Data            Hide Complexity
        |                     |
Protect State        Show Essential Features
```

---

# Combined Example

```java
class BankAccount {

    private double balance;

    public void deposit(double amount) {

        if (amount > 0)
            balance += amount;
    }

    public double getBalance() {
        return balance;
    }
}
```

### Encapsulation

```
private double balance;
```

Data is protected.

### Abstraction

```
deposit()
```

Users only know they can deposit money.

They don't know the internal logic.

---

# Real-World Examples

| Scenario | Encapsulation | Abstraction |
|----------|--------------|-------------|
| ATM | Cash storage is hidden | User withdraws money without knowing internal banking operations |
| Car | Engine components are protected | Driver uses steering and pedals |
| Mobile Phone | Internal hardware is inaccessible | User interacts through apps and icons |
| Printer | Internal mechanisms are enclosed | User clicks "Print" |
| Washing Machine | Internal motor and circuits are protected | User selects wash mode |

---

# Advantages

## Encapsulation

- Protects data
- Prevents unauthorized access
- Supports validation
- Easier maintenance
- Improves code modularity

---

## Abstraction

- Reduces complexity
- Improves readability
- Simplifies API usage
- Encourages loose coupling
- Makes systems easier to extend

---

# Memory Trick

```
Encapsulation
↓

Hide DATA
```

```
Abstraction
↓

Hide IMPLEMENTATION
```

---

# Interview Questions

### 1. What is Encapsulation?

Encapsulation is the process of wrapping data and methods into a single unit while restricting direct access to the data using access modifiers.

---

### 2. What is Abstraction?

Abstraction is the process of hiding implementation details and exposing only essential functionality to the user.

---

### 3. Can Encapsulation exist without Abstraction?

Yes. A class with private fields and getters/setters demonstrates encapsulation without necessarily using abstraction.

---

### 4. Can Abstraction exist without Encapsulation?

Yes. Interfaces and abstract classes define behavior without requiring private data.

---

### 5. Which Java features support Encapsulation?

- Classes
- Private fields
- Public methods
- Getters
- Setters
- Access modifiers

---

### 6. Which Java features support Abstraction?

- Abstract classes
- Interfaces
- Method overriding
- Polymorphism

---

# Summary

| Encapsulation | Abstraction |
|---------------|-------------|
| Hides Data | Hides Implementation |
| Achieved using Access Modifiers | Achieved using Abstract Classes & Interfaces |
| Protects Object State | Simplifies Object Usage |
| Focuses on Data Security | Focuses on Reducing Complexity |
| Example: Bank Account | Example: ATM, Car, Payment System |

---

# One-Line Interview Answer

> **Encapsulation** protects an object's data by restricting direct access and exposing controlled methods, while **Abstraction** hides implementation details and exposes only the essential functionality needed by the user.
