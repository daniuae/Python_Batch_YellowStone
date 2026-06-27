# Method Overriding in Java

## What is Method Overriding?

**Method Overriding** is a feature of **Runtime Polymorphism** where a subclass provides its own implementation of a method that is already defined in its superclass.

When an overridden method is called using a parent class reference, Java decides which method to execute **at runtime** based on the actual object.

---

# Rules for Method Overriding

* The parent and child methods must have the **same method name**.
* The method parameters must be **exactly the same**.
* The return type should be the same (or a covariant return type).
* The access modifier in the child class **cannot be more restrictive** than the parent.
* Only inherited methods can be overridden.
* `static`, `final`, and `private` methods **cannot** be overridden.
* Use the `@Override` annotation to let the compiler verify that the method is correctly overridden.

---

# Example 1: Basic Method Overriding

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

public class MethodOverridingDemo {

    public static void main(String[] args) {

        Animal animal = new Animal();
        animal.sound();

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

### Explanation

* `Animal` has a method named `sound()`.
* `Dog` overrides the `sound()` method.
* When `dog.sound()` is called, the overridden method in `Dog` executes.

---

# Example 2: Runtime Polymorphism

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

class Cat extends Animal {

    @Override
    public void sound() {
        System.out.println("Cat meows");
    }
}

public class RuntimePolymorphismDemo {

    public static void main(String[] args) {

        Animal animal;

        animal = new Dog();
        animal.sound();

        animal = new Cat();
        animal.sound();
    }
}
```

### Output

```
Dog barks
Cat meows
```

### Explanation

Although the reference type is `Animal`, Java invokes the method based on the actual object (`Dog` or `Cat`). This is known as **Dynamic Method Dispatch** or **Runtime Polymorphism**.

---

# Example 3: Calling Parent Method Using `super`

```java
class Animal {

    public void sound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {

    @Override
    public void sound() {

        super.sound();

        System.out.println("Dog barks");
    }
}

public class SuperDemo {

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

### Explanation

* `super.sound()` calls the parent class method.
* The child class then executes its own additional logic.

---

# Example 4: Real-World Banking Example

```java
class Bank {

    public double getInterestRate() {
        return 5.0;
    }
}

class SBI extends Bank {

    @Override
    public double getInterestRate() {
        return 6.5;
    }
}

class HDFC extends Bank {

    @Override
    public double getInterestRate() {
        return 7.2;
    }
}

public class BankDemo {

    public static void main(String[] args) {

        Bank bank;

        bank = new SBI();
        System.out.println("SBI Interest Rate : " + bank.getInterestRate());

        bank = new HDFC();
        System.out.println("HDFC Interest Rate : " + bank.getInterestRate());
    }
}
```

### Output

```
SBI Interest Rate : 6.5
HDFC Interest Rate : 7.2
```

### Explanation

Each bank provides its own implementation of the `getInterestRate()` method.

---

# Methods That Cannot Be Overridden

## 1. Final Method

```java
class Animal {

    public final void eat() {
        System.out.println("Eating");
    }
}

class Dog extends Animal {

    // Compilation Error
    // public void eat() { }
}
```

**Reason:** A `final` method cannot be overridden.

---

## 2. Static Method

```java
class Animal {

    public static void display() {
        System.out.println("Animal");
    }
}

class Dog extends Animal {

    public static void display() {
        System.out.println("Dog");
    }
}
```

**Note:** This is **Method Hiding**, not Method Overriding.

---

## 3. Private Method

```java
class Animal {

    private void sleep() {
        System.out.println("Sleeping");
    }
}

class Dog extends Animal {

    public void sleep() {
        System.out.println("Dog Sleeping");
    }
}
```

**Reason:** Private methods are not inherited; therefore, they cannot be overridden.

---

# Method Overloading vs Method Overriding

| Feature              | Method Overloading                         | Method Overriding                         |
| -------------------- | ------------------------------------------ | ----------------------------------------- |
| Definition           | Same method name with different parameters | Same method signature in parent and child |
| Inheritance Required | No                                         | Yes                                       |
| Parameters           | Must be different                          | Must be the same                          |
| Return Type          | Can differ (with different parameters)     | Same or Covariant                         |
| Polymorphism         | Compile-time                               | Runtime                                   |
| Binding              | Early Binding                              | Late Binding                              |
| Annotation           | Not Required                               | `@Override` Recommended                   |

---

# Real-Life Analogy

Imagine a **Remote Control**.

```
            Remote
              |
         Press Power
              |
     --------------------
     |                  |
 Samsung TV         Sony TV
     |                  |
 Turns ON          Turns ON
 Samsung Way       Sony Way
```

The action is the same (**Press Power**), but every TV performs it differently.

Similarly:

* Parent class defines the method.
* Child class provides its own implementation.
* Java selects the correct implementation at runtime.

---

# Key Points

* Method Overriding is used to achieve **Runtime Polymorphism**.
* The child class provides a new implementation of a method already defined in the parent class.
* Java decides which method to invoke at **runtime**.
* The `@Override` annotation helps detect coding mistakes.
* `final`, `static`, and `private` methods cannot be overridden.
* Overriding promotes flexibility, extensibility, and code reusability.
