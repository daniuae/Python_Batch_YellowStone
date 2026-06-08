# Lists and Tuples in Python

## Learning Objectives

In this lab, you will learn:

* What Lists and Tuples are
* How to create them
* How to access elements
* Common functions and methods
* How to convert between Lists and Tuples

---

# Lists in Python

## What is a List?

A List is a collection that:

* Maintains insertion order
* Is mutable (changeable)
* Can store different data types
* Uses square brackets `[]`

### Create a List

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)
```

**Output**

```python
['apple', 'banana', 'cherry']
```

---

## Accessing List Elements

Lists use zero-based indexing.

```python
fruits = ["apple", "banana", "cherry"]

print("First Fruit:", fruits[0])
print("Second Fruit:", fruits[1])
print("Third Fruit:", fruits[2])
```

**Output**

```python
First Fruit: apple
Second Fruit: banana
Third Fruit: cherry
```

---

## Modifying a List

### Update an Element

```python
fruits = ["apple", "banana", "cherry"]

fruits[1] = "mango"
print(fruits)
```

**Output**

```python
['apple', 'mango', 'cherry']
```

---

### Add Elements

```python
fruits.append("orange")      # Add at the end
fruits.insert(1, "grape")    # Insert at index 1

print(fruits)
```

**Output**

```python
['apple', 'grape', 'mango', 'cherry', 'orange']
```

---

### Remove Elements

```python
fruits.remove("apple")   # Remove by value

removed_item = fruits.pop()  # Remove last item

print("Removed:", removed_item)
print(fruits)
```

**Output**

```python
Removed: orange
['grape', 'mango', 'cherry']
```

---

# Common List Functions

| Function    | Description                        |
| ----------- | ---------------------------------- |
| `len()`     | Returns length                     |
| `append()`  | Adds item at end                   |
| `insert()`  | Inserts item at index              |
| `remove()`  | Removes item by value              |
| `pop()`     | Removes item by index or last item |
| `clear()`   | Removes all items                  |
| `sort()`    | Sorts list                         |
| `reverse()` | Reverses list                      |
| `index()`   | Returns index of item              |
| `count()`   | Counts occurrences                 |
| `copy()`    | Creates a copy                     |
| `max()`     | Returns maximum value              |
| `min()`     | Returns minimum value              |
| `sum()`     | Returns sum of values              |
| `list()`    | Converts iterable to list          |

---

## Demonstration of List Functions

```python
numbers = [10, 5, 20, 5, 8]

print("List:", numbers)
print("Length:", len(numbers))
print("Count of 5:", numbers.count(5))
print("Index of 20:", numbers.index(20))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

numbers_copy = numbers.copy()
print("Copied List:", numbers_copy)

numbers_copy.reverse()
print("Reversed List:", numbers_copy)

numbers_copy.sort()
print("Sorted List:", numbers_copy)
```

**Output**

```python
List: [10, 5, 20, 5, 8]
Length: 5
Count of 5: 2
Index of 20: 2
Maximum: 20
Minimum: 5
Sum: 48
Copied List: [10, 5, 20, 5, 8]
Reversed List: [8, 5, 20, 5, 10]
Sorted List: [5, 5, 8, 10, 20]
```

---

## Clear a List

```python
temp_list = ["a", "b", "c"]

temp_list.clear()

print(temp_list)
```

**Output**

```python
[]
```

---

# Tuples in Python

## What is a Tuple?

A Tuple is a collection that:

* Maintains insertion order
* Is immutable (cannot be changed)
* Uses parentheses `()`

### Create a Tuple

```python
colors = ("red", "green", "blue")

print(colors)
```

**Output**

```python
('red', 'green', 'blue')
```

---

## Access Tuple Elements

```python
colors = ("red", "green", "blue")

print("First Color:", colors[0])
print("Second Color:", colors[1])
print("Third Color:", colors[2])
```

**Output**

```python
First Color: red
Second Color: green
Third Color: blue
```

---

# Common Tuple Functions

| Function   | Description                    |
| ---------- | ------------------------------ |
| `len()`    | Returns length                 |
| `count()`  | Counts occurrences             |
| `index()`  | Returns index of value         |
| `tuple()`  | Converts iterable to tuple     |
| `sorted()` | Returns sorted list from tuple |

---

## Demonstration of Tuple Functions

```python
numbers_tuple = (10, 5, 20, 5)

print("Tuple:", numbers_tuple)
print("Length:", len(numbers_tuple))
print("Count of 5:", numbers_tuple.count(5))
print("Index of 20:", numbers_tuple.index(20))
print("Sorted Version:", sorted(numbers_tuple))
```

**Output**

```python
Tuple: (10, 5, 20, 5)
Length: 4
Count of 5: 2
Index of 20: 2
Sorted Version: [5, 5, 10, 20]
```

---

# Converting Between Lists and Tuples

## List → Tuple

```python
animals_list = ["dog", "cat", "rabbit"]

animals_tuple = tuple(animals_list)

print(animals_tuple)
```

**Output**

```python
('dog', 'cat', 'rabbit')
```

---

## Tuple → List

```python
num_tuple = (1, 2, 3)

num_list = list(num_tuple)

print(num_list)
```

**Output**

```python
[1, 2, 3]
```

---

# List vs Tuple

| Feature          | List | Tuple |
| ---------------- | ---- | ----- |
| Syntax           | `[]` | `()`  |
| Ordered          | ✅    | ✅     |
| Mutable          | ✅    | ❌     |
| Faster           | ❌    | ✅     |
| Memory Efficient | ❌    | ✅     |
| Add/Remove Items | ✅    | ❌     |

---

# Summary

### Lists

* Ordered and mutable
* Can add, update, and remove elements
* Rich set of built-in methods

### Tuples

* Ordered and immutable
* Faster and memory efficient
* Suitable for fixed collections

### Conversion

```python
tuple(my_list)   # List → Tuple
list(my_tuple)   # Tuple → List
```

You have successfully learned:

* Creating Lists and Tuples
* Accessing elements
* Modifying Lists
* Common List and Tuple functions
* Converting between Lists and Tuples
* Differences between Lists and Tuples
