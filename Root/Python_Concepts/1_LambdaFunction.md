# Lambda Function in Python

A **lambda function** is a small anonymous function defined using the `lambda` keyword.

## Syntax

```python
lambda arguments: expression
```

### Key Points

- Can take any number of arguments.
- Contains only **one expression**.
- Automatically returns the result of the expression.
- Often used for short, temporary functions.

---

# Example 1: Simple Lambda Function

```python
square = lambda x: x ** 2

print(square(5))
```

### Output

```python
25
```

### Equivalent Using `def`

```python
def square(x):
    return x ** 2

print(square(5))
```

---

# Example 2: Lambda with Multiple Arguments

```python
add = lambda a, b: a + b

print(add(10, 20))
```

### Output

```python
30
```

### Equivalent Using `def`

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

---

# Example 3: Lambda with `map()`

Apply a function to every element in a list.

```python
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))

print(squares)
```

### Output

```python
[1, 4, 9, 16, 25]
```

---

# Example 4: Lambda with `filter()`

Filter elements based on a condition.

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
```

### Output

```python
[2, 4, 6]
```

---

# Example 5: Lambda with `sorted()`

Sort data using a custom key.

```python
students = [
    ("John", 85),
    ("Alice", 92),
    ("Bob", 78)
]

sorted_students = sorted(
    students,
    key=lambda student: student[1]
)

print(sorted_students)
```

### Output

```python
[
    ('Bob', 78),
    ('John', 85),
    ('Alice', 92)
]
```

---

# Example 6: Lambda in Data Engineering

Suppose we have sales data:

```python
sales = [
    ("Laptop", 50000),
    ("Mouse", 500),
    ("Keyboard", 1500)
]

sales_sorted = sorted(
    sales,
    key=lambda item: item[1],
    reverse=True
)

print(sales_sorted)
```

### Output

```python
[
    ('Laptop', 50000),
    ('Keyboard', 1500),
    ('Mouse', 500)
]
```

---

# Lambda vs Def

| Feature | Lambda | Def |
|----------|---------|------|
| Name Required | No | Yes |
| Number of Expressions | One | Multiple |
| Return Statement | Automatic | Explicit |
| Best For | Small functions | Complex functions |
| Readability | Lower for complex logic | Better |

---

# Easy Way to Remember

Think of Lambda as:

```python
lambda input : output
```

### Examples

```python
lambda x: x * 2
```

**Meaning:**

```python
Input  -> x
Output -> x * 2
```

---

```python
lambda a, b: a + b
```

**Meaning:**

```python
Input  -> a, b
Output -> a + b
```

---

# Real-Life Analogy

Imagine a calculator:

```text
Input: 5
Operation: Square
Output: 25
```

Using lambda:

```python
lambda x: x ** 2
```

You give it an input and immediately get the result without creating a full function.

---

# Interview Questions

### Q1. What is a lambda function?

A lambda function is an anonymous function that can have multiple arguments but only one expression.

### Q2. Can a lambda function contain multiple statements?

No. It can contain only one expression.

### Q3. Why use lambda functions?

They make code shorter and are commonly used with:

- `map()`
- `filter()`
- `sorted()`
- `reduce()`

### Q4. Which is faster: lambda or def?

Performance is nearly the same. Choose based on readability.

---

# Quick Cheat Sheet

```python
# Square
lambda x: x ** 2

# Add two numbers
lambda a, b: a + b

# Check even
lambda x: x % 2 == 0

# Get string length
lambda s: len(s)

# Sort by second column
lambda x: x[1]

# Convert to uppercase
lambda s: s.upper()
```

## Rule of Thumb

Use **lambda** for short, one-line functions.

Use **def** when:
- Logic is complex
- Multiple statements are needed
- The function will be reused multiple times
