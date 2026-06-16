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

## Instructions

1. Open the Learnlytica assessment tool.
2. Enter your email address and the Question ID.
3. Click **Start Assessment**.
4. Once started, click **VSCode** to open the `solution.py` file.
5. Write your solution in the file.
6. Return to the assessment tool and click **Run Tests**.
7. After the tests execute, click **Validate**.
8. Once satisfied with your solution, click **Submit** and then **End Assessment**.

---

# Problem Statement

Implement a **Word Frequency Counter** that takes a sentence as input and returns a dictionary where:

* **Keys** → Words
* **Values** → Word Frequencies

The implementation should handle:

* Punctuation removal
* Case insensitivity

---

# Class Declaration

```python
class WordFrequencyCounter:
```

No need to use an `__init__()` method.

If required:

```python
def __init__(self):
    pass
```

---

# Operations

## 1. Clean and Tokenize Input

### Description

Removes punctuation, converts the sentence to lowercase, and tokenizes words.

### Function Prototype

```python
def preprocess_text(self, text: str) -> list:
```

### Example Input

```python
preprocess_text("Hello, hello! How are you?")
```

### Expected Output

```python
['hello', 'hello', 'how', 'are', 'you']
```

### Implementation Flow

* Convert the input text to lowercase.
* Remove punctuation using:

```python
re.sub(r'[^\w\s]', '', text)
```

* Split text into words using:

```python
text.split()
```

---

## 2. Compute Word Frequency

### Description

Counts occurrences of each word in a dictionary.

### Function Prototype

```python
def compute_word_frequency(self, words: list) -> dict:
```

### Example Input

```python
compute_word_frequency(
    ['hello', 'hello', 'how', 'are', 'you']
)
```

### Expected Output

```python
{
    'hello': 2,
    'how': 1,
    'are': 1,
    'you': 1
}
```

### Implementation Flow

* Declare an empty dictionary.
* Iterate through the list using a `for` loop.
* Use:

```python
freq_dict.get(word, 0)
```

to count occurrences.

* Return a dictionary where:

  * Keys = Words
  * Values = Frequencies

---

## 3. Get Most Frequent Word

### Description

Returns the most frequent word and its count.

### Function Prototype

```python
def get_most_frequent_word(self, freq_dict: dict) -> tuple:
```

### Example Input

```python
get_most_frequent_word(
    {'hello': 2, 'how': 1, 'are': 1, 'you': 1}
)
```

### Expected Output

```python
('hello', 2)
```

### Implementation Flow

* If the dictionary is empty, return:

```python
None
```

* Find the highest frequency using:

```python
max(freq_dict.items(), key=lambda x: x[1])
```

* Return the word and its count as a tuple.

---

## 4. Filter Words by Minimum Frequency

### Description

Returns words that appear at least `n` times.

### Function Prototype

```python
def filter_words_by_frequency(
    self,
    freq_dict: dict,
    n: int
) -> dict:
```

### Example Input

```python
filter_words_by_frequency(
    {'hello': 2, 'how': 1, 'are': 1, 'you': 1},
    2
)
```

### Expected Output

```python
{
    'hello': 2
}
```

### Implementation Flow

* Iterate over the dictionary using a `for` loop.
* Include only words that meet or exceed the threshold:

```python
count >= n
```

* Return the filtered dictionary.
* If no words qualify, return an empty dictionary.

