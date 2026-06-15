# Attendance Analyzer: Pandas vs SQL Cheat Sheet

## Why Learn This Comparison?

Most Data Engineers, Data Analysts, ETL Developers, and QA Engineers already know SQL.

The easiest way to learn Pandas is:

```text
Don't learn Pandas from scratch.

Translate SQL → Pandas
```

Think:

```text
Pandas = SQL on DataFrames
```

---

# Attendance Data

## Sample Data

| EmployeeID | Department | Date       | Attendance |
| ---------- | ---------- | ---------- | ---------- |
| 201        | Sales      | 2024-06-01 | Present    |
| 202        | HR         | 2024-06-01 | Absent     |
| 201        | Sales      | 2024-06-02 | Leave      |
| 203        | IT         | 2024-06-01 | Present    |

---

# Mental Model

| SQL       | Pandas               |
| --------- | -------------------- |
| Table     | DataFrame            |
| Column    | DataFrame Column     |
| Row       | Row                  |
| SELECT    | df[]                 |
| WHERE     | Filtering            |
| GROUP BY  | groupby()            |
| COUNT     | size(), count()      |
| SUM       | sum()                |
| AVG       | mean()               |
| JOIN      | merge()              |
| CASE WHEN | np.where(), astype() |
| PIVOT     | crosstab()           |

---

# 1. Create DataFrame

## SQL

```sql
CREATE TABLE Attendance (
    EmployeeID INT,
    Department VARCHAR(50),
    Date DATE,
    Attendance VARCHAR(20)
);
```

---

## Pandas

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

---

## Memory Trick

```text
SQL
Create Table

Pandas
Create DataFrame
```

---

# 2. Select Columns

## SQL

```sql
SELECT EmployeeID, Department
FROM Attendance;
```

---

## Pandas

```python
df[
    ["EmployeeID", "Department"]
]
```

---

## Memory Trick

```text
SQL
SELECT

Pandas
[]
```

---

# 3. Filter Rows

## Requirement

Show Present Employees.

---

## SQL

```sql
SELECT *
FROM Attendance
WHERE Attendance='Present';
```

---

## Pandas

```python
df[
    df["Attendance"] == "Present"
]
```

---

## Memory Trick

```text
SQL
WHERE

Pandas
Condition Inside []
```

Formula:

```python
df[df["column"] == value]
```

---

# 4. Add Month Column

## SQL

```sql
SELECT
    LEFT(Date,7) AS Month
FROM Attendance;
```

---

## Pandas

```python
df["Month"] = df["Date"].str[:7]
```

---

## Memory Trick

```text
SQL
LEFT()

Pandas
str[:7]
```

---

# 5. Count Attendance Records

## SQL

```sql
SELECT
    EmployeeID,
    COUNT(*)
FROM Attendance
GROUP BY EmployeeID;
```

---

## Pandas

```python
df.groupby(
    "EmployeeID"
).size()
```

---

## Memory Trick

```text
SQL
GROUP BY + COUNT

Pandas
groupby() + size()
```

---

# 6. Monthly Attendance Rate

## SQL

### Total Days

```sql
SELECT
    EmployeeID,
    LEFT(Date,7) AS Month,
    COUNT(*) AS TotalDays
FROM Attendance
GROUP BY EmployeeID,
         LEFT(Date,7);
```

---

### Present Days

```sql
SELECT
    EmployeeID,
    LEFT(Date,7) AS Month,
    COUNT(*) AS PresentDays
FROM Attendance
WHERE Attendance='Present'
GROUP BY EmployeeID,
         LEFT(Date,7);
```

---

## Pandas

```python
total_days = (
    df.groupby(
        ["EmployeeID","Month"]
    )
    .size()
    .reset_index(
        name="TotalDays"
    )
)

present_days = (
    df[
        df["Attendance"]=="Present"
    ]
    .groupby(
        ["EmployeeID","Month"]
    )
    .size()
    .reset_index(
        name="PresentDays"
    )
)
```

---

# 7. Join Results

## SQL

```sql
SELECT *
FROM TotalDays t
LEFT JOIN PresentDays p
ON t.EmployeeID = p.EmployeeID
AND t.Month = p.Month;
```

---

## Pandas

```python
result = total_days.merge(
    present_days,
    on=["EmployeeID","Month"],
    how="left"
)
```

---

## Memory Trick

```text
SQL
JOIN

Pandas
merge()
```

Formula:

```python
df1.merge(
    df2,
    on=keys,
    how="left"
)
```

---

# 8. Replace NULL Values

## SQL

```sql
COALESCE(PresentDays,0)
```

---

## Pandas

```python
result["PresentDays"] = (
    result["PresentDays"]
    .fillna(0)
)
```

---

## Memory Trick

```text
SQL
COALESCE()

Pandas
fillna()
```

---

# 9. Calculate Attendance Rate

## SQL

```sql
(
 PresentDays * 100.0
 /
 TotalDays
) AS AttendanceRate
```

---

## Pandas

```python
result["Attendance Rate"] = (
    result["PresentDays"]
    /
    result["TotalDays"]
) * 100
```

---

# 10. CASE WHEN Logic

## Requirement

Create IsAbsent Flag.

---

## SQL

```sql
CASE
    WHEN Attendance='Absent'
    THEN 1
    ELSE 0
END AS IsAbsent
```

---

## Pandas

```python
(
    df["Attendance"]=="Absent"
).astype(int)
```

---

## Memory Trick

```text
SQL
CASE WHEN

Pandas
Boolean + astype(int)
```

---

# 11. High Absentees

## SQL

```sql
SELECT
    EmployeeID,
    COUNT(*) AS AbsenceCount
FROM Attendance
WHERE Attendance='Absent'
GROUP BY EmployeeID
HAVING COUNT(*) > 2;
```

---

## Pandas

```python
(
    df[
        df["Attendance"]=="Absent"
    ]
    .groupby("EmployeeID")
    .size()
    .reset_index(
        name="Absence Count"
    )
)
```

Apply threshold:

```python
result[
    result["Absence Count"] > 2
]
```

---

## Memory Trick

```text
SQL
HAVING

Pandas
Filter After GroupBy
```

---

# 12. Department Attendance Summary

## SQL

```sql
SELECT
    Department,

    COUNT(
        CASE
        WHEN Attendance='Present'
        THEN 1
        END
    ) AS Present,

    COUNT(
        CASE
        WHEN Attendance='Absent'
        THEN 1
        END
    ) AS Absent,

    COUNT(
        CASE
        WHEN Attendance='Leave'
        THEN 1
        END
    ) AS Leave

FROM Attendance
GROUP BY Department;
```

---

## Pandas

```python
pd.crosstab(
    df["Department"],
    df["Attendance"]
)
```

---

## Memory Trick

```text
Complex SQL Pivot

↓

One-Line Crosstab
```

---

# SQL to Pandas Translation Table

| SQL              | Pandas               |
| ---------------- | -------------------- |
| SELECT *         | df                   |
| SELECT col       | df["col"]            |
| SELECT col1,col2 | df[["col1","col2"]]  |
| WHERE            | df[condition]        |
| GROUP BY         | groupby()            |
| COUNT(*)         | size()               |
| COUNT(col)       | count()              |
| SUM()            | sum()                |
| AVG()            | mean()               |
| ORDER BY         | sort_values()        |
| DISTINCT         | unique()             |
| JOIN             | merge()              |
| LEFT JOIN        | merge(how="left")    |
| INNER JOIN       | merge(how="inner")   |
| CASE WHEN        | astype(), np.where() |
| COALESCE         | fillna()             |
| PIVOT            | crosstab()           |
| LIMIT            | head()               |

---

# Ultimate Exam Memory Formula

When solving Attendance Analyzer:

```text
SQL Thinking

SELECT
WHERE
GROUP BY
COUNT
JOIN
CASE
PIVOT
```

Translate to Pandas:

```text
DataFrame
Filter
groupby()
size()
merge()
astype()
crosstab()
```

---

# The Golden Mapping

```text
SQL Developer Thinking
        ↓
SELECT
WHERE
GROUP BY
JOIN
CASE
PIVOT
        ↓
Pandas Thinking
        ↓
[]
Filter
groupby()
merge()
astype()
crosstab()
```

If you already know SQL well, you are usually 70–80% of the way toward becoming productive with Pandas because most Pandas transformations are direct translations of SQL operations.
