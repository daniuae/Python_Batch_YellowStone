# Java Collection Framework — Complete Guide with Code Examples

## What is the Java Collection Framework (JCF)?

The **Java Collection Framework (JCF)** is a unified architecture for storing and manipulating groups of objects.

It provides:

* Interfaces
* Implementations (Classes)
* Algorithms
* Utility Methods

---

# Collection Framework Hierarchy

```text
                          Iterable
                              │
                         Collection
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
      List                  Set                  Queue
        │                     │                     │
 ┌──────┼──────┐      ┌────────┼────────┐     ┌──────┴───────┐
 │      │      │      │        │        │     │              │
ArrayList LinkedList Vector HashSet LinkedHashSet TreeSet PriorityQueue ArrayDeque
                 │
               Stack


Map (Separate Interface)

         Map
   ┌──────┼─────────────┐
   │      │             │
HashMap LinkedHashMap TreeMap
               │
          Hashtable
```

---
# Java Collections Framework - Quick Summary Cheat Sheet

## Collection Summary

| Collection        | Short Summary                                                                                                             | Best Used For                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| **ArrayList**     | A dynamic array that provides fast random access (`O(1)`) and preserves insertion order. Best for read-heavy operations.  | Searching, indexing, storing ordered data.        |
| **LinkedList**    | A doubly linked list that provides fast insertion and deletion at both ends but slow random access (`O(n)`).              | Queues, frequent insertions and deletions.        |
| **Vector**        | A thread-safe version of `ArrayList`. All methods are synchronized, making it slower than `ArrayList`. Legacy collection. | Legacy multithreaded applications.                |
| **Stack**         | Implements the **LIFO (Last In First Out)** principle using `push()`, `pop()`, and `peek()`.                              | Undo operations, recursion, browser history.      |
| **HashSet**       | Stores only unique elements. Does not maintain insertion order. Provides very fast search, insertion, and deletion.       | Removing duplicates and fast membership checking. |
| **LinkedHashSet** | Same as `HashSet` but preserves insertion order while maintaining uniqueness.                                             | Unique elements with insertion order.             |
| **TreeSet**       | Stores unique elements in sorted order using a Red-Black Tree.                                                            | Sorted collections and range-based operations.    |
| **PriorityQueue** | Retrieves elements according to priority (smallest element first by default), not insertion order.                        | Task scheduling, priority processing, heaps.      |
| **ArrayDeque**    | Double-ended queue that allows insertion and deletion from both ends. Faster replacement for `Stack`.                     | Queue and stack implementations.                  |
| **HashMap**       | Stores key-value pairs with unique keys. Provides the fastest lookup and does not maintain insertion order.               | Caching, indexing, lookup tables.                 |
| **LinkedHashMap** | Same as `HashMap` but preserves insertion order (or access order if configured).                                          | LRU Cache and ordered maps.                       |
| **TreeMap**       | Stores key-value pairs sorted by keys using a Red-Black Tree.                                                             | Sorted maps, leaderboards, ranking systems.       |
| **Hashtable**     | Legacy synchronized implementation of `Map`. Does not allow `null` keys or values.                                        | Legacy thread-safe applications.                  |

---

# Quick Comparison Table

| Collection        |      Ordered      |    Sorted    |    Duplicates   | Thread Safe |               Null Allowed               |
| ----------------- | :---------------: | :----------: | :-------------: | :---------: | :--------------------------------------: |
| **ArrayList**     |       ✅ Yes       |     ❌ No     |      ✅ Yes      |     ❌ No    |                   ✅ Yes                  |
| **LinkedList**    |       ✅ Yes       |     ❌ No     |      ✅ Yes      |     ❌ No    |                   ✅ Yes                  |
| **Vector**        |       ✅ Yes       |     ❌ No     |      ✅ Yes      |    ✅ Yes    |                   ✅ Yes                  |
| **Stack**         |       ✅ LIFO      |     ❌ No     |      ✅ Yes      |    ✅ Yes    |                   ✅ Yes                  |
| **HashSet**       |        ❌ No       |     ❌ No     |       ❌ No      |     ❌ No    |               ✅ One `null`               |
| **LinkedHashSet** | ✅ Insertion Order |     ❌ No     |       ❌ No      |     ❌ No    |               ✅ One `null`               |
| **TreeSet**       |        ❌ No       |     ✅ Yes    |       ❌ No      |     ❌ No    |                ❌ No `null`               |
| **PriorityQueue** |  ❌ Priority Order | ✅ Heap Order |      ✅ Yes      |     ❌ No    |                ❌ No `null`               |
| **ArrayDeque**    |    ✅ Both Ends    |     ❌ No     |      ✅ Yes      |     ❌ No    |                ❌ No `null`               |
| **HashMap**       |        ❌ No       |     ❌ No     | Keys ❌ Values ✅ |     ❌ No    | ✅ One `null` key, Multiple `null` values |
| **LinkedHashMap** | ✅ Insertion Order |     ❌ No     | Keys ❌ Values ✅ |     ❌ No    | ✅ One `null` key, Multiple `null` values |
| **TreeMap**       |   ✅ Sorted Keys   |     ✅ Yes    | Keys ❌ Values ✅ |     ❌ No    |             ❌ No `null` keys             |
| **Hashtable**     |        ❌ No       |     ❌ No     | Keys ❌ Values ✅ |    ✅ Yes    |        ❌ No `null` keys or values        |

---

# Interview One-Liners

| Collection        | One-Line Description                                                  |
| ----------------- | --------------------------------------------------------------------- |
| **ArrayList**     | Dynamic array with fast random access and ordered storage.            |
| **LinkedList**    | Doubly linked list optimized for insertions and deletions.            |
| **Vector**        | Thread-safe version of `ArrayList`; slower due to synchronization.    |
| **Stack**         | LIFO data structure used for undo operations and recursion.           |
| **HashSet**       | Fastest collection for storing unique elements without order.         |
| **LinkedHashSet** | `HashSet` that maintains insertion order.                             |
| **TreeSet**       | Sorted set implemented using a Red-Black Tree.                        |
| **PriorityQueue** | Processes elements based on priority rather than insertion order.     |
| **ArrayDeque**    | High-performance double-ended queue used as both a queue and a stack. |
| **HashMap**       | Fastest key-value collection with unique keys and unordered storage.  |
| **LinkedHashMap** | `HashMap` that preserves insertion (or access) order.                 |
| **TreeMap**       | Sorted map implemented using a Red-Black Tree.                        |
| **Hashtable**     | Legacy synchronized `Map` that does not allow `null` keys or values.  |

---

# Selection Guide

| Requirement                          | Recommended Collection                  |
| ------------------------------------ | --------------------------------------- |
| Fast random access                   | **ArrayList**                           |
| Frequent insertion/deletion          | **LinkedList**                          |
| Thread-safe List                     | **Vector**                              |
| Stack operations (LIFO)              | **ArrayDeque** (preferred) or **Stack** |
| Unique elements                      | **HashSet**                             |
| Unique elements with insertion order | **LinkedHashSet**                       |
| Unique elements in sorted order      | **TreeSet**                             |
| Priority-based processing            | **PriorityQueue**                       |
| Fast key-value lookup                | **HashMap**                             |
| Ordered key-value storage            | **LinkedHashMap**                       |
| Sorted key-value storage             | **TreeMap**                             |
| Legacy thread-safe map               | **Hashtable**                           |

---

# Memory Trick

* **ArrayList** → **Array = Fast Access**
* **LinkedList** → **Links = Fast Insert/Delete**
* **Vector** → **Synchronized ArrayList**
* **Stack** → **LIFO**
* **HashSet** → **Unique + Unordered**
* **LinkedHashSet** → **Unique + Ordered**
* **TreeSet** → **Unique + Sorted**
* **PriorityQueue** → **Priority First**
* **ArrayDeque** → **Queue + Stack**
* **HashMap** → **Fast Key-Value Store**
* **LinkedHashMap** → **Ordered HashMap**
* **TreeMap** → **Sorted Map**
* **Hashtable** → **Legacy Thread-Safe HashMap**
# Why Collections?

## Without Collections

```java
String name1 = "John";
String name2 = "David";
String name3 = "Tom";
```

## With Collections

```java
import java.util.ArrayList;

public class CollectionsExample {

    public static void main(String[] args) {

        ArrayList<String> names = new ArrayList<>();

        names.add("John");
        names.add("David");
        names.add("Tom");

        System.out.println(names);
    }
}
```

---

# Major Interfaces

| Interface | Allows Duplicates          | Maintains Order | Sorted      |
| --------- | -------------------------- | --------------- | ----------- |
| List      | Yes                        | Yes             | No          |
| Set       | No                         | Depends         | TreeSet Yes |
| Queue     | Yes                        | FIFO            | No          |
| Deque     | Yes                        | Both Ends       | No          |
| Map       | Duplicate Keys Not Allowed | Depends         | TreeMap Yes |

---

# List Interface

## Characteristics

* Ordered
* Index Based
* Allows Duplicate Elements
* Allows Multiple Null Values

---

# ArrayList

## Features

* Dynamic Array
* Fast Random Access
* Slow Insertion in Middle

### Time Complexity

| Operation       | Complexity |
| --------------- | ---------- |
| Add (End)       | O(1)       |
| Get             | O(1)       |
| Remove (Middle) | O(n)       |

## Example

```java
import java.util.ArrayList;

public class ArrayListDemo {

    public static void main(String[] args) {

        ArrayList<String> fruits = new ArrayList<>();

        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Orange");

        System.out.println(fruits);

        fruits.add(1, "Mango");

        System.out.println(fruits);

        fruits.remove("Banana");

        System.out.println(fruits);

        System.out.println(fruits.get(1));

        fruits.set(1, "Pineapple");

        System.out.println(fruits);
    }
}
```

### Output

```text
[Apple, Banana, Orange]
[Apple, Mango, Banana, Orange]
[Apple, Mango, Orange]
Mango
[Apple, Pineapple, Orange]
```

---

# LinkedList

## Features

* Uses Doubly Linked List
* Fast Insertion
* Fast Deletion
* Slow Random Access

## Example

```java
import java.util.LinkedList;

public class LinkedListDemo {

    public static void main(String[] args) {

        LinkedList<String> list = new LinkedList<>();

        list.add("A");
        list.add("B");
        list.add("C");

        list.addFirst("Start");
        list.addLast("End");

        System.out.println(list);

        list.removeFirst();
        list.removeLast();

        System.out.println(list);
    }
}
```

---

# Vector

## Features

* Thread Safe
* Legacy Class
* Slower than ArrayList

## Example

```java
import java.util.Vector;

public class VectorDemo {

    public static void main(String[] args) {

        Vector<Integer> numbers = new Vector<>();

        numbers.add(10);
        numbers.add(20);
        numbers.add(30);

        System.out.println(numbers);
    }
}
```

---

# Stack

## LIFO (Last In First Out)

```java
import java.util.Stack;

public class StackDemo {

    public static void main(String[] args) {

        Stack<String> stack = new Stack<>();

        stack.push("Java");
        stack.push("Python");
        stack.push("Scala");

        System.out.println(stack.pop());

        System.out.println(stack.peek());
    }
}
```

### Output

```text
Scala
Python
```

---

# Set Interface

## Characteristics

* No Duplicate Elements
* No Indexing

---

# HashSet

## Features

* No Order
* Fastest Set Implementation

```java
import java.util.HashSet;

public class HashSetDemo {

    public static void main(String[] args) {

        HashSet<String> cities = new HashSet<>();

        cities.add("Delhi");
        cities.add("Mumbai");
        cities.add("Delhi");

        System.out.println(cities);
    }
}
```

### Possible Output

```text
[Mumbai, Delhi]
```

---

# LinkedHashSet

Maintains insertion order.

```java
import java.util.LinkedHashSet;

public class LinkedHashSetDemo {

    public static void main(String[] args) {

        LinkedHashSet<String> names = new LinkedHashSet<>();

        names.add("A");
        names.add("B");
        names.add("C");

        System.out.println(names);
    }
}
```

### Output

```text
[A, B, C]
```

---

# TreeSet

Stores elements in sorted order.

```java
import java.util.TreeSet;

public class TreeSetDemo {

    public static void main(String[] args) {

        TreeSet<Integer> numbers = new TreeSet<>();

        numbers.add(50);
        numbers.add(20);
        numbers.add(10);
        numbers.add(90);

        System.out.println(numbers);
    }
}
```

### Output

```text
[10, 20, 50, 90]
```

---

# Queue

## FIFO (First In First Out)

```java
import java.util.LinkedList;
import java.util.Queue;

public class QueueDemo {

    public static void main(String[] args) {

        Queue<String> queue = new LinkedList<>();

        queue.offer("One");
        queue.offer("Two");
        queue.offer("Three");

        System.out.println(queue.poll());

        System.out.println(queue.peek());
    }
}
```

### Output

```text
One
Two
```

---

# PriorityQueue

Elements are processed according to priority.

```java
import java.util.PriorityQueue;

public class PriorityQueueDemo {

    public static void main(String[] args) {

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        pq.add(40);
        pq.add(10);
        pq.add(60);
        pq.add(20);

        while (!pq.isEmpty()) {
            System.out.println(pq.poll());
        }
    }
}
```

### Output

```text
10
20
40
60
```

---

# ArrayDeque

Can be used as both Queue and Stack.

```java
import java.util.ArrayDeque;

public class ArrayDequeDemo {

    public static void main(String[] args) {

        ArrayDeque<String> dq = new ArrayDeque<>();

        dq.addFirst("A");
        dq.addLast("B");
        dq.addLast("C");

        System.out.println(dq);

        dq.removeFirst();

        System.out.println(dq);
    }
}
```

---

# Map Interface

Stores data as:

```text
Key → Value
```

* Duplicate Keys → Not Allowed
* Duplicate Values → Allowed

---

# HashMap

```java
import java.util.HashMap;

public class HashMapDemo {

    public static void main(String[] args) {

        HashMap<Integer, String> students = new HashMap<>();

        students.put(101, "John");
        students.put(102, "David");
        students.put(103, "Tom");

        System.out.println(students);

        System.out.println(students.get(102));
    }
}
```

### Output

```text
{101=John, 102=David, 103=Tom}
David
```

---

# LinkedHashMap

Maintains insertion order.

```java
import java.util.LinkedHashMap;

public class LinkedHashMapDemo {

    public static void main(String[] args) {

        LinkedHashMap<Integer, String> map = new LinkedHashMap<>();

        map.put(1, "A");
        map.put(2, "B");
        map.put(3, "C");

        System.out.println(map);
    }
}
```

---

# TreeMap

Stores keys in sorted order.

```java
import java.util.TreeMap;

public class TreeMapDemo {

    public static void main(String[] args) {

        TreeMap<Integer, String> map = new TreeMap<>();

        map.put(50, "Java");
        map.put(10, "Python");
        map.put(30, "Scala");

        System.out.println(map);
    }
}
```

### Output

```text
{10=Python, 30=Scala, 50=Java}
```

---

# Hashtable

Legacy synchronized Map implementation.

```java
import java.util.Hashtable;

public class HashtableDemo {

    public static void main(String[] args) {

        Hashtable<Integer, String> table = new Hashtable<>();

        table.put(1, "Java");
        table.put(2, "Scala");

        System.out.println(table);
    }
}
```

---

# Iterating Collections

## Using For Loop

```java
for (int i = 0; i < list.size(); i++) {
    System.out.println(list.get(i));
}
```

## Enhanced For Loop

```java
for (String s : list) {
    System.out.println(s);
}
```

## Iterator

```java
Iterator<String> iterator = list.iterator();

while (iterator.hasNext()) {
    System.out.println(iterator.next());
}
```

## ListIterator

```java
ListIterator<String> iterator = list.listIterator();

while (iterator.hasNext()) {
    System.out.println(iterator.next());
}

while (iterator.hasPrevious()) {
    System.out.println(iterator.previous());
}
```

## Lambda Expression

```java
list.forEach(System.out::println);
```

---

# Collections Utility Methods

```java
Collections.sort(list);
Collections.reverse(list);
Collections.shuffle(list);
Collections.binarySearch(list, "Apple");
Collections.max(list);
Collections.min(list);
Collections.frequency(list, "Java");
Collections.swap(list, 0, 2);
Collections.fill(list, "Hello");
Collections.copy(destination, source);
```

---

# Comparator Example

```java
import java.util.ArrayList;

class Employee {

    int id;
    String name;

    Employee(int id, String name) {
        this.id = id;
        this.name = name;
    }

    @Override
    public String toString() {
        return id + " " + name;
    }
}

public class ComparatorDemo {

    public static void main(String[] args) {

        ArrayList<Employee> list = new ArrayList<>();

        list.add(new Employee(3, "John"));
        list.add(new Employee(1, "David"));
        list.add(new Employee(2, "Tom"));

        list.sort((a, b) -> a.id - b.id);

        System.out.println(list);
    }
}
```

---

# Comparable Example

```java
import java.util.ArrayList;
import java.util.Collections;

class Student implements Comparable<Student> {

    int id;

    Student(int id) {
        this.id = id;
    }

    @Override
    public int compareTo(Student s) {
        return this.id - s.id;
    }

    @Override
    public String toString() {
        return String.valueOf(id);
    }
}

public class ComparableDemo {

    public static void main(String[] args) {

        ArrayList<Student> list = new ArrayList<>();

        list.add(new Student(30));
        list.add(new Student(10));
        list.add(new Student(20));

        Collections.sort(list);

        System.out.println(list);
    }
}
```

---

# Java 8 Stream Examples

```java
import java.util.Arrays;
import java.util.List;

public class StreamDemo {

    public static void main(String[] args) {

        List<Integer> numbers = Arrays.asList(10, 20, 30, 40);

        numbers.stream()
                .filter(x -> x > 20)
                .forEach(System.out::println);

        numbers.stream()
                .map(x -> x * 2)
                .forEach(System.out::println);

        int sum = numbers.stream()
                .reduce(0, Integer::sum);

        System.out.println("Sum = " + sum);
    }
}
```

---

# Performance Comparison

| Collection    | Search        | Insert       | Delete       | Order           | Duplicates                 |
| ------------- | ------------- | ------------ | ------------ | --------------- | -------------------------- |
| ArrayList     | O(1) by index | O(1) end     | O(n)         | Yes             | Yes                        |
| LinkedList    | O(n)          | O(1) at ends | O(1) at ends | Yes             | Yes                        |
| Vector        | O(1) by index | O(1)         | O(n)         | Yes             | Yes                        |
| Stack         | O(1)          | O(1)         | O(1)         | LIFO            | Yes                        |
| HashSet       | O(1)          | O(1)         | O(1)         | No              | No                         |
| LinkedHashSet | O(1)          | O(1)         | O(1)         | Insertion Order | No                         |
| TreeSet       | O(log n)      | O(log n)     | O(log n)     | Sorted          | No                         |
| PriorityQueue | O(log n)      | O(log n)     | O(log n)     | Priority        | Yes                        |
| ArrayDeque    | O(1)          | O(1)         | O(1)         | Deque           | Yes                        |
| HashMap       | O(1)          | O(1)         | O(1)         | No              | Duplicate Keys Not Allowed |
| LinkedHashMap | O(1)          | O(1)         | O(1)         | Insertion Order | Duplicate Keys Not Allowed |
| TreeMap       | O(log n)      | O(log n)     | O(log n)     | Sorted Keys     | Duplicate Keys Not Allowed |
| Hashtable     | O(1)          | O(1)         | O(1)         | No              | Duplicate Keys Not Allowed |

---

# Interview Questions

1. Why is `ArrayList` faster than `LinkedList` for random access?
2. What is the difference between `ArrayList` and `Vector`?
3. Why does `HashSet` not allow duplicate elements?
4. What is the difference between `HashMap` and `Hashtable`?
5. When should you use `TreeMap` instead of `HashMap`?
6. What is the difference between `Comparable` and `Comparator`?
7. Why is `ArrayDeque` preferred over `Stack`?
8. How does `PriorityQueue` determine element order?
9. What is the average and worst-case time complexity of `HashMap.get()`?
10. What is the difference between fail-fast and fail-safe iterators?

---

# Conclusion

This guide introduces the core concepts of the Java Collection Framework, including interfaces, implementations, traversal techniques, sorting, utility methods, Java 8 Streams, performance comparisons, and interview questions.

For advanced interview preparation, continue with:

* Custom Comparators
* Immutable Collections
* Concurrent Collections (`ConcurrentHashMap`, `CopyOnWriteArrayList`)
* Internal Working of `HashMap`
* Internal Working of `ArrayList`
* Java 9+ Collection Factory Methods (`List.of()`, `Set.of()`, `Map.of()`)
