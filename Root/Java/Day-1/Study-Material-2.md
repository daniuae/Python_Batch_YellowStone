# Java Scanner Class

## What is Scanner in Java?

`Scanner` is a predefined class in the `java.util` package that is used to read input from the keyboard, files, or other input sources.

---

## Import Scanner

```java
import java.util.Scanner;
```

---

## Create a Scanner Object

```java
Scanner sc = new Scanner(System.in);
```

### Explanation

* `Scanner` → Class name
* `sc` → Object name
* `new Scanner(System.in)` → Creates a Scanner object that reads input from the keyboard

---

# Example 1: Read a String

```java
import java.util.Scanner;

public class ScannerDemo {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = sc.nextLine();

        System.out.println("Hello " + name);

        sc.close();
    }
}
```

### Input

```text
Dani
```

### Output

```text
Hello Dani
```

---

# Example 2: Read an Integer

```java
import java.util.Scanner;

public class ScannerDemo {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter age: ");
        int age = sc.nextInt();

        System.out.println("Age = " + age);

        sc.close();
    }
}
```

### Input

```text
25
```

### Output

```text
Age = 25
```

---

# Common Scanner Methods

| Method          | Description                      |
| --------------- | -------------------------------- |
| `next()`        | Reads one word                   |
| `nextLine()`    | Reads an entire line             |
| `nextInt()`     | Reads an integer                 |
| `nextDouble()`  | Reads a double                   |
| `nextFloat()`   | Reads a float                    |
| `nextLong()`    | Reads a long                     |
| `nextBoolean()` | Reads a boolean (`true`/`false`) |
| `nextByte()`    | Reads a byte                     |
| `nextShort()`   | Reads a short                    |

---

# Example: Multiple Inputs

```java
import java.util.Scanner;

public class Student {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Age: ");
        int age = sc.nextInt();

        System.out.print("Enter Marks: ");
        double marks = sc.nextDouble();

        System.out.println("Name  : " + name);
        System.out.println("Age   : " + age);
        System.out.println("Marks : " + marks);

        sc.close();
    }
}
```

---

# Difference Between `next()` and `nextLine()`

```java
Scanner sc = new Scanner(System.in);

String name1 = sc.next();
String name2 = sc.nextLine();
```

### Input

```text
Dhandapani Krishnamurthi
```

### `next()`

Reads only:

```text
Dhandapani
```

### `nextLine()`

Reads:

```text
Dhandapani Krishnamurthi
```

---

# Why `sc.close()`?

```java
sc.close();
```

### Benefits

* Releases system resources.
* Prevents resource leaks.
* Considered a good coding practice.
* Should be called when the Scanner object is no longer needed.

---

# Memory View

```java
Scanner sc = new Scanner(System.in);
```

```text
Stack Memory
------------
sc  --------->

Heap Memory
-----------
Scanner Object
```

### Explanation

* Variable `sc` is stored in **Stack Memory**.
* Scanner object is created in **Heap Memory**.
* `sc` holds the reference (address) of the object.

---

# Interview Question

## Q: Why do we use `System.in` in Scanner?

### Answer

`System.in` is Java's standard input stream that receives data from the keyboard. `Scanner` uses this stream to read user input.

```java
Scanner sc = new Scanner(System.in);
```

This statement means:

> "Create a Scanner object and connect it to the keyboard input stream."

---

# Key Points to Remember

1. `Scanner` belongs to the `java.util` package.
2. It is used to accept user input.
3. `next()` reads a single word.
4. `nextLine()` reads an entire line.
5. Different methods are available for different data types.
6. Always close the Scanner object after use.
7. `System.in` represents keyboard input.
