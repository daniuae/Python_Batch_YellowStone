# Question Code: Q330

## Problem Statement

An organization tracks daily attendance logs for its employees. Each log entry includes:

* Employee ID
* Department
* Date
* Attendance Status (`Present`, `Absent`, `Leave`)

Your task is to perform analysis over this attendance data to identify attendance rates, patterns, and departmental summaries.

---

## Class Declaration

```python
class AttendanceAnalyzer:
```

> No need to use an `__init__()` method.

If needed:

```python
def __init__(self):
    pass
```

---

## 1. Create Attendance DataFrame

### Function Prototype

```python
def create_attendance_df(self, data: list) -> pd.DataFrame:
```

### Description

Converts raw attendance logs into a structured Pandas DataFrame.

### Example Input

```python
create_attendance_df([
    [201, "Sales", "2024-06-01", "Present"],
    [202, "HR", "2024-06-01", "Absent"],
    [201, "Sales", "2024-06-02", "Leave"]
])
```

### Expected Output

| EmployeeID | Department | Date       | Attendance |
| ---------- | ---------- | ---------- | ---------- |
| 201        | Sales      | 2024-06-01 | Present    |
| 202        | HR         | 2024-06-01 | Absent     |
| 201        | Sales      | 2024-06-02 | Leave      |

### Implementation Flow

* Create a DataFrame using columns:

```python
["EmployeeID", "Department", "Date", "Attendance"]
```

* Ensure `Date` remains a string (do not convert to datetime).

---

## 2. Calculate Monthly Attendance Rate per Employee

### Function Prototype

```python
def compute_monthly_attendance_rate(self, df: pd.DataFrame) -> pd.DataFrame:
```

### Description

Returns a DataFrame showing percentage of days present per employee per month.

### Expected Output

| EmployeeID | Month   | Attendance Rate |
| ---------- | ------- | --------------- |
| 201        | 2024-06 | 50.0            |
| 202        | 2024-06 | 0.0             |

### Implementation Flow

* Extract Year-Month using:

```python
df["Date"].str[:7]
```

* Group by:

```python
EmployeeID, Month
```

* Count total attendance records.
* Create a new DataFrame containing only `Present` records.
* Merge total and present counts.
* Compute:

```python
Attendance Rate = (Present / Total) * 100
```

---

## 3. Add Absence Flag Column

### Function Prototype

```python
def add_absence_flag(self, df: pd.DataFrame) -> pd.DataFrame:
```

### Description

Adds a column `IsAbsent`.

### Rules

* `1` if Attendance = `"Absent"`
* `0` otherwise

### Expected Output

| EmployeeID | Department | Date       | Attendance | IsAbsent |
| ---------- | ---------- | ---------- | ---------- | -------- |
| 201        | Sales      | 2024-06-01 | Present    | 0        |
| 202        | HR         | 2024-06-01 | Absent     | 1        |
| 201        | Sales      | 2024-06-02 | Leave      | 0        |

### Implementation Flow

```python
df["Attendance"] == "Absent"
```

Convert boolean values to integers.

---

## 4. Filter Employees with High Absenteeism

### Function Prototype

```python
def high_absentees(self, df: pd.DataFrame, threshold: int) -> pd.DataFrame:
```

### Description

Returns employees having more than `threshold` absences.

### Example Input

```python
high_absentees(df, 1)
```

### Expected Output

| EmployeeID | Absence Count |
| ---------- | ------------- |
| 202        | 3             |
| 203        | 4             |

### Implementation Flow

* Filter rows where Attendance = `"Absent"`
* Group by EmployeeID
* Count absences
* Return only records where:

```python
Absence Count > threshold
```

---

## 5. Department-wise Attendance Summary

### Function Prototype

```python
def department_attendance_summary(self, df: pd.DataFrame) -> pd.DataFrame:
```

### Description

Returns counts of each attendance type per department.

### Expected Output

| Department | Present | Absent | Leave |
| ---------- | ------- | ------ | ----- |
| HR         | 0       | 2      | 1     |
| Sales      | 3       | 1      | 2     |

### Implementation Flow

* Use:

```python
pd.crosstab()
```

with:

```python
Department
Attendance
```

* Set column name to:

```python
None
```

* Reindex columns as:

```python
["Present", "Absent", "Leave"]
```

* Replace missing values with `0`
* Reset index
* Return resulting DataFrame
            .size()
            .reset_index(name="Present")
        )

        result = pd.merge(
            total_days,
            present_days,
            on=["EmployeeID", "Month"],
            how="left"
        )

        result["Present"] = result["Present"].fillna(0)

        result["Attendance Rate"] = (
            result["Present"] / result["Total"]
        ) * 100

        return result[["EmployeeID", "Month", "Attendance Rate"]]

    def add_absence_flag(self, df: pd.DataFrame) -> pd.DataFrame:
        result = df.copy()
        result["IsAbsent"] = (result["Attendance"] == "Absent").astype(int)
        return result

    def high_absentees(self, df: pd.DataFrame, threshold: int) -> pd.DataFrame:
        absent_df = df[df["Attendance"] == "Absent"]

        result = (
            absent_df.groupby("EmployeeID")
            .size()
            .reset_index(name="Absence Count")
        )

        return result[result["Absence Count"] > threshold].reset_index(drop=True)

    def department_attendance_summary(self, df: pd.DataFrame) -> pd.DataFrame:
        summary = pd.crosstab(df["Department"], df["Attendance"])

        summary.columns.name = None

        summary = summary.reindex(
            columns=["Present", "Absent", "Leave"],
            fill_value=0
        )

        return summary.reset_index()
```

---

# Question Code: 2

```python
import re

class WordFrequencyCounter:

    def preprocess_text(self, text: str) -> list:
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        return text.split()

    def compute_word_frequency(self, words: list) -> dict:
        freq_dict = {}

        for word in words:
            freq_dict[word] = freq_dict.get(word, 0) + 1

        return freq_dict

    def get_most_frequent_word(self, freq_dict: dict) -> tuple:
        if not freq_dict:
            return None

        return max(freq_dict.items(), key=lambda x: x[1])

    def filter_words_by_frequency(self, freq_dict: dict, n: int) -> dict:
        filtered = {}

        for word, count in freq_dict.items():
            if count >= n:
                filtered[word] = count

        return filtered
```
