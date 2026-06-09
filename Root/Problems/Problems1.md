# Question 1
#  Hospital Patient Visit Analysis

## 📌 Problem Statement

A hospital tracks patient visits across departments. Each visit record contains Patient ID, Department, Visit Date, and Visit Status (`Completed` / `Cancelled` / `Follow-up`).

Your task is to analyze patient visit patterns and departmental performance.

---

## ✅ DeclareClass

```python
class HospitalVisitAnalyzer:
    pass
```

---

## ✅ 1. Create Visit DataFrame

Converts raw visit logs into a structured Pandas DataFrame.

### Function Prototype

```python
def create_visit_df(self, data: list) -> pd.DataFrame:
```

### Example Input

```python
create_visit_df([
    [501, "Cardiology", "2024-07-01", "Completed"],
    [502, "Neurology", "2024-07-01", "Cancelled"],
    [501, "Cardiology", "2024-07-10", "Follow-up"]
])
```

### Expected Output

| PatientID | Department | VisitDate | VisitStatus |
|------------|------------|------------|------------|
| 501 | Cardiology | 2024-07-01 | Completed |
| 502 | Neurology | 2024-07-01 | Cancelled |
| 501 | Cardiology | 2024-07-10 | Follow-up |

### Implementation Flow

- Create DataFrame with columns:
  `["PatientID", "Department", "VisitDate", "VisitStatus"]`
- Keep VisitDate as string.

---

## ✅ 2. Calculate Monthly Completion Rate

### Function Prototype

```python
def monthly_completion_rate(self, df: pd.DataFrame) -> pd.DataFrame:
```

### Expected Output

| PatientID | Month | Completion Rate |
|------------|------------|------------|
| 501 | 2024-07 | 50.0 |
| 502 | 2024-07 | 0.0 |

### Implementation Flow

- Extract Month using:

```python
df["VisitDate"].str[:7]
```

- Group by PatientID and Month
- Count Total Visits
- Count Completed Visits
- Merge results
- Calculate:

```python
Completion Rate = (Completed / Total) * 100
```

---

## ✅ 3. Add Cancellation Flag

### Function Prototype

```python
def add_cancellation_flag(self, df: pd.DataFrame) -> pd.DataFrame:
```

### Expected Output

| PatientID | Department | VisitDate | VisitStatus | IsCancelled |
|------------|------------|------------|------------|------------|
| 501 | Cardiology | 2024-07-01 | Completed | 0 |
| 502 | Neurology | 2024-07-01 | Cancelled | 1 |

### Implementation Flow

```python
df["VisitStatus"] == "Cancelled"
```

Convert boolean to integer.

---

## ✅ 4. Frequent Cancellers

### Function Prototype

```python
def frequent_cancellers(self, df: pd.DataFrame, threshold: int) -> pd.DataFrame:
```

### Implementation Flow

- Filter Cancelled visits
- Group by PatientID
- Count cancellations
- Return records where:

```python
Cancellation Count > threshold
```

---

## ✅ 5. Department Visit Summary

### Function Prototype

```python
def department_visit_summary(self, df: pd.DataFrame) -> pd.DataFrame:
```

### Expected Output

| Department | Completed | Cancelled | Follow-up |
|------------|------------|------------|------------|

### Implementation Flow

- Create Crosstab

```python
pd.crosstab(df["Department"], df["VisitStatus"])
```

- Reindex columns

```python
["Completed", "Cancelled", "Follow-up"]
```

- Reset index and return.

---

# Question Code: Q332

# E-Commerce Order Analysis

## 📌 Problem Statement

An online shopping platform records customer orders. Each order contains Customer ID, Product Category, Order Date, and Order Status (`Delivered` / `Cancelled` / `Returned`).

Analyze order fulfillment performance.

---

## ✅ DeclareClass

```python
class EcommerceAnalyzer:
    pass
```

---

## ✅ 1. Create Orders DataFrame

### Function Prototype

```python
def create_order_df(self, data: list) -> pd.DataFrame:
```

### Columns

```python
["CustomerID", "Category", "OrderDate", "OrderStatus"]
```

---

## ✅ 2. Monthly Delivery Rate

### Function Prototype

```python
def monthly_delivery_rate(self, df: pd.DataFrame) -> pd.DataFrame:
```

### Formula

```python
Delivery Rate = (Delivered Orders / Total Orders) * 100
```

### Implementation Flow

- Extract Month from OrderDate
- Group by CustomerID and Month
- Count Delivered Orders
- Calculate Delivery Rate

---

## ✅ 3. Add Return Flag

### Function Prototype

```python
def add_return_flag(self, df: pd.DataFrame) -> pd.DataFrame:
```

### New Column

```python
IsReturned
```

### Logic

```python
Returned -> 1
Else -> 0
```

---

## ✅ 4. Frequent Return Customers

### Function Prototype

```python
def frequent_returners(self, df: pd.DataFrame, threshold: int) -> pd.DataFrame:
```

### Logic

- Filter Returned orders
- Group by CustomerID
- Count returns
- Return customers having returns > threshold

---

## ✅ 5. Category-wise Order Summary

### Function Prototype

```python
def category_order_summary(self, df: pd.DataFrame) -> pd.DataFrame:
```

### Output

| Category | Delivered | Cancelled | Returned |
|-----------|-----------|-----------|-----------|

### Implementation Flow

Use Crosstab and reindex columns.

---

# Question Code: Q333

# Student Examination Performance Analysis

## 📌 Problem Statement

A university maintains exam participation records. Each record contains Student ID, Department, Exam Date, and Exam Result (`Pass` / `Fail` / `Absent`).

Analyze examination performance and participation.

---

## ✅ DeclareClass

```python
class ExamPerformanceAnalyzer:
    pass
```

---

## ✅ 1. Create Exam DataFrame

### Function Prototype

```python
def create_exam_df(self, data: list) -> pd.DataFrame:
```

### Columns

```python
["StudentID", "Department", "ExamDate", "Result"]
```

---

## ✅ 2. Monthly Pass Rate

### Function Prototype

```python
def monthly_pass_rate(self, df: pd.DataFrame) -> pd.DataFrame:
```

### Formula

```python
Pass Rate = (Pass Exams / Total Exams) * 100
```

### Implementation Flow

- Extract Month
- Count Total Exams
- Count Pass Exams
- Calculate Pass Rate

---

## ✅ 3. Add Absent Flag

### Function Prototype

```python
def add_absent_flag(self, df: pd.DataFrame) -> pd.DataFrame:
```

### New Column

```python
IsAbsent
```

### Logic

```python
Absent -> 1
Else -> 0
```

---

## ✅ 4. Frequently Absent Students

### Function Prototype

```python
def frequently_absent_students(self, df: pd.DataFrame, threshold: int) -> pd.DataFrame:
```

### Logic

- Filter Absent
- Group by StudentID
- Count absences
- Return count > threshold

---

## ✅ 5. Department Result Summary

### Function Prototype

```python
def department_result_summary(self, df: pd.DataFrame) -> pd.DataFrame:
```

### Output

| Department | Pass | Fail | Absent |
|------------|------------|------------|------------|

### Implementation Flow

Use Crosstab and reindex columns.

---

# Question Code: Q334

# Banking Transaction Monitoring

## 📌 Problem Statement

A bank records customer transactions. Each transaction contains Account ID, Branch, Transaction Date, and Transaction Status (`Successful` / `Failed` / `Reversed`).

Analyze transaction success trends and branch performance.

---

## ✅ DeclareClass

```python
class BankingTransactionAnalyzer:
    pass
```

---

## ✅ 1. Create Transaction DataFrame

### Columns

```python
["AccountID", "Branch", "TransactionDate", "TransactionStatus"]
```

---

## ✅ 2. Monthly Success Rate

### Function Prototype

```python
def monthly_success_rate(self, df: pd.DataFrame) -> pd.DataFrame:
```

### Formula

```python
Success Rate = (Successful Transactions / Total Transactions) * 100
```

### Implementation Flow

- Extract Month
- Count Successful Transactions
- Count Total Transactions
- Calculate Success Rate

---

## ✅ 3. Add Failure Flag

### Function Prototype

```python
def add_failure_flag(self, df: pd.DataFrame) -> pd.DataFrame:
```

### New Column

```python
IsFailed
```

### Logic

```python
Failed -> 1
Else -> 0
```

---

## ✅ 4. High Failure Accounts

### Function Prototype

```python
def high_failure_accounts(self, df: pd.DataFrame, threshold: int) -> pd.DataFrame:
```

### Logic

- Filter Failed
- Group by AccountID
- Count failures
- Return failures > threshold

---

## ✅ 5. Branch Transaction Summary

### Function Prototype

```python
def branch_transaction_summary(self, df: pd.DataFrame) -> pd.DataFrame:
```

### Output

| Branch | Successful | Failed | Reversed |
|---------|---------|---------|---------|

### Implementation Flow

Use Crosstab and reindex columns.

---

# Question Code: Q335

# Logistics Shipment Tracking

## 📌 Problem Statement

A logistics company tracks package deliveries. Each shipment record contains Shipment ID, Region, Shipment Date, and Delivery Status (`Delivered` / `Delayed` / `Lost`).

Analyze shipment efficiency and regional performance.

---

## ✅ DeclareClass

```python
class ShipmentAnalyzer:
    pass
```

---

## ✅ 1. Create Shipment DataFrame

### Function Prototype

```python
def create_shipment_df(self, data: list) -> pd.DataFrame:
```

### Columns

```python
["ShipmentID", "Region", "ShipmentDate", "DeliveryStatus"]
```

---

## ✅ 2. Monthly Delivery Rate

### Function Prototype

```python
def monthly_delivery_rate(self, df: pd.DataFrame) -> pd.DataFrame:
```

### Formula

```python
Delivery Rate = (Delivered Shipments / Total Shipments) * 100
```

---

## ✅ 3. Add Delay Flag

### Function Prototype

```python
def add_delay_flag(self, df: pd.DataFrame) -> pd.DataFrame:
```

### New Column

```python
IsDelayed
```

### Logic

```python
Delayed -> 1
Else -> 0
```

---

## ✅ 4. Frequently Delayed Shipments

### Function Prototype

```python
def frequently_delayed_shipments(self, df: pd.DataFrame, threshold: int) -> pd.DataFrame:
```

### Logic

- Filter Delayed shipments
- Group by ShipmentID
- Count delays
- Return delays > threshold

---

## ✅ 5. Region-wise Delivery Summary

### Function Prototype

```python
def region_delivery_summary(self, df: pd.DataFrame) -> pd.DataFrame:
```

### Output

| Region | Delivered | Delayed | Lost |
|---------|---------|---------|---------|

### Implementation Flow

```python
pd.crosstab(df["Region"], df["DeliveryStatus"])
```

Reindex columns:

```python
["Delivered", "Delayed", "Lost"]
```

Reset index and return.
