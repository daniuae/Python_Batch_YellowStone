# Question Code: Q330

```python
import pandas as pd

class AttendanceAnalyzer:

    def create_attendance_df(self, data: list) -> pd.DataFrame:
        columns = ["EmployeeID", "Department", "Date", "Attendance"]
        return pd.DataFrame(data, columns=columns)

    def compute_monthly_attendance_rate(self, df: pd.DataFrame) -> pd.DataFrame:
        temp_df = df.copy()

        temp_df["Month"] = temp_df["Date"].str[:7]

        total_days = (
            temp_df.groupby(["EmployeeID", "Month"])
            .size()
            .reset_index(name="Total")
        )

        present_days = (
            temp_df[temp_df["Attendance"] == "Present"]
            .groupby(["EmployeeID", "Month"])
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
