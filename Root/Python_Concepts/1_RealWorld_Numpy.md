# Practical Applications of NumPy with Real-World Examples

NumPy is rarely used alone in production systems. It acts as the **calculation engine** behind Data Science, Machine Learning, AI, Finance, Manufacturing, Healthcare, and Scientific Computing.

---

# 1. E-Commerce Sales Analysis

## Real-World Scenario

An online store wants to calculate:

- Total sales
- Average sales
- Highest sales day
- Lowest sales day

### Sample Data

```python
import numpy as np

daily_sales = np.array([
    25000,
    32000,
    28000,
    35000,
    41000,
    38000,
    45000
])

print("Total Sales:", np.sum(daily_sales))
print("Average Sales:", np.mean(daily_sales))
print("Highest Sale:", np.max(daily_sales))
print("Lowest Sale:", np.min(daily_sales))
```

### Output

```text
Total Sales: 244000
Average Sales: 34857.14
Highest Sale: 45000
Lowest Sale: 25000
```

### Used By

- Amazon
- Flipkart
- Myntra

---

# 2. Stock Market Analysis

## Real-World Scenario

A trader wants to calculate daily stock returns.

```python
import numpy as np

prices = np.array([100, 105, 103, 110, 115])

returns = np.diff(prices)

print("Price Changes:", returns)
```

### Output

```text
Price Changes: [ 5 -2  7  5 ]
```

### Used For

- Profit/Loss Analysis
- Risk Management
- Trading Algorithms

---

# 3. Manufacturing Quality Control

## Real-World Scenario

A factory produces bolts.

Target Length = 10 cm

Quality team checks measurements.

```python
import numpy as np

lengths = np.array([
    10.1,
    9.9,
    10.2,
    10.0,
    9.8
])

print("Average Length:", np.mean(lengths))
print("Standard Deviation:", np.std(lengths))
```

### Output

```text
Average Length: 10.0
Standard Deviation: 0.141
```

### Used By

- Automobile companies
- Semiconductor manufacturers
- Electronics industries

---

# 4. Weather Forecasting

## Real-World Scenario

Analyze weekly temperatures.

```python
import numpy as np

temps = np.array([
    32,
    34,
    35,
    33,
    31,
    30,
    36
])

print("Average Temp:", np.mean(temps))
print("Maximum Temp:", np.max(temps))
```

### Output

```text
Average Temp: 33.0
Maximum Temp: 36
```

### Used By

- Weather Departments
- Climate Research Teams

---

# 5. Student Performance Analysis

## Real-World Scenario

Calculate class statistics.

```python
import numpy as np

marks = np.array([
    75,
    80,
    65,
    90,
    85
])

print("Class Average:", np.mean(marks))
print("Highest Score:", np.max(marks))
print("Lowest Score:", np.min(marks))
```

### Output

```text
Class Average: 79.0
Highest Score: 90
Lowest Score: 65
```

### Used By

- Schools
- Universities
- Online Learning Platforms

---

# 6. Image Processing

## Real-World Scenario

An image is stored as a matrix of pixels.

```python
import numpy as np

image = np.array([
    [255, 100, 50],
    [200, 150, 75],
    [25, 125, 225]
])

print(image)
```

### Output

```text
[[255 100  50]
 [200 150  75]
 [ 25 125 225]]
```

### Applications

- Face Recognition
- Medical Imaging
- Satellite Imaging

---

# 7. Machine Learning

## Real-World Scenario

Training data is stored as NumPy arrays.

```python
import numpy as np

X = np.array([
    [25, 50000],
    [35, 70000],
    [45, 90000]
])

y = np.array([0, 1, 1])

print(X)
print(y)
```

### Output

```text
[[   25 50000]
 [   35 70000]
 [   45 90000]]

[0 1 1]
```

### Used For

- Recommendation Systems
- Fraud Detection
- Predictive Analytics

---

# 8. Banking Fraud Detection

## Real-World Scenario

Analyze transaction amounts.

```python
import numpy as np

transactions = np.array([
    500,
    1000,
    1200,
    45000,
    800
])

average = np.mean(transactions)

print("Average Transaction:", average)

fraud = transactions[transactions > 10000]

print("Suspicious Transactions:", fraud)
```

### Output

```text
Average Transaction: 9700.0
Suspicious Transactions: [45000]
```

### Used By

- Banks
- Credit Card Companies

---

# 9. Healthcare Analytics

## Real-World Scenario

Monitor patient heart rates.

```python
import numpy as np

heart_rates = np.array([
    72,
    75,
    80,
    90,
    85
])

print("Average Heart Rate:", np.mean(heart_rates))
```

### Output

```text
Average Heart Rate: 80.4
```

### Applications

- ICU Monitoring
- Wearable Devices
- Medical Research

---

# 10. Data Engineering (Most Relevant)

## Real-World Scenario

Clean and transform ETL data.

```python
import numpy as np

sales = np.array([
    100,
    200,
    np.nan,
    400,
    500
])

sales = np.nan_to_num(sales)

print(sales)
```

### Output

```text
[100. 200.   0. 400. 500.]
```

### Used In

- ETL Pipelines
- Data Warehouses
- Big Data Processing

---

# Manufacturing Example (Data Engineer Perspective)

Suppose a semiconductor company produces chips.

```python
import numpy as np

chip_temperatures = np.array([
    65,
    70,
    68,
    72,
    120,
    67
])

defective = chip_temperatures > 100

print("Defective Chips:")
print(chip_temperatures[defective])
```

### Output

```text
Defective Chips:
[120]
```

### Real-World Usage

- IoT Sensor Monitoring
- Manufacturing Analytics
- Predictive Maintenance
- Quality Assurance

---

# Most Common NumPy Functions in Real Projects

| Function | Purpose | Example |
|-----------|----------|----------|
| np.array() | Create array | Data storage |
| np.mean() | Average | KPI calculation |
| np.sum() | Total | Revenue calculation |
| np.max() | Maximum | Peak sales |
| np.min() | Minimum | Lowest value |
| np.std() | Standard deviation | Quality control |
| np.where() | Conditional filtering | Fraud detection |
| np.diff() | Difference between values | Stock returns |
| np.sort() | Sorting | Ranking |
| np.nan_to_num() | Handle missing data | ETL pipelines |
| np.reshape() | Change dimensions | ML preprocessing |
| np.concatenate() | Merge data | ETL jobs |

---

# NumPy in Data Engineering

As a Data Engineer, you'll often use NumPy for:

- ETL Data Transformations
- Statistical Calculations
- Data Validation
- Sensor Data Processing
- Machine Learning Preprocessing
- Batch Data Processing
- Scientific Computations

### Example

```python
import numpy as np

production = np.array([
    100,
    120,
    90,
    150,
    130
])

print("Total Production:", np.sum(production))
print("Average Production:", np.mean(production))
print("Maximum Production:", np.max(production))
```

### Output

```text
Total Production: 590
Average Production: 118.0
Maximum Production: 150
```

---

# Easy Memory Trick

Think of **NumPy as Excel on Steroids inside Python**.

| Excel | NumPy |
|---------|---------|
| Rows & Columns | Arrays |
| SUM() | np.sum() |
| AVERAGE() | np.mean() |
| MAX() | np.max() |
| MIN() | np.min() |
| IF Condition | np.where() |
| Data Analysis | Pandas + NumPy |

---

# Key Takeaway

Whenever you have:

- Large numerical datasets
- Scientific calculations
- Machine Learning data
- Manufacturing sensor data
- ETL transformations
- Statistical analysis

**NumPy is the foundation library that provides extremely fast numerical computations in Python.**
