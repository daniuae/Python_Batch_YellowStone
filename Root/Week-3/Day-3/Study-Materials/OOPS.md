# EcommerceAnalyzer Class - Detailed Explanation

## Overview

The `EcommerceAnalyzer` class performs various analyses on e-commerce order data using Pandas.

### Features

- Create an Order DataFrame
- Calculate Monthly Delivery Rate
- Add Return Flags
- Identify Frequent Returners
- Generate Category-wise Order Summary

---

# Sample Dataset

```python
data = [
    [101, "Electronics", "2025-01-05", "Delivered"],
    [101, "Electronics", "2025-01-10", "Returned"],
    [102, "Fashion", "2025-01-15", "Cancelled"],
    [101, "Books", "2025-02-01", "Delivered"],
    [103, "Fashion", "2025-02-05", "Delivered"]
]
```

---

# Complete Class

```python
class EcommerceAnalyzer:

    def create_order_df(self, data: list) -> pd.DataFrame:
        return pd.DataFrame(
            data,
            columns=["CustomerID", "Category", "OrderDate", "OrderStatus"]
        )

    def monthly_delivery_rate(self, df: pd.DataFrame) -> pd.DataFrame:

        temp = df.copy()
        temp["Month"] = temp["OrderDate"].str[:7]

        total_orders = (
            temp.groupby(["CustomerID", "Month"])
            .size()
            .reset_index(name="TotalOrders")
        )

        delivered_orders = (
            temp[temp["OrderStatus"] == "Delivered"]
            .groupby(["CustomerID", "Month"])
            .size()
            .reset_index(name="DeliveredOrders")
        )

        result = total_orders.merge(
            delivered_orders,
            on=["CustomerID", "Month"],
            how="left"
        )

        result["DeliveredOrders"] = (
            result["DeliveredOrders"]
            .fillna(0)
            .astype(int)
        )

        result["Delivery Rate"] = (
            result["DeliveredOrders"]
            / result["TotalOrders"]
            * 100
        )

        return result[["CustomerID", "Month", "Delivery Rate"]]

    def add_return_flag(self, df: pd.DataFrame) -> pd.DataFrame:

        result = df.copy()

        result["IsReturned"] = (
            result["OrderStatus"] == "Returned"
        ).astype(int)

        return result

    def frequent_returners(
        self,
        df: pd.DataFrame,
        threshold: int
    ) -> pd.DataFrame:

        result = (
            df[df["OrderStatus"] == "Returned"]
            .groupby("CustomerID")
            .size()
            .reset_index(name="ReturnCount")
        )

        return result[result["ReturnCount"] > threshold]

    def category_order_summary(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:

        summary = pd.crosstab(
            df["Category"],
            df["OrderStatus"]
        )

        summary = summary.reindex(
            columns=["Delivered", "Cancelled", "Returned"],
            fill_value=0
        )

        return summary.reset_index()
```

---

# Method 1: create_order_df()

## Purpose

Creates a Pandas DataFrame from raw order data.

### Code

```python
def create_order_df(self, data: list) -> pd.DataFrame:
    return pd.DataFrame(
        data,
        columns=["CustomerID", "Category", "OrderDate", "OrderStatus"]
    )
```

### Input

```python
[
    [101, "Electronics", "2025-01-05", "Delivered"],
    [102, "Fashion", "2025-01-15", "Cancelled"]
]
```

### Output

| CustomerID | Category | OrderDate | OrderStatus |
|------------|-----------|------------|------------|
| 101 | Electronics | 2025-01-05 | Delivered |
| 102 | Fashion | 2025-01-15 | Cancelled |

### Explanation

#### Step 1

```python
pd.DataFrame(data)
```

Converts the list into a DataFrame.

#### Step 2

```python
columns=[
    "CustomerID",
    "Category",
    "OrderDate",
    "OrderStatus"
]
```

Assigns meaningful column names.

---

# Method 2: monthly_delivery_rate()

## Purpose

Calculates delivery success percentage for every customer each month.

### Code

```python
def monthly_delivery_rate(self, df: pd.DataFrame) -> pd.DataFrame:
```

---

## Step 1: Create a Copy

```python
temp = df.copy()
```

### Why?

Prevents accidental modification of the original DataFrame.

---

## Step 2: Extract Month

```python
temp["Month"] = temp["OrderDate"].str[:7]
```

### Example

```python
2025-01-15
```

becomes

```python
2025-01
```

### Result

| OrderDate | Month |
|------------|---------|
| 2025-01-05 | 2025-01 |
| 2025-02-10 | 2025-02 |

---

## Step 3: Count Total Orders

```python
total_orders = (
    temp.groupby(["CustomerID", "Month"])
    .size()
    .reset_index(name="TotalOrders")
)
```

### Example

| CustomerID | Month |
|------------|---------|
|101|2025-01|
|101|2025-01|
|101|2025-02|

### Output

| CustomerID | Month | TotalOrders |
|------------|---------|------------|
|101|2025-01|2|
|101|2025-02|1|

---

## Step 4: Count Delivered Orders

```python
delivered_orders = (
    temp[temp["OrderStatus"] == "Delivered"]
    .groupby(["CustomerID", "Month"])
    .size()
    .reset_index(name="DeliveredOrders")
)
```

### Output

| CustomerID | Month | DeliveredOrders |
|------------|---------|----------------|
|101|2025-01|1|
|101|2025-02|1|

---

## Step 5: Merge DataFrames

```python
result = total_orders.merge(
    delivered_orders,
    on=["CustomerID", "Month"],
    how="left"
)
```

### Output

| CustomerID | Month | TotalOrders | DeliveredOrders |
|------------|---------|------------|----------------|
|101|2025-01|2|1|
|101|2025-02|1|1|

---

## Step 6: Replace Missing Values

```python
result["DeliveredOrders"] = (
    result["DeliveredOrders"]
    .fillna(0)
    .astype(int)
)
```

### Example

Before:

| DeliveredOrders |
|----------------|
| NaN |

After:

| DeliveredOrders |
|----------------|
| 0 |

---

## Step 7: Calculate Delivery Rate

```python
result["Delivery Rate"] = (
    result["DeliveredOrders"]
    / result["TotalOrders"]
    * 100
)
```

### Formula

```text
Delivery Rate =
Delivered Orders / Total Orders × 100
```

### Example

```python
1 / 2 * 100
```

Output:

```python
50.0
```

---

## Final Output

| CustomerID | Month | Delivery Rate |
|------------|---------|--------------|
|101|2025-01|50.0|
|101|2025-02|100.0|

---

# Method 3: add_return_flag()

## Purpose

Adds a binary indicator showing whether an order was returned.

### Code

```python
def add_return_flag(self, df: pd.DataFrame) -> pd.DataFrame:
```

---

## Step 1: Copy DataFrame

```python
result = df.copy()
```

---

## Step 2: Create Boolean Condition

```python
result["OrderStatus"] == "Returned"
```

### Example

| OrderStatus |
|-------------|
| Delivered |
| Returned |
| Cancelled |

Produces:

```python
False
True
False
```

---

## Step 3: Convert Boolean to Integer

```python
.astype(int)
```

### Conversion

```python
True  -> 1
False -> 0
```

---

## Output

| OrderStatus | IsReturned |
|-------------|------------|
| Delivered | 0 |
| Returned | 1 |
| Cancelled | 0 |

---

# Method 4: frequent_returners()

## Purpose

Find customers who frequently return products.

### Code

```python
def frequent_returners(
    self,
    df: pd.DataFrame,
    threshold: int
) -> pd.DataFrame:
```

---

## Step 1: Filter Returned Orders

```python
df[df["OrderStatus"] == "Returned"]
```

### Output

| CustomerID | Status |
|------------|---------|
|101|Returned|
|101|Returned|
|102|Returned|

---

## Step 2: Count Returns

```python
.groupby("CustomerID").size()
```

### Output

| CustomerID | ReturnCount |
|------------|-------------|
|101|2|
|102|1|

---

## Step 3: Convert to DataFrame

```python
.reset_index(name="ReturnCount")
```

### Output

| CustomerID | ReturnCount |
|------------|-------------|
|101|2|
|102|1|

---

## Step 4: Apply Threshold

```python
return result[result["ReturnCount"] > threshold]
```

### Example

```python
threshold = 1
```

### Result

| CustomerID | ReturnCount |
|------------|-------------|
|101|2|

---

# Method 5: category_order_summary()

## Purpose

Generates category-wise order status counts.

### Code

```python
def category_order_summary(
    self,
    df: pd.DataFrame
) -> pd.DataFrame:
```

---

## Step 1: Create Crosstab

```python
summary = pd.crosstab(
    df["Category"],
    df["OrderStatus"]
)
```

### Input

| Category | OrderStatus |
|-----------|------------|
| Electronics | Delivered |
| Electronics | Returned |
| Fashion | Delivered |
| Fashion | Cancelled |

### Output

| Category | Cancelled | Delivered | Returned |
|-----------|------------|------------|-----------|
| Electronics | 0 | 1 | 1 |
| Fashion | 1 | 1 | 0 |

---

## Why Use Crosstab?

Equivalent SQL:

```sql
SELECT
    Category,
    SUM(CASE WHEN OrderStatus='Delivered' THEN 1 ELSE 0 END) AS Delivered,
    SUM(CASE WHEN OrderStatus='Cancelled' THEN 1 ELSE 0 END) AS Cancelled,
    SUM(CASE WHEN OrderStatus='Returned' THEN 1 ELSE 0 END) AS Returned
FROM Orders
GROUP BY Category;
```

---

## Step 2: Reorder Columns

```python
summary = summary.reindex(
    columns=["Delivered", "Cancelled", "Returned"],
    fill_value=0
)
```

### Why?

Ensures consistent column order.

---

## Step 3: Convert Index to Column

```python
summary.reset_index()
```

### Before

| Category (Index) | Delivered |
|------------------|-----------|
| Books | 5 |

### After

| Category | Delivered |
|-----------|-----------|
| Books | 5 |

---

# Pandas Functions Used

| Function | Purpose |
|-----------|----------|
| DataFrame() | Create DataFrame |
| copy() | Create independent copy |
| groupby() | Group rows |
| size() | Count records |
| reset_index() | Convert index to columns |
| merge() | Join DataFrames |
| fillna() | Replace null values |
| astype() | Convert data types |
| crosstab() | Create pivot table |
| reindex() | Reorder/add columns |
| Boolean Masking | Filter rows |

---

# Key Pandas Concepts Tested

1. DataFrame Creation
2. String Manipulation
3. Filtering
4. GroupBy Aggregation
5. Merge / Join Operations
6. Missing Value Handling
7. Feature Engineering
8. Crosstab Reports
9. Business KPI Calculation
10. Data Analysis using OOP

This is an excellent intermediate-level Pandas OOP problem because it combines real-world business analysis with DataFrame manipulation, aggregation, joins, reporting, and feature engineering.
