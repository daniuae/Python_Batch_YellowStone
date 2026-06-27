# Java Collections API Deep Dive

## Table of Contents

1. Introduction
2. Collection Framework Hierarchy
3. Core Interfaces
4. List Interface
5. Set Interface
6. Queue Interface
7. Map Interface
8. Iteration Techniques
9. Sorting Collections
10. Utility Methods
11. Immutable Collections
12. Performance Comparison
13. Common Interview Questions
14. Best Practices

---

# 1. What is Java Collections Framework?

The **Java Collections Framework (JCF)** is a set of classes and interfaces that provides ready-made data structures and algorithms.

It helps developers:

- Store objects
- Retrieve objects
- Search objects
- Sort objects
- Update objects
- Remove objects efficiently

Introduced in Java 1.2.

Package:

```java
java.util
```

---

# Collection Hierarchy

```
                 Iterable
                     |
               Collection
      ___________|___________
     |           |           |
    List        Set        Queue
     |           |           |
 ArrayList    HashSet    PriorityQueue
 LinkedList   LinkedHashSet
 Vector       TreeSet

Map (Separate Hierarchy)
|
|-- HashMap
|-- LinkedHashMap
|-- TreeMap
|-- Hashtable
```

---

# Why Collections?

Without Collections:

```java
String name1 = "John";
String name2 = "David";
String name3 = "Alex";
```

With Collections:

```java
List<String> names = new ArrayList<>();
```

Unlimited objects can be stored.

---

# Advantages

- Dynamic size
- Built-in algorithms
- Searching
- Sorting
- Thread-safe collections available
- Generic support
- High performance

---

# Collection Interface

Methods:

```java
add()
remove()
contains()
size()
clear()
isEmpty()
iterator()
```

Example

```java
import java.util.*;

public class CollectionDemo {

    public static void main(String[] args) {

        Collection<String> fruits = new ArrayList<>();

        fruits.add("Apple");
        fruits.add("Orange");
        fruits.add("Banana");

        System.out.println(fruits);
        System.out.println(fruits.size());

        fruits.remove("Orange");

        System.out.println(fruits);
    }
}
```

Output

```
[Apple, Orange, Banana]
3
[Apple, Banana]
```

---

# List Interface

Characteristics

- Ordered
- Duplicate allowed
- Index based

Implementations

- ArrayList
- LinkedList
- Vector
- Stack

---

# ArrayList

Uses dynamic array internally.

Example

```java
import java.util.*;

public class ArrayListDemo {

    public static void main(String[] args) {

        List<String> cities = new ArrayList<>();

        cities.add("London");
        cities.add("Paris");
        cities.add("Tokyo");

        System.out.println(cities);

        System.out.println(cities.get(1));

        cities.set(1, "Berlin");

        System.out.println(cities);

        cities.remove(0);

        System.out.println(cities);
    }
}
```

Output

```
[London, Paris, Tokyo]
Paris
[London, Berlin, Tokyo]
[Berlin, Tokyo]
```

---

# Internal Working of ArrayList

Initially

```
Index

0
1
2
3
4
```

After adding

```
0 -> Apple
1 -> Orange
2 -> Banana
```

When capacity becomes full

```
Old Capacity = 10

New Capacity = 15
```

Formula

```
newCapacity = old + (old/2)
```

---

# LinkedList

Internally uses doubly linked list.

```
Node <-> Node <-> Node
```

Each node contains

```
Previous
Data
Next
```

Example

```java
import java.util.*;

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

        System.out.println(list);
    }
}
```

Output

```
[Start, A, B, C, End]
[A, B, C, End]
```

---

# ArrayList vs LinkedList

| Feature | ArrayList | LinkedList |
|----------|-----------|------------|
| Storage | Array | Doubly Linked List |
| Random Access | Fast O(1) | Slow O(n) |
| Insert Middle | Slow | Fast |
| Memory | Less | More |
| Search | Fast | Slow |

---

# Vector

Thread-safe version of ArrayList.

```java
Vector<Integer> numbers = new Vector<>();

numbers.add(10);
numbers.add(20);
```

---

# Stack

LIFO

```
Push

30
20
10

Pop

30 removed
```

Example

```java
import java.util.*;

public class StackDemo {

    public static void main(String[] args) {

        Stack<String> stack = new Stack<>();

        stack.push("Java");
        stack.push("Python");
        stack.push("Scala");

        System.out.println(stack);

        System.out.println(stack.pop());

        System.out.println(stack.peek());
    }
}
```

Output

```
[Java, Python, Scala]
Scala
Python
```

---

# Set Interface

Properties

- No duplicates
- No index

Implementations

- HashSet
- LinkedHashSet
- TreeSet

---

# HashSet

Uses HashMap internally.

Example

```java
import java.util.*;

public class HashSetDemo {

    public static void main(String[] args) {

        Set<String> set = new HashSet<>();

        set.add("Apple");
        set.add("Orange");
        set.add("Apple");

        System.out.println(set);
    }
}
```

Possible Output

```
[Apple, Orange]
```

Duplicate removed automatically.

---

# LinkedHashSet

Maintains insertion order.

```java
Set<Integer> numbers = new LinkedHashSet<>();

numbers.add(30);
numbers.add(10);
numbers.add(20);

System.out.println(numbers);
```

Output

```
[30, 10, 20]
```

---

# TreeSet

Stores elements in sorted order.

```java
TreeSet<Integer> numbers = new TreeSet<>();

numbers.add(50);
numbers.add(10);
numbers.add(30);

System.out.println(numbers);
```

Output

```
[10, 30, 50]
```

---

# Queue Interface

FIFO

```
Front

10
20
30

Rear
```

Example

```java
import java.util.*;

public class QueueDemo {

    public static void main(String[] args) {

        Queue<String> queue = new LinkedList<>();

        queue.offer("A");
        queue.offer("B");
        queue.offer("C");

        System.out.println(queue);

        System.out.println(queue.poll());

        System.out.println(queue);
    }
}
```

Output

```
[A, B, C]
A
[B, C]
```

---

# PriorityQueue

Stores based on priority.

```java
PriorityQueue<Integer> pq = new PriorityQueue<>();

pq.add(30);
pq.add(5);
pq.add(20);

while(!pq.isEmpty())
    System.out.println(pq.poll());
```

Output

```
5
20
30
```

---

# Map Interface

Stores

```
Key -> Value
```

No duplicate keys.

---

# HashMap

```java
import java.util.*;

public class HashMapDemo {

    public static void main(String[] args) {

        Map<Integer,String> students = new HashMap<>();

        students.put(101,"John");
        students.put(102,"David");
        students.put(103,"Alex");

        System.out.println(students);

        System.out.println(students.get(102));

        students.remove(103);

        System.out.println(students);
    }
}
```

Output

```
{101=John,102=David,103=Alex}
David
{101=John,102=David}
```

---

# LinkedHashMap

Maintains insertion order.

```java
LinkedHashMap<Integer,String> map =
        new LinkedHashMap<>();

map.put(3,"C");
map.put(1,"A");
map.put(2,"B");

System.out.println(map);
```

Output

```
{3=C,1=A,2=B}
```

---

# TreeMap

Automatically sorts keys.

```java
TreeMap<Integer,String> map =
        new TreeMap<>();

map.put(3,"C");
map.put(1,"A");
map.put(2,"B");

System.out.println(map);
```

Output

```
{1=A,2=B,3=C}
```

---

# Hashtable

Thread-safe HashMap.

```java
Hashtable<Integer,String> table =
        new Hashtable<>();

table.put(1,"Java");
table.put(2,"Python");

System.out.println(table);
```

---

# Iterating Collections

## Enhanced for-loop

```java
List<String> list = List.of("Java", "Python", "Scala");

for(String lang : list){
    System.out.println(lang);
}
```

---

## Iterator

```java
Iterator<String> it = list.iterator();

while(it.hasNext()){
    System.out.println(it.next());
}
```

---

## ListIterator

```java
List<String> list =
        new ArrayList<>(List.of("A", "B", "C"));

ListIterator<String> iterator = list.listIterator();

while(iterator.hasNext()){
    System.out.println(iterator.next());
}

while(iterator.hasPrevious()){
    System.out.println(iterator.previous());
}
```

---

# Sorting Collections

```java
List<Integer> numbers =
        new ArrayList<>(List.of(5,2,8,1));

Collections.sort(numbers);

System.out.println(numbers);
```

Output

```
[1,2,5,8]
```

Reverse Order

```java
Collections.sort(numbers,
        Collections.reverseOrder());
```

Output

```
[8,5,2,1]
```

---

# Collections Utility Methods

```java
Collections.max(list);

Collections.min(list);

Collections.reverse(list);

Collections.shuffle(list);

Collections.frequency(list,"Java");

Collections.swap(list,0,2);

Collections.binarySearch(list,20);
```

Example

```java
List<Integer> nums =
        new ArrayList<>(List.of(3, 7, 1, 5));

System.out.println(Collections.max(nums));
System.out.println(Collections.min(nums));

Collections.reverse(nums);
System.out.println(nums);

Collections.shuffle(nums);
System.out.println(nums);
```

---

# Immutable Collections (Java 9+)

```java
List<String> languages =
        List.of("Java","Python","Scala");

System.out.println(languages);

// languages.add("Go"); // UnsupportedOperationException
```

---

# Performance Comparison

| Operation | ArrayList | LinkedList | HashSet | TreeSet | HashMap | TreeMap |
|------------|-----------|------------|----------|----------|----------|----------|
| Add | O(1)* | O(1) | O(1) | O(log n) | O(1) | O(log n) |
| Remove | O(n) | O(1)** | O(1) | O(log n) | O(1) | O(log n) |
| Search | O(n) | O(n) | O(1) | O(log n) | O(1) | O(log n) |
| Get by Index | O(1) | O(n) | N/A | N/A | N/A | N/A |

\* Amortized; resizing occasionally costs O(n).  
\** O(1) when the node reference is already known; finding the node is O(n).

---

# Choosing the Right Collection

| Requirement | Recommended Collection |
|--------------|------------------------|
| Fast random access | ArrayList |
| Frequent insert/delete in middle | LinkedList |
| No duplicates | HashSet |
| Sorted unique elements | TreeSet |
| Key-Value storage | HashMap |
| Sorted keys | TreeMap |
| Preserve insertion order | LinkedHashMap |
| Thread-safe legacy list | Vector |
| LIFO operations | Stack (prefer `Deque` in new code) |
| FIFO operations | Queue / ArrayDeque |

---

# Common Interview Questions

### 1. Difference between List and Set?

| List | Set |
|------|-----|
| Duplicates allowed | No duplicates |
| Ordered | Usually unordered (except LinkedHashSet/TreeSet) |
| Index-based | Not index-based |

---

### 2. HashMap vs Hashtable

| HashMap | Hashtable |
|----------|-----------|
| Not synchronized | Synchronized |
| Allows one null key and multiple null values | No null keys or values |
| Faster | Slower |

---

### 3. HashSet vs TreeSet

| HashSet | TreeSet |
|----------|----------|
| Unordered | Sorted |
| O(1) average operations | O(log n) operations |
| Uses hashing | Uses Red-Black Tree |

---

### 4. ArrayList vs LinkedList

- Use **ArrayList** for frequent reads and random access.
- Use **LinkedList** for frequent insertions and deletions at the ends or when traversing sequentially.

---

### 5. Why Generics?

Without Generics:

```java
List list = new ArrayList();

list.add("Java");
list.add(100);

String s = (String) list.get(1); // ClassCastException
```

With Generics:

```java
List<String> list = new ArrayList<>();

list.add("Java");

// list.add(100); // Compile-time error
```

Generics provide:
- Type safety
- No explicit casting
- Better readability
- Early error detection

---

# Best Practices

- Prefer interfaces (`List`, `Set`, `Map`) over concrete implementations in variable declarations.
- Use `ArrayList` as the default `List` implementation.
- Use `HashMap` for fast key-value lookups.
- Use `LinkedHashMap` when insertion order matters.
- Use `TreeMap` or `TreeSet` when sorted data is required.
- Prefer `ArrayDeque` over the legacy `Stack` class for stack and queue implementations.
- Avoid modifying a collection while iterating over it unless using the iterator's `remove()` method.
- Use immutable collections (`List.of()`, `Set.of()`, `Map.of()`) for read-only data.
- Always use generics to ensure compile-time type safety.

---

# Summary

The Java Collections Framework provides a rich set of interfaces and implementations for managing groups of objects efficiently. Choosing the appropriate collection depends on factors such as ordering, uniqueness, sorting, lookup speed, insertion/deletion patterns, and thread-safety requirements. Understanding the internal working and time complexity of each collection is essential for writing efficient, maintainable, and scalable Java applications.
