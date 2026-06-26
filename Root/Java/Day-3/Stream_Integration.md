# Java Stream API Integration

## Objective

Learn how Java Streams process collections using:

* `stream()`
* `filter()`
* `map()`
* `collect()`

---

# Complete Executable Program

```java
import java.util.List;
import java.util.stream.Collectors;

public class StreamExample {

    public static void main(String[] args) {

        // Step 1: Create a List
        List<Integer> numbers = List.of(1, 2, 3, 4, 5, 6);

        System.out.println("Original List : " + numbers);

        // Step 2: Process using Stream API
        List<Integer> evenSquares = numbers.stream()
                                           .filter(n -> n % 2 == 0)
                                           .map(n -> n * n)
                                           .collect(Collectors.toList());

        System.out.println("Even Squares : " + evenSquares);
    }
}
```

---

# Output

```text
Original List : [1, 2, 3, 4, 5, 6]
Even Squares : [4, 16, 36]
```

---

# Stream Integration

```
Original List

[1,2,3,4,5,6]

        │
        ▼

numbers.stream()

        │
        ▼

1 → 2 → 3 → 4 → 5 → 6

        │
        ▼

filter(n -> n % 2 == 0)

        │

2 → 4 → 6

        │
        ▼

map(n -> n * n)

        │

4 → 16 → 36

        │
        ▼

collect(Collectors.toList())

        │

[4,16,36]
```

---

# Step 1: Create the List

```java
List<Integer> numbers = List.of(1, 2, 3, 4, 5, 6);
```

Creates an immutable list.

```
numbers

1
2
3
4
5
6
```

---

# Step 2: Convert List into a Stream

```java
numbers.stream()
```

A **Stream** is a sequence of elements that supports functional-style operations.

```
List
 ↓
Stream

1 → 2 → 3 → 4 → 5 → 6
```

No processing happens yet.

---

# Step 3: Filter Operation

```java
.filter(n -> n % 2 == 0)
```

Keeps only even numbers.

Lambda Expression:

```java
n -> n % 2 == 0
```

Meaning:

```
If number is divisible by 2
Keep it
Else
Discard it
```

Filtering Process

| Number | Even? | Keep |
| ------ | ----- | ---- |
| 1      | ❌     | No   |
| 2      | ✅     | Yes  |
| 3      | ❌     | No   |
| 4      | ✅     | Yes  |
| 5      | ❌     | No   |
| 6      | ✅     | Yes  |

Result

```
2
4
6
```

---

# Step 4: Map Operation

```java
.map(n -> n * n)
```

Transforms each remaining element.

```
2 → 4

4 → 16

6 → 36
```

Result

```
4
16
36
```

---

# Step 5: Collect Operation

```java
.collect(Collectors.toList())
```

Streams are not collections.

`collect()` converts the Stream into a List.

```
Stream

4
16
36

      │

      ▼

List

[4,16,36]
```

---

# Internal Working

```
Original List

1
2
3
4
5
6

          │

          ▼

filter()

1 ❌

2 ✅

3 ❌

4 ✅

5 ❌

6 ✅

          │

          ▼

map()

2 → 4

4 → 16

6 → 36

          │

          ▼

collect()

[4,16,36]
```

---

# Understanding the Lambda Expressions

## Filter

```java
.filter(n -> n % 2 == 0)
```

Equivalent Traditional Method

```java
public static boolean isEven(int n) {
    return n % 2 == 0;
}
```

---

## Map

```java
.map(n -> n * n)
```

Equivalent Traditional Method

```java
public static int square(int n) {
    return n * n;
}
```

---

# Stream Pipeline

A Java Stream consists of three stages.

## 1. Source

Creates the Stream.

```java
numbers.stream()
```

```
List
 ↓
Stream
```

---

## 2. Intermediate Operations

These return another Stream.

Examples

```java
filter()

map()

sorted()

distinct()

limit()

skip()
```

Pipeline Example

```
Stream
   │
   ▼

filter()

   │
   ▼

map()

   │
   ▼

sorted()
```

Intermediate operations are **lazy**. They execute only when a terminal operation is called.

---

## 3. Terminal Operation

Produces the final result.

Examples

```java
collect()

count()

forEach()

reduce()

findFirst()

anyMatch()
```

Example

```java
.collect(Collectors.toList())
```

---

# Complete Stream Lifecycle

```
Source

numbers.stream()

      │

      ▼

Intermediate

filter()

      │

      ▼

Intermediate

map()

      │

      ▼

Terminal

collect()

      │

      ▼

Final List

[4,16,36]
```

---

# Traditional Java vs Stream API

## Without Streams

```java
import java.util.ArrayList;
import java.util.List;

public class TraditionalExample {

    public static void main(String[] args) {

        List<Integer> numbers = List.of(1,2,3,4,5,6);

        List<Integer> result = new ArrayList<>();

        for(Integer n : numbers){

            if(n % 2 == 0){
                result.add(n * n);
            }

        }

        System.out.println(result);

    }
}
```

Output

```text
[4,16,36]
```

---

## Using Streams

```java
List<Integer> result = numbers.stream()
                              .filter(n -> n % 2 == 0)
                              .map(n -> n * n)
                              .collect(Collectors.toList());
```

The Stream API is shorter, more readable, easier to maintain, and supports parallel processing.

---

# Advantages of Java Streams

* Less code
* More readable
* Functional programming style
* No explicit loops
* Supports method chaining
* Lazy evaluation improves performance
* Easy parallel processing using `parallelStream()`

---

# Common Stream Operations

| Operation  | Purpose            | Example                        |
| ---------- | ------------------ | ------------------------------ |
| stream()   | Create Stream      | `numbers.stream()`             |
| filter()   | Select elements    | `filter(n -> n > 5)`           |
| map()      | Transform elements | `map(n -> n * 2)`              |
| sorted()   | Sort elements      | `sorted()`                     |
| distinct() | Remove duplicates  | `distinct()`                   |
| limit()    | First N elements   | `limit(5)`                     |
| skip()     | Skip N elements    | `skip(2)`                      |
| count()    | Count elements     | `count()`                      |
| collect()  | Convert to List    | `collect(Collectors.toList())` |
| forEach()  | Iterate            | `forEach(System.out::println)` |
| reduce()   | Aggregate          | `reduce(Integer::sum)`         |

---

# Interview Questions

### Q1. What is a Stream?

A Stream is a sequence of elements that supports functional-style operations on collections without modifying the original data.

---

### Q2. Does a Stream store data?

No.

A Stream processes data from a source such as a List, Set, or Array.

---

### Q3. What are Intermediate Operations?

Operations like:

* filter()
* map()
* sorted()
* distinct()

They return another Stream and are lazy.

---

### Q4. What are Terminal Operations?

Operations like:

* collect()
* count()
* reduce()
* forEach()

They produce the final result and trigger stream execution.

---

### Q5. Why use Streams?

* Less boilerplate code
* Cleaner syntax
* Functional programming support
* Better readability
* Easy parallel processing

---

# Key Takeaways

* `stream()` creates a Stream from a collection.
* `filter()` selects matching elements.
* `map()` transforms each element.
* `collect()` converts the Stream back into a collection.
* Intermediate operations are lazy.
* Terminal operations execute the pipeline.
* Streams make Java code more expressive, concise, and easier to maintain.
