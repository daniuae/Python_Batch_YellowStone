# Pandas GroupBy Lab: Sales Analysis Using Aggregation and Transformation

## Objective

Learn how to group data in Pandas using the `groupby()` function. This lab focuses on:

* Calculating aggregates
* Applying transformations
* Performing grouped analysis
* Extracting business insights from sales data

---

# Case Study

A retail company collects sales data for multiple regions and products. The dataset contains:

* Region
* Product
* Quantity Sold
* Revenue

The business wants to:

1. Analyze total and average sales by region
2. Compare product-wise sales
3. Perform custom aggregations
4. Calculate revenue contribution percentages
5. Normalize sales quantities

---

# Step 1: Import Required Libraries

```python
import pandas as pd
import numpy as np
```

---

# Step 2: Create Sales DataFrame

## Generate Synthetic Retail Sales Data

```python
data = {
    'Region': [
        'North', 'East', 'East', 'East', 'North',
        'West', 'South', 'North', 'West', 'South'
    ],
    'Product': [
        'Smartphone', 'Laptop', 'Laptop', 'Laptop', 'Smartphone',
        'Monitor', 'Laptop', 'Monitor', 'Smartphone', 'Monitor'
    ],
    'Quantity Sold': [8, 4, 3, 3, 8, 5, 7, 6, 9, 4],
    'Revenue': [246, 892, 711, 711, 246, 500, 820, 450, 650, 400]
}

df = pd.DataFrame(data)

print(df)
```

---

## Sample Output

| Region | Product    | Quantity Sold | Revenue |
| ------ | ---------- | ------------- | ------- |
| North  | Smartphone | 8             | 246     |
| East   | Laptop     | 4             | 892     |
| East   | Laptop     | 3             | 711     |
| East   | Laptop     | 3             | 711     |
| North  | Smartphone | 8             | 246     |
| West   | Monitor    | 5             | 500     |
| South  | Laptop     | 7             | 820     |
| North  | Monitor    | 6             | 450     |
| West   | Smartphone | 9             | 650     |
| South  | Monitor    | 4             | 400     |

---

# Understanding GroupBy

The `groupby()` function splits data into groups and allows aggregate calculations.

### General Syntax

```python
df.groupby('ColumnName')
```

### Split → Apply → Combine

```text
DataFrame
    ↓
Group By Region
    ↓
Apply Sum / Mean / Max
    ↓
Combined Results
```

---

# Step 3: Group by Region

## Calculate Total Revenue per Region

```python
region_sales = df.groupby('Region')['Revenue'].sum()

print("Total Revenue by Region:")
print(region_sales)
```

### Output

```text
Region
East     2314
North     942
South    1220
West     1150
```

### Explanation

Groups rows by Region and sums Revenue.

---

## Calculate Average Revenue per Region

```python
avg_revenue = df.groupby('Region')['Revenue'].mean()

print("Average Revenue by Region:")
print(avg_revenue)
```

### Output

```text
Region
East     771.33
North    314.00
South    610.00
West     575.00
```

### Business Insight

East region generates the highest average revenue.

---

# Step 4: Group by Product

## Total Quantity Sold per Product

```python
product_sales = df.groupby('Product')['Quantity Sold'].sum()

print(product_sales)
```

### Output

```text
Product
Laptop        17
Monitor       15
Smartphone    25
```

---

## Total and Average Revenue per Product

```python
product_revenue = df.groupby('Product')['Revenue'].agg(
    ['sum', 'mean']
)

print(product_revenue)
```

### Output

```text
              sum    mean
Product
Laptop      3134  783.50
Monitor     1350  450.00
Smartphone  1142  380.67
```

---

# Step 5: Group by Multiple Columns

Sometimes we need deeper analysis.

Example:

* Region + Product

---

## Revenue by Region and Product

```python
regional_product_sales = df.groupby(
    ['Region', 'Product']
)['Revenue'].sum()

print(regional_product_sales)
```

### Output

```text
Region  Product
East    Laptop        2314
North   Monitor        450
North   Smartphone     492
South   Laptop         820
South   Monitor        400
West    Monitor        500
West    Smartphone     650
```

---

## Reset the Index

Multi-level indexes can be flattened.

```python
regional_product_sales = regional_product_sales.reset_index()

print(regional_product_sales)
```

### Output

| Region | Product    | Revenue |
| ------ | ---------- | ------- |
| East   | Laptop     | 2314    |
| North  | Monitor    | 450     |
| North  | Smartphone | 492     |
| South  | Laptop     | 820     |
| South  | Monitor    | 400     |
| West   | Monitor    | 500     |
| West   | Smartphone | 650     |

---

# Step 6: Apply Custom Aggregations

Calculate multiple metrics at once.

## Revenue Summary by Region

```python
custom_agg = df.groupby('Region').agg(
    Total_Revenue=('Revenue', 'sum'),
    Avg_Quantity=('Quantity Sold', 'mean'),
    Max_Revenue=('Revenue', 'max')
)

print(custom_agg)
```

### Output

```text
        Total_Revenue  Avg_Quantity  Max_Revenue
Region
East             2314      3.33           892
North             942      7.33           450
South            1220      5.50           820
West             1150      7.00           650
```

---

## Explanation

### Total Revenue

```python
('Revenue', 'sum')
```

Adds all revenue values.

### Average Quantity

```python
('Quantity Sold', 'mean')
```

Calculates average units sold.

### Maximum Revenue

```python
('Revenue', 'max')
```

Finds highest revenue transaction.

---

# Step 7: Apply Transformations

Unlike aggregation, transformation returns a value for every row.

---

# Revenue Percentage Contribution Within Region

## Business Requirement

Determine how much each transaction contributes to its region's revenue.

### Formula

```text
(Row Revenue / Total Regional Revenue) × 100
```

---

## Implementation

```python
df['Revenue % of Region'] = df.groupby(
    'Region'
)['Revenue'].transform(
    lambda x: (x / x.sum()) * 100
)

print(df.head())
```

### Output

| Region | Revenue | Revenue % of Region |
| ------ | ------- | ------------------- |
| North  | 246     | 26.11               |
| East   | 892     | 38.55               |
| East   | 711     | 30.73               |
| East   | 711     | 30.73               |
| North  | 246     | 26.11               |

---

## Business Insight

Identifies which transactions contribute the most revenue within a region.

---

# Normalize Quantity Sold Within Region

Normalization scales values between 0 and 1.

### Formula

```text
(Value - Min) / (Max - Min)
```

---

## Implementation

```python
df['Normalized Quantity'] = df.groupby(
    'Region'
)['Quantity Sold'].transform(
    lambda x: (x - x.min()) / (x.max() - x.min())
)

print(df.head())
```

### Output

| Region | Quantity Sold | Normalized Quantity |
| ------ | ------------- | ------------------- |
| North  | 8             | 1.00                |
| East   | 4             | 1.00                |
| East   | 3             | 0.00                |
| East   | 3             | 0.00                |
| North  | 8             | 1.00                |

---

# Complete Program

```python
import pandas as pd
import numpy as np

data = {
    'Region': [
        'North', 'East', 'East', 'East', 'North',
        'West', 'South', 'North', 'West', 'South'
    ],
    'Product': [
        'Smartphone', 'Laptop', 'Laptop', 'Laptop',
        'Smartphone', 'Monitor', 'Laptop',
        'Monitor', 'Smartphone', 'Monitor'
    ],
    'Quantity Sold': [8, 4, 3, 3, 8, 5, 7, 6, 9, 4],
    'Revenue': [246, 892, 711, 711, 246, 500, 820, 450, 650, 400]
}

df = pd.DataFrame(data)

region_sales = df.groupby('Region')['Revenue'].sum()

avg_revenue = df.groupby('Region')['Revenue'].mean()

product_sales = df.groupby('Product')['Quantity Sold'].sum()

product_revenue = df.groupby('Product')['Revenue'].agg(
    ['sum', 'mean']
)

regional_product_sales = df.groupby(
    ['Region', 'Product']
)['Revenue'].sum().reset_index()

custom_agg = df.groupby('Region').agg(
    Total_Revenue=('Revenue', 'sum'),
    Avg_Quantity=('Quantity Sold', 'mean'),
    Max_Revenue=('Revenue', 'max')
)

df['Revenue % of Region'] = df.groupby(
    'Region'
)['Revenue'].transform(
    lambda x: (x / x.sum()) * 100
)

df['Normalized Quantity'] = df.groupby(
    'Region'
)['Quantity Sold'].transform(
    lambda x: (x - x.min()) / (x.max() - x.min())
)

print(df)
```

---

# GroupBy Cheat Sheet

| Task                   | Code                        |
| ---------------------- | --------------------------- |
| Sum                    | `groupby().sum()`           |
| Mean                   | `groupby().mean()`          |
| Count                  | `groupby().count()`         |
| Min                    | `groupby().min()`           |
| Max                    | `groupby().max()`           |
| Multiple Aggregations  | `agg(['sum','mean'])`       |
| Named Aggregations     | `agg(NewCol=('col','sum'))` |
| Group Multiple Columns | `groupby(['A','B'])`        |
| Flatten Index          | `reset_index()`             |
| Row-wise Calculations  | `transform()`               |

---

# Real-World Applications

## Retail Analytics

* Revenue by region
* Product performance analysis

## E-Commerce

* Customer purchase patterns
* Product demand forecasting

## Supply Chain

* Regional inventory planning
* Sales trend analysis

## Business Intelligence

* KPI dashboards
* Executive reporting

## Data Engineering

* Aggregated reporting tables
* ETL transformation logic

---

# Key Concepts Learned

✅ `groupby()`
✅ Aggregation (`sum`, `mean`, `max`)
✅ Multi-column grouping
✅ Custom aggregation using `agg()`
✅ Data transformation using `transform()`
✅ Percentage contribution calculations
✅ Data normalization
✅ Business-focused sales analysis
