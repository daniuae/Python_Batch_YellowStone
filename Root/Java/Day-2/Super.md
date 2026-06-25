# Java Method Overriding with `super` Keyword

## Program

```java
public class Animal {

    public void sound() {
        System.out.println("Generic animal sound");
    }

    public static void main(String[] args) {

        // Create a Dog object
        Dog dog = new Dog();

        // Call the overridden method
        dog.sound();
    }
}

class Dog extends Animal {

    @Override
    public void sound() {

        // Call the parent class method
        super.sound();

        // Dog's own implementation
        System.out.println("Dog barks");
    }
}
```

---

# Output

```text
Generic animal sound
Dog barks
```

---

# What is Method Overriding?

Method overriding occurs when a child class provides its own implementation of a method that already exists in the parent class.

Rules:

* The method name must be the same.
* The parameter list must be the same.
* The return type must be the same (or covariant).
* The method in the parent class cannot be `private`.
* Use `@Override` to let the compiler verify that the method is actually overriding a parent method.

---

# What is `super`?

`super` is a keyword that refers to the immediate parent class.

It can be used to:

* Call parent class methods
* Access parent class variables
* Invoke parent class constructors

In this example:

```java
super.sound();
```

calls the `sound()` method defined inside the `Animal` class.

---

# Execution Flow

```
main()
   │
   ▼
Create Dog Object
Dog dog = new Dog();
   │
   ▼
dog.sound();
   │
   ▼
Dog.sound()
   │
   ├───────────────┐
   │               │
   ▼               │
super.sound()      │
   │               │
   ▼               │
Animal.sound()     │
   │               │
   ▼               │
Print:
Generic animal sound
   │
   └───────────────┘
           │
           ▼
Continue executing Dog.sound()
           │
           ▼
Print:
Dog barks
           │
           ▼
Program Ends
```

---

# Step-by-Step Execution

## Step 1

Execution starts from:

```java
main()
```

The JVM starts executing the `main()` method.

---

## Step 2

A `Dog` object is created.

```java
Dog dog = new Dog();
```

Memory is allocated for the object.

```
Heap Memory

+----------------+
|     Dog        |
|----------------|
| inherited      |
| Animal members |
+----------------+
```

Since `Dog` extends `Animal`, the object contains all inherited members.

---

## Step 3

The following statement executes:

```java
dog.sound();
```

Because the object is of type `Dog`, Java uses **runtime polymorphism** (dynamic method dispatch).

Java searches for the overridden method.

It finds:

```java
Dog.sound()
```

---

## Step 4

Execution enters:

```java
@Override
public void sound() {
    super.sound();
    System.out.println("Dog barks");
}
```

The first statement is:

```java
super.sound();
```

---

## Step 5

`super.sound()` invokes the parent implementation.

```
Animal.sound()
```

which executes:

```java
System.out.println("Generic animal sound");
```

Output:

```text
Generic animal sound
```

After the parent method completes, control returns to `Dog.sound()`.

---

## Step 6

Execution continues with:

```java
System.out.println("Dog barks");
```

Output:

```text
Dog barks
```

---

## Final Output

```text
Generic animal sound
Dog barks
```

---

# Stack Illustration

```
                    CALL STACK

+--------------------------------------+
| main()                               |
|                                      |
| dog.sound()                          |
+------------------▲-------------------+
                   |
                   |
+------------------|-------------------+
| Dog.sound()      |                   |
|                  |                   |
| super.sound() ---┘                   |
+------------------▲-------------------+
                   |
                   |
+------------------|-------------------+
| Animal.sound()                       |
|                                      |
| Print: Generic animal sound          |
+--------------------------------------+

Return to Dog.sound()

Print:
Dog barks

Return to main()

Program Ends
```

---

# Object-Oriented View

```
              Animal
             ----------
             + sound()

                 ▲
                 │
                 │ extends
                 │

               Dog
          ----------------
          + sound()
               │
               │
               ├── super.sound()
               │
               ▼
          Animal.sound()
```

---

# Why Use `super.sound()`?

Suppose the parent method performs important work.

Example:

```java
public void sound() {
    System.out.println("Checking speaker...");
    System.out.println("Generic animal sound");
}
```

The child wants to preserve this behavior while adding its own.

```java
@Override
public void sound() {

    super.sound();

    System.out.println("Dog barks");
}
```

Output:

```text
Checking speaker...
Generic animal sound
Dog barks
```

The parent functionality is preserved.

---

# Without `super.sound()`

```java
class Dog extends Animal {

    @Override
    public void sound() {
        System.out.println("Dog barks");
    }
}
```

Output

```text
Dog barks
```

Execution Flow

```
main()
    │
    ▼
dog.sound()
    │
    ▼
Dog.sound()
    │
    ▼
Print:
Dog barks
```

Notice that `Animal.sound()` is never executed.

---

# Comparison

| With `super.sound()`               | Without `super.sound()`                |
| ---------------------------------- | -------------------------------------- |
| Parent method executes             | Parent method does not execute         |
| Parent behavior is preserved       | Parent behavior is completely replaced |
| Useful for extending functionality | Useful for replacing functionality     |

---

# Real-World Analogy

Imagine a smartphone.

### Parent Class

```
Phone.call()
```

Performs:

* Connect to network
* Verify SIM
* Start call

### Child Class

```
SmartPhone.call()
```

Wants to:

* Connect to network
* Verify SIM
* Start call
* Record the conversation

Implementation:

```java
@Override
public void call() {

    super.call();

    System.out.println("Recording started");
}
```

Output:

```
Connecting...
Verifying SIM...
Calling...
Recording started
```

If `super.call()` were omitted, the phone would only print:

```
Recording started
```

and none of the essential call setup would occur.

---

# Key Takeaways

* Method overriding enables a child class to provide a specialized implementation of a parent method.
* Java uses **runtime polymorphism** to invoke the overridden method based on the object's actual type.
* The `super` keyword refers to the immediate parent class.
* `super.sound()` explicitly calls the parent class implementation.
* Using `super` allows the child class to **extend** existing behavior instead of completely replacing it.
* Omitting `super.sound()` means only the child class implementation executes.
