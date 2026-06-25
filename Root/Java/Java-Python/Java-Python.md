# Python vs Java – Comprehensive Comparison Guide

> **Note:** This is Part 1 of a structured training guide. It is written in Markdown and can be extended into a full course.

# Table of Contents

1. JDK / JRE / JVM Architecture vs Python Runtime
2. Bytecode
3. Data Types
4. Variables
5. Literals
6. Operators
7. Basic Input / Output
8. IDE Setup
9. Compiling & Running Programs
10. Memory Areas (Stack / Heap)
11. Coding Standards
12. Control Flow
13. Loops
14. Arrays
15. Strings
16. Packages vs Modules
17. Wrapper Classes
18. Static vs Instance Members
19. Varargs
20. Inner Classes
21. Collections Framework
22. List / Set / Map
23. ArrayList vs LinkedList
24. Iterator / ListIterator
25. Generics vs Type Hints
26. Collections Utilities
27. Serialization
28. serialVersionUID
29. transient
30. Deep Copy vs Shallow Copy

---

# 1. JDK / JRE / JVM Architecture vs Python Runtime

## Java Architecture

```text
Java Source (.java)
      |
    javac
      |
Bytecode (.class)
      |
     JVM
      |
Operating System
```

### Components

| Component | Purpose |
|-----------|---------|
| JDK | Development Kit (Compiler + JRE + Tools) |
| JRE | Java Runtime Environment |
| JVM | Executes Bytecode |

### Java Example

```java
public class Hello {
    public static void main(String[] args){
        System.out.println("Hello Java");
    }
}
```

Compile:

```bash
javac Hello.java
```

Run:

```bash
java Hello
```

## Python Runtime

```text
Python Source (.py)
       |
Python Compiler
       |
Bytecode (.pyc)
       |
Python Virtual Machine
       |
Operating System
```

```python
print("Hello Python")
```

Run:

```bash
python hello.py
```

---

# 2. Bytecode

## Java

- Compiled using `javac`
- Produces `.class`
- Platform independent

Inspect:

```bash
javap -c Hello
```

## Python

- Produces `.pyc` inside `__pycache__`
- Executed by Python VM

---

# 3. Data Types

| Java | Python |
|------|--------|
| int | int |
| double | float |
| char | str (length 1) |
| boolean | bool |

```java
int age = 25;
double salary = 45000.50;
boolean active = true;
```

```python
age = 25
salary = 45000.50
active = True
```

---

# 4. Variables

## Java

```java
String name = "Alice";
```

## Python

```python
name = "Alice"
```

Java is statically typed. Python is dynamically typed.

---

# 5. Literals

```java
int x = 100;
char c = 'A';
String s = "Java";
```

```python
x = 100
c = "A"
s = "Python"
```

---

# 6. Operators

Arithmetic, Relational, Logical, Assignment, Bitwise are supported by both languages.

```java
System.out.println(10 + 20);
```

```python
print(10 + 20)
```

---

# 7. Basic Input / Output

## Java

```java
Scanner sc = new Scanner(System.in);
String name = sc.nextLine();
System.out.println(name);
```

## Python

```python
name = input("Name: ")
print(name)
```

---

# 8. IDE Setup

## Java

- IntelliJ IDEA
- Eclipse
- NetBeans

## Python

- VS Code
- PyCharm
- Jupyter Notebook

---

# 9. Memory Areas

```text
Stack
 ├─ Local variables
 └─ Method frames

Heap
 ├─ Objects
 └─ Arrays
```

Example:

```java
Employee e = new Employee();
```

`e` is stored on the stack and references an object on the heap.

---

# 10. Coding Standards

## Java

- Class → PascalCase
- Method → camelCase
- Variable → camelCase
- Constant → UPPER_CASE

## Python (PEP 8)

- Class → PascalCase
- Function → snake_case
- Variable → snake_case
- Constant → UPPER_CASE

---

# 11. Control Flow

## if/else

Java

```java
if(age >= 18){
    System.out.println("Adult");
}else{
    System.out.println("Minor");
}
```

Python

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

## switch vs match

Java

```java
switch(day){
case 1: System.out.println("Mon"); break;
default: System.out.println("Unknown");
}
```

Python

```python
match day:
    case 1:
        print("Mon")
    case _:
        print("Unknown")
```

---

# 12. Loops

## for

```java
for(int i=1;i<=5;i++){
    System.out.println(i);
}
```

```python
for i in range(1,6):
    print(i)
```

## while

```java
while(i<5){
    i++;
}
```

```python
while i < 5:
    i += 1
```

## do-while

```java
do{
    i++;
}while(i<5);
```

Python equivalent:

```python
while True:
    i += 1
    if i >= 5:
        break
```

---

# 13. Arrays vs Lists

Java

```java
int[] nums = {1,2,3};
```

Python

```python
nums = [1,2,3]
```

---

# 14. Strings

Both are immutable.

---

# 15. Packages vs Modules

Java

```java
package com.example;
```

Python

```python
import math
```

---

# 16. Wrapper Classes

Java: Integer, Double, Character, Boolean

Python: Everything is already an object.

---

# 17. Static vs Instance

```java
class Employee{
 static String company="ABC";
 String name;
}
```

```python
class Employee:
    company="ABC"
    def __init__(self,name):
        self.name=name
```

---

# 18. Varargs

Java

```java
int sum(int... nums){ return 0; }
```

Python

```python
def total(*nums):
    return sum(nums)
```

---

# 19. Inner Classes

Java supports member, static, local and anonymous inner classes.

Python supports nested classes.

---

# 20. Collections

| Java | Python |
|------|--------|
| List | list |
| Set | set |
| Map | dict |

---

# 21. ArrayList vs LinkedList

| Feature | ArrayList | LinkedList |
|---------|-----------|------------|
| Random Access | Fast | Slow |
| Insert Middle | Slow | Fast |

---

# 22. Iterator

Java:

```java
Iterator<String> it = list.iterator();
```

Python:

```python
it = iter(my_list)
```

---

# 23. Generics vs Type Hints

Java

```java
List<String> names = new ArrayList<>();
```

Python

```python
from typing import List
names: List[str] = []
```

---

# 24. Serialization

Java

```java
class Employee implements Serializable {}
```

Python

```python
import pickle
```

---

# 25. serialVersionUID

```java
private static final long serialVersionUID = 1L;
```

---

# 26. transient

```java
transient String password;
```

---

# 27. Deep Copy vs Shallow Copy

Python

```python
import copy

b = copy.copy(a)
c = copy.deepcopy(a)
```

Java

Create a copy constructor or clone objects carefully.

---

# Summary

| Feature | Java | Python |
|---------|------|--------|
| Typing | Static | Dynamic |
| Compilation | Yes | No |
| Runtime | JVM | Python VM |
| Performance | High | Moderate |
| Enterprise | Excellent | Good |
| AI/Data | Moderate | Excellent |

> This document is a foundation for a complete Java vs Python handbook.
