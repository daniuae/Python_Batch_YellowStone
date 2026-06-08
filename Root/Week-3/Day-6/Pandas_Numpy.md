# NumPy and Pandas for Data Manipulation (Pandas Focus)

## Introduction

Pandas is the most popular Python library for data manipulation and analysis. It is built on top of NumPy and provides high-level data structures and functions for working with structured data.

### Why Pandas?

* Easy data cleaning
* Data transformation
* Data aggregation
* ETL and ELT processing
* SQL-like operations
* Time series analysis
* Integration with databases, Excel, CSV, JSON, and cloud storage

---

# Installation

```bash
pip install pandas numpy
```

Import libraries:

```python
import pandas as pd
import numpy as np
```

---

# Pandas Data Structures

## Series

A one-dimensional labeled array.

```python
import pandas as pd

s = pd.Series([10, 20, 30, 40])

print(s)
```

Output:

```text
0    10
1    20
2    30
3    40
dtype: int64
```

---

## Series with Custom Index

```python
s = pd.Series(
    [100, 200, 300],
    index=["A", "B", "C"]
)

print(s)
```

Output:

```text
A    100
B    200
C    300
```

---

## Accessing Series Elements

```python
print(s["A"])
print(s[0])
```

---

# DataFrame

A two-dimensional tabular structure.

## Create DataFrame from Dictionary

```python
data = {
    "id": [1, 2, 3],
    "name": ["John", "Mary", "David"],
    "salary": [50000, 60000, 70000]
}

df = pd.DataFrame(data)

print(df)
```

---

## Create DataFrame from List

```python
data = [
    [1, "John", 50000],
    [2, "Mary", 60000]
]

df = pd.DataFrame(
    data,
    columns=["id", "name", "salary"]
)
```

---

## Create DataFrame from List of Dictionaries

```python
employees = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Mary"}
]

df = pd.DataFrame(employees)
```

---

# Reading Data

## CSV

```python
df = pd.read_csv("employees.csv")
```

## Excel

```python
df = pd.read_excel("employees.xlsx")
```

## JSON

```python
df = pd.read_json("employees.json")
```

## SQL Database

```python
import sqlite3

conn = sqlite3.connect("company.db")

df = pd.read_sql(
    "SELECT * FROM employee",
    conn
)
```

---

# Writing Data

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
df.to_json("output.json")
```

## SQL

```python
df.to_sql(
    "employee",
    conn,
    if_exists="replace"
)
```

---

# Data Exploration

## Head

```python
df.head()
```

```python
df.head(10)
```

---

## Tail

```python
df.tail()
```

---

## Shape

```python
df.shape
```

---

## Columns

```python
df.columns
```

---

## Data Types

```python
df.dtypes
```

---

## Information

```python
df.info()
```

---

## Statistics

```python
df.describe()
```

---

# Column Selection

## Single Column

```python
df["salary"]
```

---

## Multiple Columns

```python
df[["name", "salary"]]
```

---

# Row Selection

## loc

Label-based indexing.

```python
df.loc[0]
```

```python
df.loc[0:5]
```

---

## iloc

Position-based indexing.

```python
df.iloc[0]
```

```python
df.iloc[0:5]
```

---

# Filtering Data

## Single Condition

```python
df[df["salary"] > 50000]
```

---

## Multiple Conditions

### AND

```python
df[
    (df["salary"] > 50000)
    &
    (df["department"] == "IT")
]
```

### OR

```python
df[
    (df["salary"] > 50000)
    |
    (df["department"] == "IT")
]
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
    ["department", "salary"]
)
```

---

# Add Column

```python
df["bonus"] = df["salary"] * 0.10
```

---

# Delete Column

```python
df.drop(
    "bonus",
    axis=1,
    inplace=True
)
```

---

# Rename Columns

```python
df.rename(
    columns={
        "salary": "emp_salary"
    },
    inplace=True
)
```

---

# Missing Values

## Detect Missing Values

```python
df.isnull()
```

---

## Count Missing Values

```python
df.isnull().sum()
```

---

## Drop Missing Values

```python
df.dropna()
```

---

## Fill Missing Values

```python
df.fillna(0)
```

---

## Fill with Mean

```python
df["salary"].fillna(
    df["salary"].mean(),
    inplace=True
)
```

---

# Duplicates

## Remove Duplicates

```python
df.drop_duplicates()
```

---

## Remove Based on Column

```python
df.drop_duplicates(
    subset=["email"]
)
```

---

# String Operations

## Upper Case

```python
df["name"].str.upper()
```

---

## Lower Case

```python
df["name"].str.lower()
```

---

## Contains

```python
df[
    df["name"].str.contains("John")
]
```

---

## Replace

```python
df["name"].str.replace(
    "John",
    "Johnny"
)
```

---

# Date Functions

## Convert to Datetime

```python
df["date"] = pd.to_datetime(
    df["date"]
)
```

---

## Extract Year

```python
df["date"].dt.year
```

---

## Extract Month

```python
df["date"].dt.month
```

---

## Extract Day

```python
df["date"].dt.day
```

---

# Apply Function

```python
def category(salary):
    if salary > 60000:
        return "High"
    return "Normal"

df["category"] = df["salary"].apply(category)
```

---

# Lambda Function

```python
df["bonus"] = df["salary"].apply(
    lambda x: x * 0.1
)
```

---

# Aggregations

## Sum

```python
df["salary"].sum()
```

## Mean

```python
df["salary"].mean()
```

## Maximum

```python
df["salary"].max()
```

## Minimum

```python
df["salary"].min()
```

## Count

```python
df["salary"].count()
```

---

# GroupBy

## Total Salary by Department

```python
df.groupby(
    "department"
)["salary"].sum()
```

---

## Multiple Aggregations

```python
df.groupby(
    "department"
)["salary"].agg(
    ["sum", "mean", "max"]
)
```

---

# Pivot Table

```python
pd.pivot_table(
    df,
    values="sales",
    index="region",
    columns="year",
    aggfunc="sum"
)
```

---

# Cross Tab

```python
pd.crosstab(
    df["gender"],
    df["department"]
)
```

---

# Merge (SQL Joins)

## Inner Join

```python
pd.merge(
    emp,
    dept,
    on="dept_id",
    how="inner"
)
```

## Left Join

```python
pd.merge(
    emp,
    dept,
    on="dept_id",
    how="left"
)
```

## Right Join

```python
pd.merge(
    emp,
    dept,
    on="dept_id",
    how="right"
)
```

## Full Outer Join

```python
pd.merge(
    emp,
    dept,
    on="dept_id",
    how="outer"
)
```

---

# Concatenation

## Vertical

```python
pd.concat(
    [df1, df2]
)
```

## Horizontal

```python
pd.concat(
    [df1, df2],
    axis=1
)
```

---

# Window Functions

## Rank

```python
df["rank"] = (
    df["salary"]
    .rank()
)
```

## Dense Rank

```python
df["dense_rank"] = (
    df["salary"]
    .rank(method="dense")
)
```

## Row Number

```python
df["row_num"] = range(
    1,
    len(df)+1
)
```

---

# Value Counts

```python
df["department"].value_counts()
```

---

# Unique Values

```python
df["department"].unique()
```

---

# Number of Unique Values

```python
df["department"].nunique()
```

---

# Query

```python
df.query(
    "salary > 50000"
)
```

---

# Replace Values

```python
df.replace(
    "IT",
    "Technology"
)
```

---

# Map

```python
mapping = {
    "M": "Male",
    "F": "Female"
}

df["gender"] = (
    df["gender"]
    .map(mapping)
)
```

---

# Explode

```python
df = pd.DataFrame({
    "id": [1,2],
    "skills": [
        ["Python","SQL"],
        ["Spark","AWS"]
    ]
})

df.explode("skills")
```

---

# Melt (Unpivot)

```python
pd.melt(
    df,
    id_vars=["id"]
)
```

---

# Multi Index

```python
df.set_index(
    ["department","name"]
)
```

---

# Memory Optimization

```python
df["department"] = (
    df["department"]
    .astype("category")
)
```

---

# ETL Example

## Extract

```python
df = pd.read_csv(
    "sales.csv"
)
```

## Transform

```python
df.drop_duplicates(
    inplace=True
)

df.fillna(
    0,
    inplace=True
)

df["total_sales"] = (
    df["quantity"]
    * df["price"]
)
```

## Load

```python
df.to_sql(
    "fact_sales",
    conn,
    if_exists="replace"
)
```

---

# NumPy Integration

## Random Column

```python
df["random"] = np.random.randint(
    1,
    100,
    size=len(df)
)
```

---

## Conditional Column

```python
df["grade"] = np.where(
    df["salary"] > 50000,
    "High",
    "Low"
)
```

---

## Multiple Conditions

```python
df["category"] = np.select(
    [
        df["salary"] > 80000,
        df["salary"] > 50000
    ],
    [
        "Excellent",
        "Good"
    ],
    default="Average"
)
```

---

# Pandas Best Practices

1. Avoid loops whenever possible.
2. Use vectorized operations.
3. Use category datatype for repeated strings.
4. Handle nulls early in ETL.
5. Use method chaining for readability.
6. Use groupby instead of manual aggregation.
7. Use merge instead of nested loops.
8. Profile memory usage regularly.

---

# Real-World Applications

## Data Engineering

* ETL Pipelines
* ELT Pipelines
* Data Validation
* Data Migration

## Retail

* Sales Analysis
* Customer Segmentation

## Banking

* Fraud Detection
* Customer Analytics

## Manufacturing

* Production Reporting
* Quality Analysis

## Healthcare

* Clinical Reporting
* Patient Analytics

---

# Pandas Cheat Sheet

```python
df.head()
df.tail()
df.info()
df.describe()
df.shape
df.columns
df.dtypes

df.loc[]
df.iloc[]

df.groupby()
df.merge()
df.concat()

df.dropna()
df.fillna()

df.sort_values()

df.value_counts()

df.pivot_table()

df.read_csv()
df.to_csv()

df.apply()
df.map()

df.query()

df.sample()
```

This guide covers most Pandas operations used in ETL, ELT, Data Engineering, Data Analysis, Business Intelligence, and Data Science projects.
