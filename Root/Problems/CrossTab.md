# Pandas Crosstab Complete Guide

## What is `pd.crosstab()`?

`pd.crosstab()` is a Pandas function used to **count occurrences between two or more categorical columns**.

Think of it as an **Excel Pivot Table** that automatically counts values.

---

# Why Do We Need Crosstab?

Suppose HR wants to know:

```text
How many employees were Present,
Absent,
and on Leave in each department?
```

Instead of writing multiple filters and groupby statements, we can generate the report using a single function:

```python
pd.crosstab()
```

---

# Real-World Example

## Input Data

| EmployeeID | Department | Attendance |
| ---------- | ---------- | ---------- |
| 201        | Sales      | Present    |
| 202        | HR         | Absent     |
| 203        | Sales      | Present    |
| 204        | HR         | Leave      |
| 205        | Sales      | Absent     |

---

# Crosstab Syntax

```python
import pandas as pd

pd.crosstab(
    df["Department"],
    df["Attendance"]
)
```

---

# Output

| Attendance | Absent | Leave | Present |
| ---------- | ------ | ----- | ------- |
| HR         | 1      | 1     | 0       |
| Sales      | 1      | 0     | 2       |

---

# How to Read the Output

## HR Department

```text
Present = 0
Absent  = 1
Leave   = 1
```

## Sales Department

```text
Present = 2
Absent  = 1
Leave   = 0
```

---

# Visual Understanding

## Input Data

```text
Department    Attendance

Sales         Present
HR            Absent
Sales         Present
HR            Leave
Sales         Absent
```

---

## Crosstab Transformation

```text
                Attendance

Department    Present  Absent  Leave

Sales             2       1       0
HR                0       1       1
```

---

# Memory Trick

Think:

```text
Cross + Table
```

We are crossing:

```text
Rows × Columns
```

Example:

```text
Department × Attendance
```

Result:

```text
Count Matrix
```

---

# Generic Syntax

```python
pd.crosstab(
    row_category,
    column_category
)
```

---

# Example 1: Department vs Attendance

```python
pd.crosstab(
    df["Department"],
    df["Attendance"]
)
```

Output:

```text
            Present  Absent  Leave

HR              0       1      1
Sales           2       1      0
```

---

# Example 2: Gender vs Department

```python
pd.crosstab(
    df["Gender"],
    df["Department"]
)
```

Output:

| Gender | HR | IT | Sales |
| ------ | -- | -- | ----- |
| Female | 5  | 7  | 4     |
| Male   | 3  | 10 | 6     |

---

# Example 3: Product vs Region

```python
pd.crosstab(
    df["Product"],
    df["Region"]
)
```

Output:

| Product | North | South |
| ------- | ----- | ----- |
| Mobile  | 25    | 15    |
| Laptop  | 10    | 20    |

---

# SQL Equivalent

Suppose we want Department-wise attendance counts.

In SQL:

```sql
SELECT
    Department,
    COUNT(CASE WHEN Attendance='Present' THEN 1 END) AS Present,
    COUNT(CASE WHEN Attendance='Absent' THEN 1 END) AS Absent,
    COUNT(CASE WHEN Attendance='Leave' THEN 1 END) AS Leave
FROM Attendance
GROUP BY Department;
```

In Pandas:

```python
pd.crosstab(
    df["Department"],
    df["Attendance"]
)
```

One line does the work of an entire SQL query.

---

# Crosstab with Row Totals

## Syntax

```python
pd.crosstab(
    df["Department"],
    df["Attendance"],
    margins=True
)
```

---

## Output

```text
Attendance  Present  Absent  Leave  All

HR              0       1      1     2
Sales           2       1      0     3
All             2       2      1     5
```

---

# Crosstab with Percentages

## Syntax

```python
pd.crosstab(
    df["Department"],
    df["Attendance"],
    normalize=True
)
```

---

## Output

```text
Attendance  Present  Absent  Leave

HR           0.00     0.20   0.20
Sales        0.40     0.20   0.00
```

---

# Crosstab in Attendance Analyzer

## Original Code

```python
summary = pd.crosstab(
    df["Department"],
    df["Attendance"]
)
```

---

## Reorder Columns

```python
summary = summary.reindex(
    columns=["Present", "Absent", "Leave"],
    fill_value=0
)
```

---

## Reset Index

```python
summary = summary.reset_index()
```

---

## Final Output

```text
  Department  Present  Absent  Leave

0         HR        0       1      1
1      Sales        2       1      0
```

---

# When Should You Use Crosstab?

Use `pd.crosstab()` when you need:

* Attendance Summary
* Gender Distribution
* Product Sales Summary
* Survey Results
* Department Reports
* Category Comparison Reports
* Dashboard Metrics

---

# Crosstab vs GroupBy

## GroupBy

```python
df.groupby("Department").size()
```

Output:

```text
HR       2
Sales    3
```

Counts only one dimension.

---

## Crosstab

```python
pd.crosstab(
    df["Department"],
    df["Attendance"]
)
```

Output:

```text
            Present  Absent  Leave

HR              0       1      1
Sales           2       1      0
```

Counts combinations of dimensions.

---

# Exam Shortcut

Whenever you see:

```text
Count categories against categories
```

Think:

```python
pd.crosstab()
```

---

# Quick Reference Cheat Sheet

| Requirement              | Solution        |
| ------------------------ | --------------- |
| Department vs Attendance | `pd.crosstab()` |
| Gender vs Department     | `pd.crosstab()` |
| Product vs Region        | `pd.crosstab()` |
| Grade vs Subject         | `pd.crosstab()` |
| Employee vs Shift        | `pd.crosstab()` |

---

# Memory Formula

```text
Need Counts?
       +
Rows vs Columns?

= Crosstab
```

---

# One-Line Definition

```text
pd.crosstab() creates a matrix that counts occurrences between categories.
```

---

# Interview Answer

If asked:

> What is Crosstab in Pandas?

Answer:

```text
Crosstab is a Pandas function used to calculate frequency counts between two or more categorical variables. It is similar to an Excel Pivot Table and is commonly used for summary reports and category analysis.
```
