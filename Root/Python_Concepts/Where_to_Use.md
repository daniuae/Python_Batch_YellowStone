# Understanding `[ ]`, `{ }`, and `( )` in Pandas

One of the biggest challenges for beginners in Pandas is understanding **when to use square brackets `[ ]`, curly braces `{ }`, and parentheses `( )`**.

A simple rule is:

| Symbol | Purpose | Think Of |
|----------|----------|----------|
| `[ ]` | Selection / Access | "Get me something" |
| `{ }` | Dictionary / Mapping | "Define relationships" |
| `( )` | Function Call / Execution | "Do something" |

---

# 1. Square Brackets `[ ]`

Use square brackets when you want to:

- Select columns
- Filter rows
- Access positions
- Retrieve values

Think:

> "I want to get something."

---

## Example 1: Select a Single Column

```python
df["Salary"]
```

### Read as:

```text
Get the Salary column
```

Output:

```text
0    50000
1    60000
2    70000
```

---

## Example 2: Select Multiple Columns

```python
df[["Name", "Salary"]]
```

Notice:

```python
["Name", "Salary"]
```

is a Python list.

Output:

| Name | Salary |
|--------|---------|
| John | 50000 |
| Mary | 60000 |

---

## Example 3: Filter Rows

```python
df[df["Salary"] > 50000]
```

### Step-by-Step

Step 1:

```python
df["Salary"]
```

Output:

```text
50000
60000
70000
```

---

Step 2:

```python
df["Salary"] > 50000
```

Output:

```text
False
True
True
```

---

Step 3:

```python
df[
    df["Salary"] > 50000
]
```

Returns only matching rows.

---

## Example 4: Access Rows by Position

```python
df.iloc[0]
```

First row.

```python
df.iloc[0:5]
```

Rows 0 through 4.

---

# When to Use `[ ]`

✅ Select columns

```python
df["Salary"]
```

✅ Select multiple columns

```python
df[["Name", "Salary"]]
```

✅ Filter rows

```python
df[df["Salary"] > 50000]
```

✅ Access positions

```python
df.iloc[0]
```

---

# 2. Curly Braces `{ }`

Use curly braces when defining:

- Dictionaries
- Mappings
- Relationships
- Column rules

Think:

> "This maps to that."

---

## Example 1: Create a DataFrame

```python
df = pd.DataFrame({
    "Name": ["John", "Mary"],
    "Salary": [50000, 60000]
})
```

### Read as

```text
Name Column -> Values
Salary Column -> Values
```

---

## Example 2: Rename Columns

```python
df.rename(
    columns={
        "Salary": "MonthlySalary"
    }
)
```

Read as:

```text
Old Column -> New Column
```

---

## Example 3: Aggregation Rules

```python
df.groupby("Department").agg({
    "Salary": "sum",
    "Age": "mean"
})
```

Read as:

```text
Salary -> Sum
Age -> Mean
```

---

## Example 4: Fill Missing Values

```python
df.fillna({
    "Salary": 0,
    "Age": 30
})
```

Read as:

```text
Salary -> Replace with 0
Age -> Replace with 30
```

---

# When to Use `{ }`

✅ Creating dictionaries

```python
{
    "Name": ["John", "Mary"]
}
```

✅ Renaming columns

```python
{
    "Salary": "MonthlySalary"
}
```

✅ Aggregations

```python
{
    "Salary": "sum"
}
```

✅ Fill missing values

```python
{
    "Salary": 0
}
```

---

# 3. Parentheses `( )`

Use parentheses when:

- Calling functions
- Passing arguments
- Executing methods

Think:

> "Perform an action."

---

## Example 1: Read CSV

```python
pd.read_csv("sales.csv")
```

Function:

```python
read_csv()
```

Argument:

```python
"sales.csv"
```

---

## Example 2: Group Data

```python
df.groupby("Department")
```

Read as:

```text
Group data by Department
```

---

## Example 3: Sort Data

```python
df.sort_values(
    "Salary",
    ascending=False
)
```

---

## Example 4: Calculate Mean

```python
df["Salary"].mean()
```

Read as:

```text
Calculate average salary
```

---

# When to Use `( )`

✅ Function calls

```python
head()
```

✅ Aggregations

```python
mean()
sum()
count()
```

✅ Data transformations

```python
sort_values()
groupby()
```

---

# Combining All Three Symbols

Consider this statement:

```python
df.groupby("Department").agg({
    "Salary": "sum"
})
```

Let's break it down.

---

## Parentheses

```python
groupby("Department")
```

Call the function.

---

## Curly Braces

```python
{
    "Salary": "sum"
}
```

Define mapping.

---

## Parentheses

```python
agg(...)
```

Execute aggregation.

---

# Most Common Pandas Statement Explained

```python
df[df["Salary"] > 50000]
```

### Inner Brackets

```python
df["Salary"]
```

Select Salary column.

---

### Comparison

```python
df["Salary"] > 50000
```

Creates Boolean values.

```text
False
True
True
```

---

### Outer Brackets

```python
df[
    Boolean Series
]
```

Filter rows.

---

# Another Real Example

```python
df.rename(
    columns={
        "Salary": "MonthlySalary",
        "Age": "EmployeeAge"
    }
)
```

### Parentheses

```python
rename(...)
```

Call function.

---

### Curly Braces

```python
{
    "Salary": "MonthlySalary",
    "Age": "EmployeeAge"
}
```

Mapping definition.

---

# Real-World Business Example

Suppose you are analyzing employee salaries.

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["John", "Mary", "David"],
    "Department": ["IT", "HR", "IT"],
    "Salary": [50000, 60000, 70000]
})
```

### Find IT Employees

```python
df[df["Department"] == "IT"]
```

### Calculate Department Salary

```python
df.groupby("Department").agg({
    "Salary": "sum"
})
```

### Rename Column

```python
df.rename(
    columns={
        "Salary": "AnnualSalary"
    }
)
```

---

# Golden Memory Trick

Imagine a DataFrame is a cupboard.

---

## `[ ]` = Open a Drawer

```python
df["Salary"]
```

Get something.

---

## `{ }` = Label Stickers

```python
{
    "Salary": "MonthlySalary"
}
```

Define relationships.

---

## `( )` = Press a Button

```python
mean()
groupby()
sort_values()
```

Perform an action.

---

# Quick Reference Cheat Sheet

```python
# Select column
df["Salary"]

# Select multiple columns
df[["Name", "Salary"]]

# Filter rows
df[df["Salary"] > 50000]

# Create DataFrame
pd.DataFrame({
    "Name": ["John"],
    "Salary": [50000]
})

# Rename columns
df.rename(columns={
    "Salary": "MonthlySalary"
})

# Aggregation
df.groupby("Department").agg({
    "Salary": "sum"
})

# Function calls
df.head()
df.describe()
df.mean()
df.groupby("Department")
```

---

# Interview Shortcut

Whenever you see Pandas code, ask:

### 1. Is there `( )`?

```python
mean()
groupby()
sort_values()
```

➡ Function is being executed.

---

### 2. Is there `{ }`?

```python
{
    "Salary": "sum"
}
```

➡ Mapping or dictionary is being defined.

---

### 3. Is there `[ ]`?

```python
df["Salary"]
```

➡ Data is being selected or filtered.

---

# Final Rule

```text
[ ]  -> Select / Access Data

{ }  -> Define Mapping / Dictionary

( )  -> Execute Function / Method
```

If you remember this rule, you can understand **90% of Pandas syntax** quickly and confidently.
