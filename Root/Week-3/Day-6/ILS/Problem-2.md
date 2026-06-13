# Pandas Lab: Exploring Customer Transaction Data

## Objective

Set up a Python environment for working with **Pandas** and explore a DataFrame containing synthetic customer transaction data. This lab introduces basic DataFrame operations, including loading, inspecting, filtering, sorting, and performing basic data manipulations.

---

# Case Study

A company collects customer transaction data, including:

* Customer IDs
* Order Dates
* Products Purchased
* Quantity Ordered
* Price Per Unit

Your task is to explore the dataset to understand its structure and perform initial data analysis and cleaning.

---

# Step 1: Set Up the Python Environment

## Install Required Libraries

```bash
pip install pandas numpy
```

## Import Libraries

```python
import pandas as pd
import numpy as np
```

---

# Step 2: Generate Synthetic Customer Data

## Create Sample Dataset

```python
import pandas as pd

data = {
    'CustomerID': [1001, 1002, 1003, 1004, 1005],
    'OrderDate': [
        '2023-01-01',
        '2023-01-02',
        '2023-01-03',
        '2023-01-04',
        '2023-01-05'
    ],
    'Product': [
        'Smartphone',
        'Laptop',
        'Laptop',
        'Laptop',
        'Monitor'
    ],
    'Quantity': [3, 4, 1, 3, 4],
    'PricePerUnit': [655, 422, 915, 199, 177]
}

df = pd.DataFrame(data)

# Calculate Total Amount
df['TotalAmount'] = df['Quantity'] * df['PricePerUnit']

print(df)
```

## Expected Output

| CustomerID | OrderDate  | Product    | Quantity | PricePerUnit | TotalAmount |
| ---------- | ---------- | ---------- | -------- | ------------ | ----------- |
| 1001       | 2023-01-01 | Smartphone | 3        | 655          | 1965        |
| 1002       | 2023-01-02 | Laptop     | 4        | 422          | 1688        |
| 1003       | 2023-01-03 | Laptop     | 1        | 915          | 915         |
| 1004       | 2023-01-04 | Laptop     | 3        | 199          | 597         |
| 1005       | 2023-01-05 | Monitor    | 4        | 177          | 708         |

---

# Step 3: Inspect the DataFrame

Understanding the structure of a DataFrame is the first step in data analysis.

## View Data Types and Structure

```python
print("DataFrame Info:")
print(df.info())
```

### Sample Output

```text
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 6 columns):
```

### Explanation

* Number of rows and columns
* Data types of each column
* Missing values count

---

## Summary Statistics

```python
print("\nSummary Statistics:")
print(df.describe())
```

### Sample Output

```text
       CustomerID   Quantity  PricePerUnit  TotalAmount
count     5.00000   5.000000      5.000000      5.00000
mean   1003.00000   3.000000    473.600000   1174.60000
min    1001.00000   1.000000    177.000000    597.00000
max    1005.00000   4.000000    915.000000   1965.00000
```

### Explanation

`describe()` provides:

* Count
* Mean
* Standard Deviation
* Minimum
* Maximum
* Quartiles

---

# Step 4: Explore Column Operations

## Access a Single Column

```python
print("Customer IDs:")
print(df['CustomerID'].head())
```

### Output

```text
0    1001
1    1002
2    1003
3    1004
4    1005
```

---

## Access Multiple Columns

```python
print("Product and Total Amount:")
print(df[['Product', 'TotalAmount']].head())
```

### Output

```text
      Product  TotalAmount
0  Smartphone         1965
1      Laptop         1688
2      Laptop          915
3      Laptop          597
4     Monitor          708
```

---

## Rename a Column

```python
df.rename(
    columns={'TotalAmount': 'OrderValue'},
    inplace=True
)

print(df.head())
```

### Output

```text
   CustomerID   OrderDate      Product  Quantity  PricePerUnit  OrderValue
0        1001  2023-01-01   Smartphone         3           655        1965
```

### Explanation

* `rename()` changes column names.
* `inplace=True` updates the original DataFrame.

---

# Step 5: Filter Rows

Filtering helps extract specific records based on conditions.

---

## Filter High-Value Orders

Orders above $1000.

```python
high_value_orders = df[df['OrderValue'] > 1000]

print(high_value_orders)
```

### Output

```text
   CustomerID Product  OrderValue
0        1001 Smartphone      1965
1        1002 Laptop          1688
```

---

## Filter Laptop Orders

```python
laptop_orders = df[df['Product'] == 'Laptop']

print(laptop_orders)
```

### Output

```text
   CustomerID Product  Quantity
1        1002 Laptop        4
2        1003 Laptop        1
3        1004 Laptop        3
```

---

# Step 6: Sort the DataFrame

Sorting helps identify top-performing records.

## Sort by Order Value (Descending)

```python
sorted_df = df.sort_values(
    by='OrderValue',
    ascending=False
)

print(sorted_df)
```

### Output

```text
   CustomerID Product  OrderValue
0        1001 Smartphone      1965
1        1002 Laptop          1688
2        1003 Laptop           915
4        1005 Monitor          708
3        1004 Laptop           597
```

### Explanation

* Highest-value orders appear first.
* Useful for sales analysis.

---

# Step 7: Add a Calculated Column

Business Rule:

* Orders above **$2000** receive a **10% discount**.

---

## Create Discount Columns

```python
import numpy as np

df['Discount'] = np.where(
    df['OrderValue'] > 2000,
    0.10,
    0
)

df['DiscountedValue'] = (
    df['OrderValue'] *
    (1 - df['Discount'])
)

print(df)
```

### Output

```text
   CustomerID Product  OrderValue  Discount  DiscountedValue
0        1001 Smartphone      1965      0.0           1965.0
1        1002 Laptop          1688      0.0           1688.0
2        1003 Laptop           915      0.0            915.0
3        1004 Laptop           597      0.0            597.0
4        1005 Monitor          708      0.0            708.0
```

### Explanation

`np.where(condition, value_if_true, value_if_false)`

Example:

```python
np.where(df['OrderValue'] > 2000, 0.10, 0)
```

* If order value > 2000 → 10% discount
* Else → 0% discount

---

# Complete Program

```python
import pandas as pd
import numpy as np

data = {
    'CustomerID': [1001, 1002, 1003, 1004, 1005],
    'OrderDate': [
        '2023-01-01',
        '2023-01-02',
        '2023-01-03',
        '2023-01-04',
        '2023-01-05'
    ],
    'Product': [
        'Smartphone',
        'Laptop',
        'Laptop',
        'Laptop',
        'Monitor'
    ],
    'Quantity': [3, 4, 1, 3, 4],
    'PricePerUnit': [655, 422, 915, 199, 177]
}

df = pd.DataFrame(data)

df['TotalAmount'] = df['Quantity'] * df['PricePerUnit']

print(df.info())
print(df.describe())

print(df['CustomerID'])
print(df[['Product', 'TotalAmount']])

df.rename(columns={'TotalAmount': 'OrderValue'}, inplace=True)

high_value_orders = df[df['OrderValue'] > 1000]

laptop_orders = df[df['Product'] == 'Laptop']

sorted_df = df.sort_values(
    by='OrderValue',
    ascending=False
)

df['Discount'] = np.where(
    df['OrderValue'] > 2000,
    0.10,
    0
)

df['DiscountedValue'] = (
    df['OrderValue'] *
    (1 - df['Discount'])
)

print(df)
```

---

# Key Pandas Concepts Learned

| Concept                 | Method                   |
| ----------------------- | ------------------------ |
| Create DataFrame        | `pd.DataFrame()`         |
| View Structure          | `info()`                 |
| Summary Statistics      | `describe()`             |
| Access Column           | `df['column']`           |
| Access Multiple Columns | `df[['col1','col2']]`    |
| Rename Column           | `rename()`               |
| Filter Rows             | Boolean Indexing         |
| Sort Data               | `sort_values()`          |
| Create New Column       | Assignment (`df['new']`) |
| Conditional Logic       | `np.where()`             |

---

# Real-World Applications

* E-Commerce Order Analysis
* Retail Sales Reporting
* Customer Purchase Tracking
* Revenue Analysis
* Discount Calculation Systems
* Business Intelligence Dashboards
* Data Cleaning and Exploration
