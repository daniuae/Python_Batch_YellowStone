# Attendance Analyzer - Step-by-Step Demonstration Guide

## Objective

This exercise helps trainees learn the following Pandas concepts through a real-world HR attendance tracking system:

* DataFrame Creation
* Column Operations
* String Manipulation
* Filtering
* GroupBy
* Aggregation
* Merge
* Boolean Masking
* Crosstab
* Reindex
* Reset Index

---

# Business Scenario

An organization records daily employee attendance.

Each record contains:

| EmployeeID | Department | Date       | Attendance |
| ---------- | ---------- | ---------- | ---------- |
| 201        | Sales      | 2024-06-01 | Present    |
| 202        | HR         | 2024-06-01 | Absent     |
| 201        | Sales      | 2024-06-02 | Leave      |

The HR team wants answers to the following questions:

1. Can we organize the raw data into a DataFrame?
2. What is the attendance percentage of each employee?
3. Who was absent?
4. Which employees are frequently absent?
5. What is the attendance summary by department?

---

# Step 1: Create Attendance DataFrame

## Input Data

```python
data = [
    [201, "Sales", "2024-06-01", "Present"],
    [202, "HR", "2024-06-01", "Absent"],
    [201, "Sales", "2024-06-02", "Leave"]
]
```

## Convert List to DataFrame

```python
import pandas as pd

df = pd.DataFrame(
    data,
    columns=[
        "EmployeeID",
        "Department",
        "Date",
        "Attendance"
    ]
)

print(df)
```

## Output

```text
   EmployeeID Department        Date Attendance
0         201      Sales  2024-06-01    Present
1         202         HR  2024-06-01     Absent
2         201      Sales  2024-06-02      Leave
```

### Key Learning

```text
Raw List
   ↓
DataFrame
```

---

# Step 2: Extract Month from Date

Before calculating attendance percentages, we need the month.

## Code

```python
df["Month"] = df["Date"].str[:7]

print(df)
```

## Output

```text
   EmployeeID Department        Date Attendance    Month
0         201      Sales  2024-06-01    Present  2024-06
1         202         HR  2024-06-01     Absent  2024-06
2         201      Sales  2024-06-02      Leave  2024-06
```

### Key Learning

```text
2024-06-01
^^^^^^^
Keep only Year-Month
```

---

# Step 3: Calculate Total Working Days

Count how many attendance records exist for each employee per month.

## Code

```python
total_days = (
    df.groupby(["EmployeeID", "Month"])
      .size()
      .reset_index(name="TotalDays")
)

print(total_days)
```

## Output

```text
   EmployeeID    Month  TotalDays
0         201  2024-06          2
1         202  2024-06          1
```

### Key Learning

Every row represents one attendance day.

```text
Employee 201

Day 1 → Present
Day 2 → Leave

Total Days = 2
```

---

# Step 4: Calculate Present Days

Filter only Present records.

## Code

```python
present_df = df[df["Attendance"] == "Present"]

present_days = (
    present_df.groupby(["EmployeeID", "Month"])
              .size()
              .reset_index(name="PresentDays")
)

print(present_days)
```

## Output

```text
   EmployeeID    Month  PresentDays
0         201  2024-06            1
```

### Key Learning

```text
Remove:
- Absent
- Leave

Keep:
- Present
```

---

# Step 5: Merge Total Days and Present Days

Combine both datasets.

## Code

```python
attendance_rate = total_days.merge(
    present_days,
    on=["EmployeeID", "Month"],
    how="left"
)

attendance_rate["PresentDays"] = (
    attendance_rate["PresentDays"]
    .fillna(0)
)
```

## Output

```text
   EmployeeID    Month  TotalDays  PresentDays
0         201  2024-06          2          1.0
1         202  2024-06          1          0.0
```

---

# Step 6: Calculate Attendance Percentage

## Formula

```text
Attendance Rate =
(Present Days / Total Days) × 100
```

## Code

```python
attendance_rate["Attendance Rate"] = (
    attendance_rate["PresentDays"]
    /
    attendance_rate["TotalDays"]
) * 100

print(
    attendance_rate[
        ["EmployeeID", "Month", "Attendance Rate"]
    ]
)
```

## Output

```text
   EmployeeID    Month  Attendance Rate
0         201  2024-06             50.0
1         202  2024-06              0.0
```

---

# Step 7: Add Absence Flag

Business Rule:

```text
Absent → 1
Others → 0
```

## Code

```python
df["IsAbsent"] = (
    df["Attendance"] == "Absent"
).astype(int)

print(df)
```

## Output

```text
   EmployeeID Department Attendance IsAbsent
0         201      Sales    Present        0
1         202         HR     Absent        1
2         201      Sales      Leave        0
```

### Key Learning

Boolean Values:

```python
True
False
```

Converted To:

```python
1
0
```

---

# Step 8: Find Employees with High Absenteeism

Suppose HR asks:

```text
Show employees absent more than 2 times.
```

## Filter Absences

```python
absent_df = df[df["Attendance"] == "Absent"]
```

## Count Absences

```python
absence_count = (
    absent_df.groupby("EmployeeID")
             .size()
             .reset_index(name="Absence Count")
)

print(absence_count)
```

## Example Output

```text
   EmployeeID  Absence Count
0         202              3
1         203              4
```

## Apply Threshold

```python
result = absence_count[
    absence_count["Absence Count"] > 2
]

print(result)
```

### Key Learning

```text
Filter Absent
      ↓
Group By Employee
      ↓
Count Absences
      ↓
Apply Threshold
```

---

# Step 9: Department-wise Attendance Summary

HR wants to know:

```text
How many Present,
Absent,
and Leave records exist
for each department?
```

---

## Create Crosstab

```python
summary = pd.crosstab(
    df["Department"],
    df["Attendance"]
)
```

## Intermediate Output

```text
Attendance  Absent Leave Present
Department
HR               1     1       0
Sales            0     1       2
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

print(summary)
```

## Final Output

```text
  Department  Present  Absent  Leave
0         HR        0       1      1
1      Sales        2       0      1
```

---

# Final Flow Diagram

```text
Raw Attendance Data
          │
          ▼
Create DataFrame
          │
          ▼
Extract Month
          │
          ▼
Attendance Rate
(Total vs Present)
          │
          ├────────► Add Absence Flag
          │
          ├────────► High Absentees
          │
          └────────► Department Summary
```

---

# Concepts Covered

| Concept            | Used In                  |
| ------------------ | ------------------------ |
| DataFrame Creation | create_attendance_df     |
| String Slicing     | Extract Month            |
| Filtering          | Present / Absent Records |
| GroupBy            | Attendance Rate          |
| Aggregation        | Count Days               |
| Merge              | Attendance Percentage    |
| Boolean Masking    | IsAbsent                 |
| Crosstab           | Department Summary       |
| Reindex            | Column Ordering          |
| Reset Index        | Final Formatting         |

---

# Real-World Takeaway

This assignment simulates a simple HR Analytics Dashboard where trainees learn how to:

* Convert raw data into structured information
* Calculate attendance KPIs
* Identify absentee patterns
* Generate departmental reports
* Apply core Pandas operations used in industry projects
