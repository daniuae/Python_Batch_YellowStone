# Real-World NumPy Implementations with Problem Breakdown and Solutions

---

# Why NumPy?

NumPy (Numerical Python) is the foundation of:

- Data Engineering
- Data Science
- Machine Learning
- Artificial Intelligence
- Financial Analytics
- Manufacturing Analytics
- Scientific Computing
- IoT Data Processing

## Advantages of NumPy

✅ Faster than Python Lists

✅ Vectorized Operations

✅ Less Memory Consumption

✅ Mathematical Functions

✅ Multi-dimensional Arrays

---

# 1. Manufacturing Quality Control Analysis

## Business Problem

A semiconductor company manufactures 10,000 chips daily.

Each chip has a thickness measurement.

Quality team wants to:

- Find average thickness
- Find minimum and maximum thickness
- Find defective chips
- Calculate process variation
- Detect outliers

---

## Step 1: Generate Sample Data

```python
import numpy as np

np.random.seed(42)

thickness = np.random.normal(
    loc=1.0,
    scale=0.05,
    size=10000
)

print(thickness[:10])
```

### Explanation

| Parameter | Description |
|------------|------------|
| loc | Mean thickness |
| scale | Standard deviation |
| size | Number of chips |

---

## Step 2: Calculate Statistics

```python
mean_value = np.mean(thickness)

min_value = np.min(thickness)

max_value = np.max(thickness)

std_dev = np.std(thickness)

print("Average:", mean_value)
print("Minimum:", min_value)
print("Maximum:", max_value)
print("Standard Deviation:", std_dev)
```

---

## Business Interpretation

Example Output:

```text
Average Thickness = 1.00 mm
Minimum Thickness = 0.80 mm
Maximum Thickness = 1.20 mm
Std Deviation = 0.05
```

A low standard deviation indicates a stable manufacturing process.

---

## Step 3: Identify Defective Chips

Accepted Range:

```text
0.90 <= Thickness <= 1.10
```

```python
defective = thickness[
    (thickness < 0.90) |
    (thickness > 1.10)
]

print("Defective Chips:", len(defective))
```

---

## NumPy Concepts Used

- np.mean()
- np.min()
- np.max()
- np.std()
- Boolean Filtering

---

# 2. Employee Attendance Analytics

## Business Problem

HR wants to calculate:

- Present Days
- Absent Days
- Attendance Percentage

---

## Sample Dataset

```python
attendance = np.array([
    1,1,1,0,1,1,0,
    1,1,1,1,0,1,1,
    1,0,1,1,1,1,0
])
```

Where:

```text
1 = Present
0 = Absent
```

---

## Solution

### Total Present Days

```python
present_days = np.sum(attendance)

print(present_days)
```

---

### Total Absent Days

```python
absent_days = len(attendance) - present_days

print(absent_days)
```

---

### Attendance Percentage

```python
attendance_percentage = (
    present_days / len(attendance)
) * 100

print(attendance_percentage)
```

---

## Expected Output

```text
Present Days = 17
Absent Days = 4
Attendance = 80.95%
```

---

## NumPy Concepts Used

- np.sum()
- Array Aggregation
- Percentage Calculations

---

# 3. Sales Performance Analysis

## Business Problem

Management wants:

- Total Revenue
- Average Revenue
- Best Month
- Worst Month

---

## Dataset

```python
sales = np.array([
    120000,
    135000,
    98000,
    150000,
    175000,
    200000
])
```

---

## Step 1: Total Revenue

```python
total_sales = np.sum(sales)

print(total_sales)
```

---

## Step 2: Average Revenue

```python
average_sales = np.mean(sales)

print(average_sales)
```

---

## Step 3: Best Month

```python
best_month = np.argmax(sales)

print(best_month)
```

---

## Step 4: Worst Month

```python
worst_month = np.argmin(sales)

print(worst_month)
```

---

## NumPy Concepts Used

- np.sum()
- np.mean()
- np.argmax()
- np.argmin()

---

# 4. E-Commerce Order Analytics

## Business Problem

An e-commerce platform wants to identify:

- Premium Orders
- Average Order Value
- Premium Customer Count

---

## Dataset

```python
orders = np.array([
    1500,
    2500,
    7500,
    10000,
    4500,
    6000
])
```

---

## Premium Orders

```python
premium_orders = orders[
    orders > 5000
]

print(premium_orders)
```

Output:

```text
[7500 10000 6000]
```

---

## Premium Customer Count

```python
count = len(premium_orders)

print(count)
```

---

## Average Order Value

```python
average_order = np.mean(orders)

print(average_order)
```

---

## NumPy Concepts Used

- Boolean Filtering
- Aggregation
- Conditional Selection

---

# 5. Banking Fraud Detection

## Business Problem

Transactions above ₹100,000 require investigation.

---

## Dataset

```python
transactions = np.array([
    2500,
    5000,
    10000,
    150000,
    200000,
    8000
])
```

---

## Find Suspicious Transactions

```python
suspicious = transactions[
    transactions > 100000
]

print(suspicious)
```

Output:

```text
[150000 200000]
```

---

## Count Fraud Alerts

```python
alerts = np.sum(
    transactions > 100000
)

print(alerts)
```

Output:

```text
2
```

---

## Understanding Boolean Arrays

```python
transactions > 100000
```

Result:

```python
[
 False,
 False,
 False,
 True,
 True,
 False
]
```

Internally:

```text
True = 1
False = 0
```

Therefore:

```python
np.sum(...)
```

Counts total alerts.

---

## NumPy Concepts Used

- Boolean Arrays
- Conditional Filtering
- Aggregation

---

# 6. Data Engineering ETL Transformation

## Business Problem

Source System:

```text
Temperature stored in Fahrenheit
```

Target System:

```text
Temperature required in Celsius
```

---

## Dataset

```python
fahrenheit = np.array([
    98.6,
    100,
    102,
    95
])
```

---

## Traditional Python Approach

```python
result = []

for temp in fahrenheit:
    celsius = (temp - 32) * 5/9
    result.append(celsius)

print(result)
```

---

## NumPy Vectorized Solution

```python
celsius = (
    fahrenheit - 32
) * 5/9

print(celsius)
```

Output:

```text
[37.0 37.78 38.89 35.0]
```

---

## Why Data Engineers Love NumPy

NumPy performs operations on entire arrays instead of looping through each element.

This is significantly faster for:

- ETL Pipelines
- Data Warehouses
- Spark Pre-processing
- Batch Processing

---

# 7. Multi-Dimensional Sales Analysis

## Business Problem

Analyze sales by:

- Product
- Region

---

## Dataset

```python
sales = np.array([
    [100,120,130],
    [200,220,240],
    [300,320,340]
])
```

Representation:

```text
         North  South  West

Laptop    100    120   130
Phone     200    220   240
TV        300    320   340
```

---

## Total Sales

```python
np.sum(sales)
```

Output:

```text
1970
```

---

## Product-wise Sales

```python
np.sum(
    sales,
    axis=1
)
```

Output:

```text
[350 660 960]
```

---

## Region-wise Sales

```python
np.sum(
    sales,
    axis=0
)
```

Output:

```text
[600 660 710]
```

---

## Understanding Axis

### axis = 0

Column-wise Operation

```text
100 120 130
200 220 240
300 320 340
 ↓
```

Result:

```python
[600 660 710]
```

---

### axis = 1

Row-wise Operation

```text
100 120 130 →
200 220 240 →
300 320 340 →
```

Result:

```python
[350 660 960]
```

---

## NumPy Concepts Used

- Multi-Dimensional Arrays
- Axis Operations
- Aggregations

---

# Interview Questions

## Q1: Why is NumPy faster than Python Lists?

### Answer

NumPy stores data in contiguous memory blocks.

Benefits:

1. Less Memory Usage
2. Faster Access
3. Vectorized Operations
4. C-based Implementation
5. No Python Loop Overhead

---

## Q2: What is Vectorization?

Vectorization means applying operations on an entire array at once.

Example:

```python
salary = np.array([
    50000,
    60000,
    70000
])

salary = salary * 1.10

print(salary)
```

Output:

```text
[55000 66000 77000]
```

No loop required.

---

# Mini Capstone Project

## Manufacturing Production Analytics

### Dataset

```python
production = np.array([
    [120,130,110,140],
    [150,145,160,155],
    [180,175,190,185]
])
```

Rows:

```text
Plant A
Plant B
Plant C
```

Columns:

```text
Week1 Week2 Week3 Week4
```

---

## Business Tasks

1. Total Production
2. Plant-wise Production
3. Week-wise Production
4. Best Plant
5. Average Weekly Production
6. Contribution Percentage
7. Highest Production Week
8. Lowest Production Week

---

## Suggested Solution

### Total Production

```python
total_production = np.sum(production)
```

---

### Plant-wise Production

```python
plant_total = np.sum(
    production,
    axis=1
)
```

---

### Week-wise Production

```python
weekly_total = np.sum(
    production,
    axis=0
)
```

---

### Best Performing Plant

```python
best_plant = np.argmax(
    plant_total
)
```

---

### Average Weekly Production

```python
average = np.mean(production)
```

---

# Concepts Mastered

✅ NumPy Arrays

✅ Indexing

✅ Slicing

✅ Aggregation

✅ Statistics

✅ Boolean Filtering

✅ Vectorization

✅ Broadcasting

✅ Multi-Dimensional Arrays

✅ Axis Operations

✅ Real-World Analytics

---

# Where NumPy Is Used in Industry

| Industry | Use Case |
|------------|------------|
| Manufacturing | Quality Control |
| Banking | Fraud Detection |
| Insurance | Risk Analysis |
| Retail | Sales Analytics |
| Healthcare | Patient Monitoring |
| IoT | Sensor Data Processing |
| Data Engineering | ETL Processing |
| AI/ML | Feature Engineering |
| Logistics | Route Optimization |
| Finance | Market Analysis |

NumPy is one of the most important libraries for Data Engineers, Data Analysts, Data Scientists, Machine Learning Engineers, and AI Engineers because almost every modern analytics framework (Pandas, Scikit-Learn, TensorFlow, PyTorch, Spark ML) is built on top of NumPy concepts.
