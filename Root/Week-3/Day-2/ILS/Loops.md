# Introduction to Python Loops and Controls: `for`, `while`, `break`, `continue`, `pass`

## 1. Introduction

Loops allow code to execute repeatedly.

Python provides two main loop types:

- `for` loop → Iterates over a sequence
- `while` loop → Repeats while a condition is `True`

---

## 2. Basic `for` Loop

### Example

```python
for i in range(5):
    print("Current number is:", i)
```

### Output

```text
Current number is: 0
Current number is: 1
Current number is: 2
Current number is: 3
Current number is: 4
```

### Explanation

- `range(5)` generates numbers from `0` to `4`
- The loop executes once for each value

---

## 3. `for` Loop with `if-else`

### Example

```python
for num in range(5):
    if num == 3:
        print(num, "is special!")
    else:
        print(num, "is normal.")
```

### Output

```text
0 is normal.
1 is normal.
2 is normal.
3 is special!
4 is normal.
```

### Explanation

- Each number is checked
- When the number equals `3`, a special message is displayed

---

## 4. Basic `while` Loop

### Example

```python
count = 1

while count <= 5:
    print("Count is:", count)
    count += 1
```

### Output

```text
Count is: 1
Count is: 2
Count is: 3
Count is: 4
Count is: 5
```

### Explanation

- Starts from `1`
- Continues until `count` becomes greater than `5`

---

## 5. `while` Loop with `if-else`

### Example

```python
x = 1

while x <= 5:
    if x == 3:
        print("Reached the number 3!")
    else:
        print("Number is:", x)

    x += 1
```

### Output

```text
Number is: 1
Number is: 2
Reached the number 3!
Number is: 4
Number is: 5
```

### Explanation

- Prints a special message when `x == 3`
- Otherwise prints the current value

---

## 6. Using `break`

`break` immediately exits the loop.

### Example

```python
for i in range(10):
    if i == 5:
        break

    print("i is:", i)
```

### Output

```text
i is: 0
i is: 1
i is: 2
i is: 3
i is: 4
```

### Explanation

- Loop stops as soon as `i` becomes `5`

---

## 7. Using `continue`

`continue` skips the current iteration.

### Example

```python
for i in range(6):
    if i == 3:
        continue

    print("i is:", i)
```

### Output

```text
i is: 0
i is: 1
i is: 2
i is: 4
i is: 5
```

### Explanation

- When `i == 3`, the remaining code in that iteration is skipped

---

## 8. Using `pass`

`pass` is a placeholder statement that performs no action.

### Example

```python
for i in range(5):
    if i == 2:
        pass

    print("i is:", i)
```

### Output

```text
i is: 0
i is: 1
i is: 2
i is: 3
i is: 4
```

### Explanation

- `pass` does nothing
- Useful when code is required syntactically but not yet implemented

---

## 9. Comparison Table

| Statement | Purpose |
|------------|----------|
| `for` | Iterate through a sequence |
| `while` | Repeat while condition is true |
| `break` | Exit the loop immediately |
| `continue` | Skip current iteration |
| `pass` | Placeholder; performs no action |

---

## 10. Practice Exercise

### Problem

Write a program that:

1. Accepts a number from the user
2. Prints numbers from `1` to that number
3. Skips printing `5` using `continue`
4. Stops completely when the number reaches `10` using `break`

### Solution

```python
limit = int(input("Enter a number: "))

for i in range(1, limit + 1):

    if i == 5:
        continue

    if i == 10:
        break

    print(i)
```

### Sample Input

```text
15
```

### Output

```text
1
2
3
4
6
7
8
9
```

---

## Key Takeaways

✅ Use `for` when iterating over a sequence  
✅ Use `while` when repetition depends on a condition  
✅ `break` stops a loop immediately  
✅ `continue` skips the current iteration  
✅ `pass` acts as a placeholder for future code  
✅ Loops can be combined with `if-else` to create powerful logic

---
**Next Topics:** Nested Loops • Loop Else Clause • Enumerate • Zip • Iterators • Generators
