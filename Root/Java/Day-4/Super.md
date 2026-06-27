# Calling Parent Method Using `super` in Java

## What is `super`?

The `super` keyword in Java refers to the **immediate parent (superclass) object**.

It is commonly used to:

1. Call the parent class constructor.
2. Access parent class variables.
3. Call parent class methods.

---

# Calling Parent Method Using `super`

When a child class overrides a method, you can still invoke the parent class version of that method using:

```java
super.methodName();
```

This is useful when you want to:

- Reuse the parent's implementation.
- Extend the existing functionality instead of completely replacing it.

---

## Example

```java
class Animal {

    public void sound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {

    @Override
    public void sound() {

        // Call parent class method
        super.sound();

        // Child class behavior
        System.out.println("Dog barks");
    }
}

public class Main {

    public static void main(String[] args) {

        Dog dog = new Dog();
        dog.sound();
    }
}
```

### Output

```
Animal makes a sound
Dog barks
```

---

# How It Works

When this statement executes:

```java
dog.sound();
```

Java performs the following steps:

1. Calls `Dog`'s `sound()` method.
2. Inside `Dog.sound()`, `super.sound()` invokes the parent (`Animal`) implementation.
3. Control returns to `Dog.sound()`.
4. Remaining child-specific statements execute.

Execution Flow:

```
dog.sound()
      ↓
Dog.sound()
      ↓
super.sound()
      ↓
Animal.sound()
      ↓
Returns to Dog.sound()
      ↓
Prints "Dog barks"
```

---

# Another Example

```java
class Employee {

    public void work() {
        System.out.println("Employee is working");
    }
}

class Manager extends Employee {

    @Override
    public void work() {

        super.work();

        System.out.println("Manager is managing the team");
    }
}

public class Main {

    public static void main(String[] args) {

        Manager manager = new Manager();
        manager.work();
    }
}
```

### Output

```
Employee is working
Manager is managing the team
```

---

# Why Use `super.method()`?

Suppose the parent method already performs important tasks such as:

- Logging
- Validation
- Database connection
- Common business logic

Instead of rewriting everything, the child class can extend the behavior.

Example:

```java
class Vehicle {

    public void start() {
        System.out.println("Checking engine...");
    }
}

class Car extends Vehicle {

    @Override
    public void start() {

        super.start();

        System.out.println("Starting AC...");
        System.out.println("Car started");
    }
}
```

Output:

```
Checking engine...
Starting AC...
Car started
```

---

# Without `super`

```java
class Animal {

    public void sound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {

    @Override
    public void sound() {
        System.out.println("Dog barks");
    }
}
```

Output:

```
Dog barks
```

The parent implementation is completely replaced.

---

# With `super`

```java
class Dog extends Animal {

    @Override
    public void sound() {

        super.sound();

        System.out.println("Dog barks");
    }
}
```

Output:

```
Animal makes a sound
Dog barks
```

The child extends the parent behavior instead of replacing it.

---

# Key Points

- `super.method()` calls the immediate parent class method.
- It is typically used inside an overridden method.
- It helps reuse existing functionality from the parent class.
- It avoids code duplication.
- It supports extending behavior rather than replacing it entirely.

---

# Summary

| Feature | Description |
|---------|-------------|
| Keyword | `super` |
| Purpose | Access parent class members |
| Call Parent Method | `super.methodName()` |
| Used Inside | Overridden methods |
| Benefit | Reuse and extend parent behavior |
| Parent Called | Immediate superclass only |

---

# Interview Questions

### 1. What does `super.method()` do?

It invokes the immediate parent class's implementation of the method.

---

### 2. Can `super` call a grandparent's method directly?

No. `super` can only access the immediate superclass.

---

### 3. Can `super.method()` be called from a static method?

No. Since `super` refers to the current object, it cannot be used in a static context.

---

### 4. Is calling `super.method()` mandatory when overriding?

No. It is optional and used only when the child wants to reuse or extend the parent's implementation.

---

### 5. What happens if the parent class doesn't have the method?

The code will fail to compile because `super` can only call methods that exist in the immediate superclass.
