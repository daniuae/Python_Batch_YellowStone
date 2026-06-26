# Java Generics - Raw Type vs Generic Type

## Objective

Learn the difference between:

* Raw Collections (Without Generics)
* Generic Collections (With Generics)

Understand why Generics were introduced in Java.

---

# What are Generics?

**Generics** allow you to specify the type of objects a collection can store.

Instead of storing **any type**, you can restrict a collection to store only one specific type.

Example:

```java
List<String> names = new ArrayList<>();
```

Here, the list can store **only String objects**.

---

# Why Were Generics Introduced?

Before Java 5, collections could store any type of object.

Example:

```java
List list = new ArrayList();

list.add("Java");
list.add(100);
list.add(true);
```

Although this compiles, it is unsafe because different types are mixed in the same collection.

Generics solve this problem by providing **compile-time type safety**.

---

# Program 1 - Without Generics (Raw Collection)

```java
import java.util.ArrayList;
import java.util.List;

public class RawListExample {

    public static void main(String[] args) {

        // Raw List (No Generics)
        List rawList = new ArrayList();

        rawList.add("Java");
        rawList.add(Integer.valueOf(42));

        System.out.println("Contents of Raw List:");
        System.out.println(rawList);

        try {

            // Wrong casting
            String text = (String) rawList.get(1);

            System.out.println(text);

        } catch (ClassCastException e) {

            System.out.println("Exception occurred:");
            System.out.println(e);

        }

    }
}
```

---

# Output

```text
Contents of Raw List:
[Java, 42]

Exception occurred:
java.lang.ClassCastException: java.lang.Integer cannot be cast to java.lang.String
```

---

# Explanation

## Step 1

```java
List rawList = new ArrayList();
```

A raw list accepts **any type of object**.

---

## Step 2

```java
rawList.add("Java");
```

Stores a String.

---

## Step 3

```java
rawList.add(Integer.valueOf(42));
```

Stores an Integer.

Now the list contains two different data types.

```
Index      Value

0          "Java"

1          42
```

---

## Step 4

```java
String text = (String) rawList.get(1);
```

`rawList.get(1)` returns:

```java
42
```

which is actually an Integer.

Java tries to convert

```java
Integer
```

into

```java
String
```

This conversion is invalid.

Result:

```
ClassCastException
```

---

# Internal Working

```
Raw List

+------------------+
| "Java"           |
| 42               |
+------------------+

        |

get(1)

        |

42 (Integer)

        |

(String)

        |

ClassCastException
```

---

# Problems with Raw Collections

* No type safety
* Runtime errors
* Manual casting required
* Hard to maintain
* Error detected only during execution

---

# Program 2 - With Generics

```java
import java.util.ArrayList;
import java.util.List;

public class GenericListExample {

    public static void main(String[] args) {

        // Generic List
        List<String> safeList = new ArrayList<>();

        safeList.add("Java");

        // safeList.add(42);   // Compile-time Error

        String text = safeList.get(0);

        System.out.println("Contents of Generic List:");
        System.out.println(safeList);

        System.out.println("Retrieved value:");
        System.out.println(text);

    }
}
```

---

# Output

```text
Contents of Generic List:
[Java]

Retrieved value:
Java
```

---

# Explanation

## Step 1

```java
List<String> safeList = new ArrayList<>();
```

The compiler knows that this list stores **only String objects**.

---

## Step 2

```java
safeList.add("Java");
```

Allowed.

---

## Step 3

```java
safeList.add(42);
```

Compiler Error.

```
Required type:

String

Provided:

int
```

The program will not compile.

---

## Step 4

```java
String text = safeList.get(0);
```

Since the compiler already knows the list contains Strings, no explicit cast is needed.

---

# Internal Working

```
Generic List

+------------------+
| "Java"           |
+------------------+

        |

get(0)

        |

Java

        |

No Casting Needed
```

---

# Raw Type vs Generic Type

| Feature               | Raw List | Generic List |
| --------------------- | -------- | ------------ |
| Type Safety           | ❌ No     | ✅ Yes        |
| Runtime Exception     | Possible | Very Rare    |
| Compile-Time Checking | ❌ No     | ✅ Yes        |
| Casting Required      | ✅ Yes    | ❌ No         |
| Readability           | Low      | High         |
| Recommended           | ❌ No     | ✅ Yes        |

---

# Compile-Time vs Runtime

## Without Generics

```
Write Code

↓

Compile Successfully

↓

Run Program

↓

ClassCastException
```

---

## With Generics

```
Write Code

↓

Compiler Checks Types

↓

Compilation Error

↓

Fix Immediately

↓

Run Safely
```

---

# Why Compile-Time Checking Is Better

Finding errors while compiling is much better than discovering them after the program has been deployed.

Generics move many type-related errors from **runtime** to **compile time**, making Java programs safer and easier to maintain.

---

# Advantages of Generics

* Type safety
* No manual casting
* Compile-time error detection
* Cleaner code
* Better readability
* Better IDE support (auto-completion)
* Reduced runtime exceptions

---

# Interview Questions

### Q1. What are Generics?

Generics allow classes, interfaces, and methods to work with a specific data type while providing compile-time type safety.

---

### Q2. Why were Generics introduced?

To eliminate runtime `ClassCastException`, improve type safety, and remove the need for explicit type casting.

---

### Q3. What is a Raw Type?

A raw type is a generic class or interface used without specifying its type parameter.

Example:

```java
List list = new ArrayList();
```

---

### Q4. What is the advantage of `List<String>` over `List`?

`List<String>` only accepts `String` objects, preventing accidental insertion of other types and eliminating explicit casts when retrieving elements.

---

### Q5. Why doesn't `safeList.add(42)` compile?

Because `safeList` is declared as `List<String>`, and the compiler enforces that only `String` objects can be added.

---

# Key Takeaways

* A **Raw List** (`List`) can store any object type and is not type-safe.
* A **Generic List** (`List<String>`) stores only `String` objects.
* Generics eliminate the need for explicit casting when retrieving elements.
* Type mismatches are detected at **compile time**, reducing runtime errors like `ClassCastException`.
* Modern Java code should always prefer **Generics** over raw collections.
