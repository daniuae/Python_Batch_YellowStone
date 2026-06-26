# Java `var` Keyword (Local Variable Type Inference)

## Objective

Learn about Java's `var` keyword:

* What is `var`?
* Why was it introduced?
* How does type inference work?
* Difference between explicit types and `var`
* Advantages and limitations of `var`

> **Note:** `var` was introduced in **Java 10**. It can only be used for **local variables**.

---

# What is `var`?

`var` allows the Java compiler to **infer (guess)** the type of a local variable from the value assigned to it.

Instead of writing the complete type, you write:

```java
var variableName = value;
```

The compiler automatically determines the variable's type.

---

# Example Without `var`

```java
String name = "John";
```

The compiler knows that `name` is a `String`.

---

# Example With `var`

```java
var name = "John";
```

The compiler still treats `name` as a `String`.

It is equivalent to:

```java
String name = "John";
```

---

# Complete Executable Program

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class VarKeywordExample {

    public static void main(String[] args) {

        // Explicit type declaration
        HashMap<String, List<String>> map1 =
                new HashMap<String, List<String>>();

        // Using var
        var map2 = new HashMap<String, List<String>>();

        // Add data
        map1.put("Students", List.of("Alice", "Bob"));
        map2.put("Students", List.of("Charlie", "David"));

        // Compiler infers List<String>
        var names = List.of("A", "B", "C");

        System.out.println("map1 : " + map1);
        System.out.println("map2 : " + map2);
        System.out.println("Names : " + names);

        // Demonstrate inferred type
        var age = 25;
        var salary = 75000.50;
        var city = "Bangalore";
        var active = true;

        System.out.println("\nType Inference Examples:");
        System.out.println("Age = " + age);
        System.out.println("Salary = " + salary);
        System.out.println("City = " + city);
        System.out.println("Active = " + active);
    }
}
```

---

# Output

```text
map1 : {Students=[Alice, Bob]}
map2 : {Students=[Charlie, David]}
Names : [A, B, C]

Type Inference Examples:
Age = 25
Salary = 75000.5
City = Bangalore
Active = true
```

---

# Example 1 – Without `var`

```java
HashMap<String, List<String>> map1 =
        new HashMap<String, List<String>>();
```

The type is written twice.

```text
HashMap<String, List<String>>

                =

HashMap<String, List<String>>
```

This is correct but verbose.

---

# Example 2 – With `var`

```java
var map2 = new HashMap<String, List<String>>();
```

The compiler infers the type automatically.

Internally, it becomes:

```java
HashMap<String, List<String>> map2 =
        new HashMap<String, List<String>>();
```

Nothing changes except that you write less code.

---

# Example 3 – Type Inference

```java
var names = List.of("A", "B", "C");
```

The compiler sees:

```java
List.of("A","B","C")
```

Since all elements are `String`, it infers:

```java
List<String> names = List.of("A", "B", "C");
```

---

# How Type Inference Works

```text
var age = 25;

        │

        ▼

Compiler sees 25

        │

        ▼

25 is an int

        │

        ▼

Internally

int age = 25;
```

---

# More Examples

## Integer

```java
var number = 100;
```

Compiler converts it to:

```java
int number = 100;
```

---

## Double

```java
var price = 99.99;
```

Compiler converts it to:

```java
double price = 99.99;
```

---

## String

```java
var language = "Java";
```

Compiler converts it to:

```java
String language = "Java";
```

---

## ArrayList

```java
var list = new ArrayList<String>();
```

Compiler converts it to:

```java
ArrayList<String> list = new ArrayList<String>();
```

---

# Internal Working

```text
var city = "Mumbai";

        │

        ▼

Compiler examines value

        │

        ▼

Value is String

        │

        ▼

Generated Code

String city = "Mumbai";
```

---

# `var` Does NOT Mean Dynamic Typing

Some beginners think:

```java
var x = 100;
```

means `x` can later become a `String`.

This is **incorrect**.

Example:

```java
var x = 100;

// x = "Hello"; // Compile-time Error
```

Once the compiler infers the type, it cannot change.

---

# Invalid Uses of `var`

## Cannot Declare Without Initialization

❌ Invalid

```java
var name;
```

Compiler Error

The compiler cannot infer the type because no value is assigned.

---

## Cannot Assign `null`

❌ Invalid

```java
var value = null;
```

The compiler cannot determine the type from `null`.

---

## Cannot Be Used as a Class Field

❌ Invalid

```java
public class Test {

    var name = "Java";

}
```

`var` is only allowed for **local variables**.

---

# Where Can `var` Be Used?

✅ Local variables

```java
var x = 10;
```

---

✅ Enhanced `for` loop

```java
for (var name : List.of("Alice", "Bob")) {
    System.out.println(name);
}
```

---

✅ Traditional `for` loop

```java
for (var i = 0; i < 5; i++) {
    System.out.println(i);
}
```

---

# Advantages of `var`

* Less typing
* Cleaner code
* Reduces repetition
* Improves readability for long generic types
* Still type-safe
* No performance impact
* Works well with generics

---

# Disadvantages of `var`

* Can reduce readability if the assigned value is not obvious
* Cannot be used without initialization
* Cannot be used for fields or method parameters
* Overuse can make code harder to understand

---

# Explicit Type vs `var`

| Explicit Type                                 | Using `var`                           |
| --------------------------------------------- | ------------------------------------- |
| `String name = "John";`                       | `var name = "John";`                  |
| `int age = 25;`                               | `var age = 25;`                       |
| `double salary = 5000.0;`                     | `var salary = 5000.0;`                |
| `ArrayList<String> list = new ArrayList<>();` | `var list = new ArrayList<String>();` |

---

# When Should You Use `var`?

### Good

```java
var students = new ArrayList<String>();
```

The type is obvious.

---

### Good

```java
var map = new HashMap<String, List<String>>();
```

Avoids repeating a long generic type.

---

### Avoid

```java
var x = calculate();
```

If `calculate()` doesn't make the return type obvious, using the explicit type improves readability.

---

# Interview Questions

### Q1. What is `var`?

`var` is Java's **local variable type inference** feature introduced in Java 10. The compiler infers the variable's type from its initializer.

---

### Q2. Is `var` dynamically typed?

No.

Java remains a **statically typed** language. The type is determined at compile time and cannot change later.

---

### Q3. Can `var` be used for class fields?

No.

`var` is allowed only for local variables, loop variables, and enhanced `for` loop variables.

---

### Q4. Can you write this?

```java
var x;
```

No.

A `var` variable must be initialized when it is declared.

---

### Q5. What type does the compiler infer here?

```java
var names = List.of("A", "B", "C");
```

The inferred type is:

```java
List<String>
```

---

# Key Takeaways

* `var` was introduced in **Java 10**.
* It provides **local variable type inference**.
* The compiler determines the type from the assigned value.
* `var` is **not** dynamically typed.
* It works best when the type is obvious from the initializer.
* It cannot be used for fields, method parameters, or uninitialized variables.
* Using `var` with complex generic types improves readability while preserving compile-time type safety.
