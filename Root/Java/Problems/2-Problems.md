# Java Practice Problems (Interview Style)

These problems are designed to strengthen your understanding of Java fundamentals, Object-Oriented Programming (OOP), Collections, Generics, and Stream API through real-world scenarios.

---

# Problem 1: Student Result Management System

## Difficulty
⭐ Beginner → Intermediate

## Scenario

A coaching institute wants to automate the management of student results.

### Requirements

Create a class named `Student` with the following fields:

- studentId
- name
- marks

Implement the following methods:

- `calculateGrade()`
- `isPassed()`
- `displayStudent()`

### Grade Criteria

| Marks | Grade |
|--------|-------|
| 90 - 100 | A |
| 80 - 89 | B |
| 70 - 79 | C |
| 60 - 69 | D |
| Below 60 | F |

A student is considered **Passed** only if marks are **60 or above**.

### Sample Output

```text
Student ID : 101
Name       : Rahul
Marks      : 86
Grade      : B
Result     : PASS
```

### Concepts Covered

- Classes & Objects
- Constructors
- Methods
- if-else
- Encapsulation
- Instance variables

---

# Problem 2: Online Shopping Cart

## Difficulty
⭐⭐ Intermediate

## Scenario

Design a shopping cart system for an online shopping application.

### Create Class: Product

Fields

- id
- name
- price
- quantity

### Create Class: ShoppingCart

Methods

- addProduct(Product product)
- removeProduct(int productId)
- calculateTotal()
- displayCart()

### Business Rule

If total cart value is greater than **₹5000**, apply a **10% discount**.

### Sample Output

```text
Laptop      ₹45000 x 1
Mouse       ₹600 x 2

Subtotal : ₹46200
Discount : ₹4620
Total    : ₹41580
```

### Concepts Covered

- ArrayList
- Object Composition
- Loops
- Methods
- Business Logic
- Encapsulation

---

# Problem 3: Employee Payroll System

## Difficulty
⭐⭐⭐ Intermediate

## Scenario

Create an employee payroll management system.

### Create Class: Employee

Fields

- employeeId
- name
- designation
- basicSalary

Methods

- calculateHRA()
- calculateDA()
- calculateTax()
- calculateNetSalary()
- displaySalarySlip()

### Salary Rules

| Designation | HRA | DA |
|-------------|-----|----|
| Manager | 25% | 18% |
| Developer | 20% | 15% |
| Tester | 18% | 12% |

### Tax Rules

| Net Salary | Tax |
|------------|-----|
| Above ₹80,000 | 20% |
| ₹80,000 or Below | 10% |

### Sample Output

```text
Employee ID : 2001
Name        : Priya
Designation : Developer

Basic Salary : ₹70000
HRA          : ₹14000
DA           : ₹10500
Tax          : ₹9450

Net Salary   : ₹85050
```

### Concepts Covered

- switch statement
- Methods
- OOP
- Arithmetic operations
- Encapsulation

---

# Problem 4: Library Management System

## Difficulty
⭐⭐⭐ Intermediate

## Scenario

Design a library system that manages books.

### Create Class: Book

Fields

- bookId
- title
- author
- available

Methods

- issueBook()
- returnBook()
- displayBook()

### Store Books In

```java
ArrayList<Book>
```

### Functionalities

- Add book
- Search book
- Issue book
- Return book
- Display available books
- Count issued books

### Business Rules

If a book is available:

```text
Book issued successfully.
```

Otherwise:

```text
Book is currently unavailable.
```

### Sample Output

```text
Book ID : 1001
Title   : Clean Code
Author  : Robert Martin
Status  : Available
```

### Concepts Covered

- Objects
- ArrayList
- Boolean
- Loops
- Search operations
- Methods

---

# Problem 5: Customer Management System

## Difficulty
⭐⭐⭐⭐ Advanced

## Scenario

A company wants to analyze customer purchasing data.

### Create Class: Customer

Fields

- customerId
- name
- city
- age
- membershipType
- purchaseAmount

Store customers inside

```java
ArrayList<Customer>
```

### Tasks

### Part A

Display customers whose age is greater than **30** using Stream API.

### Part B

Display customers whose purchase amount is greater than **₹10,000**.

### Part C

Sort customers by **Name**.

### Part D

Sort customers by **Purchase Amount (Descending)**.

### Part E

Group customers by **City** using

```java
Collectors.groupingBy()
```

### Part F

Find the customer with the **highest purchase amount**.

### Part G

Count the number of customers from each city.

### Sample Output

```text
Customers Above Age 30

Rahul
Anita
Vijay

Highest Purchasing Customer

Customer : Anita
Amount   : ₹75000
```

### Concepts Covered

- ArrayList
- Comparator
- Comparable
- Stream API
- Lambda Expressions
- Collectors
- Optional
- Generics

---

# Bonus Challenges

## Problem 6: Bank Account Management System

### Features

- Deposit money
- Withdraw money
- Check balance
- Transfer money
- Prevent negative balance
- Display transaction history

### Concepts

- OOP
- Exception Handling
- ArrayList
- Methods
- Encapsulation

---

## Problem 7: Hospital Appointment System

### Features

- Register patient
- Add doctor
- Book appointment
- Cancel appointment
- Search doctor by specialization
- Display appointment schedule

### Concepts

- Object Composition
- Collections
- Enums
- OOP

---

## Problem 8: Inventory Management System

### Features

- Add product
- Update stock
- Remove product
- Low stock alert
- Search product
- Sort products by price

### Concepts

- Collections
- Comparator
- CRUD Operations
- Streams

---

## Problem 9: Movie Ticket Booking System

### Features

- Add movies
- Display shows
- Book tickets
- Cancel tickets
- Calculate bill
- Apply discount coupons

### Concepts

- Classes
- Collections
- Business Logic
- Exception Handling

---

## Problem 10: University Course Registration System

### Features

- Register student
- Add course
- Enroll in course
- Drop course
- Display enrolled courses
- Generate student report

### Concepts

- OOP
- Collections
- Streams
- Generics
- Relationships between classes

---

# Topics Covered Across All Problems

| Java Topic | Covered |
|------------|----------|
| Variables & Data Types | ✅ |
| Operators | ✅ |
| Control Statements (if/else, switch) | ✅ |
| Loops | ✅ |
| Arrays | ✅ |
| Strings | ✅ |
| Methods | ✅ |
| Constructors | ✅ |
| Classes & Objects | ✅ |
| Encapsulation | ✅ |
| Inheritance | ✅ (Can be extended) |
| Polymorphism | ✅ (Can be extended) |
| Abstraction | ✅ (Can be extended) |
| Interfaces | ✅ (Can be extended) |
| Exception Handling | ✅ |
| Packages | ✅ |
| ArrayList | ✅ |
| List, Set, Map | ✅ (Can be extended) |
| Iterator/ListIterator | ✅ (Optional enhancement) |
| Generics | ✅ |
| Comparable | ✅ |
| Comparator | ✅ |
| Stream API | ✅ |
| Lambda Expressions | ✅ |
| Collectors | ✅ |
| Optional | ✅ |
| Business Logic Implementation | ✅ |
| Real-world Object-Oriented Design | ✅ |

---

# Suggested Learning Order

1. Student Result Management System
2. Online Shopping Cart
3. Employee Payroll System
4. Library Management System
5. Bank Account Management System
6. Inventory Management System
7. Hospital Appointment System
8. Movie Ticket Booking System
9. University Course Registration System
10. Customer Management System (Streams & Comparator)

By completing these problems in order, you'll progressively build proficiency in Java fundamentals, object-oriented programming, collections, generics, and the Stream API while practicing realistic business scenarios commonly encountered in coding interviews and software development.
