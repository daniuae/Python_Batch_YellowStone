# Pickling in Python

## Definition

**Pickling** is the process of converting a Python object into a byte stream so that it can be stored in a file, database, or transmitted over a network.

**Unpickling** is the reverse process of converting the byte stream back into the original Python object.

Python provides the built-in `pickle` module for this purpose.

---

# Why Use Pickling?

Consider the following Python object:

```python
employees = {
    "101": "John",
    "102": "Alice",
    "103": "David"
}
```

Without pickling:

* Data exists only while the program is running.
* Once the program terminates, the data is lost.

With pickling:

* Save the object to a file.
* Load it later without recreating it manually.

---

# Basic Example

## Step 1: Save Object (Pickling)

```python
import pickle

employee = {
    "id": 101,
    "name": "John",
    "salary": 50000
}

with open("employee.pkl", "wb") as file:
    pickle.dump(employee, file)

print("Object saved successfully")
```

### Explanation

```python
pickle.dump(object, file)
```

* `dump()` writes the object to a file.
* `wb` means write binary mode.

---

## Step 2: Load Object (Unpickling)

```python
import pickle

with open("employee.pkl", "rb") as file:
    employee = pickle.load(file)

print(employee)
```

### Output

```python
{
    'id': 101,
    'name': 'John',
    'salary': 50000
}
```

### Explanation

```python
pickle.load(file)
```

* Reads binary data from the file.
* Reconstructs the original Python object.

---

# Pickling a List

```python
import pickle

students = ["John", "Alice", "David"]

with open("students.pkl", "wb") as f:
    pickle.dump(students, f)
```

Load the list:

```python
with open("students.pkl", "rb") as f:
    data = pickle.load(f)

print(data)
```

### Output

```python
['John', 'Alice', 'David']
```

---

# Pickling a Custom Class Object

```python
import pickle

class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def display(self):
        print(self.emp_id, self.name)

emp = Employee(101, "John")

with open("emp.pkl", "wb") as f:
    pickle.dump(emp, f)
```

Load the object:

```python
with open("emp.pkl", "rb") as f:
    emp_obj = pickle.load(f)

emp_obj.display()
```

### Output

```python
101 John
```

---

# Illustration

## Before Pickling

```text
Employee Object
   |
   v
+----------------+
| id = 101       |
| name = John    |
+----------------+
```

## After Pickling

```text
Employee Object
      |
      v
pickle.dump()

      |
      v

employee.pkl

101011010101001010...
(Binary Data)
```

## Unpickling

```text
employee.pkl
(Binary Data)

      |
      v

pickle.load()

      |
      v

Employee Object Restored
```

---

# Important Pickle Functions

| Function         | Purpose                      |
| ---------------- | ---------------------------- |
| `pickle.dump()`  | Write object to file         |
| `pickle.load()`  | Read object from file        |
| `pickle.dumps()` | Convert object to bytes      |
| `pickle.loads()` | Convert bytes back to object |

---

# dump() vs dumps()

## dump()

Stores the object directly in a file.

```python
pickle.dump(data, file)
```

## dumps()

Returns a byte stream.

```python
import pickle

data = [1, 2, 3]

binary_data = pickle.dumps(data)

print(binary_data)
```

### Output

```python
b'\x80\x04\x95...'
```

Restore the object:

```python
original = pickle.loads(binary_data)
print(original)
```

### Output

```python
[1, 2, 3]
```

---

# Real-World Use Case

Suppose you train a machine learning model:

```python
import pickle

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
```

Later:

```python
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
```

This avoids retraining the model every time.

---

# Limitations

Pickle is **Python-specific**.

A pickle file created in Python cannot be easily read by:

* Java
* C#
* JavaScript

For cross-platform data exchange, use:

* JSON
* CSV
* XML

---

# Security Warning ⚠️

Never unpickle data from an untrusted source.

Example:

```python
pickle.load(file)
```

A malicious pickle file may execute arbitrary code during unpickling.

### Best Practice

```text
Only unpickle data from trusted sources.
```

---

# Interview Questions

## 1. What is Pickling?

Pickling is the process of converting a Python object into a byte stream for storage or transmission.

---

## 2. What is Unpickling?

Unpickling is the process of converting the byte stream back into the original Python object.

---

## 3. What is the difference between dump() and dumps()?

| dump()                    | dumps()          |
| ------------------------- | ---------------- |
| Writes directly to a file | Returns bytes    |
| Requires a file object    | No file required |

---

## 4. Why do we use binary mode (`wb` and `rb`)?

Pickle stores data as binary bytes rather than text.

---

## 5. Is Pickle secure?

No. Never unpickle data from untrusted sources because it may execute malicious code.

---

# Memory Trick

```text
Pickle   = Object → Bytes

Unpickle = Bytes → Object
```

Think of **pickling** as freezing a Python object to disk and **unpickling** as thawing it back into memory.
