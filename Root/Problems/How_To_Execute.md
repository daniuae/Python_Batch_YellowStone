# How to Execute the EcommerceAnalyzer Program

## Step 1: Save the Class Code

Save your class in a file named:

```text
ecommerce_analyzer.py
```

This file should contain your complete `EcommerceAnalyzer` class.

---

## Step 2: Create a Main Program

Create another file called:

```text
main.py
```

Add the following code:

```python
import pandas as pd
from ecommerce_analyzer import EcommerceAnalyzer

# -------------------------------------
# Sample Order Data
# -------------------------------------
data = [
    [101, "Electronics", "2026-06-01", "Delivered"],
    [101, "Electronics", "2026-06-05", "Returned"],
    [102, "Fashion", "2026-06-03", "Delivered"],
    [102, "Fashion", "2026-06-08", "Cancelled"],
    [103, "Books", "2026-06-10", "Delivered"],
    [103, "Books", "2026-06-15", "Delivered"],
    [101, "Books", "2026-07-01", "Delivered"],
    [101, "Books", "2026-07-05", "Returned"]
]

# -------------------------------------
# Create Object
# -------------------------------------
analyzer = EcommerceAnalyzer()

# -------------------------------------
# Create DataFrame
# -------------------------------------
df = analyzer.create_order_df(data)

print("\nOriginal Data")
print(df)

# -------------------------------------
# Monthly Delivery Rate
# -------------------------------------
print("\nMonthly Delivery Rate")
print(analyzer.monthly_delivery_rate(df))

# -------------------------------------
# Add Return Flag
# -------------------------------------
print("\nReturn Flag")
print(analyzer.add_return_flag(df))

# -------------------------------------
# Frequent Returners
# -------------------------------------
print("\nFrequent Returners")
print(analyzer.frequent_returners(df, threshold=1))

# -------------------------------------
# Category Order Summary
# -------------------------------------
print("\nCategory Summary")
print(analyzer.category_order_summary(df))
```

---

## Step 3: Install Pandas

If Pandas is not installed:

```bash
pip install pandas
```

Verify installation:

```bash
pip show pandas
```

---

## Step 4: Execute the Program

Open Terminal / Command Prompt:

```bash
python main.py
```

or

```bash
python3 main.py
```

---

# Expected Output

## Original Data

```text
   CustomerID     Category   OrderDate OrderStatus
0         101  Electronics  2026-06-01   Delivered
1         101  Electronics  2026-06-05    Returned
2         102      Fashion  2026-06-03   Delivered
3         102      Fashion  2026-06-08   Cancelled
4         103        Books  2026-06-10   Delivered
5         103        Books  2026-06-15   Delivered
6         101        Books  2026-07-01   Delivered
7         101        Books  2026-07-05    Returned
```

---

## Monthly Delivery Rate

```text
   CustomerID    Month  Delivery Rate
0         101  2026-06      50.000000
1         101  2026-07      50.000000
2         102  2026-06      50.000000
3         103  2026-06     100.000000
```

---

## Return Flag

```text
   CustomerID     Category   OrderDate OrderStatus  IsReturned
0         101  Electronics  2026-06-01   Delivered           0
1         101  Electronics  2026-06-05    Returned           1
2         102      Fashion  2026-06-03   Delivered           0
3         102      Fashion  2026-06-08   Cancelled           0
4         103        Books  2026-06-10   Delivered           0
5         103        Books  2026-06-15   Delivered           0
6         101        Books  2026-07-01   Delivered           0
7         101        Books  2026-07-05    Returned           1
```

---

## Frequent Returners

```text
   CustomerID  ReturnCount
0         101            2
```

---

## Category Summary

```text
      Category  Delivered  Cancelled  Returned
0        Books          2          0         1
1  Electronics          1          0         1
2      Fashion          1          1         0
```

---

# Why Doesn't the Original Program Print Anything?

Your original code only **defines a class** and its methods.

```python
class EcommerceAnalyzer:
    ...
```

Python reads and stores the class definition but does not execute any method automatically.

For example:

```python
class Car:

    def start(self):
        print("Car Started")
```

Nothing happens here.

To execute it:

```python
car = Car()
car.start()
```

Output:

```text
Car Started
```

Similarly, for `EcommerceAnalyzer`:

```python
analyzer = EcommerceAnalyzer()
df = analyzer.create_order_df(data)

print(df)
```

Now the methods are executed and produce output.

---

# Execution Flow

```text
Create Object
      │
      ▼
EcommerceAnalyzer()
      │
      ▼
create_order_df()
      │
      ▼
DataFrame Created
      │
      ├────────► monthly_delivery_rate()
      │
      ├────────► add_return_flag()
      │
      ├────────► frequent_returners()
      │
      └────────► category_order_summary()
```
