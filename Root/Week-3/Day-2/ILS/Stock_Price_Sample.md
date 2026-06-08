# Stock Price Case Study

## Section 1: Introduction

A **list** in Python is a collection that can hold multiple values in a single variable.

### Important Points About Lists

- Lists are **ordered**
- Lists are **changeable** (you can add, remove, or modify elements)
- Lists use square brackets `[]`
- Lists can store different types of data (numbers, strings, etc.)

In this lab, we will learn lists through a simple **stock market example**.

---

## Section 2: Creating a List (Stock Prices)

Here we create a list of stock prices for a company over five days.

### Example

```python
stock_prices = [150.25, 152.30, 148.90, 155.00, 157.45]

print("Stock Prices:", stock_prices)
```

### Sample Output

```text
Stock Prices: [150.25, 152.3, 148.9, 155.0, 157.45]
```

### Explanation

We created a list called `stock_prices` that stores the stock price for each day.

---

## Section 3: Accessing List Elements

We can retrieve values using their index.

> Indexing starts at `0`.

### Example

```python
print("Price on Day 1:", stock_prices[0])
print("Price on Day 3:", stock_prices[2])
print("Price on Day 5:", stock_prices[4])
```

### Sample Output

```text
Price on Day 1: 150.25
Price on Day 3: 148.9
Price on Day 5: 157.45
```

### Explanation

We access values using:

```python
list[index]
```

For example:

- Index `0` → First item
- Index `1` → Second item
- Index `2` → Third item

---

## Section 4: Modifying a List

Example: Updating the stock price on Day 3.

### Example

```python
stock_prices[2] = 149.50
print("Updated Prices:", stock_prices)
```

### Sample Output

```text
Updated Prices: [150.25, 152.3, 149.5, 155.0, 157.45]
```

### Explanation

We replaced the old Day 3 price (`148.90`) with the new value (`149.50`).

---

## Section 5: Adding Items to a List

We can add more stock prices using `append()`.

### Example

```python
stock_prices.append(160.10)
print("After Adding New Price:", stock_prices)
```

### Sample Output

```text
After Adding New Price: [150.25, 152.3, 149.5, 155.0, 157.45, 160.1]
```

### Explanation

```python
append()
```

adds a new value at the end of the list.

---

## Section 6: Removing Items From a List

We can remove stock prices using `remove()`.

### Example

```python
stock_prices.remove(152.30)
print("After Removing 152.30:", stock_prices)
```

### Sample Output

```text
After Removing 152.30: [150.25, 149.5, 155.0, 157.45, 160.1]
```

### Explanation

```python
remove(value)
```

deletes the first matching value from the list.

---

## Section 7: Basic List Functions (Length, Max, Min)

### Example

```python
print("Number of Price Records:", len(stock_prices))
print("Highest Price:", max(stock_prices))
print("Lowest Price:", min(stock_prices))
```

### Sample Output

```text
Number of Price Records: 5
Highest Price: 160.1
Lowest Price: 149.5
```

### Explanation

| Function | Purpose |
|----------|----------|
| `len()` | Returns the number of items |
| `max()` | Returns the highest value |
| `min()` | Returns the lowest value |

---

## Section 8: Counting and Finding Index

### Example

```python
print("Count of 155.00:", stock_prices.count(155.00))
print("Index of 157.45:", stock_prices.index(157.45))
```

### Sample Output

```text
Count of 155.00: 1
Index of 157.45: 3
```

### Explanation

| Function | Purpose |
|----------|----------|
| `count(x)` | Counts how many times `x` appears |
| `index(x)` | Returns the position of `x` |

---

## Section 9: Sorting and Reversing Lists

### Sorting the Stock Prices

```python
sorted_prices = sorted(stock_prices)
print("Sorted Prices:", sorted_prices)
```

### Sample Output

```text
Sorted Prices: [149.5, 150.25, 155.0, 157.45, 160.1]
```

### Reversing the List

```python
reversed_prices = list(reversed(stock_prices))
print("Reversed Prices:", reversed_prices)
```

### Sample Output

```text
Reversed Prices: [160.1, 157.45, 155.0, 149.5, 150.25]
```

### Explanation

| Function | Purpose |
|----------|----------|
| `sorted()` | Returns a new sorted list |
| `reversed()` | Returns items from last to first |

---

## Section 10: Practice Exercise

### Problem Statement

Write a program that:

1. Creates a list of 5 stock prices
2. Prints:
   - The highest price
   - The lowest price
   - The total number of prices
3. Updates the last price with a new value
4. Prints the updated list

### Starter Template

```python
stock_prices = [___, ___, ___, ___, ___]

# Print highest and lowest price

# Update last price

# Print updated list
```

---

## Challenge Exercise

Write a program that:

- Accepts 5 stock prices from the user
- Stores them in a list
- Displays:
  - Highest price
  - Lowest price
  - Average price
- Sorts the prices in ascending order
- Displays the sorted list

### Solution

```python
stock_prices = []

for i in range(5):
    price = float(input(f"Enter stock price {i+1}: "))
    stock_prices.append(price)

print("Highest Price:", max(stock_prices))
print("Lowest Price:", min(stock_prices))
print("Average Price:", sum(stock_prices) / len(stock_prices))

print("Sorted Prices:", sorted(stock_prices))
```

---

# End of Lab

## You Learned

✅ How to create a list

✅ How to access and modify list values

✅ How to add and remove items

✅ Basic list functions:
- `len()`
- `max()`
- `min()`
- `count()`
- `index()`

✅ How to sort and reverse a list

✅ How lists help in real-world scenarios such as tracking stock prices

---

## Key Takeaway

Lists are one of the most important data structures in Python. They allow us to store and manage collections of related data efficiently, making them ideal for real-world applications such as:

- Stock Market Analysis
- Student Marks Management
- Employee Records
- Sales Tracking
- Inventory Management
- Data Analytics
