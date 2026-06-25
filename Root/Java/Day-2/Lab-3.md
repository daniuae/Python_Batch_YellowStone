# Fixing the Error: `Could not find or load main class RefDemo.java`

## Error

```text
dhandapanidhandapaniyedappalli@Dhandapanis-MacBook-Pro java % java RefDemo.java
Error: Could not find or load main class RefDemo.java
```

---

# Why This Error Occurs

The `java` command expects the **compiled class name**, **not the source file name**.

❌ Incorrect:

```bash
java RefDemo.java
```

Here, Java tries to find a class literally named `RefDemo.java`, which does not exist.

---

# Correct Way to Compile and Run

## Step 1: Verify Your Files

Run:

```bash
ls
```

Expected output:

```text
Person.java
RefDemo.java
```

---

## Step 2: Compile the Java Files

Compile both files together because `RefDemo.java` depends on `Person.java`.

```bash
javac Person.java RefDemo.java
```

If compilation is successful, no output is displayed.

---

## Step 3: Verify the Generated Class Files

Run:

```bash
ls
```

Expected output:

```text
Person.java
Person.class
RefDemo.java
RefDemo.class
```

The `.class` files are the compiled Java bytecode.

---

## Step 4: Execute the Program

Run:

```bash
java RefDemo
```

> **Do NOT include `.java` when running the program.**

---

# Expected Output

```text
========== Step 1 & Step 2 : Aliasing ==========
p1.name = Bob
p2.name = Bob

========== Primitive Value Copy ==========
a = 10
b = 20

========== Step 3 : null and NullPointerException ==========
Caught NPE: java.lang.NullPointerException

========== Step 4 : Method Parameter Semantics ==========
Before rename(): Init
After rename(): Updated
After reassign(): Updated

========== End of Lab ==========
```

---

# Verify Java Installation

Check the installed Java Runtime Environment (JRE):

```bash
java -version
```

Example output:

```text
openjdk version "17.0.15"
```

Check the Java Compiler:

```bash
javac -version
```

Example output:

```text
javac 17.0.15
```

Both versions should match.

---

# Common Mistakes

## Mistake 1

```bash
java RefDemo.java
```

❌ Incorrect

---

## Correct

```bash
java RefDemo
```

---

## Mistake 2

Compiling only one file:

```bash
javac RefDemo.java
```

If `Person.class` does not already exist, compilation fails because `RefDemo` depends on `Person`.

Correct:

```bash
javac Person.java RefDemo.java
```

---

## Mistake 3

Running before compilation.

Always compile first:

```bash
javac Person.java RefDemo.java
```

Then execute:

```bash
java RefDemo
```

---

# Verify Your Working Directory

Check the current directory:

```bash
pwd
```

List all files:

```bash
ls -l
```

You should see:

```text
Person.java
Person.class
RefDemo.java
RefDemo.class
```

---

# Troubleshooting Checklist

If the program does not run, execute the following commands:

```bash
pwd

ls -l

java -version

javac -version

javac Person.java RefDemo.java

java RefDemo
```

Review the output for:

- Missing `.java` files
- Missing `.class` files
- Compilation errors
- Java version mismatch
- Incorrect working directory

---

# Java Compilation Workflow

```text
        Source Code
     ┌──────────────┐
     │ Person.java  │
     │ RefDemo.java │
     └──────┬───────┘
            │
            ▼
      javac Compiler
            │
            ▼
     ┌──────────────┐
     │ Person.class │
     │ RefDemo.class│
     └──────┬───────┘
            │
            ▼
      java RefDemo
            │
            ▼
     Program Executes
```

---

# Quick Reference

| Task | Command |
|------|---------|
| List files | `ls` |
| Show current directory | `pwd` |
| Compile Java files | `javac Person.java RefDemo.java` |
| Run the program | `java RefDemo` |
| Check Java version | `java -version` |
| Check compiler version | `javac -version` |

---

# Key Takeaways

- `javac` compiles `.java` files into `.class` bytecode files.
- `java` executes the compiled class by its **class name**, **without the `.java` extension**.
- Always compile all dependent classes before running.
- Ensure that both `java` and `javac` use the same Java version.
```
