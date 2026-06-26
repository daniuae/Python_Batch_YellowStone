# Databricks Unity Catalog, Governance & Performance Tuning

## Table of Contents

1. Unity Catalog Architecture
2. Metastore Concepts
3. Catalogs
4. Schemas
5. Tables
6. Fine-Grained Access Control
7. Table-Level Permissions
8. Row-Level & Column-Level Security
9. Data Lineage
10. Audit Logging
11. Governance Best Practices
12. Role-Based Access Control (RBAC)
13. Cluster Performance Tuning
14. Query Performance Tuning
15. Data Skew Mitigation
16. Data Skipping (ZORDER)
17. OPTIMIZE Command
18. VACUUM Command
19. Performance Tuning Checklist
20. Interview Questions

---

# 1. Unity Catalog Architecture

## What is Unity Catalog?

Unity Catalog is Databricks' centralized governance solution for managing:

- Data
- AI Models
- ML Features
- Files
- Notebooks
- External Storage

It provides a single place to manage permissions, security, auditing, and lineage across all workspaces.

---

## Architecture

```
Organization

      │

Metastore
      │
      ├──────────────┐
      │              │

Catalog A      Catalog B
      │              │

Schemas       Schemas
      │              │

Tables       Views
Functions
Volumes
```

Hierarchy

```
Metastore

    ↓

Catalog

    ↓

Schema

    ↓

Table/View/Function
```

---

# Components

|Component|Purpose|
|----------|--------|
|Metastore|Top-level governance container|
|Catalog|Business domain|
|Schema|Logical grouping|
|Table|Actual data|
|View|Virtual table|
|Function|Reusable SQL function|
|Volume|Non-tabular files|

---

# Example

```
Metastore

Company

│

├── Sales Catalog

│      ├── Bronze

│      ├── Silver

│      └── Gold

│

├── Finance Catalog

│

└── HR Catalog
```

---

# 2. Metastore Concepts

A Metastore stores metadata.

Metadata includes

- Table names
- Locations
- Schemas
- Permissions
- Ownership
- Lineage

It does NOT store actual data.

Actual data resides in:

- ADLS
- Amazon S3
- Google Cloud Storage

---

## One Metastore

```
Users

↓

Unity Catalog Metastore

↓

External Storage
```

One metastore can be shared across multiple Databricks workspaces.

Advantages

- Central governance
- Central security
- Shared metadata
- Easier administration

---

# 3. Catalogs

A Catalog is the top-level namespace.

Example

```
Sales

Finance

Marketing

HR
```

SQL

```sql
CREATE CATALOG sales;
```

List catalogs

```sql
SHOW CATALOGS;
```

---

# 4. Schemas

Schemas organize objects inside a catalog.

Example

```
Sales

    Bronze

    Silver

    Gold
```

SQL

```sql
CREATE SCHEMA sales.bronze;
```

---

# 5. Tables

Tables store data.

Example

```
sales.bronze.transactions

sales.silver.customers

sales.gold.revenue
```

Create table

```sql
CREATE TABLE sales.gold.orders
(
order_id INT,
customer STRING,
amount DOUBLE
);
```

---

# Three-Level Namespace

```
catalog.schema.table
```

Example

```
sales.gold.transactions
```

---

# 6. Fine-Grained Access Control

Unity Catalog supports security at multiple levels.

```
Catalog

↓

Schema

↓

Table

↓

Column

↓

Row
```

Permissions can be granted to:

- Users
- Groups
- Service Principals

---

# SQL Example

Grant SELECT

```sql
GRANT SELECT
ON TABLE sales.gold.orders
TO analysts;
```

Grant INSERT

```sql
GRANT INSERT
ON TABLE sales.gold.orders
TO engineers;
```

---

# 7. Table-Level Permissions

Examples

```
SELECT

INSERT

UPDATE

DELETE

MODIFY

OWNERSHIP

ALL PRIVILEGES
```

Example

```sql
GRANT ALL PRIVILEGES
ON TABLE sales.gold.orders
TO admin;
```

---

# 8. Row-Level & Column-Level Security

## Row-Level Security

Only show rows for India.

```
User A

↓

Country = India
```

SQL Example

```sql
CREATE VIEW india_orders AS

SELECT *

FROM sales.orders

WHERE country='India';
```

---

## Column-Level Security

Hide salary column.

```
Employee

Name

Department

Salary ❌
```

---

Masking Example

```sql
SELECT

employee_name,

department,

'*****' AS salary

FROM employee;
```

---

# 9. Data Lineage

Lineage shows

Where data comes from

↓

Which tables were used

↓

Which notebooks updated them

↓

Who modified them

Example

```
Raw Sales CSV

↓

Bronze

↓

Silver

↓

Gold Dashboard
```

Benefits

- Impact analysis
- Debugging
- Compliance
- Governance

---

# 10. Audit Logging

Audit logs record

- Login
- Query execution
- Permission changes
- Table creation
- Deletes
- Access attempts

Example

```
User

↓

SELECT

↓

sales.gold.orders

↓

Logged
```

Benefits

- Security
- Compliance
- Investigation
- Monitoring

---

# 11. Governance Best Practices

✔ Separate catalogs by business

```
Sales

Finance

HR

Marketing
```

✔ Follow Bronze/Silver/Gold architecture

✔ Use Groups instead of individual users

✔ Enable audit logging

✔ Use managed tables

✔ Use Unity Catalog everywhere

✔ Apply least privilege

✔ Regular permission reviews

✔ Use naming conventions

---

# 12. Role-Based Access Control (RBAC)

Instead of assigning permissions individually,

Assign them to groups.

```
Users

↓

Groups

↓

Permissions
```

Example

```
Analysts

↓

Read Gold Tables

Engineers

↓

Read Bronze

Write Silver

Admins

↓

Full Control
```

Example SQL

```sql
GRANT SELECT

ON SCHEMA sales.gold

TO analysts;
```

---

# 13. Cluster Performance Tuning

Performance depends on

- Cluster size
- Number of workers
- Memory
- CPU
- Autoscaling

---

## Cluster Types

### All Purpose

Used for

- Interactive notebooks

### Job Cluster

Used for

- ETL
- Scheduled jobs

Job clusters are cheaper because they terminate automatically.

---

## Autoscaling

Instead of fixed workers

```
2 Workers

↓

5 Workers

↓

10 Workers

↓

Back to 2
```

Benefits

- Lower cost
- Better utilization

---

# Best Practices

✔ Enable autoscaling

✔ Use Photon engine

✔ Use latest runtime

✔ Enable autoscaling local storage

✔ Choose SSD-backed instances

---

# 14. Query Performance Tuning

## Avoid SELECT *

Instead of

```sql
SELECT *

FROM sales;
```

Use

```sql
SELECT customer_id,

amount

FROM sales;
```

Less data

↓

Faster

---

## Predicate Pushdown

```sql
SELECT *

FROM sales

WHERE year=2025;
```

Only required files are scanned.

---

## Partition Pruning

Partition

```
Year

2023

2024

2025
```

Query

```sql
WHERE year=2025
```

Only 2025 partition is read.

---

## Cache Frequently Used Tables

```sql
CACHE TABLE sales;
```

---

# 15. Data Skew Mitigation

## What is Data Skew?

One partition contains much more data than others.

Example

```
Partition 1

100 rows

Partition 2

150 rows

Partition 3

9 Million rows
```

One executor becomes slow.

Entire job waits.

---

## Solutions

### Repartition

```python
df = df.repartition(200)
```

---

### Salting

Add random values

```
Customer_1

↓

Customer_1_3
```

Distributes data evenly.

---

### Broadcast Join

Small table

↓

Broadcast

↓

Avoid shuffle

```python
from pyspark.sql.functions import broadcast

df.join(broadcast(dim),"id")
```

---

### AQE

Adaptive Query Execution automatically detects skew.

Enable

```python
spark.conf.set(
"spark.sql.adaptive.enabled",
"true")
```

---

# 16. Data Skipping (ZORDER)

Without ZORDER

```
Customer IDs

2

900

15

800

100
```

Scattered

---

With ZORDER

```
2

15

100

800

900
```

Grouped together.

Spark skips many files.

---

Syntax

```sql
OPTIMIZE sales

ZORDER BY(customer_id);
```

Benefits

- Faster filtering
- Better data skipping
- Lower I/O

---

# 17. OPTIMIZE

Compacts small files.

Before

```
1000 Files

↓

OPTIMIZE

↓

25 Files
```

Syntax

```sql
OPTIMIZE sales;
```

Partition

```sql
OPTIMIZE sales

WHERE year=2025;
```

Benefits

- Faster reads
- Less metadata
- Better cache

---

# 18. VACUUM

Removes obsolete files.

```
Old Files

↓

VACUUM

↓

Deleted
```

Default retention

```
7 Days
```

Syntax

```sql
VACUUM sales;
```

Specify retention

```sql
VACUUM sales

RETAIN 168 HOURS;
```

Never use

```sql
RETAIN 0 HOURS
```

in production.

---

# 19. Performance Tuning Checklist

|Technique|Purpose|
|----------|-------|
|Photon|Fast execution engine|
|Autoscaling|Reduce costs|
|OPTIMIZE|Merge small files|
|ZORDER|Improve data skipping|
|VACUUM|Remove obsolete files|
|Partitioning|Reduce scanned data|
|Broadcast Join|Avoid shuffle|
|Caching|Speed repeated queries|
|AQE|Optimize execution plan|
|Predicate Pushdown|Read fewer records|

---

# Complete Workflow

```
Raw Data

↓

Bronze Table

↓

Silver Table

↓

Gold Table

↓

OPTIMIZE

↓

ZORDER

↓

VACUUM

↓

BI Dashboard
```

---

# 20. Common Interview Questions

### Unity Catalog

- What is Unity Catalog?
- What is a Metastore?
- Difference between Catalog and Schema?
- Managed vs External Tables?
- Benefits of Unity Catalog?

---

### Security

- What is RBAC?
- How do you grant table permissions?
- What is row-level security?
- What is column masking?
- What are service principals?

---

### Governance

- What is data lineage?
- Why is audit logging important?
- Governance best practices?
- Least privilege principle?

---

### Performance

- Explain data skew.
- What is Adaptive Query Execution (AQE)?
- Difference between partitioning and ZORDER?
- What does OPTIMIZE do?
- Why use VACUUM?
- What is predicate pushdown?
- What is partition pruning?
- When should broadcast joins be used?
- What is Photon?
- How does autoscaling improve performance?

---

# Summary

- **Unity Catalog** provides centralized governance for data, AI assets, and metadata.
- **Metastore → Catalog → Schema → Table** is the object hierarchy.
- **RBAC** and fine-grained permissions secure access at the catalog, schema, table, column, and row levels.
- **Data lineage** and **audit logging** improve transparency, compliance, and troubleshooting.
- **Performance tuning** combines good cluster sizing, Photon, partitioning, predicate pushdown, AQE, broadcast joins, and caching.
- **OPTIMIZE**, **ZORDER**, and **VACUUM** are essential Delta Lake maintenance commands that improve performance and manage storage efficiently.
