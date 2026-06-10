# 📈 Case Study – Stock Portfolio Manager

---

# Section 1: Introduction

In this case study, you will apply the following Python concepts:

- Creating and calling functions
- Using `if`, `elif`, and `else`
- Using loops
- List operations (`add`, `remove`, `search`, `reverse`)
- Returning values from functions
- Using comparison operators

---

# Section 2: Portfolio List

We start with an empty list that stores stock symbols.

```python
portfolio = []

print("Your stock portfolio has been created:", portfolio)
```

### Sample Output

```text
Your stock portfolio has been created: []
```

---

# Section 3: Function to Add a Stock

```python
def add_stock(stock):
    portfolio.append(stock)
    return stock
```

### Sample Usage

```python
print("Added:", add_stock("AAPL"))
print("Added:", add_stock("TSLA"))
```

### Sample Output

```text
Added: AAPL
Added: TSLA
```

### Explanation

- Adds a stock symbol to the portfolio list.
- Uses the `append()` method.

---

# Section 4: Function to Remove a Stock

```python
def remove_stock(stock):
    if stock in portfolio:
        portfolio.remove(stock)
        return stock
    else:
        return "Stock not found"
```

### Sample Usage

```python
print(remove_stock("TSLA"))
print(remove_stock("GOOG"))
```

### Sample Output

```text
TSLA
Stock not found
```

### Explanation

- Checks whether the stock exists in the portfolio.
- Removes it if found.
- Returns an error message if not found.

---

# Section 5: Function to Search a Stock

```python
def find_stock(stock):
    if stock in portfolio:
        return portfolio.index(stock)
    else:
        return "Stock not found"
```

### Sample Usage

```python
print("Position of AAPL:", find_stock("AAPL"))
print(find_stock("MSFT"))
```

### Sample Output

```text
Position of AAPL: 0
Stock not found
```

### Explanation

- Uses the `in` operator to search.
- Uses `index()` to return the position.

---

# Section 6: Function to Reverse Portfolio

```python
def reverse_portfolio():
    portfolio.reverse()
    return portfolio
```

### Sample Usage

```python
print("Reversed Portfolio:", reverse_portfolio())
```

### Sample Output

```text
Reversed Portfolio: ['AAPL']
```

### Explanation

- Reverses the order of stocks in the list.
- Uses the `reverse()` method.

---

# Section 7: Function to Compare Stock Symbol Lengths

This function demonstrates comparisons and return values.

```python
def compare_stock_length(stock1, stock2):
    if len(stock1) > len(stock2):
        return stock1 + " has a longer symbol."
    elif len(stock2) > len(stock1):
        return stock2 + " has a longer symbol."
    else:
        return "Both have equal length."
```

### Sample Usage

```python
print(compare_stock_length("AAPL", "MSFT"))
```

### Sample Output

```text
Both have equal length.
```

### Explanation

- Uses `len()` to measure string length.
- Compares lengths using `>`, `<`, and `==`.

---

# Section 8: Function to Display Portfolio

```python
def show_portfolio():
    if len(portfolio) == 0:
        print("Portfolio is empty.")
    else:
        print("Your current portfolio:")
        for stock in portfolio:
            print("-", stock)
```

### Sample Usage

```python
show_portfolio()
```

### Sample Output

```text
Your current portfolio:
- AAPL
- TSLA
```

---

# Section 9: Main Menu Loop (User Interaction)

The following menu combines all portfolio operations.

```python
while True:

    print("\n--- Stock Portfolio Menu ---")
    print("1. Add Stock")
    print("2. Remove Stock")
    print("3. Find Stock")
    print("4. Reverse Portfolio")
    print("5. Show Portfolio")
    print("6. Compare Stock Symbol Lengths")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        s = input("Enter stock symbol to add: ")
        print("Added:", add_stock(s))

    elif choice == "2":
        s = input("Enter stock symbol to remove: ")
        print(remove_stock(s))

    elif choice == "3":
        s = input("Enter stock symbol to find: ")
        print("Result:", find_stock(s))

    elif choice == "4":
        print("Reversed Portfolio:", reverse_portfolio())

    elif choice == "5":
        show_portfolio()

    elif choice == "6":
        s1 = input("Enter first stock symbol: ")
        s2 = input("Enter second stock symbol: ")
        print(compare_stock_length(s1, s2))

    elif choice == "7":
        print("Exiting Portfolio Manager...")
        break

    else:
        print("Invalid choice. Try again.")
```

---

# Section 10: Example Program Run

### Sample Output

```text
--- Stock Portfolio Menu ---

Enter your choice: 1

Enter stock symbol to add: AAPL

Added: AAPL


--- Stock Portfolio Menu ---

Enter your choice: 1

Enter stock symbol to add: TSLA

Added: TSLA


--- Stock Portfolio Menu ---

Enter your choice: 5

Your current portfolio:

- AAPL

- TSLA


--- Stock Portfolio Menu ---

Enter your choice: 3

Enter stock symbol to find: TSLA

Result: 1


--- Stock Portfolio Menu ---

Enter your choice: 7

Exiting Portfolio Manager...
```

---

# Key Concepts Learned

| Concept | Example |
|----------|----------|
| Function Definition | `def add_stock():` |
| Function Call | `add_stock("AAPL")` |
| List Append | `portfolio.append(stock)` |
| List Remove | `portfolio.remove(stock)` |
| List Search | `stock in portfolio` |
| List Index | `portfolio.index(stock)` |
| Reverse List | `portfolio.reverse()` |
| Loop | `while True:` |
| Conditional Statements | `if`, `elif`, `else` |
| Comparison Operators | `>`, `<`, `==` |
| Return Values | `return stock` |

---

# Final Portfolio Manager Workflow

```text
Start Program
      │
      ▼
Display Menu
      │
      ▼
User Selects Option
      │
      ├── Add Stock
      ├── Remove Stock
      ├── Find Stock
      ├── Reverse Portfolio
      ├── Show Portfolio
      ├── Compare Symbols
      └── Exit
      │
      ▼
Perform Operation
      │
      ▼
Return to Menu
      │
      ▼
Exit When User Chooses 7
```

---
✅ This case study covers Functions, Lists, Loops, Conditions, Comparisons, User Input, and Return Values in one practical application.
