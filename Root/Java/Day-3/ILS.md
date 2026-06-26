# Java Collections Framework - Complete Hands-on Labs

## Lab 1: Why Collections? — Dynamic Data vs Fixed Arrays

### 🎯 Objective

Understand the limitations of Java arrays and learn why the Java Collections Framework exists.

You will learn:

- Arrays have a fixed size.
- Resizing arrays requires copying.
- Collections grow automatically.
- Collections provide built-in algorithms like sorting and reversing.

---

## Step 1: Arrays Hit the Wall

### File: `ArrayLimits.java`

```java
import java.util.Arrays;

public class ArrayLimits {

    public static void main(String[] args) {

        // Fixed-size array
        String[] names = new String[2];

        names[0] = "Asha";
        names[1] = "Ravi";

        // Uncommenting the following line throws
        // ArrayIndexOutOfBoundsException

        // names[2] = "Meera";

        // Manual resizing
        String[] bigger = Arrays.copyOf(names, 3);

        bigger[2] = "Meera";

        System.out.println("Resized Array:");
        System.out.println(Arrays.toString(bigger));
    }
}
```

### Output

```
Resized Array:
[Asha, Ravi, Meera]
```

### Explanation

Arrays have a fixed length.

If you need more space, you must:

1. Create a new array.
2. Copy the old values.
3. Add new values.

This process becomes inefficient when data size changes frequently.

---

## Step 2: Collections Grow Automatically

### File: `CollectionsIntro.java`

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class CollectionsIntro {

    public static void main(String[] args) {

        List<String> names = new ArrayList<>();

        names.add("Asha");
        names.add("Ravi");
        names.add("Meera");

        Collections.sort(names);

        Collections.reverse(names);

        System.out.println(names);
    }
}
```

### Output

```
[Ravi, Meera, Asha]
```

### Explanation

ArrayList grows automatically.

No manual resizing is required.

Collections also provide many utility algorithms like:

- sort()
- reverse()
- shuffle()
- binarySearch()
- max()
- min()

---

## Compile & Run

```bash
javac ArrayLimits.java CollectionsIntro.java

java ArrayLimits

java CollectionsIntro
```

---

## Key Takeaways

| Arrays | Collections |
|---------|-------------|
| Fixed Size | Dynamic Size |
| Manual Resize | Automatic Resize |
| No Built-in Algorithms | Rich Utility Methods |
| Primitive Data Structure | Object-Oriented Framework |

---

# Lab 2: Collections Hierarchy

## 🎯 Objective

Understand the hierarchy of the Java Collections Framework.

There are two major branches:

```
                 Java Collections Framework

                       Iterable
                           |
                     Collection
                  /      |       \
               List     Set     Queue

Map (Separate Hierarchy)
```

Notice:

**Map is NOT part of the Collection interface.**

---

## Step 1: Program to Interfaces

### File: `HierarchySketch.java`

```java
import java.util.*;

public class HierarchySketch {

    public static void main(String[] args) {

        List<String> list = new ArrayList<>();

        Set<String> set = new HashSet<>();

        Map<String, Integer> map = new HashMap<>();

        list.add("A");
        list.add("B");
        list.add("A");

        set.add("A");
        set.add("B");
        set.add("A");

        map.put("A", 1);
        map.put("A", 2);

        System.out.println("List : " + list);
        System.out.println("Set  : " + set);
        System.out.println("Map  : " + map);
    }
}
```

### Output

```
List : [A, B, A]

Set : [A, B]

Map : {A=2}
```

### Explanation

**List**

- Ordered
- Allows duplicates

**Set**

- No duplicates
- Ordering depends on implementation

**Map**

- Key → Value pairs
- Keys must be unique
- Duplicate keys overwrite existing values

---

## Key Takeaways

Always program to interfaces:

```java
List<String> list = new ArrayList<>();

Set<String> set = new HashSet<>();

Map<String, Integer> map = new HashMap<>();
```

This makes your code flexible.

---

# Lab 3: List vs Set vs Map

## 🎯 Objective

Compare List, Set, and Map based on:

- Ordering
- Duplicate handling
- Access mechanism

### List

```java
List<String> names = new ArrayList<>(
        List.of("Asha", "Ravi", "Asha")
);

System.out.println(names);
System.out.println(names.get(1));
```

Output

```
[Asha, Ravi, Asha]

Ravi
```

### Set

```java
Set<String> ids = new HashSet<>(
        List.of("X1", "X2", "X1")
);

System.out.println(ids);
```

Output

```
[X1, X2]
```

### TreeSet

```java
Set<String> sorted = new TreeSet<>(
        List.of("b","a","c","a")
);

System.out.println(sorted);
```

Output

```
[a, b, c]
```

### Map

```java
Map<String,Integer> marks = new HashMap<>();

marks.put("Rahul",85);
marks.put("Rahul",92);

marks.put("Kavya",92);

System.out.println(marks);
System.out.println(marks.get("Rahul"));
```

Output

```
{Rahul=92, Kavya=92}

92
```

---

## Summary Table

| Feature | List | Set | Map |
|----------|------|-----|-----|
| Ordered | Yes | Depends | Depends |
| Duplicates | Yes | No | Keys No |
| Index Access | Yes | No | No |
| Key Lookup | No | No | Yes |

---

*Continue with Labs 4–7 following the same structure, including objectives, executable code, sample output, detailed explanations, performance notes, and interview tips.*
