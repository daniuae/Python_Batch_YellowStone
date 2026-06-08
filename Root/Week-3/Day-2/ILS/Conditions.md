# If, Elif, Else in Python

## Section 1: Introduction

Conditional statements allow a program to make decisions.

In Python, the main conditional statements are:

- `if` → Checks the first condition
- `elif` → Checks additional conditions
- `else` → Runs when none of the above conditions are true

---

## Section 2: Basic `if` Statement

The `if` statement runs when its condition is `True`.

### Example

```python
number = 10

if number > 5:
    print("The number is greater than 5.")
```

### Output

```text
The number is greater than 5.
```

### Explanation

- Python checks whether `number > 5`.
- Since `10 > 5` is `True`, the message is printed.

---

## Section 3: `if - else` Statement

The `else` block runs when the `if` condition is `False`.

### Example

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

### Sample Output

```text
Enter your age: 20
You are eligible to vote.
```

### Explanation

- If age is 18 or more, the user can vote.
- Otherwise, the `else` block executes.

---

## Section 4: `if - elif - else`

Use `elif` when you want to check multiple conditions.

Only one block runs—the first condition that evaluates to `True`.

### Example

```python
marks = int(input("Enter your marks (0-100): "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")
```

### Sample Output

```text
Enter your marks (0-100): 82
Grade: B
```

### Explanation

Python checks conditions from top to bottom:

1. Is marks ≥ 90?
2. If not, is marks ≥ 75?
3. If not, is marks ≥ 60?
4. Otherwise, assign Grade D.

---

## Section 5: Checking Even or Odd

This is one of the most common beginner programs.

### Example

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is EVEN.")
else:
    print("The number is ODD.")
```

### Sample Output

```text
Enter a number: 12
The number is EVEN.
```

### Explanation

- `%` is the modulus operator.
- It returns the remainder after division.
- Even numbers leave remainder `0`.

---

## Section 6: Checking Positive, Negative, or Zero

A simple example using `if`, `elif`, and `else`.

### Example

```python
num = float(input("Enter any number: "))

if num > 0:
    print("The number is POSITIVE.")
elif num < 0:
    print("The number is NEGATIVE.")
else:
    print("The number is ZERO.")
```

### Sample Output

```text
Enter any number: -10
The number is NEGATIVE.
```

### Explanation

- Greater than 0 → Positive
- Less than 0 → Negative
- Equal to 0 → Zero

---

## Section 7: Simple String Comparison

Conditional statements can also compare strings.

### Example

```python
city = input("Enter your favorite city: ")

if city == "Paris":
    print("Paris is known as the City of Light.")
elif city == "London":
    print("London is famous for Big Ben.")
else:
    print("That's a wonderful city!")
```

### Sample Output

```text
Enter your favorite city: Paris
Paris is known as the City of Light.
```

### Explanation

- `==` compares string values.
- Python checks if the entered text matches the specified string.

---

## Section 8: Checking Password Match

A simple authentication example.

### Example

```python
password = input("Enter password: ")

if password == "python123":
    print("Access Granted.")
else:
    print("Access Denied.")
```

### Sample Output

```text
Enter password: python123
Access Granted.
```

### Explanation

- The entered password is compared with the expected password.
- If it matches, access is granted.

---

## Section 9: Minimum Interactive Exercise

### Problem Statement

Write a program that:

- Takes a number from the user
- Prints:
  - `"Small Number"` if number < 50
  - `"Medium Number"` if number is between 50 and 100
  - `"Large Number"` if number > 100

### Starter Template

```python
num = int(input("Enter a number: "))

# Write your if, elif, else below:
```

### Solution

```python
num = int(input("Enter a number: "))

if num < 50:
    print("Small Number")
elif num <= 100:
    print("Medium Number")
else:
    print("Large Number")
```

### Sample Output

```text
Enter a number: 75
Medium Number
```

---

# Additional Examples

## Example 1: Largest of Two Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("A is larger")
else:
    print("B is larger")
```

---

## Example 2: Check Divisibility

```python
num = int(input("Enter a number: "))

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")
```

---

## Example 3: Login System

```python
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "admin123":
    print("Login Successful")
else:
    print("Invalid Credentials")
```

---

## Example 4: Traffic Signal Program

```python
signal = input("Enter signal color: ")

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Ready")
elif signal == "green":
    print("Go")
else:
    print("Invalid Signal")
```

---

# Common Comparison Operators

| Operator | Meaning |
|-----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

---

# Common Logical Operators

| Operator | Meaning |
|-----------|---------|
| `and` | Both conditions must be True |
| `or` | At least one condition must be True |
| `not` | Reverses the result |

### Example

```python
age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote")
```

---

# Key Takeaways

✅ `if` checks a condition.

✅ `elif` checks additional conditions.

✅ `else` runs when all previous conditions are false.

✅ Conditions can work with:
- Numbers
- Strings
- Boolean values

✅ Conditional statements help Python programs make decisions.

---

# End of Lab

You learned:

- How to use `if`, `elif`, and `else`
- How Python makes decisions
- How to compare numbers and strings
- How to build simple interactive programs
- How to use logical operators in conditions
