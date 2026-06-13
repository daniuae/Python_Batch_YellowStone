# Pandas Lab: Positional Indexing with `iloc`

## Objective

Learn to use the **`iloc`** indexer to select and manipulate data based on **positional indexing** in Pandas.

This lab focuses on:

* Accessing specific rows and columns
* Extracting subsets of data
* Modifying values using positions
* Performing calculations on selected data
* Applying conditional filtering with `iloc`

---

# Case Study

You have a DataFrame containing employee information:

* EmployeeID
* Department
* Salary
* YearsExperience

Your goal is to analyze employee data using **positional indexing (`iloc`)**.

---

# Step 1: Import Required Libraries

```python
import pandas as pd
```

---

# Step 2: Create Employee DataFrame

## Generate Synthetic Employee Data

```python
import pandas as pd

data = {
    'EmployeeID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                   11, 12, 13, 14, 15, 16, 17, 18, 19, 20],

    'Department': [
        'IT', 'Finance', 'Finance', 'Marketing', 'IT',
        'HR', 'Finance', 'IT', 'Marketing', 'HR',
        'Finance', 'IT', 'Marketing', 'HR', 'Finance',
        'IT', 'Marketing', 'HR', 'Finance', 'IT'
    ],

    'Salary': [
        51283, 88043, 63777, 98867, 51452,
        60000, 72000, 55000, 68000, 75000,
        80000, 62000, 71000, 58000, 94000,
        67000, 73000, 61000, 89000, 65000
    ],

    'YearsExperience': [
        11, 10, 10, 1, 9,
        5, 3, 12, 2, 15,
        8, 4, 7, 6, 14,
        2, 1, 9, 11, 3
    ]
}

df = pd.DataFrame(data)

print(df.head())
```

---

## Sample Data

| EmployeeID | Department | Salary | YearsExperience |
| ---------- | ---------- | ------ | --------------- |
| 1          | IT         | 51283  | 11              |
| 2          | Finance    | 88043  | 10              |
| 3          | Finance    | 63777  | 10              |
| 4          | Marketing  | 98867  | 1               |
| 5          | IT         | 51452  | 9               |

---

# Understanding `iloc`

`iloc` stands for:

```text
Integer Location
```

It selects data based on **row and column positions**.

---

## Syntax

```python
df.iloc[row_position, column_position]
```

### Structure

```text
df.iloc[
    rows,
    columns
]
```

---

# Column Position Reference

| Position | Column          |
| -------- | --------------- |
| 0        | EmployeeID      |
| 1        | Department      |
| 2        | Salary          |
| 3        | YearsExperience |

---

# Step 3: Access Specific Rows

---

## First 5 Rows

```python
print("First 5 Rows:")
print(df.iloc[:5])
```

### Explanation

```python
df.iloc[:5]
```

Equivalent to:

```text
Rows 0 through 4
```

---

## Rows 10 Through 15

```python
print("Rows 10 to 15:")
print(df.iloc[9:15])
```

### Explanation

```python
df.iloc[9:15]
```

Selects:

```text
Rows:
9,10,11,12,13,14
```

---

# Step 4: Access Specific Columns

---

## Select First Column (EmployeeID)

```python
print("Employee IDs:")
print(df.iloc[:, 0])
```

### Explanation

```python
:
```

Means:

```text
All rows
```

```python
0
```

Means:

```text
First column
```

---

## Select Salary and Experience Columns

```python
print("Salary and Experience:")
print(df.iloc[:, 2:4])
```

### Output

| Salary | YearsExperience |
| ------ | --------------- |
| 51283  | 11              |
| 88043  | 10              |
| ...    | ...             |

### Explanation

```python
2:4
```

Selects columns:

```text
2 → Salary
3 → YearsExperience
```

---

# Step 5: Extract Specific Cells

---

## Salary of the 5th Employee

```python
print("Salary of 5th Employee:")
print(df.iloc[4, 2])
```

### Explanation

```python
Row Position = 4
Column Position = 2
```

Result:

```text
51452
```

---

## Department and Experience of the 10th Employee

```python
print("Details of 10th Employee:")
print(df.iloc[9, [1, 3]])
```

### Explanation

```python
Row = 9
Columns = [1,3]
```

Returns:

```text
Department
YearsExperience
```

---

# Step 6: Slice Rows and Columns

---

## Extract Rows 5–10 and Columns Salary & Experience

```python
print("Slice of Rows and Columns:")
print(df.iloc[5:11, 2:4])
```

### Visualization

```text
Rows      5 → 10
Columns   Salary, YearsExperience
```

---

## Every Second Row

```python
print("Every Second Row:")
print(df.iloc[::2])
```

### Explanation

```python
start : stop : step
```

```python
::2
```

Means:

```text
Take every 2nd row
```

Rows:

```text
0,2,4,6,8,10,12...
```

---

# Step 7: Modify Data Using iloc

---

## Update Salary of 3rd Employee

Original Salary:

```python
print(df.iloc[2])
```

Update:

```python
df.iloc[2, 2] = 70000
```

Verify:

```python
print(df.iloc[2])
```

### Result

```text
Salary changed from:
63777 → 70000
```

---

## Set Experience of First 5 Employees to 15

```python
df.iloc[:5, 3] = 15

print(df.head())
```

### Explanation

```python
Rows 0–4
Column 3 (YearsExperience)
```

Updated value:

```text
15
```

---

# Step 8: Conditional Access with iloc

Although `iloc` uses positions, we can combine it with Boolean conditions.

---

## Employees with Experience Greater Than 10

### Create Boolean Mask

```python
high_experience = df.iloc[:, 3] > 10
```

Result:

```text
True
False
True
...
```

---

### Filter Rows

```python
print(
    df.iloc[high_experience.values]
)
```

### Output

Employees having:

```text
YearsExperience > 10
```

---

## Employees Between Rows 5–15 With Experience < 5

### Create Condition

```python
low_experience_salaries = (
    df.iloc[5:15, 3] < 5
)
```

---

### Filter Data

```python
print(
    df.iloc[5:15][low_experience_salaries]
)
```

### Example Output

| EmployeeID | Department | Salary | YearsExperience |
| ---------- | ---------- | ------ | --------------- |
| 7          | Finance    | 72000  | 3               |
| 12         | IT         | 62000  | 4               |

---

# Complete Program

```python
import pandas as pd

data = {
    'EmployeeID': [1,2,3,4,5,6,7,8,9,10,
                   11,12,13,14,15,16,17,18,19,20],

    'Department': [
        'IT','Finance','Finance','Marketing','IT',
        'HR','Finance','IT','Marketing','HR',
        'Finance','IT','Marketing','HR','Finance',
        'IT','Marketing','HR','Finance','IT'
    ],

    'Salary': [
        51283,88043,63777,98867,51452,
        60000,72000,55000,68000,75000,
        80000,62000,71000,58000,94000,
        67000,73000,61000,89000,65000
    ],

    'YearsExperience': [
        11,10,10,1,9,
        5,3,12,2,15,
        8,4,7,6,14,
        2,1,9,11,3
    ]
}

df = pd.DataFrame(data)

print(df.iloc[:5])

print(df.iloc[9:15])

print(df.iloc[:, 0])

print(df.iloc[:, 2:4])

print(df.iloc[4, 2])

print(df.iloc[9, [1, 3]])

print(df.iloc[5:11, 2:4])

print(df.iloc[::2])

df.iloc[2, 2] = 70000

df.iloc[:5, 3] = 15

high_experience = df.iloc[:, 3] > 10

print(df.iloc[high_experience.values])

low_experience_salaries = df.iloc[5:15, 3] < 5

print(df.iloc[5:15][low_experience_salaries])
```

---

# iloc Cheat Sheet

| Operation            | Example                |
| -------------------- | ---------------------- |
| First Row            | `df.iloc[0]`           |
| First Column         | `df.iloc[:,0]`         |
| Specific Cell        | `df.iloc[3,2]`         |
| Multiple Columns     | `df.iloc[:,1:3]`       |
| Multiple Rows        | `df.iloc[5:10]`        |
| Every Second Row     | `df.iloc[::2]`         |
| Last Row             | `df.iloc[-1]`          |
| Last Column          | `df.iloc[:,-1]`        |
| Modify Cell          | `df.iloc[2,1] = value` |
| Modify Column Values | `df.iloc[:,2] = value` |

---

# Difference Between loc and iloc

| Feature           | loc               | iloc             |
| ----------------- | ----------------- | ---------------- |
| Uses Labels       | ✅ Yes             | ❌ No             |
| Uses Position     | ❌ No              | ✅ Yes            |
| Column Names      | ✅ Yes             | ❌ No             |
| Integer Positions | ❌ Not Required    | ✅ Required       |
| Common Use        | Business Analysis | Data Engineering |

### Example

```python
df.loc[0, 'Salary']
```

vs

```python
df.iloc[0, 2]
```

Both return the same value, but use different indexing methods.

---

# Real-World Applications

### HR Analytics

* Employee salary analysis
* Experience segmentation

### Data Engineering

* Extracting subsets during ETL
* Sampling data

### Machine Learning

* Train/Test splitting
* Feature selection

### Reporting

* Selecting specific metrics
* Creating custom reports

---

# Key Concepts Learned

✅ Positional Indexing (`iloc`)
✅ Row Selection
✅ Column Selection
✅ Cell Access
✅ Slicing Rows and Columns
✅ Step Indexing
✅ Data Modification
✅ Boolean Filtering with `iloc`
✅ Practical HR Analytics Examples
