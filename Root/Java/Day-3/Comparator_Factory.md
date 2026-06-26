# Comparator Examples - Complete Executable Java Program

## Objective

This example demonstrates how to use the `Comparator` interface to sort objects in different ways:

1. Natural Order
2. Reverse Order
3. Sort by Object Property
4. Multiple-Level (Chained) Sorting

---

# File Name

```text
ComparatorDemo.java
```

---

# Complete Executable Program

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

class Customer {

    private String name;
    private int tier;

    public Customer(String name, int tier) {
        this.name = name;
        this.tier = tier;
    }

    public String getName() {
        return name;
    }

    public int getTier() {
        return tier;
    }

    @Override
    public String toString() {
        return "Customer{name='" + name + "', tier=" + tier + "}";
    }
}

public class ComparatorDemo {

    public static void main(String[] args) {

        // -----------------------------
        // Example 1 : Natural Order
        // -----------------------------

        List<String> fruits = new ArrayList<>();

        fruits.add("Banana");
        fruits.add("Orange");
        fruits.add("Apple");
        fruits.add("Mango");

        System.out.println("Original List:");
        System.out.println(fruits);

        Comparator<String> natural = Comparator.naturalOrder();

        Collections.sort(fruits, natural);

        System.out.println("\nNatural Order:");
        System.out.println(fruits);

        // -----------------------------
        // Example 2 : Reverse Order
        // -----------------------------

        Comparator<String> reverse = Comparator.reverseOrder();

        Collections.sort(fruits, reverse);

        System.out.println("\nReverse Order:");
        System.out.println(fruits);

        // -----------------------------
        // Example 3 : Customer Objects
        // -----------------------------

        List<Customer> customers = new ArrayList<>();

        customers.add(new Customer("John", 2));
        customers.add(new Customer("Alice", 1));
        customers.add(new Customer("David", 3));
        customers.add(new Customer("Bob", 1));

        System.out.println("\nOriginal Customers:");
        System.out.println(customers);

        // Sort by Name

        Comparator<Customer> byName =
                Comparator.comparing(Customer::getName);

        customers.sort(byName);

        System.out.println("\nSorted by Name:");
        System.out.println(customers);

        // -----------------------------
        // Example 4 : Tier then Name
        // -----------------------------

        Comparator<Customer> byTierThenName =
                Comparator.comparingInt(Customer::getTier)
                          .thenComparing(Customer::getName);

        customers.sort(byTierThenName);

        System.out.println("\nSorted by Tier then Name:");
        System.out.println(customers);

    }
}
```

---

# Compile

```bash
javac ComparatorDemo.java
```

---

# Run

```bash
java ComparatorDemo
```

---

# Output

```text
Original List:
[Banana, Orange, Apple, Mango]

Natural Order:
[Apple, Banana, Mango, Orange]

Reverse Order:
[Orange, Mango, Banana, Apple]

Original Customers:
[Customer{name='John', tier=2},
 Customer{name='Alice', tier=1},
 Customer{name='David', tier=3},
 Customer{name='Bob', tier=1}]

Sorted by Name:
[Customer{name='Alice', tier=1},
 Customer{name='Bob', tier=1},
 Customer{name='David', tier=3},
 Customer{name='John', tier=2}]

Sorted by Tier then Name:
[Customer{name='Alice', tier=1},
 Customer{name='Bob', tier=1},
 Customer{name='John', tier=2},
 Customer{name='David', tier=3}]
```

---

# Explanation

## 1. Natural Order

```java
Comparator<String> natural = Comparator.naturalOrder();
```

### What it does

Creates a comparator that sorts objects in their **natural (ascending)** order.

For strings:

```text
Apple
Banana
Mango
Orange
```

For integers:

```text
10
20
30
40
```

It is equivalent to:

```java
Collections.sort(list);
```

---

## 2. Reverse Order

```java
Comparator<String> reverse = Comparator.reverseOrder();
```

### What it does

Sorts the collection in **descending** order.

Example:

```text
Orange
Mango
Banana
Apple
```

---

## 3. Sort by Object Property

```java
Comparator<Customer> byName =
        Comparator.comparing(Customer::getName);
```

### Explanation

`Comparator.comparing()` sorts objects using one of their fields.

```java
Customer::getName
```

is a **method reference**.

It is equivalent to:

```java
customer -> customer.getName()
```

Java extracts each customer's name and compares those names alphabetically.

Example:

```text
John
Alice
David
Bob
```

becomes

```text
Alice
Bob
David
John
```

---

## 4. Sort by Multiple Fields

```java
Comparator<Customer> byTierThenName =
        Comparator.comparingInt(Customer::getTier)
                  .thenComparing(Customer::getName);
```

### Step 1

Sort customers by **tier**.

```text
Tier 1
Tier 2
Tier 3
```

### Step 2

If two customers have the same tier, compare their names.

Example:

```text
Alice Tier 1
Bob   Tier 1
John  Tier 2
David Tier 3
```

Bob and Alice both belong to Tier 1, so they are sorted alphabetically.

---

# Understanding Method References

```java
Customer::getName
```

means:

```java
customer -> customer.getName()
```

Similarly,

```java
Customer::getTier
```

means:

```java
customer -> customer.getTier()
```

Method references make code shorter and easier to read.

---

# Why `comparingInt()` Instead of `comparing()`?

For integer fields, use:

```java
Comparator.comparingInt(Customer::getTier);
```

instead of:

```java
Comparator.comparing(Customer::getTier);
```

### Reason

* Avoids unnecessary boxing of `int` to `Integer`
* Better performance
* Recommended by Java API

---

# Time Complexity

Sorting uses **TimSort** (for Lists).

| Operation | Complexity     |
| --------- | -------------- |
| Sort      | **O(n log n)** |
| Compare   | **O(1)**       |
| Overall   | **O(n log n)** |

---

# Interview Questions

### Q1. What is `Comparator`?

A `Comparator` is an interface used to define **custom sorting logic** for objects.

---

### Q2. Difference between `Comparable` and `Comparator`?

| Comparable                   | Comparator                    |
| ---------------------------- | ----------------------------- |
| Defines natural ordering     | Defines custom ordering       |
| Implemented inside the class | Implemented outside the class |
| One sorting logic            | Multiple sorting strategies   |

---

### Q3. What does `Comparator.comparing()` do?

It creates a comparator based on a specified object property.

---

### Q4. What is `thenComparing()`?

It performs **secondary sorting** when the primary comparison results in equality.

---

### Q5. What is a Method Reference?

A method reference is a shorter form of a lambda expression.

Example:

```java
Customer::getName
```

is equivalent to

```java
customer -> customer.getName()
```

---

# Key Takeaways

* `Comparator.naturalOrder()` → Ascending order.
* `Comparator.reverseOrder()` → Descending order.
* `Comparator.comparing()` → Sort using an object field.
* `Comparator.comparingInt()` → Optimized sorting for integer fields.
* `thenComparing()` → Secondary sorting.
* Method references (`Class::method`) are concise alternatives to lambda expressions.
* `Comparator` is the preferred approach when you need multiple sorting strategies for the same class.
