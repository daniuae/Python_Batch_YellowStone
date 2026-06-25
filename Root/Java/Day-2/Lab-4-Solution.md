# Fixing the Error: `javac: directory not found: out`

## Problem

You ran the following command:

```bash
javac -d out $(find src -name "*.java")
```

and received this error:

```text
javac: directory not found: out
Usage: javac <options> <source files>
```

---

# Why This Error Occurred

Your current directory is:

```text
/Users/dhandapanidhandapaniyedappalli/java
```

The output of `ls -l` shows:

```text
Animal.java
Demo.java
PrimitiveBasics.java
RefDemo.java
src/
```

Notice that there is **no `out` directory**.

The `-d out` option tells the Java compiler to place all compiled `.class` files into the `out` directory.

Since the directory doesn't exist, the compiler throws this error.

---

# Step 1 — Verify Your Current Directory

Run:

```bash
pwd
```

Expected Output:

```text
/Users/dhandapanidhandapaniyedappalli/java
```

---

# Step 2 — Verify That the `src` Folder Exists

Run:

```bash
ls -l
```

Expected Output:

```text
Animal.java
Demo.java
PrimitiveBasics.java
RefDemo.java
src
```

The `src` directory should be present.

---

# Step 3 — Check Your Java Source Files

Run:

```bash
find src -name "*.java"
```

Expected Output:

```text
src/com/example/a/Base.java
src/com/example/a/SamePackage.java
src/com/example/b/Sub.java
src/com/example/b/Other.java
```

If you see these files, your project structure is correct.

---

# Step 4 — Create the Output Directory

Since the `out` folder does not exist, create it.

```bash
mkdir out
```

Verify:

```bash
ls
```

Expected Output:

```text
Animal.java
Demo.java
PrimitiveBasics.java
RefDemo.java
src
out
```

Now the compiler has a destination for the compiled `.class` files.

---

# Step 5 — Compile the Project

Run:

```bash
javac -d out $(find src -name "*.java")
```

If the compilation is successful, **no output** will be displayed.

---

# Step 6 — Verify the Compiled Files

Run:

```bash
find out
```

Expected Output:

```text
out
out/com
out/com/example
out/com/example/a
out/com/example/a/Base.class
out/com/example/a/SamePackage.class
out/com/example/b
out/com/example/b/Sub.class
out/com/example/b/Other.class
```

This confirms that all Java files have been compiled successfully.

---

# Step 7 — Run the Programs

## Run `SamePackage`

```bash
java -cp out com.example.a.SamePackage
```

Expected Output:

```text
Public    : 1
Protected : 2
Default   : 3
```

---

## Run `Sub`

```bash
java -cp out com.example.b.Sub
```

Expected Output:

```text
Public    : 1
Protected : 2
```

---

## Run `Other`

```bash
java -cp out com.example.b.Other
```

Expected Output:

```text
Public : 1
```

---

# Project Structure Before Compilation

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
│
└── out/    ← Create this directory
```

---

# Project Structure After Compilation

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
│
└── out/
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

# Common Errors and Solutions

## Error 1

```text
javac: directory not found: out
```

**Reason**

The `out` directory does not exist.

**Solution**

```bash
mkdir out
```

---

## Error 2

```text
find: src: No such file or directory
```

**Reason**

You are not in the correct project directory.

**Solution**

```bash
pwd
cd /path/to/your/project
```

---

## Error 3

```text
Could not find or load main class
```

**Reason**

Incorrect package name or classpath.

**Correct Command**

```bash
java -cp out com.example.b.Sub
```

**Incorrect Command**

```bash
java -cp out src.com.example.b.Sub
```

The `src` directory is **not** part of the package name.

---

# Complete Workflow

```bash
# Navigate to the project directory
cd /Users/dhandapanidhandapaniyedappalli/java

# Verify the current directory
pwd

# Check the source files
find src -name "*.java"

# Create the output directory
mkdir out

# Compile all Java files
javac -d out $(find src -name "*.java")

# Verify compiled classes
find out

# Run SamePackage
java -cp out com.example.a.SamePackage

# Run Sub
java -cp out com.example.b.Sub

# Run Other
java -cp out com.example.b.Other
```

---

# Key Takeaways

- The `-d` option specifies the destination directory for compiled `.class` files.
- The destination directory (e.g., `out`) **must exist** before compiling.
- The `src` directory contains source code and is **not** part of the package name.
- Use the fully qualified package name when running Java programs.

Example:

```bash
java -cp out com.example.b.Sub
```

**Not**

```bash
java -cp out src.com.example.b.Sub
```
