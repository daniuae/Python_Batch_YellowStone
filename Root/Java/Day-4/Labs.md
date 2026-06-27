# Java OOP Labs

---

# Lab 1: Class vs Object — From Blueprint to Live Instances

## Objective

Differentiate a **class (blueprint)** from an **object (instance)** by creating a `Car` class, instantiating multiple objects, and observing independent state.

---

## Step 1 — Define the Class Blueprint

**File:** `Car.java`

```java
public class Car {
    String brand;
    int speed;

    public void accelerate() {
        speed = speed + 20;
    }
}
```

### Why?

A class declares **state (fields)** and **behavior (methods)**. It is only a blueprint and does not occupy memory until an object is created.

---

## Step 2 — Create Two Independent Objects

**File:** `Demo.java`

```java
public class Demo {
    public static void main(String[] args) {

        Car c1 = new Car();
        Car c2 = new Car();

        c1.brand = "BMW";
        c2.brand = "Audi";

        c1.speed = 0;
        c2.speed = 0;

        c1.accelerate();   // 20
        c2.accelerate();   // 20
        c2.accelerate();   // 40

        System.out.println(c1.brand + " speed = " + c1.speed);
        System.out.println(c2.brand + " speed = " + c2.speed);
    }
}
```

### Why?

Both objects are created from the same blueprint but maintain **independent state**.

---

## Step 3 — Compile & Run

```bash
javac Car.java Demo.java
java Demo
```

---

## Step 4 — Verify Object Identity (Optional)

```java
System.out.println("c1 == c2 ? " + (c1 == c2));
```

### Why?

Each object has its own identity.

Output:

```
c1 == c2 ? false
```

---

## Conclusion

One class can create multiple independent objects, each having its own state and identity.

---

# Lab 3: Methods and Method Overloading — Building Behavioural Depth

## Objective

Learn how methods define object behavior and how **method overloading** allows multiple methods with the same name but different parameter lists.

---

## Step 1 — Behavior on Object State

**File:** `BankAccount.java`

```java
public class BankAccount {

    int balance;

    public void deposit(int amount) {
        balance = balance + amount;
    }
}
```

### Why?

Methods change an object's internal state.

---

## Step 2 — Create Overloaded Methods

**File:** `Printer.java`

```java
public class Printer {

    // Method 1: Print a String
    public void print(String message) {
        System.out.println(message);
    }

    // Method 2: Print an Integer
    public void print(int value) {
        System.out.println(value);
    }

    // Method 3: Print a String multiple times
    public void print(String message, int count) {
        for (int i = 0; i < count; i++) {
            System.out.println(message);
        }
    }

    // Main method
    public static void main(String[] args) {

        Printer printer = new Printer();

        System.out.println("Calling print(String):");
        printer.print("Welcome to Java!");

        System.out.println("\nCalling print(int):");
        printer.print(100);

        System.out.println("\nCalling print(String, int):");
        printer.print("Method Overloading", 3);
    }

    public Printer() {
    }
}
```

### Why?

Methods share the same name but differ in parameter lists.

This is **compile-time polymorphism**.

---

## Step 3 — Invoke the Overloaded Methods

**File:** `PrinterTest.java`

```java
public class PrinterTest {

    public static void main(String[] args) {

        Printer p = new Printer();

        p.print("Hello");
        p.print(42);
        p.print("Repeat", 3);
    }
}
```

---

## Step 4 — Invalid Overloading Example

```java
// INVALID

// public int print(String message) {
//     return 1;
// }
```

### Why?

Changing only the return type does **not** create a new overloaded method.

---

## Step 5 — Compile & Run

```bash
javac BankAccount.java Printer*.java
java PrinterTest
```

---

## Conclusion

Method overloading allows one method name to perform similar tasks using different parameter lists.

---

# Lab 5: Polymorphism — Overriding and Dynamic Dispatch

## Objective

Understand **runtime polymorphism** through **method overriding**.

---

## Step 1 — Parent Class

**File:** `Animal.java`

```java
public class Animal {

    public void sound() {
        System.out.println("Animal makes sound");
    }
}
```

---

## Step 2 — Child Classes

**Files:** `Dog.java`, `Cat.java`

```java
public class Dog extends Animal {

    @Override
    public void sound() {
        System.out.println("Dog barks");
    }
}
```

```java
public class Cat extends Animal {

    @Override
    public void sound() {
        System.out.println("Cat meows");
    }
}
```

---

## Step 3 — Dynamic Dispatch

**File:** `TestPoly.java`

```java
public class TestPoly {

    public static void main(String[] args) {

        Animal a1 = new Dog();
        Animal a2 = new Cat();

        a1.sound();
        a2.sound();

        Animal[] zoo = {
                new Dog(),
                new Cat(),
                new Animal()
        };

        for (Animal a : zoo) {
            a.sound();
        }
    }
}
```

### Why?

The actual object determines which overridden method executes.

---

## Step 4 — Compile & Run

```bash
javac Animal.java Dog.java Cat.java TestPoly.java
java TestPoly
```

---

## Conclusion

Runtime polymorphism enables generic code to execute specialized behavior based on the actual object type.

---

# Lab 6: Abstraction — Abstract Classes vs Interfaces

## Objective

Understand the difference between **abstract classes** and **interfaces**.

---

## Step 1 — Abstract Class

**File:** `Shape.java`

```java
public abstract class Shape {

    double area;

    public abstract void calculateArea();

    public void displayArea() {
        System.out.println("Area = " + area);
    }
}
```

---

## Step 2 — Concrete Implementation

**File:** `Circle.java`

```java
public class Circle extends Shape {

    double radius;

    public Circle(double r) {
        radius = r;
    }

    public void calculateArea() {
        area = Math.PI * radius * radius;
    }
}
```

---

## Step 3 — Interface

**File:** `PaymentProcessor.java`

```java
public interface PaymentProcessor {

    void pay(double amount);

    default void audit(String message) {
        System.out.println("[AUDIT] " + message);
    }
}
```

---

## Step 4 — Implement Interface

**File:** `CreditCardPayment.java`

```java
public class CreditCardPayment implements PaymentProcessor {

    public void pay(double amount) {
        System.out.println("Paying by Credit Card: " + amount);
    }
}
```

**File:** `UPIPayment.java`

```java
public class UPIPayment implements PaymentProcessor {

    public void pay(double amount) {
        System.out.println("Paying by UPI: " + amount);
    }
}
```

---

## Step 5 — Test

**File:** `AbstractionTest.java`

```java
public class AbstractionTest {

    public static void main(String[] args) {

        Shape s = new Circle(3.0);

        s.calculateArea();
        s.displayArea();

        PaymentProcessor p1 = new CreditCardPayment();
        PaymentProcessor p2 = new UPIPayment();

        p1.pay(1500.0);
        p1.audit("cc ok");

        p2.pay(850.0);
        p2.audit("upi ok");
    }
}
```

---

## Step 6 — Compile & Run

```bash
javac *.java
java AbstractionTest
```

---

## Conclusion

Abstract classes provide shared implementation.

Interfaces define capabilities that multiple classes can implement.

---

# Lab 7: Encapsulation & Data Hiding

## Objective

Protect object integrity using **private fields** and controlled access through methods.

---

## Step 1 — Encapsulated Class

**File:** `BankAccount.java`

```java
public class BankAccount {

    private double balance;
    private final String accountNumber;

    public BankAccount(String acc) {
        this.accountNumber = acc;
        this.balance = 0.0;
    }

    public void deposit(double amount) {
        if (amount > 0)
            balance += amount;
    }

    public boolean withdraw(double amount) {

        if (amount > 0 && amount <= balance) {
            balance -= amount;
            return true;
        }

        return false;
    }

    public double getBalance() {
        return balance;
    }

    public String getAccountNumber() {
        return accountNumber;
    }
}
```

---

## Step 2 — Test Encapsulation

**File:** `EncapTest.java`

```java
public class EncapTest {

    public static void main(String[] args) {

        BankAccount acct = new BankAccount("ACC123");

        acct.deposit(1000);

        boolean ok = acct.withdraw(300);

        System.out.println(
                "OK? " + ok +
                ", balance=" + acct.getBalance());
    }
}
```

---

## Step 3 — Compile & Run

```bash
javac BankAccount.java EncapTest.java
java EncapTest
```

---

## Conclusion

Encapsulation:

- Hides internal data
- Prevents invalid modifications
- Protects object integrity
- Improves maintainability
- Encourages controlled access through methods

---
