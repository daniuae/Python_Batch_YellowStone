# LAB 4: Access Modifiers in Java

## 📌 Objective

In this lab, you will learn how Java controls access to variables and methods using the four access modifiers:

- **public**
- **private**
- **protected**
- **default (package-private)**

You will also understand how access changes depending on:

- Same class
- Same package
- Different package
- Subclass (Inheritance)
- Non-subclass

---

# What are Access Modifiers?

Access modifiers determine **who can access a class member (variables, methods, constructors).**

Think of them like security levels in a building.

| Modifier | Who Can Access? |
|-----------|-----------------|
| **public** | Everyone |
| **protected** | Same package + subclasses |
| **default** | Same package only |
| **private** | Same class only |

---

# Real-World Analogy

Imagine your house.

| Modifier | Example |
|----------|---------|
| **public** | Front garden (everyone can see) |
| **protected** | Family members |
| **default** | People inside your apartment building |
| **private** | Your bedroom |

---

# Project Structure

Create the following folders and files.

```text
AccessModifierLab/
│
├── src/
│   └── com/
│       └── example/
│           ├── a/
│           │   ├── Base.java
│           │   └── SamePackage.java
│           │
│           └── b/
│               ├── Sub.java
│               └── Other.java
│
└── out/
```

---

# Step 1 — Create Base.java

**Location**

```text
src/com/example/a/Base.java
```

**Code**

```java
package com.example.a;

public class Base {

    public int pub = 1;

    protected int prot = 2;

    int pack = 3;

    private int priv = 4;

    public void show() {
        System.out.println(pub);
        System.out.println(prot);
        System.out.println(pack);
        System.out.println(priv);
    }
}
```

---

## Explanation

### 1. Public Variable

```java
public int pub = 1;
```

Accessible from **everywhere**.

---

### 2. Protected Variable

```java
protected int prot = 2;
```

Accessible from

- Same package
- Subclasses in another package

---

### 3. Default Variable

```java
int pack = 3;
```

No modifier means **default** (package-private).

Accessible **only within the same package**.

---

### 4. Private Variable

```java
private int priv = 4;
```

Accessible **only inside the Base class**.

---

## Memory Illustration

```
Base Object

+----------------------+
| pub  = 1             |
| prot = 2             |
| pack = 3             |
| priv = 4             |
+----------------------+
```

Inside `Base` itself:

```
public      ✔
protected   ✔
default     ✔
private     ✔
```

---

# Step 2 — Create SamePackage.java

**Location**

```text
src/com/example/a/SamePackage.java
```

**Code**

```java
package com.example.a;

public class SamePackage {

    public static void main(String[] args) {

        Base b = new Base();

        System.out.println("Public    : " + b.pub);
        System.out.println("Protected : " + b.prot);
        System.out.println("Default   : " + b.pack);

        // System.out.println(b.priv); // ERROR
    }
}
```

---

## Why does this work?

Both classes belong to the same package.

```
com.example.a
```

Therefore,

```
public      ✔
protected   ✔
default     ✔
private     ✘
```

---

## Illustration

```
Package A

+---------------------+
| Base                |
|                     |
| public              |
| protected           |
| default             |
| private             |
+---------------------+

        ▲

SamePackage

Can access

✔ public
✔ protected
✔ default
✘ private
```

---

## Output

```
Public    : 1
Protected : 2
Default   : 3
```

---

# Step 3 — Create Sub.java

**Location**

```text
src/com/example/b/Sub.java
```

**Code**

```java
package com.example.b;

import com.example.a.Base;

public class Sub extends Base {

    public static void main(String[] args) {

        Sub s = new Sub();

        System.out.println("Public    : " + s.pub);
        System.out.println("Protected : " + s.prot);

        // System.out.println(s.pack); // ERROR
        // System.out.println(s.priv); // ERROR
    }
}
```

---

## Why does protected work?

Because `Sub` extends `Base`.

```
Sub
 ↓
Base
```

Inheritance allows access to **protected** members even if the subclass is in another package.

---

## Access Diagram

```
Package A

Base

     ▲
     │
Inheritance
     │
Package B

Sub
```

Accessible:

```
public      ✔
protected   ✔
default     ✘
private     ✘
```

---

## Output

```
Public    : 1
Protected : 2
```

---

# Step 4 — Create Other.java

**Location**

```text
src/com/example/b/Other.java
```

**Code**

```java
package com.example.b;

import com.example.a.Base;

public class Other {

    public static void main(String[] args) {

        Base b = new Base();

        System.out.println("Public : " + b.pub);

        // System.out.println(b.prot); // ERROR
        // System.out.println(b.pack); // ERROR
        // System.out.println(b.priv); // ERROR
    }
}
```

---

## Why only public?

`Other` is:

- In a different package
- Not a subclass

Therefore,

```
public      ✔
protected   ✘
default     ✘
private     ✘
```

---

## Illustration

```
Package A

Base

------------------------

Package B

Other

(No inheritance)

Can access

✔ public
✘ protected
✘ default
✘ private
```

---

## Output

```
Public : 1
```

---

# Step 5 — Compile the Program

Open Terminal and move to your project directory.

```bash
cd AccessModifierLab
```

### macOS / Linux

```bash
javac -d out $(find src -name "*.java")
```

### Windows

```cmd
javac -d out src\com\example\a\*.java src\com\example\b\*.java
```

If compilation succeeds, the `out` folder will contain compiled `.class` files.

```
out/
└── com
    └── example
        ├── a
        └── b
```

---

# Step 6 — Run the Programs

## Run SamePackage

```bash
java -cp out com.example.a.SamePackage
```

Output

```
Public    : 1
Protected : 2
Default   : 3
```

---

## Run Sub

```bash
java -cp out com.example.b.Sub
```

Output

```
Public    : 1
Protected : 2
```

---

## Run Other

```bash
java -cp out com.example.b.Other
```

Output

```
Public : 1
```

---

# What Happens if You Uncomment the Error Lines?

## Example 1

```java
System.out.println(b.priv);
```

Compiler Error

```
priv has private access in Base
```

---

## Example 2

```java
System.out.println(b.pack);
```

Compiler Error

```
pack is not public in Base;
cannot be accessed from outside package
```

---

## Example 3

```java
System.out.println(b.prot);
```

Compiler Error

```
prot has protected access in Base
```

---

# Complete Access Matrix

| Access From | public | protected | default | private |
|-------------|:------:|:---------:|:-------:|:-------:|
| Same Class | ✅ | ✅ | ✅ | ✅ |
| Same Package | ✅ | ✅ | ✅ | ❌ |
| Subclass (Different Package) | ✅ | ✅ | ❌ | ❌ |
| Different Package (No Inheritance) | ✅ | ❌ | ❌ | ❌ |

---

# Visual Summary

```
                    ACCESS MODIFIERS

                 Base Class Members
            +------------------------+
            | public                 |
            | protected              |
            | default                |
            | private                |
            +------------------------+

            Same Class
            ✔ ✔ ✔ ✔

            Same Package
            ✔ ✔ ✔ ✘

            Different Package
            Subclass
            ✔ ✔ ✘ ✘

            Different Package
            Non-Subclass
            ✔ ✘ ✘ ✘
```

---

# Difference Between protected and default

| Feature | protected | default |
|---------|-----------|----------|
| Same Package | ✅ | ✅ |
| Different Package | ❌ | ❌ |
| Subclass in Different Package | ✅ | ❌ |
| Non-subclass in Different Package | ❌ | ❌ |

**Key Point**

- **protected** = Same package + subclasses (even in different packages)
- **default** = Same package only

---

# Interview Questions

### 1. Which access modifier is accessible everywhere?

**Answer:** `public`

---

### 2. Which modifier is visible only inside the class?

**Answer:** `private`

---

### 3. What is the default access modifier in Java?

**Answer:** Package-private (no modifier specified).

---

### 4. Can a subclass in another package access protected members?

**Answer:** Yes.

---

### 5. Can another package access default members?

**Answer:** No.

---

### 6. Which modifier provides the highest level of encapsulation?

**Answer:** `private`

---

# Key Takeaways

- `public` → Accessible from anywhere.
- `private` → Accessible only within the same class.
- `protected` → Accessible within the same package and by subclasses in other packages.
- `default` (package-private) → Accessible only within the same package.
- Access modifiers are a core part of **encapsulation** and help protect data while enforcing object-oriented design principles.
