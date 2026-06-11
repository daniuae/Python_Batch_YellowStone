# Lab 1: Basic Class Structure and Constructors

## Objective

Learn to create a basic class in Python, define attributes, and initialize them using constructors.

---

# Step 1: Open VS Code

1. Open **Visual Studio Code**.
2. Create a folder named:

```text
basic_class_lab
```

---

# Step 2: Create a Python File

Inside the folder, create a file named:

```text
basic_class.py
```

---

# Step 3: Define a Class

Create a simple class named `Person`.

```python
class Person:
    pass
```

### Explanation

- `class` keyword is used to create a class.
- `Person` is the class name.
- `pass` indicates an empty class.

---

# Step 4: Add a Constructor (__init__)

A constructor initializes object attributes when an object is created.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### Explanation

| Component | Description |
|------------|-------------|
| `__init__()` | Constructor method |
| `self` | Refers to the current object |
| `self.name` | Stores the name attribute |
| `self.age` | Stores the age attribute |

---

# Step 5: Add a Method

Create a method to display person details.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")
```

### Explanation

Methods define the behavior of an object.

---

# Step 6: Create an Object

Instantiate the class.

```python
person1 = Person("Alice", 30)
person1.display_details()
```

### Output

```text
Name: Alice, Age: 30
```

### Explanation

- `Person("Alice", 30)` creates an object.
- Values are assigned through the constructor.
- `display_details()` prints the attributes.

---

# Step 7: Run the Script

Open terminal and execute:

```bash
python basic_class.py
```

---

# Step 8: Add Default Values

Modify the constructor to include default values.

```python
class Person:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")
```

### Why Use Default Values?

Default values allow object creation without passing arguments.

---

# Step 9: Test Default Constructor

```python
person2 = Person()
person2.display_details()
```

### Output

```text
Name: Unknown, Age: 0
```

### Explanation

Since no arguments were provided, Python uses the default values.

---

# Step 10: Add Additional Attributes

Extend the class with a gender attribute.

```python
class Person:
    def __init__(self, name="Unknown", age=0, gender="Not specified"):
        self.name = name
        self.age = age
        self.gender = gender
```

### Explanation

The class now stores:

- Name
- Age
- Gender

---

# Step 11: Display All Attributes

Update the display method.

```python
def display_details(self):
    print(
        f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
    )
```

---

# Step 12: Experiment with Multiple Objects

```python
person3 = Person("Bob", 40, "Male")
person3.display_details()
```

### Output

```text
Name: Bob, Age: 40, Gender: Male
```

### Explanation

Each object maintains its own data.

---

# Step 13: Add Input Validation

Validate the age value.

```python
class Person:
    def __init__(self, name="Unknown", age=0, gender="Not specified"):

        if age < 0:
            raise ValueError("Age cannot be negative")

        self.name = name
        self.age = age
        self.gender = gender
```

### Explanation

Validation prevents invalid object creation.

---

# Step 14: Handle Constructor Exceptions

Use a try-except block.

```python
try:
    person4 = Person("Charlie", -5)
except ValueError as e:
    print(e)
```

### Output

```text
Age cannot be negative
```

### Explanation

- Invalid age raises a `ValueError`.
- Exception is caught and displayed gracefully.

---

# Step 15: Refactor Using main()

Organize code using a main function.

```python
def main():
    person1 = Person("Alice", 30)
    person1.display_details()

if __name__ == "__main__":
    main()
```

### Explanation

| Component | Purpose |
|------------|---------|
| `main()` | Entry point of the program |
| `__name__ == "__main__"` | Ensures code runs only when executed directly |

---

# Complete Program

```python
class Person:

    def __init__(self, name="Unknown", age=0, gender="Not specified"):

        if age < 0:
            raise ValueError("Age cannot be negative")

        self.name = name
        self.age = age
        self.gender = gender

    def display_details(self):
        print(
            f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
        )


def main():

    person1 = Person("Alice", 30, "Female")
    person1.display_details()

    person2 = Person()
    person2.display_details()

    person3 = Person("Bob", 40, "Male")
    person3.display_details()

    try:
        person4 = Person("Charlie", -5)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```

---

# Expected Output

```text
Name: Alice, Age: 30, Gender: Female
Name: Unknown, Age: 0, Gender: Not specified
Name: Bob, Age: 40, Gender: Male
Age cannot be negative
```

---

# Real-World Example

Consider an HR system:

```python
employee = Person(
    name="Rahul",
    age=28,
    gender="Male"
)

employee.display_details()
```

Output:

```text
Name: Rahul, Age: 28, Gender: Male
```

Here, each employee is represented as an object, making the system easier to manage and scale.

---

# Key Concepts Learned

✅ Creating Classes

✅ Creating Objects

✅ Constructors (`__init__`)

✅ Instance Attributes

✅ Methods

✅ Default Parameters

✅ Input Validation

✅ Exception Handling

✅ Multiple Objects

✅ Using `main()` Function

---

# Practice Exercises

### Exercise 1

Create a `Car` class with:

- brand
- model
- year

Display all details.

---

### Exercise 2

Create a `Student` class with:

- name
- roll_number
- marks

Add a method to display student information.

---

### Exercise 3

Add validation to ensure marks cannot be negative.

---

### Exercise 4

Create three student objects and print their details.

---

### Exercise 5

Modify the Student class to include a default grade value.

---
