# SQL vs Pandas Complete Guide for Data Engineers

# Table of Contents

1. Introduction
2. SQL vs Pandas Overview
3. Sample Dataset
4. SELECT
5. WHERE
6. ORDER BY
7. DISTINCT
8. LIMIT / TOP
9. GROUP BY
10. HAVING
11. JOINs
12. CASE WHEN
13. Window Functions
14. CTEs
15. UNION
16. Pivot
17. Missing Data Handling
18. Date Functions
19. String Functions
20. Real Business Scenarios
21. Performance Considerations
22. Interview Questions

---

# Introduction

SQL and Pandas solve similar data-processing problems.

SQL works directly on databases.

Pandas works on data loaded into memory.

Data Engineers commonly use both:

* SQL → Extract data
* Pandas → Transform and Analyze data

---

# Sample Dataset

## Employees

```python
import pandas as pd

employees = pd.DataFrame({
    "emp_id":[1,2,3,4,5],
    "name":["Raj","John","Mary","David","Priya"],
    "department":["IT","HR","IT","Finance","IT"],
    "salary":[80000,50000,90000,70000,85000]
})

employees
```

| emp_id | name  | department | salary |
| ------ | ----- | ---------- | ------ |
| 1      | Raj   | IT         | 80000  |
| 2      | John  | HR         | 50000  |
| 3      | Mary  | IT         | 90000  |
| 4      | David | Finance    | 70000  |
| 5      | Priya | IT         | 85000  |

---

# SELECT

## SQL

```sql
SELECT * FROM employees;
```

## Pandas

```python
employees
```

---

## Select Specific Columns

### SQL

```sql
SELECT name, salary
FROM employees;
```

### Pandas

```python
employees[["name","salary"]]
```

---

# WHERE

## SQL

```sql
SELECT *
FROM employees
WHERE salary > 70000;
```

## Pandas

```python
employees[employees["salary"] > 70000]
```

---

## Multiple Conditions

### SQL

```sql
SELECT *
FROM employees
WHERE department='IT'
AND salary > 80000;
```

### Pandas

```python
employees[
    (employees["department"]=="IT")
    &
    (employees["salary"] > 80000)
]
```

---

# ORDER BY

## SQL

```sql
SELECT *
FROM employees
ORDER BY salary DESC;
```

## Pandas

```python
employees.sort_values(
    "salary",
    ascending=False
)
```

---

# DISTINCT

## SQL

```sql
SELECT DISTINCT department
FROM employees;
```

## Pandas

```python
employees["department"].unique()
```

or

```python
employees["department"].drop_duplicates()
```

---

# LIMIT

## SQL

```sql
SELECT *
FROM employees
LIMIT 3;
```

## Pandas

```python
employees.head(3)
```

---

# GROUP BY

## Business Problem

Find average salary by department.

### SQL

```sql
SELECT department,
       AVG(salary) avg_salary
FROM employees
GROUP BY department;
```

### Pandas

```python
employees.groupby(
    "department"
)["salary"].mean()
```

---

## Multiple Aggregations

### SQL

```sql
SELECT department,
       COUNT(*) cnt,
       AVG(salary) avg_sal,
       MAX(salary) max_sal
FROM employees
GROUP BY department;
```

### Pandas

```python
employees.groupby(
    "department"
).agg({
    "salary":["count","mean","max"]
})
```

---

# HAVING

## SQL

```sql
SELECT department,
       AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 75000;
```

## Pandas

```python
result = employees.groupby(
    "department"
)["salary"].mean()

result[result > 75000]
```

---

# INNER JOIN

## Orders Dataset

```python
orders = pd.DataFrame({
    "order_id":[101,102,103],
    "emp_id":[1,3,5],
    "sales":[5000,10000,7000]
})
```

---

### SQL

```sql
SELECT *
FROM employees e
INNER JOIN orders o
ON e.emp_id = o.emp_id;
```

### Pandas

```python
pd.merge(
    employees,
    orders,
    on="emp_id",
    how="inner"
)
```

---

# LEFT JOIN

### SQL

```sql
SELECT *
FROM employees e
LEFT JOIN orders o
ON e.emp_id = o.emp_id;
```

### Pandas

```python
pd.merge(
    employees,
    orders,
    on="emp_id",
    how="left"
)
```

---

# RIGHT JOIN

### SQL

```sql
SELECT *
FROM employees e
RIGHT JOIN orders o
ON e.emp_id = o.emp_id;
```

### Pandas

```python
pd.merge(
    employees,
    orders,
    on="emp_id",
    how="right"
)
```

---

# FULL OUTER JOIN

### SQL

```sql
SELECT *
FROM employees e
FULL OUTER JOIN orders o
ON e.emp_id=o.emp_id;
```

### Pandas

```python
pd.merge(
    employees,
    orders,
    on="emp_id",
    how="outer"
)
```

---

# CASE WHEN

## SQL

```sql
SELECT name,
       salary,
       CASE
          WHEN salary > 80000
          THEN 'High'
          ELSE 'Medium'
       END grade
FROM employees;
```

## Pandas

```python
employees["grade"] = employees[
    "salary"
].apply(
    lambda x:
    "High"
    if x > 80000
    else "Medium"
)
```

---

# Window Functions

## Running Total

### SQL

```sql
SELECT emp_id,
       salary,
       SUM(salary)
       OVER(
          ORDER BY emp_id
       ) running_total
FROM employees;
```

### Pandas

```python
employees[
    "running_total"
] = employees[
    "salary"
].cumsum()
```

---

# ROW_NUMBER

### SQL

```sql
SELECT *,
       ROW_NUMBER()
       OVER(
         ORDER BY salary DESC
       )
FROM employees;
```

### Pandas

```python
employees[
    "row_num"
] = range(
    1,
    len(employees)+1
)
```

---

# RANK

### SQL

```sql
RANK()
OVER(
ORDER BY salary DESC
)
```

### Pandas

```python
employees[
    "rank"
] = employees[
    "salary"
].rank(
    ascending=False
)
```

---

# LAG

### SQL

```sql
LAG(salary)
OVER(
ORDER BY emp_id
)
```

### Pandas

```python
employees[
    "prev_salary"
] = employees[
    "salary"
].shift(1)
```

---

# LEAD

### SQL

```sql
LEAD(salary)
OVER(
ORDER BY emp_id
)
```

### Pandas

```python
employees[
    "next_salary"
] = employees[
    "salary"
].shift(-1)
```

---

# CTE

## SQL

```sql
WITH high_salary AS
(
SELECT *
FROM employees
WHERE salary > 80000
)
SELECT *
FROM high_salary;
```

## Pandas

```python
high_salary = employees[
    employees["salary"] > 80000
]

high_salary
```

---

# UNION

## SQL

```sql
SELECT * FROM table1
UNION
SELECT * FROM table2;
```

## Pandas

```python
pd.concat(
    [df1,df2]
).drop_duplicates()
```

---

# PIVOT

## SQL

```sql
SELECT *
FROM sales
PIVOT
(
SUM(revenue)
FOR month IN
(
Jan,Feb,Mar
)
)
```

## Pandas

```python
pd.pivot_table(
    sales,
    index="product",
    columns="month",
    values="revenue",
    aggfunc="sum"
)
```

---

# Missing Values

## SQL

```sql
COALESCE(salary,0)
```

## Pandas

```python
employees[
    "salary"
].fillna(0)
```

---

# Date Functions

## SQL

```sql
YEAR(order_date)
MONTH(order_date)
DAY(order_date)
```

## Pandas

```python
df["order_date"].dt.year

df["order_date"].dt.month

df["order_date"].dt.day
```

---

# String Functions

## SQL

```sql
UPPER(name)
LOWER(name)
```

## Pandas

```python
df["name"].str.upper()

df["name"].str.lower()
```

---

# Real Business Scenario 1

## Top 3 Customers by Revenue

### SQL

```sql
SELECT customer_id,
       SUM(revenue)
FROM sales
GROUP BY customer_id
ORDER BY SUM(revenue) DESC
LIMIT 3;
```

### Pandas

```python
sales.groupby(
    "customer_id"
)["revenue"].sum() \
.sort_values(
    ascending=False
).head(3)
```

---

# Real Business Scenario 2

## Monthly Revenue Trend

### SQL

```sql
SELECT MONTH(order_date),
       SUM(revenue)
FROM sales
GROUP BY MONTH(order_date);
```

### Pandas

```python
sales.groupby(
    sales["order_date"].dt.month
)["revenue"].sum()
```

---

# Real Business Scenario 3

## Customer Retention Analysis

### SQL

```sql
COUNT(DISTINCT customer_id)
```

### Pandas

```python
sales[
    "customer_id"
].nunique()
```

---

# Performance Considerations

| Operation          | SQL       | Pandas    |
| ------------------ | --------- | --------- |
| Billion Rows       | Excellent | Poor      |
| In-memory Analysis | Limited   | Excellent |
| ETL Development    | Good      | Excellent |
| Analytics          | Good      | Excellent |
| Dashboard Backend  | Excellent | Good      |
| Machine Learning   | Limited   | Excellent |

---

# When to Use SQL

Use SQL when:

* Data lives in a database
* Dataset > RAM
* Large joins
* Data warehouse queries
* Production reporting

Examples:

* PostgreSQL
* Oracle
* Snowflake
* Redshift
* BigQuery

---

# When to Use Pandas

Use Pandas when:

* Data fits in memory
* Exploratory analysis
* Data cleaning
* Feature engineering
* Machine learning preparation
* Python automation

---

# SQL to Pandas Quick Mapping

| SQL        | Pandas         |
| ---------- | -------------- |
| SELECT     | df[]           |
| WHERE      | Boolean Filter |
| GROUP BY   | groupby()      |
| ORDER BY   | sort_values()  |
| JOIN       | merge()        |
| UNION      | concat()       |
| DISTINCT   | unique()       |
| COUNT      | count()        |
| SUM        | sum()          |
| AVG        | mean()         |
| MAX        | max()          |
| MIN        | min()          |
| CASE WHEN  | apply()        |
| RANK       | rank()         |
| ROW_NUMBER | range()        |
| LAG        | shift()        |
| LEAD       | shift(-1)      |
| PIVOT      | pivot_table()  |

---

# Data Engineer Interview Questions

1. Difference between loc and iloc.
2. Difference between merge and join.
3. Difference between apply and vectorization.
4. How to handle large CSV files?
5. How does groupby work internally?
6. Difference between rank and dense_rank?
7. How would you optimize Pandas code?
8. How would you perform SQL window functions in Pandas?
9. Difference between concat and merge?
10. When would you choose SQL over Pandas?

# Key Takeaway

SQL and Pandas are complementary, not competing technologies.

A modern Data Engineer typically:

1. Extracts data using SQL.
2. Processes data using Pandas.
3. Loads data into a warehouse or data lake.
4. Builds dashboards and ML pipelines using the transformed data.
