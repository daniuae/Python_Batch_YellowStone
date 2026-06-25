# Fixing the Java Package Declaration Error

## Problem

You declared the package as:

```java
package src.com.example.b;
```

This is **incorrect**.

When you try to run:

```bash
java -cp out com.example.b.Sub
```

Java throws:

```text
Error: Could not find or load main class com.example.b.Sub
```

---

# Why Does This Happen?

Your project structure is:

```text
java/
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
```

Notice that **`src` is only the source folder**.

It is **NOT** part of the Java package.

---

# Java Rule

The package name is determined by the folders **inside the source root**.

General rule:

```text
Source Root
     │
     ▼
src/
   └── com/
       └── example/
           └── b/
               Sub.java
```

The package is:

```java
package com.example.b;
```

**NOT**

```java
package src.com.example.b;
```

---

# Incorrect Package Declaration

```java
package src.com.example.b;
```

Java expects the file to be located here:

```text
src/
└── src/
    └── com/
        └── example/
            └── b/
                Sub.java
```

Since this folder does not exist, Java cannot locate the class.

---

# Correct Package Declaration

### Base.java

```java
package com.example.a;
```

---

### SamePackage.java

```java
package com.example.a;
```

---

### Sub.java

```java
package com.example.b;
```

---

### Other.java

```java
package com.example.b;
```

---

# Folder Structure vs Package

| File Location | Correct Package |
|---------------|-----------------|
| `src/com/example/a/Base.java` | `package com.example.a;` |
| `src/com/example/a/SamePackage.java` | `package com.example.a;` |
| `src/com/example/b/Sub.java` | `package com.example.b;` |
| `src/com/example/b/Other.java` | `package com.example.b;` |

---

# Visual Illustration

```
Project Folder

java
│
├── src
│
│   └── com
│       └── example
│           ├── a
│           │    Base.java
│           │
│           └── b
│                Sub.java
```

The package starts **after `src`**.

```
src
 │
 └── com
      └── example
           └── b
```

Therefore:

```java
package com.example.b;
```

---

# Common Mistake

Many beginners think the package should include the `src` folder.

Example:

```
src/com/example/b/Sub.java
```

They write:

```java
package src.com.example.b;
```

This is incorrect because `src` is only the source directory.

---

# Correct Relationship

```
Folder

src/
   └── com/
       └── example/
           └── b/
```

↓

```
Package

com.example.b
```

---

# After Fixing the Package

Delete the old compiled files.

```bash
rm -rf out
```

Create the output folder.

```bash
mkdir out
```

Compile all Java files.

```bash
javac -d out $(find src -name "*.java")
```

If there are no compilation errors, verify the output.

```bash
find out
```

Expected:

```text
out/
└── com/
    └── example/
        ├── a/
        │   ├── Base.class
        │   └── SamePackage.class
        │
        └── b/
            ├── Sub.class
            └── Other.class
```

---

# Run the Programs

Run `SamePackage`

```bash
java -cp out com.example.a.SamePackage
```

Run `Sub`

```bash
java -cp out com.example.b.Sub
```

Run `Other`

```bash
java -cp out com.example.b.Other
```

---

# Why These Commands Work

The `-cp out` option tells Java:

> "The root of all compiled packages is the `out` directory."

Java then searches for:

```text
out/
└── com/
    └── example/
        └── b/
            Sub.class
```

Because the package is:

```java
package com.example.b;
```

Java successfully locates:

```text
out/com/example/b/Sub.class
```

---

# Summary

## ❌ Incorrect

```java
package src.com.example.a;
```

```java
package src.com.example.b;
```

---

## ✅ Correct

```java
package com.example.a;
```

```java
package com.example.b;
```

---

# Key Takeaways

- `src` is the **source root**, not part of the package name.
- The package declaration must match the directory structure **inside** the source root.
- Always ensure that the package declaration and folder hierarchy are consistent.
- Compile using the `-d` option to generate the correct package hierarchy in the output directory.
- Run Java classes using their **fully qualified package names**, not file paths.

Example:

```bash
java -cp out com.example.b.Sub
```

**Not**

```bash
java -cp out src.com.example.b.Sub
```
