# Python Data Structures Lab

## Lists, Tuples, Dictionaries, and Sets

---

# Lab Objective

The objective of this lab is to explore the critical functionality of Lists, Tuples, Dictionaries, and Sets in Python.

Participants will learn how to:

* Create data structures
* Access elements
* Add and remove elements
* Iterate through data structures
* Manipulate data
* Apply these structures in real-world scenarios

By the end of this lab, learners should be able to:

✅ Understand the properties and use cases of Lists, Tuples, Dictionaries, and Sets.

✅ Perform essential operations such as:

* Creation
* Accessing Elements
* Adding Elements
* Removing Elements
* Iteration
* Manipulation

✅ Apply these data structures to solve real-world problems.

---

# Introduction to Data Structures

## Lists

* Ordered collection of items
* Mutable (can be modified)
* Allows duplicate values
* Indexed

### Example

```python
students = ["Alice", "Bob", "Carol"]
```

### Use Cases

* Shopping carts
* Employee lists
* Product catalogs
* Student records

---

## Tuples

* Ordered collection of items
* Immutable (cannot be modified)
* Allows duplicate values
* Indexed

### Example

```python
coordinates = (10, 20)
```

### Use Cases

* Geographic coordinates
* Fixed configurations
* Database records
* Constant values

---

## Dictionaries

* Collection of key-value pairs
* Mutable
* Fast lookup using keys

### Example

```python
student = {
    "name": "Alice",
    "age": 20
}
```

### Use Cases

* Contact books
* Employee records
* API responses
* Configuration settings

---

## Sets

* Unordered collection
* Stores unique values only
* Mutable

### Example

```python
unique_ids = {101, 102, 103}
```

### Use Cases

* Remove duplicates
* Membership testing
* Data validation
* Mathematical set operations

---

# Part 1: Working with Lists

## Step 1: Create File

Create a Python file:

```bash
data_structures_lab.py
```

---

## List Operations Program

```python
# Lists

# Creation
# Using list literals
my_list = [1, 2, 3, 4, 5]

# Using the list() constructor
another_list = list(range(1, 6))

print("Created list:", my_list)
print("Another list:", another_list)

# Accessing Elements
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Slicing
print("Sliced elements:", my_list[1:4])

# Adding Elements
my_list.append(6)
print("After append:", my_list)

my_list.insert(2, 10)
print("After insert:", my_list)

# Removing Elements
my_list.remove(3)
print("After remove:", my_list)

popped_element = my_list.pop()

print("Popped element:", popped_element)
print("After pop:", my_list)

# Iteration using for loop
print("Iterating using for loop:")

for item in my_list:
    print(item)

# List Comprehension
print("Iterating using list comprehension:")

squared_list = [x ** 2 for x in my_list]

print(squared_list)

# Sorting
my_list.sort()

print("Sorted list:", my_list)

# Reversing
my_list.reverse()

print("Reversed list:", my_list)
```

---

## Execute Program

```bash
python data_structures_lab.py
```

---

## Sample Output

```text
Created list: [1, 2, 3, 4, 5]
Another list: [1, 2, 3, 4, 5]

First element: 1
Last element: 5

Sliced elements: [2, 3, 4]

After append: [1, 2, 3, 4, 5, 6]

After insert: [1, 2, 10, 3, 4, 5, 6]

After remove: [1, 2, 10, 4, 5, 6]

Popped element: 6

After pop: [1, 2, 10, 4, 5]

Iterating using for loop:
1
2
10
4
5

Iterating using list comprehension:
[1, 4, 100, 16, 25]

Sorted list: [1, 2, 4, 5, 10]

Reversed list: [10, 5, 4, 2, 1]
```

---

## List Case Study

### Shopping Cart System

```python
cart = ["Laptop", "Mouse", "Keyboard"]

cart.append("Monitor")

cart.remove("Mouse")

print(cart)
```

Output:

```text
['Laptop', 'Keyboard', 'Monitor']
```

---

# Part 2: Working with Tuples

## Step 1: Create File

```bash
tuplesample.py
```

---

## Tuple Operations Program

```python
# Tuples

# Creation
my_tuple = (1, 2, 3, 4, 5)

another_tuple = tuple(range(1, 6))

print("Created tuple:", my_tuple)
print("Another tuple:", another_tuple)

# Accessing Elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Iteration
print("Iterating using for loop:")

for item in my_tuple:
    print(item)
```

---

## Execute Program

```bash
python tuplesample.py
```

---

## Sample Output

```text
Created tuple: (1, 2, 3, 4, 5)

Another tuple: (1, 2, 3, 4, 5)

First element: 1

Last element: 5

Iterating using for loop:
1
2
3
4
5
```

---

## Tuple Case Study

### GPS Coordinates

```python
location = (19.0760, 72.8777)

print("Latitude:", location[0])
print("Longitude:", location[1])
```

Output:

```text
Latitude: 19.0760
Longitude: 72.8777
```

---

# Part 3: Working with Sets

## Step 1: Create File

```bash
setsample.py
```

---

## Set Operations Program

```python
# Sets

# Creation
my_set = {1, 2, 3, 4, 5}

another_set = set(range(1, 6))

print("Created set:", my_set)
print("Another set:", another_set)

# Adding Elements
my_set.add(6)

print("After add:", my_set)

# Removing Elements
my_set.remove(3)

print("After remove:", my_set)

# Iteration
print("Iterating using for loop:")

for item in my_set:
    print(item)

# Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)

print("Union set:", union_set)

intersection_set = set1.intersection(set2)

print("Intersection set:", intersection_set)

difference_set = set1.difference(set2)

print("Difference set:", difference_set)
```

---

## Execute Program

```bash
python setsample.py
```

---

## Sample Output

```text
Created set: {1, 2, 3, 4, 5}

After add: {1, 2, 3, 4, 5, 6}

After remove: {1, 2, 4, 5, 6}

Union set: {1, 2, 3, 4, 5}

Intersection set: {3}

Difference set: {1, 2}
```

---

## Set Case Study

### Remove Duplicate Employee IDs

```python
employee_ids = [101, 102, 103, 101, 102]

unique_ids = set(employee_ids)

print(unique_ids)
```

Output:

```text
{101, 102, 103}
```

---

# Part 4: Working with Dictionaries

## Step 1: Create File

```bash
dictsample.py
```

---

## Dictionary Operations Program

```python
# Dictionaries

# Creation
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

another_dict = dict(
    name='Bob',
    age=25,
    city='Chicago'
)

print("Created dictionary:", my_dict)

print("Another dictionary:", another_dict)

# Accessing Elements
print("Name:", my_dict['name'])

print("Age:", my_dict['age'])

# Adding Elements
my_dict['email'] = 'alice@example.com'

print("After adding email:", my_dict)

# Removing Elements
removed_value = my_dict.pop('age')

print("Removed age:", removed_value)

print("After removing age:", my_dict)

# Iteration using keys
print("Iterating keys:")

for key in my_dict:
    print(key)

# Iteration using values
print("Iterating values:")

for value in my_dict.values():
    print(value)

# Iteration using items
print("Iterating items:")

for key, value in my_dict.items():
    print(key, ":", value)

# Contact Book Example
contact_book = {
    'Alice': {
        'phone': '123-456-7890',
        'email': 'alice@example.com'
    },
    'Bob': {
        'phone': '987-654-3210',
        'email': 'bob@example.com'
    }
}

print("Contact book:", contact_book)
```

---

## Execute Program

```bash
python dictsample.py
```

---

## Sample Output

```text
Created dictionary:
{'name': 'Alice', 'age': 30, 'city': 'New York'}

Name: Alice

Age: 30

After adding email:
{'name': 'Alice', 'age': 30,
 'city': 'New York',
 'email': 'alice@example.com'}

Removed age: 30

After removing age:
{'name': 'Alice',
 'city': 'New York',
 'email': 'alice@example.com'}
```

---

## Dictionary Case Study

### Employee Management System

```python
employee = {
    "emp_id": 1001,
    "name": "Rahul",
    "department": "IT",
    "salary": 75000
}

print(employee["name"])
print(employee["salary"])
```

Output:

```text
Rahul
75000
```

---

# Comparison of Python Data Structures

| Feature            | List | Tuple | Dictionary   | Set |
| ------------------ | ---- | ----- | ------------ | --- |
| Ordered            | Yes  | Yes   | Yes (Py3.7+) | No  |
| Mutable            | Yes  | No    | Yes          | Yes |
| Duplicates Allowed | Yes  | Yes   | Keys No      | No  |
| Indexed            | Yes  | Yes   | By Key       | No  |
| Key-Value Pair     | No   | No    | Yes          | No  |
| Unique Elements    | No   | No    | Keys Unique  | Yes |

---

# Summary

## List

Used when data changes frequently.

Examples:

* Shopping Cart
* Student List
* Product Catalog

---

## Tuple

Used for fixed data.

Examples:

* Coordinates
* Configuration Values
* Database Records

---

## Dictionary

Used for key-value mapping.

Examples:

* Employee Records
* Contact Books
* API Responses

---

## Set

Used for unique values.

Examples:

* Remove Duplicates
* Membership Checking
* Mathematical Set Operations

---

# Lab Outcome

After completing this lab, you should be able to:

✅ Create Lists, Tuples, Dictionaries, and Sets

✅ Access and manipulate elements

✅ Add and remove elements

✅ Iterate through data structures

✅ Apply real-world use cases

✅ Choose the right data structure based on business requirements
