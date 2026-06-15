# Pandas + OOP Practice Set (10 Real-World Scenarios)

## Objective

These exercises are designed to help trainees master:

### OOP Concepts

* Class Creation
* Methods
* Object-Oriented Design
* Data Encapsulation
* Reusable Code Structure

### Pandas Concepts

* DataFrame Creation
* Filtering
* GroupBy
* Aggregation
* Merge
* Crosstab
* Pivot Tables
* Sorting
* Ranking
* Window Operations
* Missing Values
* Date Manipulation
* String Operations
* Apply Functions
* Value Counts

---

# Question 1: Employee Salary Analyzer

## Scenario

An organization maintains employee salary records.

Analyze salary distribution across departments.

### Class

```python
class SalaryAnalyzer:
```

### Functions

#### 1. Create DataFrame

```python
create_salary_df()
```

Columns:

```text
EmployeeID
Department
Salary
Experience
```

---

#### 2. Department Average Salary

Use:

```python
groupby()
mean()
```

Output:

```text
Department
Average Salary
```

---

#### 3. High Earners

Filter employees earning above threshold.

Use:

```python
filtering
```

---

#### 4. Salary Band

Create column:

```text
Salary > 100000  -> High
Salary > 50000   -> Medium
Else             -> Low
```

Use:

```python
apply()
lambda
```

---

#### 5. Department Salary Summary

Use:

```python
crosstab()
```

---

# Concepts Covered

```text
DataFrame
groupby
mean
apply
lambda
crosstab
```

---

# Question 2: Student Performance Analyzer

## Scenario

School tracks student marks.

### Class

```python
class StudentAnalyzer:
```

### Functions

#### Create DataFrame

Columns:

```text
StudentID
Class
Subject
Marks
```

---

#### Calculate Grade

```text
90+ A
75+ B
60+ C
Else D
```

Use:

```python
apply()
```

---

#### Top Students Per Class

Use:

```python
groupby()
max()
```

---

#### Subject Average

Use:

```python
groupby()
mean()
```

---

#### Grade Distribution

Use:

```python
crosstab()
```

---

# Concepts

```text
apply
groupby
mean
max
crosstab
```

---

# Question 3: E-Commerce Order Analyzer

## Scenario

Online store tracks orders.

### Class

```python
class OrderAnalyzer:
```

### Columns

```text
OrderID
CustomerID
Product
Category
Amount
OrderDate
```

---

### Functions

#### Monthly Revenue

Use:

```python
str[:7]
groupby
sum
```

---

#### Top Selling Categories

Use:

```python
groupby
sum
sort_values
```

---

#### High Value Orders

Filter:

```text
Amount > Threshold
```

---

#### Revenue Contribution %

Calculate:

```text
Category Revenue
---------------- × 100
Total Revenue
```

---

# Concepts

```text
groupby
sum
sort_values
filter
calculated columns
```

---

# Question 4: Hospital Patient Analyzer

## Scenario

Hospital tracks patient visits.

### Class

```python
class PatientAnalyzer:
```

### Columns

```text
PatientID
Department
Doctor
VisitDate
BillAmount
```

---

### Functions

#### Total Revenue per Department

```python
groupby
sum
```

---

#### Most Visited Doctor

```python
value_counts
```

---

#### Department Visit Summary

```python
crosstab
```

---

#### Top 5 Patients

```python
groupby
sum
sort_values
head
```

---

# Concepts

```text
value_counts
groupby
sum
head
sorting
```

---

# Question 5: Retail Inventory Analyzer

## Scenario

Store tracks inventory.

### Class

```python
class InventoryAnalyzer:
```

### Columns

```text
ProductID
Category
Stock
Warehouse
```

---

### Functions

#### Low Stock Products

```python
filter
```

---

#### Stock per Warehouse

```python
groupby
sum
```

---

#### Inventory Matrix

```python
crosstab
```

Warehouse vs Category

---

#### Stock Ranking

```python
rank()
```

---

# Concepts

```text
rank
groupby
sum
filter
crosstab
```

---

# Question 6: Banking Transaction Analyzer

## Scenario

Bank records customer transactions.

### Class

```python
class TransactionAnalyzer:
```

### Columns

```text
CustomerID
TransactionDate
TransactionType
Amount
```

---

### Functions

#### Monthly Transaction Volume

```python
groupby
count
```

---

#### Deposit vs Withdrawal Summary

```python
crosstab
```

---

#### Highest Spending Customers

```python
groupby
sum
sort_values
```

---

#### Running Total

```python
cumsum()
```

---

# Concepts

```text
cumsum
groupby
sum
sorting
```

---

# Question 7: Movie Rating Analyzer

## Scenario

Streaming platform tracks ratings.

### Class

```python
class MovieAnalyzer:
```

### Columns

```text
MovieID
Genre
UserID
Rating
```

---

### Functions

#### Average Rating per Genre

```python
groupby
mean
```

---

#### Rating Distribution

```python
value_counts
```

---

#### Top Rated Movies

```python
groupby
mean
sort_values
```

---

#### Genre Summary

```python
crosstab
```

---

# Concepts

```text
mean
groupby
sorting
crosstab
```

---

# Question 8: Logistics Shipment Analyzer

## Scenario

Shipping company tracks deliveries.

### Class

```python
class ShipmentAnalyzer:
```

### Columns

```text
ShipmentID
Region
Status
Cost
```

---

### Functions

#### Total Cost per Region

```python
groupby
sum
```

---

#### Delivery Status Summary

```python
crosstab
```

---

#### Delayed Shipments

```python
filter
```

---

#### Cost Ranking

```python
rank
```

---

# Concepts

```text
rank
groupby
sum
crosstab
```

---

# Question 9: Telecom Usage Analyzer

## Scenario

Telecom company tracks customer usage.

### Class

```python
class TelecomAnalyzer:
```

### Columns

```text
CustomerID
Plan
DataUsage
CallMinutes
```

---

### Functions

#### Average Usage by Plan

```python
groupby
mean
```

---

#### Heavy Data Users

```python
filter
```

---

#### Usage Category

```text
Heavy
Medium
Light
```

Use:

```python
apply
lambda
```

---

#### Plan Summary

```python
crosstab
```

---

# Concepts

```text
apply
lambda
groupby
mean
crosstab
```

---

# Question 10: Cricket Tournament Analyzer

## Scenario

Tournament tracks player performance.

### Class

```python
class CricketAnalyzer:
```

### Columns

```text
PlayerID
Team
Runs
Matches
```

---

### Functions

#### Average Runs

```python
groupby
mean
```

---

#### Top Scorers

```python
sort_values
head
```

---

#### Team Performance

```python
groupby
sum
```

---

#### Player Ranking

```python
rank
```

---

#### Team vs Player Count

```python
crosstab
```

---

# Master Pandas Concepts Covered Across All 10 Problems

| Concept      | Used In                           |
| ------------ | --------------------------------- |
| DataFrame    | All                               |
| Filtering    | 1,3,5,6,8,9                       |
| groupby      | All                               |
| sum          | 3,4,5,6,8,10                      |
| mean         | 1,2,7,9,10                        |
| size         | Many                              |
| count        | 6                                 |
| crosstab     | Almost All                        |
| value_counts | 4,7                               |
| apply        | 1,2,9                             |
| lambda       | 1,9                               |
| sort_values  | 3,4,6,7,10                        |
| rank         | 5,8,10                            |
| cumsum       | 6                                 |
| head         | 4,10                              |
| str[:7]      | 3                                 |
| merge        | Can be added in advanced versions |
| fillna       | Advanced scenarios                |
| reset_index  | All groupby outputs               |

---

# Interview Preparation Roadmap

### Beginner

```text
Question 1
Question 2
Question 3
```

### Intermediate

```text
Question 4
Question 5
Question 6
Question 7
```

### Advanced

```text
Question 8
Question 9
Question 10
```

### Expert Enhancement

Add:

```text
merge()
pivot_table()
rolling()
transform()
shift()
duplicated()
drop_duplicates()
explode()
melt()
```

to any of the above scenarios.
