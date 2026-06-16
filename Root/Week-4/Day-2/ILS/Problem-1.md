# Introduction to Exception Handling in Python

Exception handling is used to prevent a program from crashing when an error occurs. Python provides three main keywords for handling exceptions:

## 1. `try`

The `try` block contains code that might cause an error.

```python
try:
    x = int(input("Enter a number: "))
```

---

## 2. `except`

The `except` block runs only if an error occurs inside the `try` block.

```python
except:
    print("Something went wrong.")
```

---

## 3. `finally`

The `finally` block always runs, whether an error occurs or not.

```python
finally:
    print("This block always runs.")
```

---

# Example Demonstrating `try`, `except`, and `finally`

```python
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except:
    print("An error occurred.")

finally:
    print("End of program.")
```

---

# What This Teaches

- The program does not crash when an error occurs.
- The `except` block catches and handles the error.
- The `finally` block always executes, regardless of whether an error occurred.

## Sample Output

### Valid Input

```text
Enter a number: 10
You entered: 10
End of program.
```

### Invalid Input

```text
Enter a number: abc
An error occurred.
End of program.
```
