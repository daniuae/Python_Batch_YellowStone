# Pandas Cheat Sheet (Data Engineering & Analytics)

## Import Pandas

```python
import pandas as pd
import numpy as np
```

---

# Creating DataFrames

## From Dictionary

```python
df = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Raj", "John", "Mary"],
    "salary": [50000, 60000, 70000]
})
```

## From List of Lists

```python
data = [
    [1, "Raj", 50000],
    [2, "John", 60000]
]

df = pd.DataFrame(
    data,
    columns=["id", "name", "salary"]
)
```

## From CSV

```python
df = pd.read_csv("employees.csv")
```

## From Excel

```python
df = pd.read_excel("employees.xlsx")
```

## From JSON

```python
df = pd.read_json("employees.json")
```

---

# Viewing Data

## First Records

```python
df.head()
df.head(10)
```

## Last Records

```python
df.tail()
```

## Random Sample

```python
df.sample(5)
```

## Shape

```python
df.shape
```

Output:

```python
(rows, columns)
```

## Column Names

```python
df.columns
```

## Index

```python
df.index
```

## Data Types

```python
df.dtypes
```

## Data Information

```python
df.info()
```

## Statistics

```python
df.describe()
```

---

# Selecting Data

## Single Column

```python
df["salary"]
```

## Multiple Columns

```python
df[["name", "salary"]]
```

## Row by Position

```python
df.iloc[0]
```

## Multiple Rows

```python
df.iloc[0:5]
```

## Row by Label

```python
df.loc[0]
```

## Rows and Columns

```python
df.loc[0:5, ["name", "salary"]]
```

---

# Filtering Data

## Single Condition

```python
df[df["salary"] > 50000]
```

## Multiple Conditions (AND)

```python
df[
    (df["salary"] > 50000)
    &
    (df["department"] == "IT")
]
```

## Multiple Conditions (OR)

```python
df[
    (df["salary"] > 50000)
    |
    (df["department"] == "HR")
]
```

## NOT Condition

```python
df[~(df["department"] == "HR")]
```

## isin()

```python
df[df["department"].isin(["IT", "HR"])]
```

## between()

```python
df[df["salary"].between(50000, 80000)]
```

---

# Sorting

## Ascending

```python
df.sort_values("salary")
```

## Descending

```python
df.sort_values(
    "salary",
    ascending=False
)
```

## Multiple Columns

```python
df.sort_values(
    ["department", "salary"],
    ascending=[True, False]
)
```

---

# Creating New Columns

## Constant Value

```python
df["country"] = "India"
```

## Derived Column

```python
df["bonus"] = df["salary"] * 0.10
```

## Using apply()

```python
df["grade"] = df["salary"].apply(
    lambda x: "A" if x > 70000 else "B"
)
```

---

# Renaming Columns

```python
df.rename(
    columns={
        "salary": "monthly_salary"
    },
    inplace=True
)
```

---

# Dropping Columns

## Single Column

```python
df.drop("salary", axis=1)
```

## Multiple Columns

```python
df.drop(
    ["salary", "bonus"],
    axis=1
)
```

---

# Missing Values

## Find Nulls

```python
df.isnull()
```

## Count Nulls

```python
df.isnull().sum()
```

## Drop Null Rows

```python
df.dropna()
```

## Fill Nulls

```python
df.fillna(0)
```

## Fill with Mean

```python
df["salary"].fillna(
    df["salary"].mean()
)
```

---

# Duplicates

## Find Duplicates

```python
df.duplicated()
```

## Remove Duplicates

```python
df.drop_duplicates()
```

---

# GroupBy Operations

## Sum

```python
df.groupby("department")["salary"].sum()
```

## Average

```python
df.groupby("department")["salary"].mean()
```

## Multiple Aggregations

```python
df.groupby("department").agg({
    "salary": ["sum", "mean", "max"],
    "id": "count"
})
```

---

# Pivot Table

```python
pd.pivot_table(
    df,
    index="department",
    values="salary",
    aggfunc="sum"
)
```

---

# Value Counts

## Count Categories

```python
df["department"].value_counts()
```

## Percentage Distribution

```python
df["department"].value_counts(
    normalize=True
)
```

---

# Merge (SQL Joins)

## Inner Join

```python
pd.merge(
    customers,
    orders,
    on="customer_id",
    how="inner"
)
```

## Left Join

```python
pd.merge(
    customers,
    orders,
    on="customer_id",
    how="left"
)
```

## Right Join

```python
pd.merge(
    customers,
    orders,
    on="customer_id",
    how="right"
)
```

## Full Outer Join

```python
pd.merge(
    customers,
    orders,
    on="customer_id",
    how="outer"
)
```

---

# Concatenation

## Vertical

```python
pd.concat([df1, df2])
```

## Horizontal

```python
pd.concat(
    [df1, df2],
    axis=1
)
```

---

# String Functions

## Uppercase

```python
df["name"].str.upper()
```

## Lowercase

```python
df["name"].str.lower()
```

## Contains

```python
df[
    df["email"].str.contains("@gmail")
]
```

## Replace

```python
df["name"].str.replace(
    "Raj",
    "Raja"
)
```

---

# Date Functions

## Convert to Datetime

```python
df["order_date"] = pd.to_datetime(
    df["order_date"]
)
```

## Extract Year

```python
df["order_date"].dt.year
```

## Extract Month

```python
df["order_date"].dt.month
```

## Extract Day

```python
df["order_date"].dt.day
```

## Day Name

```python
df["order_date"].dt.day_name()
```

---

# Window Functions

## Running Total

```python
df["running_sales"] = (
    df["sales"].cumsum()
)
```

## Rolling Average

```python
df["rolling_avg"] = (
    df["sales"]
      .rolling(3)
      .mean()
)
```

## Shift

```python
df["previous_day"] = (
    df["sales"].shift(1)
)
```

## Lag Difference

```python
df["difference"] = (
    df["sales"]
    - df["sales"].shift(1)
)
```

---

# Ranking

## Rank

```python
df["rank"] = df["salary"].rank()
```

## Dense Rank

```python
df["dense_rank"] = df["salary"].rank(
    method="dense"
)
```

---

# Apply Functions

## Row-wise Apply

```python
df.apply(
    lambda row: row["salary"] * 0.10,
    axis=1
)
```

## Column-wise Apply

```python
df["salary"].apply(
    lambda x: x * 1.1
)
```

---

# Mapping

```python
dept_map = {
    "IT": "Technology",
    "HR": "Human Resource"
}

df["department"] = (
    df["department"]
      .map(dept_map)
)
```

---

# Replace Values

```python
df["status"].replace({
    "A": "Active",
    "I": "Inactive"
})
```

---

# Binning

## cut()

```python
df["salary_band"] = pd.cut(
    df["salary"],
    bins=[0, 50000, 100000, 200000],
    labels=["Low", "Medium", "High"]
)
```

## qcut()

```python
df["quartile"] = pd.qcut(
    df["salary"],
    q=4
)
```

---

# Export Data

## CSV

```python
df.to_csv(
    "output.csv",
    index=False
)
```

## Excel

```python
df.to_excel(
    "output.xlsx",
    index=False
)
```

## JSON

```python
df.to_json(
    "output.json"
)
```

---

# Performance Tips

## Avoid Loops

### Slow

```python
for i in range(len(df)):
    df.loc[i, "bonus"] = (
        df.loc[i, "salary"] * 0.10
    )
```

### Fast (Vectorized)

```python
df["bonus"] = (
    df["salary"] * 0.10
)
```

---

# Top 25 Most Used Pandas Functions

```text
read_csv()
head()
tail()
info()
describe()
shape
columns
dtypes
loc[]
iloc[]
query()
sort_values()
groupby()
agg()
merge()
concat()
pivot_table()
fillna()
dropna()
drop_duplicates()
apply()
map()
value_counts()
cumsum()
rolling()
shift()
```

---

# SQL vs Pandas Quick Reference

| SQL | Pandas |
|------|---------|
| SELECT * | df |
| SELECT column | df["column"] |
| WHERE | df[df["column"] > 10] |
| ORDER BY | sort_values() |
| GROUP BY | groupby() |
| JOIN | merge() |
| COUNT | count() |
| SUM | sum() |
| AVG | mean() |
| RANK | rank() |
| LAG | shift() |
| Running Total | cumsum() |
| Pivot | pivot_table() |

---

# Data Engineer Interview Topics

Focus on these Pandas concepts:

1. Data Cleaning
2. Missing Value Handling
3. Merge / Join
4. GroupBy Aggregations
5. Pivot Tables
6. Window Functions
7. Time Series Analysis
8. String Manipulation
9. Apply vs Vectorization
10. Memory Optimization
11. MultiIndex
12. Chunk Processing
13. Reading Large Files
14. ETL Pipelines
15. Performance Tuning

---

# Pandas Interview Tips

### Always Prefer

- Vectorized operations
- `merge()` over loops
- `groupby()` for aggregations
- `loc[]` and `iloc[]` correctly
- Method chaining when possible

### Avoid

- Iterating through DataFrames with loops
- Excessive use of `apply()`
- Storing huge datasets without optimization

### Performance Optimization

```python
df.info(memory_usage="deep")
```

```python
df["department"] = (
    df["department"]
      .astype("category")
)
```

```python
df = pd.read_csv(
    "large_file.csv",
    chunksize=100000
)
```

---

# Summary

Pandas is the most important Python library for:

- Data Analysis
- Data Cleaning
- ETL Pipelines
- Data Engineering
- Business Intelligence
- Machine Learning Data Preparation

Mastering:

- Filtering
- GroupBy
- Joins
- Window Functions
- Missing Value Handling
- Performance Optimization

will cover most real-world Data Engineering, Data Analyst, BI Engineer, and Data Scientist interview scenarios.
