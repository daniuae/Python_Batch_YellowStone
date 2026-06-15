# Attendance Analyzer - Pandas Cheat Sheet for Exams

## Rule #1: Don't Memorize Programs

Memorize these patterns:

```text
Create
Filter
Group
Aggregate
Merge
Transform
Pivot/Crosstab
```

Almost every Data Engineering, Data Analysis, and Pandas interview question uses these patterns.

---

# Complete Keyword Cheat Sheet

| Keyword        | Purpose                 | Memory Trick              |
| -------------- | ----------------------- | ------------------------- |
| pd.DataFrame() | Create table            | List → Table              |
| columns=       | Set column names        | Name the fields           |
| df["col"]      | Access column           | Pick one column           |
| .str[:7]       | Slice string            | Extract part of text      |
| groupby()      | Group records           | Put similar rows together |
| size()         | Count rows              | Count records             |
| reset_index()  | Convert index to column | Flatten output            |
| name=          | Name aggregation column | Give count a name         |
| merge()        | Join two DataFrames     | SQL Join                  |
| fillna()       | Replace null values     | Fill blanks               |
| astype(int)    | Convert datatype        | Boolean → Number          |
| reindex()      | Reorder columns         | Arrange columns           |
| crosstab()     | Create summary matrix   | Excel Pivot Table         |
| ==             | Comparison              | Check equality            |
| []             | Filtering               | Apply condition           |
| how="left"     | Left Join               | Keep left table           |

---

# Pattern 1: Create DataFrame

## Syntax

```python
df = pd.DataFrame(
    data,
    columns=[
        "EmployeeID",
        "Department",
        "Date",
        "Attendance"
    ]
)
```

## Logic

```text
Raw List
    ↓
DataFrame
```

## Memory Trick

Think:

```text
Data + Columns = DataFrame
```

Formula:

```text
DataFrame = Data + Headers
```

---

# Pattern 2: Select Column

## Syntax

```python
df["Date"]
```

## Logic

```text
Pick one column
```

Visual:

```text
DataFrame
   ↓
Date Column
```

Memory:

```text
[] means Pick
```

---

# Pattern 3: Extract Month

## Syntax

```python
df["Month"] = df["Date"].str[:7]
```

## Logic

Date:

```text
2024-06-01
```

Take:

```text
2024-06
```

Ignore:

```text
-01
```

## Memory Trick

```text
str = string operation

[:7]
means first 7 characters
```

Visual:

```text
0 1 2 3 4 5 6
2 0 2 4 - 0 6
```

---

# Pattern 4: Filter Data

## Syntax

```python
present_df = df[
    df["Attendance"] == "Present"
]
```

## Logic

Keep only:

```text
Present
```

Remove:

```text
Absent
Leave
```

## Memory Trick

```text
Condition inside []
```

Formula:

```text
DataFrame[Condition]
```

Examples:

```python
df[df["Salary"] > 50000]

df[df["Department"] == "IT"]

df[df["Attendance"] == "Present"]
```

---

# Pattern 5: Group By

## Syntax

```python
df.groupby(
    ["EmployeeID", "Month"]
)
```

## Logic

Group similar records together.

Example:

```text
201 June
201 June
201 June

→ One Group
```

Memory:

```text
groupby()
means
Put Similar Things Together
```

---

# Pattern 6: Count Records

## Syntax

```python
.size()
```

## Logic

Count rows.

Example:

```text
201
201
201
```

Count:

```text
3
```

Memory:

```text
size()
means
How Many?
```

---

# Pattern 7: Reset Index

## Syntax

```python
.reset_index()
```

## Logic

GroupBy creates special index.

Convert back to normal DataFrame.

Before:

```text
EmployeeID
201
202
```

After:

```text
EmployeeID Count
201        3
202        2
```

Memory:

```text
Flatten Result
```

---

# Pattern 8: Name Aggregation Column

## Syntax

```python
.reset_index(
    name="TotalDays"
)
```

## Logic

Instead of:

```text
0
1
2
```

Give meaningful name:

```text
TotalDays
```

Memory:

```text
name=
Rename Result Column
```

---

# Pattern 9: Complete GroupBy Formula

## Syntax

```python
result = (
    df.groupby(
        ["EmployeeID", "Month"]
    )
    .size()
    .reset_index(
        name="TotalDays"
    )
)
```

## Exam Memory

```text
Group
 ↓
Count
 ↓
Reset
 ↓
Name
```

Golden Formula:

```python
df.groupby(...)
  .size()
  .reset_index(name="Count")
```

---

# Pattern 10: Merge DataFrames

## Syntax

```python
result = df1.merge(
    df2,
    on=["EmployeeID","Month"],
    how="left"
)
```

## Logic

Join two tables.

Visual:

```text
Table A
+
Table B
=
Combined Table
```

Memory:

```text
merge = SQL Join
```

---

# Pattern 11: Fill Missing Values

## Syntax

```python
df["PresentDays"] = (
    df["PresentDays"]
    .fillna(0)
)
```

## Logic

Replace:

```text
NaN
```

with

```text
0
```

Memory:

```text
fillna()
means
Fill Empty Cells
```

---

# Pattern 12: Boolean to Integer

## Syntax

```python
(
    df["Attendance"] == "Absent"
).astype(int)
```

## Logic

Before:

```text
True
False
```

After:

```text
1
0
```

Memory:

```text
astype(int)

Convert To Number
```

---

# Pattern 13: Attendance Rate Formula

Formula:

```text
Attendance Rate =
(Present Days / Total Days) × 100
```

Code:

```python
df["Attendance Rate"] = (
    df["PresentDays"]
    /
    df["TotalDays"]
) * 100
```

Memory:

```text
Part / Whole × 100
```

---

# Pattern 14: Crosstab

## Syntax

```python
pd.crosstab(
    df["Department"],
    df["Attendance"]
)
```

## Logic

Convert:

```text
Department
Attendance
```

into

```text
Department Present Absent Leave
```

Memory:

```text
Crosstab
=
Excel Pivot Table
```

---

# Pattern 15: Reindex

## Syntax

```python
summary.reindex(
    columns=[
        "Present",
        "Absent",
        "Leave"
    ],
    fill_value=0
)
```

## Logic

Arrange columns.

Before:

```text
Absent Leave Present
```

After:

```text
Present Absent Leave
```

Memory:

```text
Reindex
=
Rearrange
```

---

# Ultimate Exam Formula

Whenever you see a Pandas question:

```text
Step 1 → Create DataFrame

Step 2 → Filter

Step 3 → GroupBy

Step 4 → Aggregate

Step 5 → Merge (if required)

Step 6 → Calculate

Step 7 → Format Output
```

Visual Memory:

```text
Raw Data
    ↓
Filter
    ↓
Group
    ↓
Count/Sum/Avg
    ↓
Merge
    ↓
Calculation
    ↓
Final Output
```

---

# 90% Pandas Interview Questions Use Only These Patterns

```python
pd.DataFrame()

df["column"]

df[condition]

groupby()

size()

count()

sum()

mean()

reset_index()

merge()

fillna()

astype()

crosstab()

reindex()
```

Master these 12-15 keywords and you can solve most beginner-to-intermediate Pandas coding assessments, ETL transformations, and Data Engineering interview problems.
