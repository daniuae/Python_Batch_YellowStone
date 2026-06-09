# Real-World NumPy and Pandas Business Problems

These problems are designed for **Data Engineering**, **Data Analytics**, **Data Science**, and **Python Interviews**.

The objective is to practice:

- Data Cleaning
- Data Transformation
- Aggregations
- Joins and Merges
- Window Functions
- Time-Series Analysis
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Business KPI Calculations

---

# Dataset 1: E-Commerce Sales

## sales.csv

| order_id | customer_id | product_id | category | quantity | price | order_date |
|-----------|------------|------------|----------|----------|--------|------------|
| 1001 | C101 | P201 | Electronics | 2 | 500 | 2025-01-01 |
| 1002 | C102 | P202 | Clothing | 1 | 120 | 2025-01-01 |
| 1003 | C101 | P203 | Electronics | 3 | 300 | 2025-01-02 |

---

## Business Problems

### Basic Level

1. Find total sales amount.
2. Calculate revenue by category.
3. Find total orders per day.
4. Find top-selling products.
5. Calculate average order value.

### Intermediate Level

6. Find customers spending more than ₹50,000.
7. Monthly sales trend analysis.
8. Calculate cumulative sales.
9. Identify repeat customers.
10. Find highest revenue category.

### Advanced Level

11. RFM Analysis
    - Recency
    - Frequency
    - Monetary

12. Customer Lifetime Value (CLV).
13. Market Basket Analysis Preparation.
14. Cohort Analysis.
15. Sales Forecasting Dataset Preparation.

---

# Dataset 2: Banking Transactions

## transactions.csv

| txn_id | account_id | txn_type | amount | txn_date |
|---------|------------|----------|---------|----------|
| T001 | A101 | Credit | 5000 | 2025-01-01 |
| T002 | A101 | Debit | 1000 | 2025-01-02 |

---

## Business Problems

### Basic Level

1. Total credits and debits.
2. Average transaction amount.
3. Top customers by transaction volume.
4. Daily transaction count.

### Intermediate Level

5. Running account balance.
6. Largest withdrawal per customer.
7. Detect duplicate transactions.
8. Monthly transaction summary.

### Advanced Level

9. Fraud Detection Rules:

   - More than 5 transactions within 1 minute.
   - Transactions from multiple locations.
   - Sudden high-value transaction.

10. Customer Segmentation.
11. Churn Prediction Dataset Creation.
12. AML (Anti-Money Laundering) Detection.

---

# Dataset 3: Telecom Customer Churn

## customers.csv

| customer_id | tenure | monthly_charge | contract_type | churn |
|-------------|---------|---------------|---------------|-------|
| C101 | 24 | 1500 | Monthly | Yes |

---

## Business Problems

### Basic Level

1. Count churned customers.
2. Average monthly charge.
3. Churn percentage.

### Intermediate Level

4. Churn by contract type.
5. Churn by tenure group.
6. Revenue lost due to churn.

### Advanced Level

7. Customer Risk Score.
8. Predict Likely Churners.
9. Create ML-ready dataset.
10. Retention Strategy Recommendations.

---

# Dataset 4: Manufacturing Plant

## production.csv

| date | machine_id | units_produced | defective_units |
|--------|-----------|---------------|----------------|
| 2025-01-01 | M001 | 1000 | 20 |

---

## Business Problems

### Basic Level

1. Total production.
2. Defect percentage.
3. Best performing machine.

### Intermediate Level

4. Production trend analysis.
5. Daily defect rate.
6. Machine utilization analysis.

### Advanced Level

7. Predict maintenance requirements.
8. Detect anomaly production days.
9. Quality Control Dashboard Metrics.
10. OEE (Overall Equipment Effectiveness).

---

# Dataset 5: HR Analytics

## employees.csv

| emp_id | department | salary | experience | attrition |
|---------|-----------|---------|------------|-----------|
| E101 | IT | 80000 | 5 | No |

---

## Business Problems

### Basic Level

1. Average salary by department.
2. Employee count by department.
3. Highest-paid employees.

### Intermediate Level

4. Attrition rate by department.
5. Salary distribution.
6. Promotion eligibility analysis.

### Advanced Level

7. Workforce planning.
8. Attrition prediction.
9. Diversity analysis.
10. Compensation benchmarking.

---

# Dataset 6: Hospital Management

## patient_visits.csv

| patient_id | visit_date | department | bill_amount |
|------------|------------|-----------|------------|
| P101 | 2025-01-01 | Cardiology | 5000 |

---

## Business Problems

### Basic Level

1. Total patients.
2. Revenue by department.
3. Average bill amount.

### Intermediate Level

4. Frequent patients.
5. Monthly revenue trend.
6. Peak visit days.

### Advanced Level

7. Readmission analysis.
8. Patient segmentation.
9. Revenue forecasting.
10. Capacity planning.

---

# Dataset 7: Logistics and Supply Chain

## shipments.csv

| shipment_id | route | delivery_days | status |
|-------------|-------|--------------|---------|
| S101 | Chennai-Bangalore | 2 | Delivered |

---

## Business Problems

### Basic Level

1. Average delivery time.
2. Delayed shipment count.
3. Delivery success rate.

### Intermediate Level

4. Route performance.
5. Monthly shipment volume.
6. Delayed shipment trend.

### Advanced Level

7. Delivery delay prediction.
8. Route optimization.
9. Carrier performance analysis.
10. Supply Chain KPI Dashboard.

---

# Dataset 8: Retail Inventory

## inventory.csv

| product_id | stock | reorder_level | sales_last_30_days |
|------------|--------|--------------|-------------------|
| P101 | 100 | 50 | 120 |

---

## Business Problems

### Basic Level

1. Low stock products.
2. Current inventory value.
3. Top stocked products.

### Intermediate Level

4. Days of inventory remaining.
5. Fast-moving products.
6. Slow-moving products.

### Advanced Level

7. Inventory optimization.
8. Reorder recommendations.
9. ABC Analysis.
10. Demand forecasting.

---

# NumPy-Specific Business Problems

---

## Problem 1: Stock Market Analysis

```python
import numpy as np

prices = np.array([100,105,110,108,115,120,125])
```

### Tasks

1. Daily returns
2. Average return
3. Volatility
4. Moving average
5. Maximum drawdown

---

## Problem 2: Manufacturing Sensor Data

```python
temperature = np.array([32,34,33,35,100,34,36])
```

### Tasks

1. Detect anomalies
2. Mean temperature
3. Standard deviation
4. Z-score analysis

---

## Problem 3: Employee Salary Analytics

```python
salary = np.array([40000,50000,60000,80000,120000])
```

### Tasks

1. Median salary
2. Percentiles
3. Salary bands
4. Outlier detection

---

## Problem 4: Sales Performance

```python
sales = np.array([
    [100,200,300],
    [150,250,350],
    [200,300,400]
])
```

### Tasks

1. Row-wise totals
2. Column-wise totals
3. Best month
4. Growth percentage

---

# Capstone Project

# Retail Data Warehouse Analytics

## Customers

| customer_id | name | city |

## Orders

| order_id | customer_id | order_date |

## Order_Items

| order_id | product_id | quantity |

## Products

| product_id | category | price |

---

## Business Questions

1. Top 10 customers by revenue.
2. Monthly sales growth.
3. Customer retention rate.
4. Category-wise profit.
5. Product affinity analysis.
6. Customer segmentation.
7. Customer lifetime value.
8. Cohort analysis.
9. Inventory forecasting.
10. Executive dashboard metrics.

---

# Important Pandas Concepts Covered

```python
groupby()
agg()
transform()
pivot_table()

merge()
join()
concat()

apply()
map()
replace()

fillna()
dropna()

duplicated()

rank()

rolling()
expanding()

shift()

cumsum()
cumcount()

value_counts()

cut()
qcut()

melt()
stack()
unstack()

datetime operations
```

---

# Important NumPy Concepts Covered

```python
array()

reshape()
flatten()
ravel()

where()
select()

mean()
median()

std()
var()

percentile()
quantile()

corrcoef()

dot()
matmul()

broadcasting

masking

boolean indexing

vectorization

random module
```

---

# Interview Preparation Tips

These datasets help practice:

- Data Cleaning
- Data Wrangling
- Data Modeling
- Exploratory Data Analysis
- KPI Calculations
- Feature Engineering
- Time-Series Analysis
- Window Functions
- Business Reporting
- Dashboard Development
- Data Science Feature Creation
- ETL Pipeline Development

They are highly relevant for:

- Data Engineer
- Data Analyst
- Business Analyst
- Data Scientist
- Analytics Engineer
- BI Developer
- Machine Learning Engineer Interviews
