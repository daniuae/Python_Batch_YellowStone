# Pandas Cheat Sheet - Real World Business Use Cases with E-Commerce Dataset

> Based on the Pandas Cheat Sheet provided, this document demonstrates how Pandas functions are used in real-world business scenarios.

---

# Dataset: E-Commerce Sales Analytics

## Business Scenario

You work for an E-Commerce company such as Amazon, Flipkart, Myntra, or Walmart.

The company wants to analyze:

- Sales Performance
- Customer Behavior
- Product Performance
- Regional Revenue
- Monthly Trends
- Customer Segmentation

---

## Sample Dataset

```csv
OrderID,CustomerID,CustomerName,Product,Category,Region,OrderDate,Quantity,Price
1001,C001,John Doe,Laptop,Electronics,North,2025-01-01,2,50000
1002,C002,Mary Smith,Mobile,Electronics,South,2025-01-02,1,25000
1003,C001,John Doe,Mouse,Accessories,North,2025-01-03,3,500
1004,C003,Ravi Kumar,Keyboard,Accessories,West,2025-01-04,2,1500
1005,C004,Priya Sharma,Laptop,Electronics,East,2025-01-05,1,52000
1006,C002,Mary Smith,Headphones,Accessories,South,2025-01-06,2,2000
```

---

# 1. Reading Data

## Business Use Case

Daily sales data arrives as CSV files.

```python
import pandas as pd

df = pd.read_csv("sales.csv")
```

---

# 2. Data Exploration

## Business Question

How many records and columns exist?

```python
print(df.shape)
```

Output:

```python
(6, 9)
```

---

## Business Question

What are the data types?

```python
df.info()
```

---

## Business Question

What is the statistical summary?

```python
df.describe()
```

---

# 3. Creating New Columns

## Business Use Case

Calculate Revenue.

Revenue = Quantity × Price

```python
df["Revenue"] = df["Quantity"] * df["Price"]
```

### Alternative using assign()

```python
df = df.assign(
    Revenue=lambda x: x.Quantity * x.Price
)
```

Output:

| Product | Quantity | Price | Revenue |
|----------|----------|----------|----------|
| Laptop | 2 | 50000 | 100000 |
| Mobile | 1 | 25000 | 25000 |

---

# 4. Filtering Rows

## Business Question

Find orders generating more than ₹50,000 revenue.

```python
df[df["Revenue"] > 50000]
```

### Using query()

```python
df.query("Revenue > 50000")
```

Output:

| OrderID | Product | Revenue |
|----------|----------|----------|
| 1001 | Laptop | 100000 |
| 1005 | Laptop | 52000 |

---

# 5. Selecting Columns

## Business Question

Show customer names and revenues.

```python
df[["CustomerName", "Revenue"]]
```

---

# 6. Sorting Data

## Business Question

Which customers generated the highest revenue?

```python
df.sort_values(
    "Revenue",
    ascending=False
)
```

---

# 7. GroupBy Analysis

## Business Question

Revenue by Region

```python
df.groupby("Region")["Revenue"].sum()
```

Output:

```text
East      52000
North    101500
South     29000
West       3000
```

---

# 8. Aggregations

## Business Question

Average, Maximum and Total Revenue by Region

```python
df.groupby("Region").agg({
    "Revenue": ["sum", "mean", "max"]
})
```

Output:

| Region | Sum | Mean | Max |
|----------|----------|----------|----------|
| North | 101500 | 50750 | 100000 |

---

# 9. Top Selling Products

## Business Question

Find Top 3 Revenue Generating Products.

```python
df.nlargest(3, "Revenue")
```

---

# 10. Handling Missing Values

## Business Scenario

Price data is missing.

```python
df.loc[2, "Price"] = None
```

### Identify Missing Values

```python
df.isnull().sum()
```

### Replace Missing Values

```python
df["Price"] = df["Price"].fillna(
    df["Price"].mean()
)
```

---

# 11. Removing Duplicates

## Business Use Case

Create unique customer list for marketing.

```python
customers = df.drop_duplicates(
    subset=["CustomerID"]
)
```

---

# 12. Date Analysis

## Convert Date Column

```python
df["OrderDate"] = pd.to_datetime(
    df["OrderDate"]
)
```

### Extract Year

```python
df["Year"] = df["OrderDate"].dt.year
```

### Extract Month

```python
df["Month"] = df["OrderDate"].dt.month
```

### Extract Quarter

```python
df["Quarter"] = df["OrderDate"].dt.quarter
```

---

## Business Question

Quarterly Revenue

```python
df.groupby("Quarter")["Revenue"].sum()
```

---

# 13. Customer Ranking

## Business Question

Who are the highest revenue customers?

```python
customer_sales = (
    df.groupby("CustomerName")
      ["Revenue"]
      .sum()
      .reset_index()
)

customer_sales["Rank"] = (
    customer_sales["Revenue"]
      .rank(
          method="dense",
          ascending=False
      )
)
```

Output:

| Customer | Revenue | Rank |
|-----------|-----------|------|
| John Doe | 101500 | 1 |
| Priya Sharma | 52000 | 2 |

---

# 14. Rolling Window Analysis

## Business Use Case

Calculate 7-Day Moving Average Revenue.

```python
daily_sales = (
    df.groupby("OrderDate")
      ["Revenue"]
      .sum()
      .reset_index()
)

daily_sales["MovingAvg"] = (
    daily_sales["Revenue"]
      .rolling(7)
      .mean()
)
```

### Used In

- Banking
- Stock Market
- Retail Sales
- Demand Forecasting

---

# 15. Cumulative Revenue

## Business Question

What is the cumulative revenue over time?

```python
daily_sales["CumulativeRevenue"] = (
    daily_sales["Revenue"]
      .cumsum()
)
```

Output:

| Date | Revenue | Cumulative Revenue |
|---------|---------|---------|
| Jan 1 | 100000 | 100000 |
| Jan 2 | 25000 | 125000 |
| Jan 3 | 1500 | 126500 |

---

# 16. Merging Data

## Customer Master Dataset

```python
customers = pd.DataFrame({
    "CustomerID": ["C001", "C002", "C003"],
    "City": ["Mumbai", "Chennai", "Delhi"]
})
```

### Merge Customer Details

```python
result = pd.merge(
    df,
    customers,
    on="CustomerID",
    how="left"
)
```

### Business Use Case

Customer Segmentation

---

# 17. Pivot Tables

## Business Question

Revenue by Region and Category

```python
pivot = df.pivot_table(
    values="Revenue",
    index="Region",
    columns="Category",
    aggfunc="sum"
)
```

Output:

| Region | Accessories | Electronics |
|----------|----------|----------|
| North | 1500 | 100000 |
| South | 4000 | 25000 |

---

# 18. Melt (Unpivot)

## Business Use Case

Prepare data for Power BI or Tableau.

```python
pd.melt(df)
```

Before:

| Month | Sales | Profit |
|----------|----------|----------|
| Jan | 1000 | 200 |

After:

| Variable | Value |
|----------|----------|
| Sales | 1000 |
| Profit | 200 |

---

# 19. String Operations

## Business Question

Find customers whose names start with J.

```python
df[
    df["CustomerName"]
      .str.startswith("J")
]
```

### Convert Names to Title Case

```python
df["CustomerName"] = (
    df["CustomerName"]
      .str.title()
)
```

---

# 20. Visualizations

## Revenue by Product

```python
import matplotlib.pyplot as plt

df.groupby("Product")["Revenue"] \
  .sum() \
  .plot.bar()

plt.show()
```

---

# 21. KPI Dashboard Metrics

## Total Revenue

```python
total_revenue = df["Revenue"].sum()
```

---

## Average Order Value

```python
average_order_value = (
    df["Revenue"].mean()
)
```

---

## Unique Customers

```python
unique_customers = (
    df["CustomerID"]
      .nunique()
)
```

---

## Best Selling Product

```python
top_product = (
    df.groupby("Product")
      ["Revenue"]
      .sum()
      .idxmax()
)
```

---

## Revenue by Region

```python
region_sales = (
    df.groupby("Region")
      ["Revenue"]
      .sum()
)
```

---

## Monthly Revenue

```python
monthly_sales = (
    df.groupby("Month")
      ["Revenue"]
      .sum()
)
```

---

# Complete Business Workflow

```python
import pandas as pd

# Load data
df = pd.read_csv("sales.csv")

# Create Revenue Column
df["Revenue"] = df["Quantity"] * df["Price"]

# Convert Date
df["OrderDate"] = pd.to_datetime(
    df["OrderDate"]
)

# Extract Month
df["Month"] = df["OrderDate"].dt.month

# Regional Revenue
region_sales = (
    df.groupby("Region")
      ["Revenue"]
      .sum()
)

# Monthly Revenue
monthly_sales = (
    df.groupby("Month")
      ["Revenue"]
      .sum()
)

# Top Customers
customer_sales = (
    df.groupby("CustomerName")
      ["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

print(region_sales)
print(monthly_sales)
print(customer_sales)
```

---

# Industry-wise Pandas Use Cases

| Industry | Business Problem | Pandas Functions |
|------------|------------------|------------------|
| Banking | Fraud Detection | groupby(), rolling(), query() |
| Retail | Sales Dashboard | pivot_table(), merge(), plot() |
| Healthcare | Patient Analytics | fillna(), groupby(), datetime |
| Logistics | Shipment Tracking | merge(), sort_values() |
| Manufacturing | Production Monitoring | cumsum(), rolling() |
| Marketing | Campaign Analysis | melt(), pivot_table() |
| Finance | Stock Analysis | rolling(), rank(), cumsum() |
| E-Commerce | Customer Segmentation | merge(), groupby(), query() |

---

# Key Pandas Functions Covered

- read_csv()
- head()
- info()
- describe()
- shape
- query()
- sort_values()
- groupby()
- agg()
- merge()
- pivot_table()
- melt()
- fillna()
- drop_duplicates()
- assign()
- rank()
- rolling()
- cumsum()
- to_datetime()
- dt.month
- dt.quarter
- str.startswith()
- nlargest()
- plot.bar()

These functions represent approximately **80–90% of the Pandas operations used in real-world Data Engineering, Data Analytics, and Business Intelligence projects**.
