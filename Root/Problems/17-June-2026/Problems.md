# Pandas Debugging Challenge - 10 Error Fixing Exercises

## Dataset Used

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["John", "Mary", "David", "Sara", "Tom"],
    "Age": [25, 32, 45, 28, 38],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, 80000, 55000, 70000]
})
```

---

# Problem 1: Display First 3 Rows

## Task

Display the first 3 rows.

## Broken Code

```python
df.head[3]
```

### Expected Output

First 3 records.

---

## Solution

```python
df.head(3)
```

### Error

`head` is a method and requires parentheses.

---

# Problem 2: Select Age Column

## Task

Display only the Age column.

## Broken Code

```python
df["Age'
```

### Error Type

Syntax Error

---

## Solution

```python
df["Age"]
```

### Error

Quotation marks do not match.

---

# Problem 3: Filter Employees Older Than 30

## Task

Display employees whose age is greater than 30.

## Broken Code

```python
df[df["Age"] > 30
```

### Error Type

Syntax Error

---

## Solution

```python
df[df["Age"] > 30]
```

### Error

Missing closing bracket.

---

# Problem 4: Calculate Average Salary

## Task

Find average salary.

## Broken Code

```python
df["Salary"].mean(
```

### Error Type

Syntax Error

---

## Solution

```python
df["Salary"].mean()
```

### Error

Missing closing parenthesis.

---

# Problem 5: Group By Department

## Task

Find average salary by department.

## Broken Code

```python
df.groupby("Department").mean
```

### Expected

Grouped average values.

---

## Solution

```python
df.groupby("Department").mean()
```

### Error

Method not invoked.

---

# Problem 6: Sort Salary Descending

## Task

Sort employees by salary descending.

## Broken Code

```python
df.sort_values(by="Salary", ascending=False
```

### Error Type

Syntax Error

---

## Solution

```python
df.sort_values(by="Salary", ascending=False)
```

### Error

Missing closing parenthesis.

---

# Problem 7: Create New Bonus Column

## Task

Create Bonus = Salary * 0.10

## Broken Code

```python
df["Bonus"] = df["Salary"] * .10))
```

### Error Type

Syntax Error

---

## Solution

```python
df["Bonus"] = df["Salary"] * 0.10
```

### Error

Extra closing parenthesis.

---

# Problem 8: Rename Salary Column

## Task

Rename Salary to MonthlySalary.

## Broken Code

```python
df.rename(columns={"Salary":"MonthlySalary"}
```

### Error Type

Syntax Error

---

## Solution

```python
df.rename(columns={"Salary":"MonthlySalary"})
```

### Error

Missing closing parenthesis.

---

# Problem 9: Drop Age Column

## Task

Remove Age column.

## Broken Code

```python
df.drop("Age", axis=1))
```

### Error Type

Syntax Error

---

## Solution

```python
df.drop("Age", axis=1)
```

### Error

Extra closing parenthesis.

---

# Problem 10: Save DataFrame to CSV

## Task

Write DataFrame to employees.csv

## Broken Code

```python
df.to_csv("employees.csv", index=False
```

### Error Type

Syntax Error

---

## Solution

```python
df.to_csv("employees.csv", index=False)
```

### Error

Missing closing parenthesis.

---

# Bonus Challenge

Find and Fix All Errors

```python
import pandas as pd

data = {
    "Name":["John","Mary","Tom"],
    "Age":[25,30,35]
}

df = pd.DataFrame(data

print(df.head(2)

df["Bonus"] = df["Age"] * .5))

print(df.sort_values(by="Age")
```

## Correct Solution

```python
import pandas as pd

data = {
    "Name":["John","Mary","Tom"],
    "Age":[25,30,35]
}

df = pd.DataFrame(data)

print(df.head(2))

df["Bonus"] = df["Age"] * 0.5

print(df.sort_values(by="Age"))
```

## Learning Outcome

Students will practice:

* Parentheses errors
* Bracket errors
* Quote errors
* Method invocation mistakes
* Column selection mistakes
* GroupBy operations
* Sorting
* Column creation
* Renaming columns
* CSV operations
* Reading Python tracebacks
