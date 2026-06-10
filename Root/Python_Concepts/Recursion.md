# Recursion in Python

## What is Recursion?

**Recursion** is a programming technique where a function calls itself to solve a smaller version of the same problem.

Instead of using loops (`for` or `while`), recursion repeatedly calls the same function until a stopping condition is met.

---

## Real-Life Example

Imagine standing between two mirrors.

The image keeps repeating itself again and again until it becomes too small to see.

Recursion works in a similar way:

- A function calls itself.
- The problem becomes smaller each time.
- Eventually, a stopping condition ends the process.

---

## Components of Recursion

Every recursive function must have:

### 1. Base Case

The condition that stops the recursion.

Without a base case, the function will call itself forever.

### 2. Recursive Case

The part where the function calls itself.

---

## Syntax

```python
def function_name():
    if base_condition:
        return value

    return function_name()
```

---

# Example 1: Print Numbers from 1 to 5

```python
def print_numbers(n):

    if n == 6:
        return

    print(n)

    print_numbers(n + 1)

print_numbers(1)
```

### Output

```text
1
2
3
4
5
```

### How it Works

```text
print_numbers(1)
    ↓
print_numbers(2)
    ↓
print_numbers(3)
    ↓
print_numbers(4)
    ↓
print_numbers(5)
    ↓
print_numbers(6) ← Base Case
```

---

# Example 2: Factorial Using Recursion

## Mathematical Formula

```text
5! = 5 × 4 × 3 × 2 × 1
```

```text
5! = 5 × 4!
4! = 4 × 3!
3! = 3 × 2!
2! = 2 × 1!
1! = 1
```

### Code

```python
def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

### Output

```text
120
```

### Function Calls

```text
factorial(5)
    ↓
5 * factorial(4)
    ↓
5 * 4 * factorial(3)
    ↓
5 * 4 * 3 * factorial(2)
    ↓
5 * 4 * 3 * 2 * factorial(1)
    ↓
5 * 4 * 3 * 2 * 1
    ↓
120
```

---

# Example 3: Sum of Numbers

Find:

```text
1 + 2 + 3 + 4 + 5
```

### Code

```python
def sum_numbers(n):

    if n == 1:
        return 1

    return n + sum_numbers(n - 1)

print(sum_numbers(5))
```

### Output

```text
15
```

### Flow

```text
sum_numbers(5)

5 + sum_numbers(4)
4 + sum_numbers(3)
3 + sum_numbers(2)
2 + sum_numbers(1)

5 + 4 + 3 + 2 + 1

15
```

---

# Example 4: Fibonacci Series

### Formula

```text
F(n) = F(n-1) + F(n-2)
```

### Sequence

```text
0 1 1 2 3 5 8 13 ...
```

### Code

```python
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(8):
    print(fibonacci(i), end=" ")
```

### Output

```text
0 1 1 2 3 5 8 13
```

---

# Example 5: Reverse a String

### Code

```python
def reverse_string(text):

    if len(text) == 0:
        return ""

    return text[-1] + reverse_string(text[:-1])

print(reverse_string("Python"))
```

### Output

```text
nohtyP
```

---

# Call Stack Visualization

Example:

```python
factorial(3)
```

### Stack Building

```text
factorial(3)
factorial(2)
factorial(1)
```

### Stack Unwinding

```text
factorial(1) = 1

factorial(2)
= 2 × 1
= 2

factorial(3)
= 3 × 2
= 6
```

---

# Advantages of Recursion

✅ Simple and elegant code

✅ Useful for tree structures

✅ Useful for divide-and-conquer algorithms

✅ Easier to solve mathematical problems

---

# Disadvantages of Recursion

❌ More memory usage

❌ Slower than loops for simple tasks

❌ Can cause stack overflow if recursion is too deep

---

# Recursion vs Loop

| Feature | Recursion | Loop |
|----------|------------|--------|
| Uses Function Calls | Yes | No |
| Uses Stack Memory | Yes | No |
| Easy for Tree Problems | Yes | No |
| Faster | No | Yes |
| Readability | Often Better | Sometimes Complex |

---

# Common Interview Questions

### 1. What is recursion?

A function calling itself to solve a smaller version of the same problem.

---

### 2. What is a base case?

The stopping condition that prevents infinite recursion.

---

### 3. What happens without a base case?

The function keeps calling itself until a `RecursionError` occurs.

Example:

```python
def hello():
    hello()

hello()
```

Output:

```text
RecursionError: maximum recursion depth exceeded
```

---

### 4. When should recursion be used?

- Factorial
- Fibonacci
- Tree Traversal
- Graph Traversal
- Divide and Conquer Algorithms
- Backtracking Problems

---

# Easy Way to Remember

Think of recursion as:

```text
1. Solve a small part.
2. Ask the same function to solve the remaining part.
3. Stop when the problem becomes very small.
```

### Formula

```text
Recursion = Base Case + Function Calling Itself
```

Example:

```python
def recursion(problem):

    if small_problem:
        return answer

    return recursion(smaller_problem)
```
