# Java Core Concepts Cheat Sheet

## Control Flow Statements

### if Statement

```java
if (condition) {
    // code block
}
```

Example:

```java
int age = 18;

if (age >= 18) {
    System.out.println("Eligible to vote");
}
```

### if-else Statement

```java
if (condition) {
    // code
} else {
    // code
}
```

Example:

```java
int age = 16;

if (age >= 18) {
    System.out.println("Adult");
} else {
    System.out.println("Minor");
}
```

### else-if Ladder

```java
if (condition1) {
    // code
} else if (condition2) {
    // code
} else {
    // code
}
```

Example:

```java
int marks = 75;

if (marks >= 90) {
    System.out.println("Grade A");
} else if (marks >= 75) {
    System.out.println("Grade B");
} else {
    System.out.println("Grade C");
}
```

### switch Statement

```java
switch(expression) {
    case value1:
        // code
        break;

    case value2:
        // code
        break;

    default:
        // code
}
```

Example:

```java
int day = 3;

switch(day) {
    case 1:
        System.out.println("Monday");
        break;
    case 2:
        System.out.println("Tuesday");
        break;
    case 3:
        System.out.println("Wednesday");
        break;
    default:
        System.out.println("Invalid Day");
}
```

---

# Loops

## for Loop

```java
for(initialization; condition; increment/decrement) {
    // code
}
```

Example:

```java
for(int i = 1; i <= 5; i++) {
    System.out.println(i);
}
```

## while Loop

```java
while(condition) {
    // code
}
```

Example:

```java
int i = 1;

while(i <= 5) {
    System.out.println(i);
    i++;
}
```

## do-while Loop

```java
do {
    // code
} while(condition);
```

Example:

```java
int i = 1;

do {
    System.out.println(i);
    i++;
} while(i <= 5);
```

## Enhanced For Loop

```java
int[] numbers = {10, 20, 30};

for(int num : numbers) {
    System.out.println(num);
}
```

---

# Arrays

Arrays store multiple values of the same type.

## One-Dimensional Array

```java
int[] arr = {10, 20, 30, 40};

System.out.println(arr[0]);
```

## Array Declaration

```java
int[] arr = new int[5];
```

## Two-Dimensional Array

```java
int[][] matrix = {
    {1, 2},
    {3, 4}
};

System.out.println(matrix[1][0]);
```

---

# Strings

Strings are immutable objects.

## Creating Strings

```java
String s1 = "Hello";
String s2 = new String("World");
```

## Common Methods

```java
String text = "Java Programming";

text.length();
text.toUpperCase();
text.toLowerCase();
text.substring(0, 4);
text.contains("Java");
text.replace("Java", "Python");
```

## Comparing Strings

```java
String a = "Java";
String b = "Java";

System.out.println(a.equals(b));
```

---

# Packages

Packages are used to organize classes and interfaces.

## Create Package

```java
package com.company.utils;
```

## Import Package

```java
import java.util.Scanner;
import java.util.*;
```

## Advantages

- Avoid naming conflicts
- Better code organization
- Access control
- Reusability

---

# Wrapper Classes

Wrapper classes convert primitive data types into objects.

| Primitive | Wrapper Class |
|-----------|---------------|
| byte | Byte |
| short | Short |
| int | Integer |
| long | Long |
| float | Float |
| double | Double |
| char | Character |
| boolean | Boolean |

## Autoboxing

```java
Integer num = 100;
```

## Unboxing

```java
int value = num;
```

## Common Methods

```java
Integer.parseInt("123");
Double.parseDouble("12.5");
Integer.valueOf("100");
```

---

# Static vs Instance Members

## Static Members

Belong to the class.

```java
class Employee {
    static String company = "ABC";
}
```

Access:

```java
Employee.company;
```

## Instance Members

Belong to individual objects.

```java
class Employee {
    String name;
}
```

Access:

```java
Employee emp = new Employee();
emp.name = "John";
```

## Comparison

| Static | Instance |
|----------|----------|
| Shared among all objects | Separate for each object |
| Accessed using class name | Accessed using object |
| Single memory allocation | Multiple copies |

---

# Varargs

Allows variable number of arguments.

```java
public static int sum(int... numbers) {
    int total = 0;

    for(int n : numbers) {
        total += n;
    }

    return total;
}
```

Usage:

```java
sum(10, 20);
sum(10, 20, 30, 40);
```

Rules:

- Only one varargs parameter allowed.
- Must be the last parameter.

```java
void display(String name, int... marks)
```

---

# Inner Classes

## Member Inner Class

```java
class Outer {

    class Inner {
        void show() {
            System.out.println("Inner Class");
        }
    }
}
```

Usage:

```java
Outer outer = new Outer();
Outer.Inner inner = outer.new Inner();

inner.show();
```

## Static Nested Class

```java
class Outer {

    static class Nested {
        void display() {
            System.out.println("Static Nested Class");
        }
    }
}
```

Usage:

```java
Outer.Nested obj = new Outer.Nested();
```

## Anonymous Inner Class

```java
Runnable r = new Runnable() {
    @Override
    public void run() {
        System.out.println("Running");
    }
};
```

---

# Collections Framework

Provides ready-made data structures and algorithms.

```text
Iterable
   |
Collection
   |
-------------------------
|          |            |
List       Set         Queue
```

`Map` is not part of the Collection hierarchy.

---

# List Interface

Maintains insertion order and allows duplicates.

## ArrayList

```java
List<String> list = new ArrayList<>();

list.add("Java");
list.add("Python");
```

### Characteristics

- Dynamic array
- Fast random access
- Slower insertion/deletion in middle

## LinkedList

```java
List<String> list = new LinkedList<>();

list.add("Java");
list.add("Python");
```

### Characteristics

- Doubly linked list
- Faster insertion/deletion
- Slower random access

## ArrayList vs LinkedList

| Feature | ArrayList | LinkedList |
|----------|-----------|------------|
| Storage | Dynamic Array | Linked List |
| Access | Fast | Slow |
| Insert/Delete | Slower | Faster |
| Memory Usage | Less | More |

---

# Set Interface

Stores unique values.

## HashSet

```java
Set<Integer> set = new HashSet<>();

set.add(10);
set.add(20);
set.add(10);
```

Characteristics:

- No duplicates
- Unordered
- Fast operations

## TreeSet

```java
Set<Integer> set = new TreeSet<>();
```

Characteristics:

- Sorted order
- No duplicates

---

# Map Interface

Stores key-value pairs.

## HashMap

```java
Map<Integer, String> map = new HashMap<>();

map.put(1, "John");
map.put(2, "David");

System.out.println(map.get(1));
```

Characteristics:

- Unique keys
- Fast retrieval
- Unordered

---

# Iterator

Used to traverse collections.

```java
Iterator<String> itr = list.iterator();

while(itr.hasNext()) {
    System.out.println(itr.next());
}
```

Remove element safely:

```java
itr.remove();
```

---

# ListIterator

Supports bidirectional traversal.

```java
ListIterator<String> itr = list.listIterator();

while(itr.hasNext()) {
    System.out.println(itr.next());
}

while(itr.hasPrevious()) {
    System.out.println(itr.previous());
}
```

Features:

- Forward traversal
- Backward traversal
- Add, remove, update elements

---

# Generics

Provide compile-time type safety.

Without Generics:

```java
ArrayList list = new ArrayList();
list.add("Java");
```

With Generics:

```java
ArrayList<String> list = new ArrayList<>();

list.add("Java");
```

## Generic Class

```java
class Box<T> {

    private T value;

    public void set(T value) {
        this.value = value;
    }

    public T get() {
        return value;
    }
}
```

Usage:

```java
Box<Integer> box = new Box<>();
```

Benefits:

- Type safety
- No explicit casting
- Reusable code

---

# Collections Utility Class

Located in:

```java
import java.util.Collections;
```

## Sorting

```java
Collections.sort(list);
```

## Reverse

```java
Collections.reverse(list);
```

## Shuffle

```java
Collections.shuffle(list);
```

## Maximum

```java
Collections.max(list);
```

## Minimum

```java
Collections.min(list);
```

---

# Serialization

Serialization converts an object into a byte stream.

```text
Object → Byte Stream
```

Uses:

- File storage
- Network communication
- Caching
- Persistence

## Serializable Interface

```java
import java.io.Serializable;

class Employee implements Serializable {

    private static final long serialVersionUID = 1L;

    int id;
    String name;
}
```

---

# serialVersionUID

Unique version identifier for serialized classes.

```java
private static final long serialVersionUID = 1L;
```

Benefits:

- Version control for serialized objects
- Prevents InvalidClassException
- Ensures compatibility during deserialization

---

# transient Keyword

Prevents field serialization.

```java
class Employee implements Serializable {

    String username;

    transient String password;
}
```

After deserialization:

```java
password == null;
```

Common Use Cases:

- Passwords
- Tokens
- Temporary data
- Sensitive information

---

# Deep Copy vs Shallow Copy

## Shallow Copy

Copies references only.

```java
Employee e2 = e1;
```

```text
e1 ----\
        > Same Object
e2 ----/
```

Changes in one reference affect the other.

---

## Deep Copy

Creates a completely new object.

```java
Employee e2 = new Employee();

e2.id = e1.id;
e2.name = e1.name;
```

```text
e1 --> Object 1

e2 --> Object 2
```

Changes are independent.

---

## Comparison

| Feature | Shallow Copy | Deep Copy |
|----------|-------------|-----------|
| New Object | No | Yes |
| Shared References | Yes | No |
| Memory Usage | Less | More |
| Performance | Faster | Slower |
| Side Effects | Possible | None |

---

# Frequently Asked Interview Questions

1. Difference between ArrayList and LinkedList?
2. Difference between HashSet and TreeSet?
3. Difference between Iterator and ListIterator?
4. Why use Generics?
5. What is Autoboxing and Unboxing?
6. Difference between static and instance members?
7. What are Varargs?
8. What is Serialization?
9. Why is serialVersionUID important?
10. What does transient keyword do?
11. Difference between Deep Copy and Shallow Copy?
12. Why are Strings immutable?
13. Difference between == and equals()?
14. Difference between HashMap and TreeMap?
15. Advantages of Collections Framework?
