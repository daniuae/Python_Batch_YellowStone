# Execute EcommerceAnalyzer Step by Step

Instead of running everything together, you can execute each method separately and observe the output.

---

# Step 1: Import Library and Class

```python
import pandas as pd
from ecommerce_analyzer import EcommerceAnalyzer
```

---

# Step 2: Create Object

```python
analyzer = EcommerceAnalyzer()
```

Verify:

```python
print(analyzer)
```

Output:

```text
<__main__.EcommerceAnalyzer object at 0x...>
```

---

# Step 3: Create Sample Data

```python
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
```

---

# Step 4: Execute create_order_df()

## Method Call

```python
df = analyzer.create_order_df(data)
```

## Print Result

```python
print(df)
```

Output:

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

# Step 5: Execute monthly_delivery_rate()

## Method Call

```python
delivery_rate_df = analyzer.monthly_delivery_rate(df)
```

## Print Result

```python
print(delivery_rate_df)
```

Output:

```text
   CustomerID    Month  Delivery Rate
0         101  2026-06      50.000000
1         101  2026-07      50.000000
2         102  2026-06      50.000000
3         103  2026-06     100.000000
```

---

# Step 6: Execute add_return_flag()

## Method Call

```python
return_flag_df = analyzer.add_return_flag(df)
```

## Print Result

```python
print(return_flag_df)
```

Output:

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

# Step 7: Execute frequent_returners()

## Method Call

```python
returners_df = analyzer.frequent_returners(
    df,
    threshold=1
)
```

## Print Result

```python
print(returners_df)
```

Output:

```text
   CustomerID  ReturnCount
0         101            2
```

---

# Step 8: Execute category_order_summary()

## Method Call

```python
summary_df = analyzer.category_order_summary(df)
```

## Print Result

```python
print(summary_df)
```

Output:

```text
      Category  Delivered  Cancelled  Returned
0        Books          2          0         1
1  Electronics          1          0         1
2      Fashion          1          1         0
```

---

# Running in Jupyter Notebook

Create separate cells:

### Cell 1

```python
import pandas as pd
from ecommerce_analyzer import EcommerceAnalyzer

analyzer = EcommerceAnalyzer()
```

### Cell 2

```python
data = [
    [101, "Electronics", "2026-06-01", "Delivered"],
    [101, "Electronics", "2026-06-05", "Returned"],
    [102, "Fashion", "2026-06-03", "Delivered"],
    [102, "Fashion", "2026-06-08", "Cancelled"]
]
```

### Cell 3

```python
df = analyzer.create_order_df(data)
df
```

### Cell 4

```python
analyzer.monthly_delivery_rate(df)
```

### Cell 5

```python
analyzer.add_return_flag(df)
```

### Cell 6

```python
analyzer.frequent_returners(df, threshold=0)
```

### Cell 7

```python
analyzer.category_order_summary(df)
```

This approach helps trainees understand **how each method works independently** before executing the complete workflow.
