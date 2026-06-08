# Retail Sales Data Warehouse using Python

## Project Overview

A complete end-to-end Data Engineering project using **Python as the primary language**.

### Objectives

* Build ETL pipelines using Python
* Load data into PostgreSQL
* Implement Data Quality Checks
* Design a Star Schema Data Warehouse
* Generate Business Reports
* Automate execution using Airflow
* Visualize data using Power BI

---

# Business Problem

A retail organization receives data from multiple systems:

1. Customer Management System
2. Product Master System
3. Sales Transactions
4. Inventory System
5. Third-Party APIs

Management requires:

* Daily Sales Reports
* Revenue Trends
* Product Performance
* Customer Analytics
* Inventory Monitoring
* Profitability Analysis

---

# Technology Stack

| Layer           | Technology         |
| --------------- | ------------------ |
| Programming     | Python             |
| Database        | PostgreSQL         |
| ETL             | Python             |
| Processing      | Pandas             |
| API Integration | Requests           |
| Data Validation | Great Expectations |
| Scheduling      | Apache Airflow     |
| Dashboarding    | Power BI           |
| Logging         | Python Logging     |
| Configuration   | YAML               |
| Testing         | Pytest             |

---

# Solution Architecture

```text
+----------------+
| Sales CSV      |
+----------------+
         |
+----------------+
| Customer CSV   |
+----------------+
         |
+----------------+
| Product CSV    |
+----------------+
         |
+----------------+
| Inventory CSV  |
+----------------+
         |
+----------------+
| Weather API    |
+----------------+
         |
      Python ETL
         |
  Staging Tables
         |
 Transformation
         |
 Data Warehouse
         |
     Power BI
```

---

# Project Structure

```text
retail_dw_project/

├── config/
│   └── config.yaml
│
├── data/
│   ├── customers.csv
│   ├── products.csv
│   ├── sales.csv
│   └── inventory.csv
│
├── sql/
│   ├── ddl.sql
│   ├── staging.sql
│   └── warehouse.sql
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
│
├── logs/
├── tests/
├── requirements.txt
└── README.md
```

---

# Sample Datasets

## customers.csv

```csv
customer_id,name,city,state
1,Ravi,Mumbai,MH
2,Anita,Pune,MH
3,John,Bangalore,KA
4,Priya,Chennai,TN
```

## products.csv

```csv
product_id,product_name,category,price,cost
101,Laptop,Electronics,60000,50000
102,Mobile,Electronics,25000,18000
103,TV,Electronics,45000,35000
```

## sales.csv

```csv
sale_id,customer_id,product_id,qty,sale_date
1,1,101,1,2025-01-01
2,2,102,2,2025-01-02
3,3,103,1,2025-01-03
4,1,102,1,2025-01-04
```

## inventory.csv

```csv
product_id,stock_qty
101,100
102,150
103,75
```

---

# Data Warehouse Design

## Star Schema

```text
               DIM_CUSTOMER
                      |
                      |
DIM_DATE ---- FACT_SALES ---- DIM_PRODUCT
                      |
                      |
               DIM_INVENTORY
```

---

# PostgreSQL DDL

## DIM_CUSTOMER

```sql
CREATE TABLE dim_customer
(
    customer_key SERIAL PRIMARY KEY,
    customer_id INTEGER,
    customer_name VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(50)
);
```

## DIM_PRODUCT

```sql
CREATE TABLE dim_product
(
    product_key SERIAL PRIMARY KEY,
    product_id INTEGER,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price NUMERIC(10,2),
    cost NUMERIC(10,2)
);
```

## FACT_SALES

```sql
CREATE TABLE fact_sales
(
    sales_key SERIAL PRIMARY KEY,
    customer_key INTEGER,
    product_key INTEGER,
    sale_date DATE,
    quantity INTEGER,
    sales_amount NUMERIC(12,2),
    profit NUMERIC(12,2)
);
```

---

# Extract Layer

## extract.py

```python
import pandas as pd

customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
sales = pd.read_csv("data/sales.csv")
inventory = pd.read_csv("data/inventory.csv")
```

---

# Transform Layer

## transform.py

```python
import pandas as pd

customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
sales = pd.read_csv("data/sales.csv")

df = pd.merge(
    sales,
    products,
    on="product_id"
)

df["sales_amount"] = df["qty"] * df["price"]

df["profit"] = (
    df["qty"] *
    (df["price"] - df["cost"])
)
```

---

# Data Validation

```python
assert df.shape[0] > 0

assert df["customer_id"].isnull().sum() == 0

assert df["product_id"].isnull().sum() == 0
```

---

# Database Load Layer

## load.py

```python
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:admin@localhost:5432/retail"
)

df.to_sql(
    "fact_sales",
    engine,
    if_exists="append",
    index=False
)
```

---

# Pipeline Orchestration

## pipeline.py

```python
from extract import *
from transform import *
from load import *

def run_pipeline():

    print("Extract Started")
    print("Transform Started")
    print("Validation Completed")
    print("Load Completed")

if __name__ == "__main__":
    run_pipeline()
```

---

# Logging Framework

```python
import logging

logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO
)

logging.info("Pipeline Started")
```

---

# Incremental Loading

## SQL

```sql
SELECT MAX(sale_date)
FROM fact_sales;
```

## Python

```python
last_load_date = get_last_load_date()

sales = sales[
    sales["sale_date"] > last_load_date
]
```

---

# API Integration

```python
import requests

response = requests.get(
    "https://dummyjson.com/products"
)

products = response.json()
```

---

# Reporting Queries

## Total Revenue

```sql
SELECT SUM(sales_amount)
FROM fact_sales;
```

## Monthly Sales

```sql
SELECT
DATE_TRUNC('month', sale_date),
SUM(sales_amount)
FROM fact_sales
GROUP BY 1;
```

## Top Customers

```sql
SELECT
customer_key,
SUM(sales_amount)
FROM fact_sales
GROUP BY customer_key
ORDER BY 2 DESC;
```

---

# Unit Testing

## test_sales.py

```python
def test_sales_amount():
    assert df["sales_amount"].sum() > 0
```

---

# Airflow DAG

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG(
    dag_id="retail_pipeline",
    start_date=datetime(2025,1,1),
    schedule="@daily",
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=load
    )

    extract_task >> transform_task >> load_task
```

---

# Power BI Dashboards

## Executive Dashboard

* Revenue
* Profit
* Orders
* Customers

## Product Dashboard

* Top Products
* Category Revenue
* Category Profit

## Customer Dashboard

* Top Customers
* Revenue by City
* Customer Segmentation

---

# Production Enhancements

## Slowly Changing Dimension (SCD Type 2)

```sql
effective_date DATE,
expiry_date DATE,
is_current CHAR(1)
```

## Audit Table

```sql
CREATE TABLE etl_audit
(
    batch_id BIGINT,
    record_count BIGINT,
    load_time TIMESTAMP,
    status VARCHAR(20)
);
```

## Error Logging Table

```sql
CREATE TABLE etl_errors
(
    error_id BIGSERIAL,
    error_message TEXT,
    source_file VARCHAR(200),
    error_timestamp TIMESTAMP
);
```

## Metadata Table

```sql
CREATE TABLE metadata_control
(
    table_name VARCHAR(100),
    last_load_date TIMESTAMP
);
```

---

# Recommended Enhancements for Lead Data Engineer Portfolio

* Metadata-Driven ETL Framework
* Configuration-Driven Processing
* Reusable ETL Components
* SCD Type 1 & Type 2
* Data Quality Framework
* Audit Framework
* Exception Handling Framework
* Dockerized Deployment
* CI/CD Pipeline
* Airflow Scheduling
* Power BI Reporting
* Unit & Integration Testing
* Cloud Migration (AWS/GCP/Azure)

---

# Expected Interview Topics

1. ETL vs ELT
2. Star vs Snowflake Schema
3. SCD Types
4. Incremental Loading
5. CDC (Change Data Capture)
6. Data Quality Validation
7. Airflow DAG Design
8. Python ETL Frameworks
9. PostgreSQL Optimization
10. Partitioning & Indexing
11. Error Handling
12. Data Warehouse Design
13. Dimensional Modeling
14. Performance Tuning
15. Data Governance
16. Cloud Data Engineering
17. CI/CD for Data Pipelines
18. Monitoring & Alerting
19. Metadata Management
20. Production Support Best Practices

```
```
