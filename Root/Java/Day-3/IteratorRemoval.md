# Iterator Remove Example (Proper Executable Java Program)

## Objective

This example demonstrates the **correct way to remove elements from a collection while iterating**. Removing elements directly inside an enhanced `for` loop causes a `ConcurrentModificationException`. The correct approach is to use the `Iterator.remove()` method.

---

## File Name

```text
IteratorRemoveDemo.java
```

---

## Source Code

```java
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class IteratorRemoveDemo {

    public static void main(String[] args) {

        // Create and initialize the list
        List<String> words = new ArrayList<>();

        words.add("apple");
        words.add("banana");
        words.add("cherry");
        words.add("date");

        System.out.println("Original List:");
        System.out.println(words);

        // Correct way to remove elements while iterating
        Iterator<String> iterator = words.iterator();

        while (iterator.hasNext()) {

            String word = iterator.next();

            if (word.startsWith("c")) {
                iterator.remove();   // Safe removal
            }
        }

        System.out.println("\nAfter Removing Words Starting With 'c':");
        System.out.println(words);
    }
}
```

---

## Compile

```bash
javac IteratorRemoveDemo.java
```

---

## Run

```bash
java IteratorRemoveDemo
```

---

## Output

```text
Original List:
[apple, banana, cherry, date]

After Removing Words Starting With 'c':
[apple, banana, date]
```

---

# Incorrect Approach (Do NOT Use)

The following code throws a **ConcurrentModificationException** because the collection is modified while it is being traversed using an enhanced `for` loop.

```java
for (String word : words) {

    if (word.startsWith("c")) {
        words.remove(word);   // ❌ Wrong
    }
}
```

---

# Why Does It Fail?

* The enhanced `for` loop internally uses an `Iterator`.
* Directly modifying the collection using `add()` or `remove()` changes its structure.
* The iterator detects this structural modification and throws a **ConcurrentModificationException**.

---

# Correct Approach

Always remove elements using the iterator itself.

```java
Iterator<String> iterator = words.iterator();

while (iterator.hasNext()) {

    String word = iterator.next();

    if (word.startsWith("c")) {
        iterator.remove();   // ✅ Safe
    }
}
```

---

# Time Complexity

| Operation | Complexity                      |
| --------- | ------------------------------- |
| Traversal | **O(n)**                        |
| Removal   | **O(1)** (per iterator removal) |
| Overall   | **O(n)**                        |

---

# Interview Tip

> **Question:** Why does `ConcurrentModificationException` occur?

**Answer:**
It occurs when a collection is structurally modified while it is being iterated using an iterator, except through the iterator's own `remove()` method. To safely remove elements during iteration, always use `Iterator.remove()` instead of calling `Collection.remove()` directly.

---

# Key Takeaways

* ✔ Use `Iterator` when removing elements during iteration.
* ✔ Call `iterator.remove()` instead of `list.remove()`.
* ✔ Avoid modifying a collection inside an enhanced `for` loop.
* ✔ This is a common Java interview question related to fail-fast iterators.
