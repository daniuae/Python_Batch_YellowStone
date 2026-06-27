# Java Exception Handling & File I/O Labs (Day 6)

# Labs Day 6

---

# Lab 1: Exception Basics — Seeing the Failure Signal and Control Transfer

## 🎯 Objective

Experience how an exception interrupts normal flow, how the JVM looks for a handler, and how handling lets the program continue instead of crashing.

---

## Step 1 — Trigger a Simple Unchecked Exception

**File:** `BasicExceptionDemo.java`

```java
public class BasicExceptionDemo {

    public static void main(String[] args) {

        System.out.println("Before risky code");

        int x = 10;
        int y = 0;

        int z = x / y;   // ArithmeticException

        System.out.println("After risky code"); // never reached
    }
}
```

### 💡 Why?

Shows that an exception immediately interrupts normal program execution.

---

## Step 2 — Handle the Exception using try-catch

```java
public static void main(String[] args) {

    System.out.println("Before risky code");

    try {

        int x = 10;
        int y = 0;

        int z = x / y;

        System.out.println("Computation result : " + z);

    } catch (ArithmeticException e) {

        System.out.println("Handled : " + e);

    }

    System.out.println("After catch — program continues");
}
```

### 💡 Why?

A matching catch block prevents the program from terminating.

---

## Step 3 — finally Always Executes

```java
try {

    System.out.println("try start");

    int value = 42 / 2;

    System.out.println("Value = " + value);

} catch (Exception e) {

    System.out.println("Catch block");

} finally {

    System.out.println("finally always runs");

}
```

### 💡 Why?

`finally` executes whether or not an exception occurs.

---

## Step 4 — Compile & Run

```bash
javac BasicExceptionDemo.java
java BasicExceptionDemo
```

---

## ✅ Conclusion

* Exceptions interrupt normal flow.
* `try-catch` handles failures gracefully.
* `finally` always executes for cleanup.

---

# Lab 2: Checked vs Unchecked Exceptions

## 🎯 Objective

Understand the difference between checked and unchecked exceptions.

---

## Checked Example

```java
import java.io.*;

public class CheckedVsUnchecked {

    public static void main(String[] args) {

        try {

            FileReader fr = new FileReader("missing-file.txt");
            fr.close();

        } catch (FileNotFoundException e) {

            System.out.println("Checked handled : " + e.getClass().getSimpleName());

        } catch (IOException e) {

            System.out.println("IO Problem : " + e);

        }

        int a = 10;
        int b = 0;

        try {

            int c = a / b;

        } catch (ArithmeticException e) {

            System.out.println("Unchecked handled : " + e.getClass().getSimpleName());

        }
    }
}
```

### 💡 Why?

* Checked exceptions must be handled or declared.
* Unchecked exceptions are programming errors.

---

## Compile & Run

```bash
javac CheckedVsUnchecked.java
java CheckedVsUnchecked
```

---

## ✅ Conclusion

| Checked                    | Unchecked                          |
| -------------------------- | ---------------------------------- |
| Compiler enforces handling | Compiler does not enforce handling |
| Recoverable                | Programming bug                    |
| Must handle or declare     | Optional to handle                 |

---

# Lab 3: try, catch, finally Control Flow

## Objective

Learn exactly when each block executes.

---

### Case 1 — No Exception

```java
try {

    System.out.println("Try");

} catch(RuntimeException e){

    System.out.println("Catch");

} finally {

    System.out.println("Finally");

}
```

---

### Case 2 — Exception Caught

```java
try {

    int x = 1 / 0;

} catch(ArithmeticException e){

    System.out.println("Handled");

} finally {

    System.out.println("Cleanup");

}
```

---

### Case 3 — return inside try

```java
static int demo(){

    try{

        return 1;

    } finally {

        System.out.println("Finally executes");

    }
}
```

---

## Compile

```bash
javac TryCatchFinallyFlow.java
java TryCatchFinallyFlow
```

---

## ✅ Conclusion

* `try` protects risky code.
* `catch` handles matching exceptions.
* `finally` always executes.

---

# Lab 4: throw Keyword

## Objective

Throw exceptions manually.

```java
public class BusinessRuleThrow {

    static void registerAge(int age){

        if(age < 0){

            throw new IllegalArgumentException("Age cannot be negative");

        }

        System.out.println(age);

    }

    public static void main(String[] args){

        try{

            registerAge(-5);

        }catch(Exception e){

            System.out.println(e.getMessage());

        }
    }
}
```

---

## Compile

```bash
javac BusinessRuleThrow.java
java BusinessRuleThrow
```

---

## ✅ Conclusion

`throw` allows developers to explicitly signal business rule violations.

---

# Lab 5: throws Keyword

## Objective

Understand exception propagation.

```java
import java.io.*;

public class ThrowsPropagation {

    static void readConfig() throws IOException{

        FileReader fr = new FileReader("config.txt");
        fr.close();

    }

    static void initialize() throws IOException{

        readConfig();

    }

    public static void main(String[] args){

        try{

            initialize();

        }catch(IOException e){

            System.out.println(e);

        }
    }
}
```

---

## ✅ Conclusion

`throws` transfers exception handling responsibility to the caller.

---

# Lab 6: Custom Exceptions

## Objective

Create application-specific exceptions.

### Custom Exception

```java
public class InvalidAgeException extends Exception{

    public InvalidAgeException(String message){

        super(message);

    }

}
```

---

### Service

```java
public class AccountService {

    public void register(int age) throws InvalidAgeException{

        if(age < 0){

            throw new InvalidAgeException("Age cannot be negative");

        }

    }
}
```

---

### Driver

```java
public class CustomExceptionDemo {

    public static void main(String[] args){

        AccountService service = new AccountService();

        try{

            service.register(-10);

        }catch(InvalidAgeException e){

            System.out.println(e.getMessage());

        }

    }
}
```

---

## ✅ Conclusion

Custom exceptions provide meaningful business-specific error messages.

---

# Lab 7: Exception Handling Best Practices

## Guidelines

* Catch specific exceptions.
* Never swallow exceptions.
* Use meaningful messages.
* Prefer try-with-resources.
* Fail fast.

Example:

```java
try{

    Files.readString(Path.of("config.json"));

}catch(NoSuchFileException e){

    System.err.println("Missing configuration");

}catch(IOException e){

    System.err.println(e.getMessage());

}
```

---

# Character Streams Lab

## FileReader & FileWriter

```java
FileWriter writer = new FileWriter("output.txt");

writer.write("Hello Java");

writer.close();

FileReader reader = new FileReader("output.txt");

int ch;

while((ch = reader.read()) != -1){

    System.out.print((char)ch);

}

reader.close();
```

---

## Conclusion

Character streams are simple but inefficient for large files.

---

# Line-by-Line Processing

```java
BufferedReader br = new BufferedReader(new FileReader("input.txt"));

String line;

while((line = br.readLine()) != null){

    System.out.println(line);

}

br.close();
```

---

# Writing Patterns

Overwrite:

```java
new FileWriter("report.txt");
```

Append:

```java
new FileWriter("report.txt", true);
```

---

# Serialization

## Employee.java

```java
public class Employee implements Serializable{

    private static final long serialVersionUID = 1L;

    String name;

    int age;

}
```

---

## Serialize

```java
ObjectOutputStream out =
new ObjectOutputStream(
new FileOutputStream("employees.ser"));

out.writeObject(employeeList);

out.close();
```

---

## Deserialize

```java
ObjectInputStream in =
new ObjectInputStream(
new FileInputStream("employees.ser"));

List<Employee> employees =
(List<Employee>) in.readObject();

in.close();
```

---

# serialVersionUID

```java
private static final long serialVersionUID = 1L;
```

Increment the UID whenever incompatible class changes are introduced.

---

# Final Summary

## Exception Handling

* try
* catch
* finally
* throw
* throws
* Checked Exceptions
* Unchecked Exceptions
* Custom Exceptions
* Best Practices

## File I/O

* FileReader
* FileWriter
* BufferedReader
* BufferedWriter
* Serialization
* Deserialization
* serialVersionUID
* Try-with-Resources
