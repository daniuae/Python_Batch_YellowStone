# Java Exception Handling, File I/O & Serialization

## Topics Covered

* Exception Handling (`try`, `catch`, `finally`)
* Checked vs Unchecked Exceptions
* Custom Exceptions
* Exception Hierarchy
* Resource Management (`try-with-resources`)
* Logging Basics
* `FileInputStream`
* `FileOutputStream`
* `PrintWriter`
* Serialization & Deserialization
* Directory Traversal
* Best Practices

---

# 1. Exception Handling

An **exception** is an event that interrupts the normal flow of a Java program.

## Exception Flow

```text
            Exception Occurs
                   |
              try block
                   |
          ------------------
          |                |
     No Exception      Exception
          |                |
     Continue         catch block
          |                |
          -------finally----
                   |
              Program Ends
```

## Syntax

```java
try {
    // Risky code
}
catch(ExceptionType e) {
    // Handle exception
}
finally {
    // Cleanup code
}
```

## Example

```java
public class TryCatchExample {

    public static void main(String[] args) {

        try {
            int result = 10 / 0;
            System.out.println(result);
        }
        catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero.");
        }
        finally {
            System.out.println("Finally block executed.");
        }

        System.out.println("Program continues.");
    }
}
```

### Output

```text
Cannot divide by zero.
Finally block executed.
Program continues.
```

---

# 2. Multiple Catch Blocks

```java
public class MultipleCatch {

    public static void main(String[] args) {

        try {
            String s = null;
            System.out.println(s.length());
        }
        catch (ArithmeticException e) {
            System.out.println("Arithmetic Error");
        }
        catch (NullPointerException e) {
            System.out.println("Null Pointer Error");
        }
        catch (Exception e) {
            System.out.println("General Exception");
        }
    }
}
```

### Output

```text
Null Pointer Error
```

---

# 3. Finally Block

The `finally` block always executes, whether an exception occurs or not.

```java
public class FinallyExample {

    public static void main(String[] args) {

        try {
            System.out.println("Inside try");
            return;
        }
        finally {
            System.out.println("Finally executed");
        }
    }
}
```

### Output

```text
Inside try
Finally executed
```

---

# 4. Java Exception Hierarchy

```text
                     Object
                        |
                  Throwable
                 /         \
             Error       Exception
                             |
          ----------------------------------
          |                                |
   RuntimeException              Checked Exceptions
          |
   ----------------------------
   |            |             |
Arithmetic   NullPointer   IndexOutOfBounds
Exception    Exception     Exception
```

### Error

Represents serious system-level problems.

Examples:

* OutOfMemoryError
* StackOverflowError

Usually not handled by applications.

### Exception

Represents recoverable problems that applications can handle.

---

# 5. Checked vs Unchecked Exceptions

## Checked Exceptions

* Checked during compilation.
* Must be handled or declared using `throws`.

Examples:

* IOException
* SQLException
* FileNotFoundException

```java
import java.io.*;

public class CheckedExample {

    public static void main(String[] args) {

        try {
            FileInputStream fis =
                new FileInputStream("sample.txt");
        }
        catch(IOException e) {
            System.out.println(e);
        }
    }
}
```

---

## Unchecked Exceptions

* Occur during runtime.
* Compiler does not force handling.

Examples:

* NullPointerException
* ArithmeticException
* ArrayIndexOutOfBoundsException

```java
public class UncheckedExample {

    public static void main(String[] args) {

        int[] arr = {10,20};

        System.out.println(arr[5]);
    }
}
```

### Output

```text
Exception in thread "main"
ArrayIndexOutOfBoundsException
```

---

## Comparison

| Checked Exception     | Unchecked Exception          |
| --------------------- | ---------------------------- |
| Compile-time          | Runtime                      |
| Must handle           | Optional                     |
| Subclass of Exception | Subclass of RuntimeException |
| IOException           | NullPointerException         |

---

# 6. throw Keyword

Used to explicitly throw an exception.

```java
public class ThrowExample {

    public static void main(String[] args) {

        throw new ArithmeticException("Invalid Operation");
    }
}
```

---

# 7. throws Keyword

Declares that a method may throw exceptions.

```java
import java.io.*;

public class ThrowsExample {

    public static void readFile() throws IOException {

        FileInputStream fis =
            new FileInputStream("sample.txt");
    }

    public static void main(String[] args) {

        try {
            readFile();
        }
        catch(IOException e) {
            System.out.println(e);
        }
    }
}
```

---

# 8. Custom Exception

## Creating Custom Exception

```java
class AgeException extends Exception {

    public AgeException(String message) {
        super(message);
    }
}
```

## Using Custom Exception

```java
public class CustomExceptionDemo {

    public static void validateAge(int age)
            throws AgeException {

        if(age < 18)
            throw new AgeException("Age must be at least 18.");
    }

    public static void main(String[] args) {

        try {
            validateAge(16);
        }
        catch(AgeException e) {
            System.out.println(e.getMessage());
        }
    }
}
```

### Output

```text
Age must be at least 18.
```

---

# 9. Resource Management (Try-With-Resources)

Automatically closes resources implementing the `AutoCloseable` interface.

## Traditional Approach

```java
FileInputStream fis = null;

try {
    fis = new FileInputStream("sample.txt");
}
finally {
    if(fis != null)
        fis.close();
}
```

---

## Modern Approach

```java
import java.io.*;

public class ResourceExample {

    public static void main(String[] args) {

        try(FileInputStream fis =
                new FileInputStream("sample.txt")) {

            System.out.println("Reading file...");
        }
        catch(IOException e) {
            e.printStackTrace();
        }
    }
}
```

---

# 10. Logging Basics

Instead of `System.out.println()`, use Java Logging.

```java
import java.util.logging.Logger;

public class LoggingExample {

    private static final Logger logger =
            Logger.getLogger(LoggingExample.class.getName());

    public static void main(String[] args) {

        logger.info("Application Started");
        logger.warning("Memory usage is high");
        logger.severe("Application crashed");
    }
}
```

---

# 11. FileInputStream

Reads binary data from a file.

## Illustration

```text
File
 |
 | bytes
 V
FileInputStream
 |
 V
Program
```

## Example

```java
import java.io.*;

public class FileInputExample {

    public static void main(String[] args) {

        try(FileInputStream fis =
                new FileInputStream("sample.txt")) {

            int data;

            while((data = fis.read()) != -1) {
                System.out.print((char)data);
            }

        }
        catch(IOException e) {
            e.printStackTrace();
        }
    }
}
```

---

# 12. FileOutputStream

Writes binary data to a file.

## Illustration

```text
Program
   |
   | bytes
   V
FileOutputStream
   |
   V
 File
```

## Example

```java
import java.io.*;

public class FileOutputExample {

    public static void main(String[] args) {

        try(FileOutputStream fos =
                new FileOutputStream("sample.txt")) {

            String text = "Hello Java";

            fos.write(text.getBytes());

        }
        catch(IOException e) {
            e.printStackTrace();
        }
    }
}
```

---

# 13. PrintWriter

Writes formatted text.

```java
import java.io.*;

public class PrintWriterExample {

    public static void main(String[] args) {

        try(PrintWriter pw =
                new PrintWriter("student.txt")) {

            pw.println("John");
            pw.println(90);
            pw.printf("%.2f",95.75);

        }
        catch(IOException e) {
            e.printStackTrace();
        }
    }
}
```

### Generated File

```text
John
90
95.75
```

---

# 14. Serialization

Serialization converts an object into a byte stream.

## Illustration

```text
Object
   |
Serializable
   |
ObjectOutputStream
   |
student.ser
```

## Serializable Class

```java
import java.io.Serializable;

class Student implements Serializable {

    private static final long serialVersionUID = 1L;

    String name;
    int age;

    Student(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```

---

## Serialize Object

```java
import java.io.*;

public class SerializeDemo {

    public static void main(String[] args) throws Exception {

        Student s = new Student("Alice",22);

        ObjectOutputStream out =
                new ObjectOutputStream(
                        new FileOutputStream("student.ser"));

        out.writeObject(s);

        out.close();
    }
}
```

---

# 15. Deserialization

Reads an object back from a file.

## Illustration

```text
student.ser
     |
ObjectInputStream
     |
 Object
```

## Example

```java
import java.io.*;

public class DeserializeDemo {

    public static void main(String[] args) throws Exception {

        ObjectInputStream in =
                new ObjectInputStream(
                        new FileInputStream("student.ser"));

        Student s = (Student) in.readObject();

        in.close();

        System.out.println(s.name);
        System.out.println(s.age);
    }
}
```

### Output

```text
Alice
22
```

---

# 16. Directory Traversal

Lists files and folders inside a directory.

## Directory Structure

```text
Documents
│
├── Resume.pdf
├── Notes.txt
├── Projects
│      ├── Java
│      └── Python
└── Images
```

---

## Using File Class

```java
import java.io.File;

public class DirectoryTraversal {

    public static void main(String[] args) {

        File folder = new File("Documents");

        File[] files = folder.listFiles();

        if(files != null) {

            for(File file : files) {

                if(file.isDirectory())
                    System.out.println("Directory : " + file.getName());
                else
                    System.out.println("File : " + file.getName());
            }
        }
    }
}
```

---

## Recursive Directory Traversal

```java
import java.io.File;

public class RecursiveTraversal {

    public static void list(File file) {

        if(file.isDirectory()) {

            System.out.println("Directory : " + file.getName());

            File[] files = file.listFiles();

            if(files != null) {

                for(File f : files) {
                    list(f);
                }
            }

        } else {

            System.out.println("File : " + file.getName());
        }
    }

    public static void main(String[] args) {

        list(new File("Documents"));
    }
}
```

### Sample Output

```text
Directory : Documents
File : Resume.pdf
File : Notes.txt
Directory : Projects
File : Employee.java
File : Student.java
Directory : Images
File : photo.png
```

---

# Best Practices

* Catch the most specific exception possible.
* Avoid empty `catch` blocks.
* Use `try-with-resources` for file and stream handling.
* Prefer logging over `System.out.println()` in production applications.
* Always provide meaningful messages in custom exceptions.
* Declare `serialVersionUID` for serializable classes.
* Check for `null` before iterating over `listFiles()`.
* Close streams automatically using `try-with-resources`.

---

# Quick Revision

| Topic               | Purpose                                |
| ------------------- | -------------------------------------- |
| `try`               | Contains risky code                    |
| `catch`             | Handles exceptions                     |
| `finally`           | Cleanup code                           |
| Checked Exception   | Compile-time exception                 |
| Unchecked Exception | Runtime exception                      |
| `throw`             | Throws an exception                    |
| `throws`            | Declares possible exceptions           |
| Custom Exception    | User-defined exception                 |
| Try-with-Resources  | Automatically closes resources         |
| Logger              | Records application events             |
| FileInputStream     | Reads binary files                     |
| FileOutputStream    | Writes binary files                    |
| PrintWriter         | Writes formatted text                  |
| Serialization       | Converts object to bytes               |
| Deserialization     | Reconstructs object from bytes         |
| Directory Traversal | Iterates through files and directories |
