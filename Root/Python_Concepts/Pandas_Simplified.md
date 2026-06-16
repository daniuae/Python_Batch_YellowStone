# Pandas for Freshers - Step-by-Step Guide

## What is Pandas?

Pandas is a Python library used for:

- Reading data
- Cleaning data
- Analyzing data
- Transforming data
- Exporting data

Think of a **Pandas DataFrame** as an Excel sheet inside Python.

---

# 1. Import Pandas

```python
import pandas as pd
```

---

# 2. Create DataFrame

## From Dictionary

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["John", "Mary", "Sam"],
    "Age": [25, 30, 22],
    "City": ["Chennai", "Bangalore", "Hyderabad"]
})

print(df)
```

Output:

| Name | Age | City |
|--------|------|------|
| John | 25 | Chennai |
| Mary | 30 | Bangalore |
| Sam | 22 | Hyderabad |

---

## From List

```python
data = [
    ["John", 25],
    ["Mary", 30],
    ["Sam", 22]
]

df = pd.DataFrame(data, columns=["Name", "Age"])
```

---

# 3. Read Files

## Read CSV

```python
df = pd.read_csv("employees.csv")
```

## Read Excel

```python
df = pd.read_excel("employees.xlsx")
```

---

# 4. View Data

## Entire Data

```python
print(df)
```

## First 5 Rows

```python
df.head()
```

## First 10 Rows

```python
df.head(10)
```

## Last 5 Rows

```python
df.tail()
```

## Shape

```python
df.shape
```

Output:

```python
(100, 5)
```

Meaning:

- 100 rows
- 5 columns

---

# 5. Understand Data

## Column Names

```python
df.columns
```

## Data Types

```python
df.dtypes
```

## Complete Information

```python
df.info()
```

## Statistics

```python
df.describe()
```

---

# 6. Select Columns

## Single Column

```python
df["Name"]
```

or

```python
df.Name
```

## Multiple Columns

```python
df[["Name", "Age"]]
```

---

# 7. Select Rows

## By Position (iloc)

### First Row

```python
df.iloc[0]
```

### First Three Rows

```python
df.iloc[0:3]
```

### Specific Row and Column

```python
df.iloc[0, 1]
```

---

## By Label (loc)

```python
df.loc[0]
```

```python
df.loc[0:2]
```

---

# 8. Filter Data

## Equal

```python
df[df["Age"] == 25]
```

## Greater Than

```python
df[df["Age"] > 25]
```

## Less Than

```python
df[df["Age"] < 25]
```

---

## Multiple Conditions

### AND

```python
df[(df["Age"] > 20) & (df["Age"] < 30)]
```

### OR

```python
df[(df["Age"] < 21) | (df["Age"] > 29)]
```

### NOT

```python
df[~(df["Age"] > 25)]
```

---

# 9. Add Columns

## Static Value

```python
df["Country"] = "India"
```

## Dynamic Value

```python
df["Bonus"] = df["Salary"] * 0.1
```

---

# 10. Update Data

## Update One Cell

```python
df.loc[0, "Age"] = 26
```

## Update Entire Column

```python
df["Age"] = df["Age"] + 1
```

---

# 11. Delete Data

## Remove Column

```python
df.drop("Salary", axis=1)
```

Permanent:

```python
df.drop("Salary", axis=1, inplace=True)
```

---

## Remove Row

```python
df.drop(0)
```

---

# 12. Rename Columns

## Single Column

```python
df.rename(columns={"Name": "Employee_Name"})
```

## Multiple Columns

```python
df.rename(columns={
    "Name": "Employee_Name",
    "Age": "Employee_Age"
})
```

---

# 13. Missing Values

## Check Missing Values

```python
df.isnull()
```

## Count Missing Values

```python
df.isnull().sum()
```

---

## Fill Missing Values

### With Zero

```python
df.fillna(0)
```

### With Text

```python
df.fillna("Unknown")
```

### Forward Fill

```python
df.fillna(method="ffill")
```

### Backward Fill

```python
df.fillna(method="bfill")
```

---

## Remove Missing Values

```python
df.dropna()
```

---

# 14. Sorting

## Ascending

```python
df.sort_values("Age")
```

## Descending

```python
df.sort_values("Age", ascending=False)
```

## Multiple Columns

```python
df.sort_values(["City", "Age"])
```

---

# 15. Unique Values

## Unique

```python
df["City"].unique()
```

## Number of Unique Values

```python
df["City"].nunique()
```

## Frequency Count

```python
df["City"].value_counts()
```

---

# 16. Aggregation Functions

## Sum

```python
df["Salary"].sum()
```

## Mean

```python
df["Salary"].mean()
```

## Maximum

```python
df["Salary"].max()
```

## Minimum

```python
df["Salary"].min()
```

## Count

```python
df["Salary"].count()
```

## Median

```python
df["Salary"].median()
```

---

# 17. GroupBy

Sample Data:

```python
df = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 40000, 45000]
})
```

---

## Sum

```python
df.groupby("Department")["Salary"].sum()
```

## Average

```python
df.groupby("Department")["Salary"].mean()
```

## Count

```python
df.groupby("Department")["Salary"].count()
```

---

## Multiple Aggregations

```python
df.groupby("Department")["Salary"].agg([
    "sum",
    "mean",
    "max",
    "min",
    "count"
])
```

---

# 18. String Operations

## Upper Case

```python
df["Name"].str.upper()
```

## Lower Case

```python
df["Name"].str.lower()
```

## Length

```python
df["Name"].str.len()
```

## Contains

```python
df["Name"].str.contains("J")
```

## Replace

```python
df["Name"].str.replace("John", "Johnny")
```

---

# 19. Date Operations

## Convert to Date

```python
df["Date"] = pd.to_datetime(df["Date"])
```

---

## Extract Year

```python
df["Date"].dt.year
```

## Extract Month

```python
df["Date"].dt.month
```

## Extract Day

```python
df["Date"].dt.day
```

## Day Name

```python
df["Date"].dt.day_name()
```

---

# 20. Apply Function

## Normal Function

```python
def calculate_bonus(salary):
    return salary * 0.1

df["Bonus"] = df["Salary"].apply(calculate_bonus)
```

---

## Lambda Function

```python
df["Bonus"] = df["Salary"].apply(
    lambda x: x * 0.1
)
```

---

# 21. Merge DataFrames

Employee Table

```python
emp = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["John", "Mary", "Sam"]
})
```

Salary Table

```python
salary = pd.DataFrame({
    "ID": [1, 2, 3],
    "Salary": [50000, 60000, 40000]
})
```

---

## Inner Join

```python
pd.merge(emp, salary, on="ID")
```

---

## Left Join

```python
pd.merge(emp, salary,
         on="ID",
         how="left")
```

---

## Right Join

```python
pd.merge(emp, salary,
         on="ID",
         how="right")
```

---

## Outer Join

```python
pd.merge(emp, salary,
         on="ID",
         how="outer")
```

---

# 22. Concatenate

## Vertical

```python
pd.concat([df1, df2])
```

## Horizontal

```python
pd.concat([df1, df2], axis=1)
```

---

# 23. Duplicate Handling

## Find Duplicates

```python
df.duplicated()
```

## Remove Duplicates

```python
df.drop_duplicates()
```

---

# 24. Export Data

## CSV

```python
df.to_csv("output.csv", index=False)
```

## Excel

```python
df.to_excel("output.xlsx", index=False)
```

---

# 25. Top 10 Pandas Commands Used in Industry

```python
pd.read_csv()

df.head()

df.info()

df.describe()

df["column"]

df[df["column"] > value]

df.groupby()

df.sort_values()

pd.merge()

df.to_csv()
```

---

# Learning Roadmap

## Day 1

- Pandas Basics
- DataFrame
- Read CSV
- View Data

## Day 2

- Columns
- Rows
- Filtering
- Sorting

## Day 3

- Missing Values
- String Functions
- Date Functions

## Day 4

- Aggregations
- GroupBy
- Apply

## Day 5

- Merge
- Join
- Concat
- Project

---

# Mini Project

Using Employee Dataset:

1. Find highest salary employee
2. Find average salary by department
3. Find employees older than 30
4. Count missing values
5. Find department with highest average salary
6. Export final report to Excel

---

# Summary

The most important Pandas concepts are:

1. Read Data
2. View Data
3. Select Data
4. Filter Data
5. Modify Data
6. Group Data
7. Merge Data
8. Export Data

Master these 8 topics and you can perform most real-world data analysis tasks using Pandas.
