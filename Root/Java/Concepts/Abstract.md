# Abstract Class in Java

## What is an Abstract Class?

An **Abstract Class** is a special type of class that **cannot be instantiated (you cannot create an object directly)**. It serves as a blueprint for other classes and is designed to be extended by subclasses.

An abstract class can contain:
- Abstract methods (methods without implementation)
- Concrete methods (methods with implementation)
- Constructors
- Instance variables
- Static methods
- Final methods

A subclass must implement all abstract methods unless the subclass is also declared abstract.

---

# Syntax

```java
abstract class ClassName {
    // Abstract method
    abstract void methodName();

    // Concrete method
    void anotherMethod() {
        // implementation
    }
}
```

---

# Why Use an Abstract Class?

Abstract classes are used when:

- Multiple classes share common behavior.
- You want to enforce certain methods to be implemented by subclasses.
- You want code reusability.
- You want to partially implement functionality while leaving some methods for subclasses.

---

# Real-World Example

Imagine different types of vehicles.

Every vehicle:
- Starts
- Stops

But every vehicle starts differently.

Examples:
- Car
- Bike
- Bus

Instead of writing the same code repeatedly, create an abstract Vehicle class.

---

# Example 1: Basic Abstract Class

```java
abstract class Animal {

    // Abstract method
    abstract void sound();

    // Concrete method
    void sleep() {
        System.out.println("Animal is sleeping.");
    }
}

class Dog extends Animal {

    @Override
    void sound() {
        System.out.println("Dog barks.");
    }
}

public class Main {

    public static void main(String[] args) {

        Dog dog = new Dog();

        dog.sound();
        dog.sleep();
    }
}
```

### Output

```
Dog barks.
Animal is sleeping.
```

---

# Example 2: Multiple Child Classes

```java
abstract class Shape {

    abstract double area();
}

class Circle extends Shape {

    double radius = 5;

    @Override
    double area() {
        return 3.14 * radius * radius;
    }
}

class Rectangle extends Shape {

    double length = 10;
    double breadth = 5;

    @Override
    double area() {
        return length * breadth;
    }
}

public class Main {

    public static void main(String[] args) {

        Shape c = new Circle();
        Shape r = new Rectangle();

        System.out.println(c.area());
        System.out.println(r.area());
    }
}
```

### Output

```
78.5
50.0
```

---

# Abstract Methods

An abstract method has:

- No body
- Only declaration
- Ends with a semicolon

Example:

```java
abstract void calculateSalary();
```

The child class must implement it.

---

# Concrete Methods

Abstract classes can also contain normal methods.

```java
abstract class Employee {

    abstract void work();

    void login() {
        System.out.println("Employee logged in");
    }
}
```

---

# Constructors in Abstract Class

Yes, abstract classes can have constructors.

```java
abstract class Animal {

    Animal() {
        System.out.println("Animal Constructor");
    }

    abstract void sound();
}

class Dog extends Animal {

    Dog() {
        System.out.println("Dog Constructor");
    }

    void sound() {
        System.out.println("Bark");
    }
}

public class Main {

    public static void main(String[] args) {

        Dog d = new Dog();
    }
}
```

### Output

```
Animal Constructor
Dog Constructor
```

Even though an abstract class cannot be instantiated directly, its constructor executes when a subclass object is created.

---

# Instance Variables

Abstract classes can contain instance variables.

```java
abstract class Employee {

    String company = "Google";

    abstract void work();
}
```

---

# Static Methods

```java
abstract class Employee {

    static void companyName() {
        System.out.println("OpenAI");
    }
}
```

Usage:

```java
Employee.companyName();
```

---

# Final Methods

Final methods cannot be overridden.

```java
abstract class Employee {

    final void login() {
        System.out.println("Login Success");
    }

    abstract void work();
}
```

---

# Can We Create an Object of an Abstract Class?

No.

```java
Animal a = new Animal(); // Compilation Error
```

Correct:

```java
Animal a = new Dog();
```

This is called **Runtime Polymorphism**.

---

# Abstract Class with Polymorphism

```java
abstract class Animal {

    abstract void sound();
}

class Dog extends Animal {

    void sound() {
        System.out.println("Bark");
    }
}

class Cat extends Animal {

    void sound() {
        System.out.println("Meow");
    }
}

public class Main {

    public static void main(String[] args) {

        Animal a;

        a = new Dog();
        a.sound();

        a = new Cat();
        a.sound();
    }
}
```

### Output

```
Bark
Meow
```

---

# Abstract Class vs Normal Class

| Feature | Normal Class | Abstract Class |
|----------|-------------|----------------|
| Object Creation | ✅ Yes | ❌ No |
| Constructors | ✅ Yes | ✅ Yes |
| Concrete Methods | ✅ Yes | ✅ Yes |
| Abstract Methods | ❌ No | ✅ Yes |
| Can be inherited | ✅ Yes | ✅ Yes |

---

# Abstract Class vs Interface

| Feature | Abstract Class | Interface |
|----------|----------------|-----------|
| Keyword | abstract class | interface |
| Constructors | ✅ Yes | ❌ No |
| Instance Variables | ✅ Yes | ❌ No |
| Abstract Methods | ✅ Yes | ✅ Yes |
| Concrete Methods | ✅ Yes | ✅ (default/static) |
| Multiple Inheritance | ❌ No | ✅ Yes |
| Object Creation | ❌ No | ❌ No |

---

# When Should You Use an Abstract Class?

Use an abstract class when:

- Classes have a strong "is-a" relationship.
- You want to share common code.
- You want to provide default implementations.
- You need constructors.
- You need instance variables.
- You want partial abstraction.

---

# Advantages

- Promotes code reuse.
- Provides partial abstraction.
- Encourages cleaner design.
- Supports polymorphism.
- Reduces duplicate code.
- Can contain constructors and fields.

---

# Disadvantages

- Does not support multiple inheritance.
- Cannot create objects directly.
- Subclasses are tightly coupled to the parent.

---

# Interview Questions

### 1. Can we instantiate an abstract class?

No.

---

### 2. Can an abstract class have constructors?

Yes.

---

### 3. Can an abstract class have static methods?

Yes.

---

### 4. Can an abstract class have final methods?

Yes.

---

### 5. Can an abstract class contain concrete methods?

Yes.

---

### 6. Can an abstract class have private methods?

Yes.

---

### 7. Can an abstract class have variables?

Yes, it can have:
- Instance variables
- Static variables
- Final variables

---

### 8. Can an abstract class extend another abstract class?

Yes.

```java
abstract class A {
    abstract void display();
}

abstract class B extends A {
}
```

---

### 9. Can an abstract class implement an interface?

Yes.

```java
interface Printable {
    void print();
}

abstract class Report implements Printable {
}
```

---

### 10. Difference between Abstract Class and Interface?

- Use an **Abstract Class** when classes share common state and behavior.
- Use an **Interface** when you want to define a contract that unrelated classes can implement.

---

# Summary

- An abstract class **cannot be instantiated**.
- It can contain **both abstract and concrete methods**.
- It **supports constructors, fields, and static methods**.
- It is used to provide **partial abstraction** and **code reuse**.
- Subclasses **must implement** all abstract methods unless they are also abstract.
- Use abstract classes when related classes share common implementation and state.
