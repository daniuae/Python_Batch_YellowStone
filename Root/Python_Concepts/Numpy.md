# NumPy Aggregation and GroupBy – Real-World Examples

## Learning Objectives

After completing this topic, you will be able to:

- Understand aggregation in NumPy
- Use common aggregation functions
- Perform GroupBy-like operations in NumPy
- Analyze real-world business datasets
- Build reporting logic commonly used in ETL pipelines

---

# What is Aggregation?

Aggregation means combining multiple values into a single summarized value.

Examples:

| Data | Aggregation |
|--------|------------|
| Sales Amounts | Total Sales |
| Employee Salaries | Average Salary |
| Exam Marks | Maximum Mark |
| Attendance Records | Attendance Percentage |

---

# Why Aggregation is Important?

In real-world projects, stakeholders rarely want raw data.

Instead they ask questions such as:

- What is the total revenue?
- What is the average salary?
- Which region performed best?
- How many employees are present?

Aggregation helps answer these questions.

---

# Sample Dataset

Daily sales of a store:

```python
import numpy as np

sales = np.array([1000, 1200, 900, 1500, 1800])
```

---

# Common Aggregation Functions

## Sum

```python
np.sum(sales)
```

Output:

```text
6400
```

Meaning:

```text
1000 + 1200 + 900 + 1500 + 1800
```

---

## Mean (Average)

```python
np.mean(sales)
```

Output:

```text
1280.0
```

Formula:

```text
Total Sales / Number of Sales
```

---

## Maximum

```python
np.max(sales)
```

Output:

```text
1800
```

Highest sale value.

---

## Minimum

```python
np.min(sales)
```

Output:

```text
900
```

Lowest sale value.

---

## Standard Deviation

```python
np.std(sales)
```

Measures data spread.

---

## Variance

```python
np.var(sales)
```

Measures variability in data.

---

# Aggregation Example

```python
import numpy as np

sales = np.array([1000, 1200, 900, 1500, 1800])

print("Total Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Maximum Sale:", np.max(sales))
print("Minimum Sale:", np.min(sales))
```

Output:

```text
Total Sales: 6400
Average Sales: 1280.0
Maximum Sale: 1800
Minimum Sale: 900
```

---

# Real-World Scenario: E-Commerce Sales Analysis

Suppose an e-commerce company stores the following data:

| Order ID | Region | Sales |
|-----------|---------|---------|
| 1 | North | 1000 |
| 2 | South | 1200 |
| 3 | North | 1500 |
| 4 | East | 900 |
| 5 | South | 1800 |
| 6 | North | 1100 |

Management wants:

1. Total Sales per Region
2. Average Sales per Region
3. Highest Sales per Region

This is known as a GroupBy operation.

---

# Does NumPy Have GroupBy?

No.

Unlike Pandas:

```python
df.groupby("Region")
```

NumPy does not provide a built-in GroupBy method.

However, we can achieve similar functionality using:

- np.unique()
- Boolean Masking
- Aggregation Functions

---

# Step 1: Create Dataset

```python
import numpy as np

regions = np.array([
    "North",
    "South",
    "North",
    "East",
    "South",
    "North"
])

sales = np.array([
    1000,
    1200,
    1500,
    900,
    1800,
    1100
])
```

---

# Step 2: Find Unique Groups

```python
unique_regions = np.unique(regions)

print(unique_regions)
```

Output:

```text
['East' 'North' 'South']
```

---

# Step 3: GroupBy Using Boolean Masking

```python
for region in unique_regions:

    mask = regions == region

    total_sales = np.sum(sales[mask])

    print(region, total_sales)
```

Output:

```text
East 900
North 3600
South 3000
```

---

# Understanding Boolean Masking

For region = North

```python
regions == "North"
```

Output:

```python
array([
 True,
 False,
 True,
 False,
 False,
 True
])
```

Applying mask:

```python
sales[regions == "North"]
```

Output:

```python
array([1000, 1500, 1100])
```

Aggregation:

```python
np.sum([1000,1500,1100])
```

Output:

```text
3600
```

---

# Complete GroupBy Example

```python
import numpy as np

regions = np.array([
    "North",
    "South",
    "North",
    "East",
    "South",
    "North"
])

sales = np.array([
    1000,
    1200,
    1500,
    900,
    1800,
    1100
])

unique_regions = np.unique(regions)

for region in unique_regions:

    mask = regions == region

    total_sales = np.sum(sales[mask])
    average_sales = np.mean(sales[mask])
    highest_sales = np.max(sales[mask])

    print(f"""
Region: {region}
Total Sales: {total_sales}
Average Sales: {average_sales}
Highest Sale: {highest_sales}
""")
```

Output:

```text
Region: East
Total Sales: 900
Average Sales: 900.0
Highest Sale: 900

Region: North
Total Sales: 3600
Average Sales: 1200.0
Highest Sale: 1500

Region: South
Total Sales: 3000
Average Sales: 1500.0
Highest Sale: 1800
```

---

# Visual Representation

```text
Raw Data
------------------------------------------------
Region      Sales
------------------------------------------------
North       1000
South       1200
North       1500
East        900
South       1800
North       1100
------------------------------------------------

Group By Region
------------------------------------------------
North -> [1000,1500,1100]
South -> [1200,1800]
East  -> [900]
------------------------------------------------

Aggregation
------------------------------------------------
North Total = 3600
South Total = 3000
East Total  = 900
------------------------------------------------
```

---

# Real-World Example: Employee Salary Analysis

## Dataset

```python
departments = np.array([
    "IT",
    "HR",
    "IT",
    "Finance",
    "HR",
    "IT"
])

salaries = np.array([
    60000,
    45000,
    70000,
    55000,
    50000,
    65000
])
```

---

## Business Requirement

HR wants:

- Department-wise total salary
- Average salary
- Highest salary

---

## Solution

```python
unique_departments = np.unique(departments)

for dept in unique_departments:

    dept_salary = salaries[departments == dept]

    print(f"""
Department: {dept}
Total Salary: {np.sum(dept_salary)}
Average Salary: {np.mean(dept_salary)}
Maximum Salary: {np.max(dept_salary)}
""")
```

Output:

```text
Department: Finance
Total Salary: 55000
Average Salary: 55000

Department: HR
Total Salary: 95000
Average Salary: 47500

Department: IT
Total Salary: 195000
Average Salary: 65000
```

---

# Faster GroupBy Using np.bincount()

Useful when categories are numeric.

## Example

```python
department_id = np.array([
    0,
    1,
    0,
    2,
    1,
    0
])

salary = np.array([
    60000,
    45000,
    70000,
    55000,
    50000,
    65000
])

totals = np.bincount(
    department_id,
    weights=salary
)

print(totals)
```

Output:

```text
[195000 95000 55000]
```

Meaning:

```text
Department 0 = 195000
Department 1 = 95000
Department 2 = 55000
```

---

# Real-World Data Engineering Use Cases

## 1. Sales Analytics

```text
Group By Region
Calculate Total Revenue
Calculate Average Order Value
Find Top Performing Region
```

---

## 2. Attendance Analytics

```text
Group By Department
Calculate Attendance Percentage
Calculate Leave Count
Find Departments with Low Attendance
```

---

## 3. Manufacturing Analytics

```text
Group By Factory
Calculate Production Quantity
Calculate Defect Rate
Calculate Daily Output
```

---

## 4. Banking Analytics

```text
Group By Branch
Calculate Total Deposits
Calculate Loan Amounts
Calculate Customer Counts
```

---

## 5. Healthcare Analytics

```text
Group By Hospital
Calculate Patient Count
Calculate Average Treatment Cost
Calculate Recovery Rates
```

---

# Interview Questions

## Q1. What is aggregation?

Aggregation is the process of summarizing multiple values into a single value such as:

- Sum
- Average
- Maximum
- Minimum

---

## Q2. Does NumPy support GroupBy?

No.

NumPy does not have a direct GroupBy function.

Alternatives:

- np.unique()
- Boolean Masking
- np.bincount()
- Structured Arrays

---

## Q3. Why is aggregation important?

Aggregation helps convert raw data into business insights such as:

- Revenue Reports
- Salary Reports
- Attendance Reports
- Production Reports

---

## Q4. Which aggregation functions are most commonly used?

```python
np.sum()
np.mean()
np.max()
np.min()
np.std()
np.var()
np.median()
```

---

# Key Takeaways

```text
Aggregation
    ↓
Summarize Data
    ↓
sum(), mean(), min(), max()

GroupBy
    ↓
Split Data into Groups
    ↓
Aggregate Each Group

NumPy GroupBy
    ↓
np.unique()
+
Boolean Masking
+
Aggregation Functions

Real Example:
North -> 3600
South -> 3000
East  -> 900
```

### Rule to Remember

```text
GroupBy = Split + Apply + Combine

Split    → Divide data into groups
Apply    → Perform aggregation
Combine  → Produce summarized output
```

This pattern is heavily used in ETL pipelines, data warehousing, reporting systems, manufacturing analytics, attendance systems, banking analytics, and dashboard development.
