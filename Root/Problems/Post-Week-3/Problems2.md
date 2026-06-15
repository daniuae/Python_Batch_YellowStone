# Pandas + OOP Practice Questions Collection

# Question 1: Employee Salary Analyzer

## 📌 Problem Statement

An organization maintains employee salary records. Each record contains Employee ID, Department, Salary, and Experience. Analyze salary trends and departmental compensation patterns.

## ✅ Declare Class

```python
class SalaryAnalyzer:
```

---

## 📌 Operations

### ✅ 1. Create Salary DataFrame

Function Prototype:

```python
def create_salary_df(self, data: list) -> pd.DataFrame:
```

Columns:

```text
EmployeeID
Department
Salary
Experience
```

Implementation Flow:

* Create DataFrame.
* Assign proper column names.

---

### ✅ 2. Calculate Average Salary Per Department

Function Prototype:

```python
def average_salary_by_department(self, df):
```

Implementation Flow:

* Group by Department.
* Calculate average Salary.
* Rename column as AverageSalary.

---

### ✅ 3. Add High Salary Flag

Create:

```text
IsHighSalary
```

Rule:

```text
Salary > 100000 → 1
Else → 0
```

---

### ✅ 4. Top Earners

Return employees earning above threshold.

---

### ✅ 5. Department Salary Summary

Generate salary distribution by department using Crosstab.

---

# Question 2: Student Performance Analyzer

## 📌 Problem Statement

A school maintains student marks data. Analyze academic performance and grading patterns.

## ✅ Declare Class

```python
class StudentAnalyzer:
```

---

## Operations

### 1. Create Student DataFrame

Columns:

```text
StudentID
Class
Subject
Marks
```

---

### 2. Calculate Average Marks Per Student

Group by:

```text
StudentID
```

Calculate average marks.

---

### 3. Add Grade Column

Rules:

```text
90+ A
75+ B
60+ C
Else D
```

---

### 4. High Performing Students

Return students with average marks greater than threshold.

---

### 5. Grade Distribution Summary

Generate Crosstab:

```text
Class vs Grade
```

---

# Question 3: Sales Analyzer

## 📌 Problem Statement

A company tracks product sales across multiple regions.

## ✅ Declare Class

```python
class SalesAnalyzer:
```

---

### 1. Create Sales DataFrame

Columns:

```text
SaleID
Product
Region
Amount
SaleDate
```

---

### 2. Monthly Sales Summary

Extract:

```python
df["SaleDate"].str[:7]
```

Calculate monthly revenue.

---

### 3. High Revenue Flag

```text
Amount > 50000
```

---

### 4. Top Selling Regions

Group by Region.

Calculate total revenue.

---

### 5. Product vs Region Summary

Use Crosstab.

---

# Question 4: Hospital Patient Analyzer

## 📌 Problem Statement

A hospital tracks patient visits and billing information.

## ✅ Declare Class

```python
class PatientAnalyzer:
```

---

### 1. Create Patient DataFrame

Columns:

```text
PatientID
Department
Doctor
BillAmount
VisitDate
```

---

### 2. Revenue By Department

Group by Department.

Calculate revenue.

---

### 3. High Bill Flag

```text
BillAmount > 20000
```

---

### 4. Frequent Visitors

Patients visiting more than N times.

---

### 5. Department-wise Visit Summary

Department vs Doctor Crosstab.

---

# Question 5: Banking Transaction Analyzer

## 📌 Problem Statement

A bank tracks customer transactions.

## ✅ Declare Class

```python
class TransactionAnalyzer:
```

---

### 1. Create Transaction DataFrame

Columns:

```text
TransactionID
CustomerID
TransactionType
Amount
TransactionDate
```

---

### 2. Monthly Transaction Volume

Calculate monthly transaction count.

---

### 3. Add Withdrawal Flag

```text
Withdrawal → 1
Others → 0
```

---

### 4. High Value Customers

Customers with transaction totals above threshold.

---

### 5. Transaction Summary

Customer Type vs Transaction Type Crosstab.

---

# Question 6: Inventory Analyzer

## 📌 Problem Statement

A warehouse tracks inventory stock levels.

## ✅ Declare Class

```python
class InventoryAnalyzer:
```

---

### 1. Create Inventory DataFrame

Columns:

```text
ProductID
Category
Warehouse
Stock
```

---

### 2. Stock Per Warehouse

Group by Warehouse.

Calculate total stock.

---

### 3. Low Stock Flag

```text
Stock < 20
```

---

### 4. Critical Inventory Items

Filter low stock products.

---

### 5. Warehouse Inventory Summary

Warehouse vs Category Crosstab.

---

# Question 7: Telecom Usage Analyzer

## 📌 Problem Statement

A telecom company tracks customer usage.

## ✅ Declare Class

```python
class TelecomAnalyzer:
```

---

### 1. Create Usage DataFrame

Columns:

```text
CustomerID
Plan
DataUsage
CallMinutes
```

---

### 2. Average Data Usage By Plan

Group by Plan.

Calculate average usage.

---

### 3. Heavy User Flag

```text
DataUsage > 500
```

---

### 4. Heavy Data Consumers

Filter heavy users.

---

### 5. Plan Usage Summary

Plan vs Usage Category Crosstab.

---

# Question 8: Logistics Shipment Analyzer

## 📌 Problem Statement

A logistics company tracks shipment deliveries.

## ✅ Declare Class

```python
class ShipmentAnalyzer:
```

---

### 1. Create Shipment DataFrame

Columns:

```text
ShipmentID
Region
Status
Cost
```

---

### 2. Total Cost Per Region

Group by Region.

Calculate shipment cost.

---

### 3. Delayed Shipment Flag

```text
Status = Delayed
```

---

### 4. Regions With Maximum Delays

Count delayed shipments.

---

### 5. Shipment Summary

Region vs Status Crosstab.

---

# Question 9: Movie Rating Analyzer

## 📌 Problem Statement

A streaming platform collects movie ratings.

## ✅ Declare Class

```python
class MovieAnalyzer:
```

---

### 1. Create Rating DataFrame

Columns:

```text
MovieID
Genre
UserID
Rating
```

---

### 2. Average Rating Per Genre

Group by Genre.

Calculate average rating.

---

### 3. Highly Rated Flag

```text
Rating >= 4
```

---

### 4. Popular Movies

Movies with average rating above threshold.

---

### 5. Genre Rating Summary

Genre vs Rating Category Crosstab.

---

# Question 10: Cricket Tournament Analyzer

## 📌 Problem Statement

A cricket board tracks player performance.

## ✅ Declare Class

```python
class CricketAnalyzer:
```

---

### 1. Create Cricket DataFrame

Columns:

```text
PlayerID
Team
Runs
MatchDate
```

---

### 2. Monthly Runs Summary

Extract month from MatchDate.

Calculate runs scored per month.

---

### 3. Century Flag

```text
Runs >= 100
```

---

### 4. Consistent Players

Players with more than N centuries.

---

### 5. Team Performance Summary

Team vs Century Flag Crosstab.

---

# Pandas Concepts Covered

| Concept            | Questions                       |
| ------------------ | ------------------------------- |
| DataFrame Creation | All                             |
| Filtering          | All                             |
| groupby()          | All                             |
| size()             | Attendance, Banking, Cricket    |
| count()            | Banking, Logistics              |
| sum()              | Sales, Inventory, Logistics     |
| mean()             | Salary, Student, Telecom, Movie |
| astype(int)        | All Flag Questions              |
| str[:7]            | Sales, Banking, Cricket         |
| merge()            | Advanced Extensions             |
| fillna()           | Advanced Extensions             |
| crosstab()         | All                             |
| reindex()          | Summary Reports                 |
| reset_index()      | All Aggregations                |
| sort_values()      | Top Performers                  |
| value_counts()     | Extensions                      |
| apply()            | Grade and Category Creation     |
| lambda             | Advanced Solutions              |

# Difficulty Progression

### Beginner

```text
Attendance Analyzer
Salary Analyzer
Student Analyzer
```

### Intermediate

```text
Sales Analyzer
Inventory Analyzer
Telecom Analyzer
```

### Advanced

```text
Banking Analyzer
Hospital Analyzer
Movie Analyzer
Cricket Analyzer
```
