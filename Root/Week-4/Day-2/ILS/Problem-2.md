# Types of Exceptions in Python

## Section 1: Lab Objective

By completing this lab, you will learn:

- What exceptions are
- How different exceptions occur in Python
- How to handle each exception using `try` and `except`
- How to write simple, error-safe programs

---

## Section 2: Common Exception Types

Python has many built-in exception types.

In this lab, you will practice the most common ones:

- `ValueError`
- `ZeroDivisionError`
- `TypeError`
- `IndexError`
- `KeyError`
- `FileNotFoundError`

Each example below shows how the error occurs and how to handle it.

---

## Section 3: Exception Examples

### 1. ValueError

Occurs when converting invalid input to a number.

```python
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Error: Please enter numbers only.")
```

---

### 2. ZeroDivisionError

Occurs when dividing by zero.

```python
try:
    x = int(input("Enter divisor: "))
    result = 10 / x
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
```

---

### 3. TypeError

Occurs when operating on incompatible data types.

```python
try:
    result = "age" + 5
    print(result)

except TypeError:
    print("Error: Cannot add a string and a number.")
```

---

### 4. IndexError

Occurs when accessing an invalid list index.

```python
numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError:
    print("Error: List index out of range.")
```

---

### 5. KeyError

Occurs when trying to access a non-existent dictionary key.

```python
student = {"name": "Alice", "age": 21}

try:
    print(student["grade"])

except KeyError:
    print("Error: Key 'grade' does not exist in the dictionary.")
```

---

### 6. FileNotFoundError

Occurs when trying to open a file that does not exist.

```python
try:
    f = open("missing_file.txt", "r")
    print(f.read())

except FileNotFoundError:
    print("Error: File not found.")
```

---

## Section 4: Combined Exception Handling

You can handle multiple exceptions in one program.

```python
try:
    value = int(input("Enter a number: "))
    result = 100 / value
    print("Result:", result)

except ValueError:
    print("Error: Please enter a valid number.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
```

---

## Summary

| Exception Type | When It Occurs |
|---------------|----------------|
| `ValueError` | Invalid value for a function (e.g., converting text to an integer) |
| `ZeroDivisionError` | Division by zero |
| `TypeError` | Operation on incompatible data types |
| `IndexError` | Invalid list index |
| `KeyError` | Missing dictionary key |
| `FileNotFoundError` | File does not exist |

### Key Takeaways

- Exceptions help prevent program crashes.
- Use `try` to write code that may cause errors.
- Use `except` to handle specific exceptions.
- Different exception types help identify different kinds of errors.
- Handling exceptions makes programs more reliable and user-friendly.
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Error: Please enter numbers only.")


2. ZeroDivisionError
Occurs when dividing by zero.

try:
    x = int(input("Enter divisor: "))
    result = 10 / x
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")


3. TypeError
Occurs when operating on incompatible data types.

try:
    result = "age" + 5
    print(result)
except TypeError:
    print("Error: Cannot add a string and a number.")


4. IndexError
Occurs when accessing an invalid list index.

numbers = [10, 20, 30]

try:
    print(numbers[5])
except IndexError:
    print("Error: List index out of range.")


5. KeyError
Occurs when trying to access a non-existent dictionary key.

student = {"name": "Alice", "age": 21}

try:
    print(student["grade"])
except KeyError:
    print("Error: Key 'grade' does not exist in the dictionary.")


6. FileNotFoundError
Occurs when trying to open a file that doesn’t exist.

try:
    f = open("missing_file.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("Error: File not found.")

Section 4: Combined Exception Handling
You can handle multiple exceptions in one program.

try:
    value = int(input("Enter a number: "))
    result = 100 / value
    print("Result:", result)

except ValueError:
    print("Error: Please enter a valid number.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
