# Introduction to Python Dictionaries

---

# Section 1: Introduction

A **Dictionary** in Python stores data as **key-value pairs**.

## Important Points

* Uses curly braces `{ }`
* Data is stored as `key : value`
* Keys must be unique
* Values can be:

  * Numbers
  * Strings
  * Lists
  * Tuples
  * Sets
  * Other Dictionaries
* Dictionaries are ideal for storing structured data such as:

  * Employee Records
  * Student Information
  * Product Catalogs
  * API Responses

---

## Dictionary Syntax

```python
dictionary_name = {
    "key1": value1,
    "key2": value2
}
```

### Example

```python
student = {
    "id": 101,
    "name": "Alice",
    "course": "Python"
}
```

---

# Section 2: Creating a Dictionary (Employee Details Example)

```python
employee = {
    "id": 101,
    "name": "John Doe",
    "department": "IT",
    "salary": 55000
}

print("Employee Dictionary:", employee)
```

## Sample Output

```text
Employee Dictionary:
{'id': 101, 'name': 'John Doe', 'department': 'IT', 'salary': 55000}
```

## Explanation

We created a dictionary storing an employee's:

* Employee ID
* Name
* Department
* Salary

Each piece of information is stored as a key-value pair.

---

# Section 3: Accessing Dictionary Values

Values can be accessed using their keys.

```python
print("Employee Name:", employee["name"])
print("Department:", employee["department"])
```

## Sample Output

```text
Employee Name: John Doe
Department: IT
```

## Explanation

The syntax is:

```python
dictionary[key]
```

Example:

```python
employee["name"]
```

returns:

```text
John Doe
```

---

# Section 4: Updating Values

Dictionary values can be modified using their keys.

```python
employee["salary"] = 60000

print("Updated Salary:", employee)
```

## Sample Output

```text
Updated Salary:
{'id': 101,
 'name': 'John Doe',
 'department': 'IT',
 'salary': 60000}
```

## Explanation

The old salary value:

```text
55000
```

is replaced with:

```text
60000
```

---

# Section 5: Adding a New Key-Value Pair

New entries can be added by assigning a value to a new key.

```python
employee["location"] = "New York"

print("After Adding Location:", employee)
```

## Sample Output

```text
After Adding Location:
{'id': 101,
 'name': 'John Doe',
 'department': 'IT',
 'salary': 60000,
 'location': 'New York'}
```

## Explanation

Since the key `"location"` did not exist, Python created it automatically.

---

# Section 6: Removing an Item (pop)

## Method 1: `pop()`

Removes a specific key and returns its value.

```python
removed = employee.pop("department")

print("Removed:", removed)
print(employee)
```

## Sample Output

```text
Removed: IT

{'id': 101,
 'name': 'John Doe',
 'salary': 60000,
 'location': 'New York'}
```

## Explanation

* `"department"` key is removed.
* Its value `"IT"` is returned.

---

# Section 7: Removing Last Inserted Item (popitem)

## Method 2: `popitem()`

Removes the last inserted key-value pair.

```python
last_removed = employee.popitem()

print("Removed last item:", last_removed)
print(employee)
```

## Sample Output

```text
Removed last item:
('location', 'New York')

{'id': 101,
 'name': 'John Doe',
 'salary': 60000}
```

## Explanation

Since `"location"` was added last, it gets removed.

---

# Section 8: Checking Key Existence (in)

## Method 3: `in` Operator

Checks whether a key exists.

```python
print("Is 'salary' present?", "salary" in employee)

print("Is 'department' present?",
      "department" in employee)
```

## Sample Output

```text
Is 'salary' present? True
Is 'department' present? False
```

## Explanation

Useful for avoiding errors before accessing keys.

---

# Section 9: Getting All Keys

## Method 4: `keys()`

Returns all dictionary keys.

```python
print("Keys:", employee.keys())
```

## Sample Output

```text
Keys:
dict_keys(['id', 'name', 'salary'])
```

## Explanation

Used when you only need the keys.

---

# Section 10: Getting All Values

## Method 5: `values()`

Returns all dictionary values.

```python
print("Values:", employee.values())
```

## Sample Output

```text
Values:
dict_values([101, 'John Doe', 60000])
```

## Explanation

Used when only values are required.

---

# Section 11: Getting Key-Value Pairs

## Method 6: `items()`

Returns keys and values together.

```python
print("Items:", employee.items())
```

## Sample Output

```text
Items:
dict_items([
('id', 101),
('name', 'John Doe'),
('salary', 60000)
])
```

## Explanation

Useful when iterating through both keys and values.

---

# Section 12: Using get() to Access Values Safely

## Method 7: `get()`

Accesses values safely.

```python
print("Salary using get:",
      employee.get("salary"))

print("Department using get:",
      employee.get("department"))
```

## Sample Output

```text
Salary using get: 60000
Department using get: None
```

## Explanation

### Using Square Brackets

```python
employee["department"]
```

Produces:

```python
KeyError
```

if the key is missing.

### Using get()

```python
employee.get("department")
```

Returns:

```text
None
```

without raising an error.

---

# Section 13: Clearing All Items

## Method 8: `clear()`

Removes all items from a dictionary.

```python
temp_emp = {
    "role": "Engineer",
    "level": 2
}

temp_emp.clear()

print("After clear:", temp_emp)
```

## Sample Output

```text
After clear:
{}
```

## Explanation

The dictionary becomes empty.

---

# Section 14: Copying a Dictionary

## Method 9: `copy()`

Creates a shallow copy.

```python
employee_copy = employee.copy()

print("Copied Employee:",
      employee_copy)
```

## Sample Output

```text
Copied Employee:
{'id': 101,
 'name': 'John Doe',
 'salary': 60000}
```

## Explanation

Changes to one dictionary will not affect the other.

---

# Section 15: Updating a Dictionary

## Method 10: `update()`

Updates existing keys and adds new keys.

```python
employee.update({
    "salary": 65000,
    "department": "HR"
})

print("Updated Employee:",
      employee)
```

## Sample Output

```text
Updated Employee:

{'id': 101,
 'name': 'John Doe',
 'salary': 65000,
 'department': 'HR'}
```

## Explanation

* Salary is modified from `60000` to `65000`
* Department is added back

---

# Complete Dictionary Methods Summary

| Method      | Purpose                   |
| ----------- | ------------------------- |
| `get()`     | Safely access values      |
| `keys()`    | Return all keys           |
| `values()`  | Return all values         |
| `items()`   | Return key-value pairs    |
| `update()`  | Update dictionary         |
| `pop()`     | Remove specific key       |
| `popitem()` | Remove last inserted item |
| `copy()`    | Create a copy             |
| `clear()`   | Remove all items          |
| `in`        | Check key existence       |

---

# Real-World Case Study: Employee Management System

```python
employee = {
    "id": 101,
    "name": "John Doe",
    "department": "IT",
    "salary": 55000
}

employee["salary"] = 60000

employee["location"] = "New York"

if "department" in employee:
    print("Department:",
          employee["department"])

employee.update({
    "designation": "Senior Engineer"
})

print(employee)
```

## Output

```text
{
 'id': 101,
 'name': 'John Doe',
 'department': 'IT',
 'salary': 60000,
 'location': 'New York',
 'designation': 'Senior Engineer'
}
```

---

# Dictionary vs List

| Feature        | Dictionary      | List            |
| -------------- | --------------- | --------------- |
| Storage        | Key-Value Pairs | Values Only     |
| Access Speed   | Fast using Keys | By Index        |
| Mutable        | Yes             | Yes             |
| Duplicate Keys | Not Allowed     | Values Allowed  |
| Best For       | Structured Data | Sequential Data |

---

# Key Takeaways

✅ Dictionaries store data as key-value pairs

✅ Keys must be unique

✅ Values can be any Python object

✅ Dictionaries are mutable

✅ Common methods include:

* `get()`
* `keys()`
* `values()`
* `items()`
* `update()`
* `pop()`
* `copy()`
* `clear()`

✅ Dictionaries are widely used in:

* Employee Management Systems
* Student Databases
* Configuration Files
* JSON Data
* API Responses
* Contact Management Systems
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
