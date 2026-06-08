# Matplotlib and Seaborn for Visualization
# SQLite and SQLAlchemy for Database Interaction

---

# Table of Contents

1. Introduction to Data Visualization
2. Matplotlib Fundamentals
3. Matplotlib Plot Types
4. Matplotlib Customizations
5. Seaborn Fundamentals
6. Seaborn Plot Types
7. Matplotlib vs Seaborn
8. Combining Matplotlib and Seaborn
9. SQLite Database Basics
10. SQLite with Python
11. SQLAlchemy Fundamentals
12. SQLAlchemy ORM
13. SQLAlchemy CRUD Operations
14. SQLAlchemy with SQLite
15. Complete SQL Connectivity Lab
16. Real-World Project Example

---

# 1. Introduction to Data Visualization

Data visualization helps us:

- Understand trends
- Identify patterns
- Detect anomalies
- Communicate insights

Popular Python Visualization Libraries:

| Library | Purpose |
|----------|----------|
| Matplotlib | Basic plotting |
| Seaborn | Statistical visualization |
| Plotly | Interactive dashboards |
| Bokeh | Interactive visualization |

---

# 2. Matplotlib Fundamentals

Import Library

```python
import matplotlib.pyplot as plt
```

---

## Line Plot

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 150, 200, 250]

plt.plot(months, sales)
plt.show()
```

Output:

```
Sales Trend Chart
```

---

## Add Labels

```python
plt.plot(months, sales)

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Revenue")

plt.show()
```

---

# 3. Matplotlib Plot Types

---

## 1. Line Chart

Best for trends.

```python
x = [1,2,3,4]
y = [10,20,30,40]

plt.plot(x,y)
plt.show()
```

---

## 2. Bar Chart

Best for comparison.

```python
products = ["Laptop","Mobile","Tablet"]
sales = [100,200,150]

plt.bar(products,sales)
plt.show()
```

---

## 3. Horizontal Bar Chart

```python
plt.barh(products,sales)
plt.show()
```

---

## 4. Pie Chart

```python
sizes = [40,30,20,10]

plt.pie(
    sizes,
    labels=["A","B","C","D"],
    autopct='%1.1f%%'
)

plt.show()
```

---

## 5. Histogram

Distribution of data.

```python
import numpy as np

data = np.random.randn(1000)

plt.hist(data)
plt.show()
```

---

## 6. Scatter Plot

Relationship between variables.

```python
x = [1,2,3,4,5]
y = [10,15,20,25,30]

plt.scatter(x,y)

plt.show()
```

---

## 7. Box Plot

```python
scores = [60,70,80,90,95,100]

plt.boxplot(scores)

plt.show()
```

---

## 8. Subplots

```python
fig, axes = plt.subplots(1,2)

axes[0].plot([1,2,3],[10,20,30])

axes[1].bar(["A","B"],[5,10])

plt.show()
```

---

# 4. Matplotlib Customizations

---

## Colors

```python
plt.plot(x,y,color="red")
```

---

## Line Styles

```python
plt.plot(x,y,linestyle="--")
```

---

## Markers

```python
plt.plot(
    x,
    y,
    marker="o"
)
```

---

## Grid

```python
plt.grid(True)
```

---

## Legends

```python
plt.plot(x,y,label="Revenue")

plt.legend()
```

---

## Save Figure

```python
plt.savefig("sales.png")
```

---

# 5. Seaborn Fundamentals

Seaborn is built on top of Matplotlib.

Advantages:

- Better appearance
- Statistical plots
- Easy syntax
- Pandas integration

Install:

```bash
pip install seaborn
```

Import:

```python
import seaborn as sns
```

---

# Sample Dataset

```python
import seaborn as sns

df = sns.load_dataset("tips")

print(df.head())
```

---

# 6. Seaborn Plot Types

---

## 1. Scatter Plot

```python
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip"
)
```

---

## 2. Line Plot

```python
sns.lineplot(
    data=df,
    x="size",
    y="tip"
)
```

---

## 3. Bar Plot

```python
sns.barplot(
    data=df,
    x="day",
    y="total_bill"
)
```

---

## 4. Count Plot

Counts category frequency.

```python
sns.countplot(
    data=df,
    x="day"
)
```

---

## 5. Histogram

```python
sns.histplot(
    data=df,
    x="total_bill",
    kde=True
)
```

---

## 6. Box Plot

```python
sns.boxplot(
    data=df,
    x="day",
    y="total_bill"
)
```

---

## 7. Violin Plot

```python
sns.violinplot(
    data=df,
    x="day",
    y="total_bill"
)
```

---

## 8. Pair Plot

Shows all combinations.

```python
sns.pairplot(df)
```

---

## 9. Heatmap

Correlation matrix.

```python
corr = df.corr(numeric_only=True)

sns.heatmap(
    corr,
    annot=True
)
```

---

## 10. Regression Plot

```python
sns.regplot(
    data=df,
    x="total_bill",
    y="tip"
)
```

---

# 7. Matplotlib vs Seaborn

| Feature | Matplotlib | Seaborn |
|----------|-----------|-----------|
| Easy | Medium | High |
| Styling | Manual | Automatic |
| Statistical Charts | Limited | Excellent |
| Flexibility | High | Medium |
| Performance | High | High |

---

# 8. Combining Matplotlib and Seaborn

Most common practice.

```python
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

sns.boxplot(
    data=tips,
    x="day",
    y="total_bill"
)

plt.title("Bills by Day")

plt.show()
```

---

# 9. SQLite Database Basics

SQLite is:

- Lightweight
- Serverless
- Embedded
- File-based

Database file:

```text
company.db
```

---

# Creating SQLite Database

```python
import sqlite3

conn = sqlite3.connect("company.db")

print("Connected")
```

---

# Create Table

```python
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE employee(
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary REAL
)
""")

conn.commit()
```

---

# Insert Data

```python
cursor.execute("""
INSERT INTO employee
VALUES
(1,'Rahul',50000)
""")

conn.commit()
```

---

# Read Data

```python
cursor.execute(
    "SELECT * FROM employee"
)

rows = cursor.fetchall()

for row in rows:
    print(row)
```

---

# Update Data

```python
cursor.execute("""
UPDATE employee
SET salary = 60000
WHERE id = 1
""")

conn.commit()
```

---

# Delete Data

```python
cursor.execute("""
DELETE FROM employee
WHERE id = 1
""")

conn.commit()
```

---

# Close Connection

```python
conn.close()
```

---

# 10. SQLite with Pandas

Read SQL Data

```python
import pandas as pd

df = pd.read_sql_query(
    "SELECT * FROM employee",
    conn
)

print(df)
```

---

# Write DataFrame to SQL

```python
df.to_sql(
    "employee",
    conn,
    if_exists="replace",
    index=False
)
```

---

# 11. SQLAlchemy Fundamentals

SQLAlchemy provides:

- Database abstraction
- ORM
- Connection pooling
- Query generation

Install:

```bash
pip install sqlalchemy
```

---

# Create Engine

```python
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///company.db"
)
```

---

# Test Connection

```python
with engine.connect() as conn:
    print("Connected")
```

---

# Execute SQL

```python
from sqlalchemy import text

with engine.connect() as conn:

    result = conn.execute(
        text("SELECT 1")
    )

    print(result.fetchone())
```

---

# 12. SQLAlchemy ORM

---

## Create Model

```python
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

class Base(DeclarativeBase):
    pass

class Employee(Base):

    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    department = Column(String)
```

---

## Create Table

```python
Base.metadata.create_all(engine)
```

---

# 13. SQLAlchemy CRUD Operations

---

## Create Session

```python
from sqlalchemy.orm import Session

session = Session(engine)
```

---

## Insert

```python
emp = Employee(
    name="Anita",
    department="IT"
)

session.add(emp)

session.commit()
```

---

## Read

```python
employees = session.query(
    Employee
).all()

for emp in employees:
    print(emp.name)
```

---

## Update

```python
emp = session.query(
    Employee
).first()

emp.department = "Finance"

session.commit()
```

---

## Delete

```python
session.delete(emp)

session.commit()
```

---

# 14. SQLAlchemy + Pandas

Read Table

```python
import pandas as pd

df = pd.read_sql(
    "employee",
    engine
)

print(df)
```

---

Write DataFrame

```python
df.to_sql(
    "employee",
    engine,
    if_exists="append",
    index=False
)
```

---

# 15. SQL Connectivity Lab

## Employee Analytics System

---

### Step 1: Create SQLite Database

```python
import sqlite3

conn = sqlite3.connect("company.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employee(
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary REAL
)
""")

conn.commit()
```

---

### Step 2: Insert Data

```python
employees = [

(1,"Rahul","IT",70000),

(2,"Anita","Finance",65000),

(3,"Karan","HR",50000),

(4,"Sneha","IT",80000),

(5,"Priya","Finance",90000)

]

cursor.executemany(
"""
INSERT OR REPLACE INTO employee
VALUES (?,?,?,?)
""",
employees
)

conn.commit()
```

---

### Step 3: Read into Pandas

```python
import pandas as pd

df = pd.read_sql_query(
    "SELECT * FROM employee",
    conn
)

print(df)
```

---

### Step 4: Analytics

```python
print(
df.groupby("department")["salary"]
.mean()
)
```

Output:

```text
Finance 77500
HR      50000
IT      75000
```

---

### Step 5: Visualization

```python
import seaborn as sns
import matplotlib.pyplot as plt

avg_salary = (
    df.groupby("department")
      ["salary"]
      .mean()
      .reset_index()
)

sns.barplot(
    data=avg_salary,
    x="department",
    y="salary"
)

plt.title(
    "Average Salary by Department"
)

plt.show()
```

---

### Step 6: SQLAlchemy Connection

```python
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///company.db"
)

df = pd.read_sql(
    "employee",
    engine
)

print(df)
```

---

# 16. Real-World Mini Project

Employee Dashboard

Features:

- Read employee data from SQLite
- Perform salary analytics using Pandas
- Store processed data using SQLAlchemy
- Generate charts using Seaborn
- Export reports using Matplotlib

Technology Stack:

```text
SQLite
    ↓
SQLAlchemy
    ↓
Pandas
    ↓
Matplotlib
    ↓
Seaborn
    ↓
Dashboard / Reports
```

---

# Interview Questions

### Matplotlib

1. Difference between plot() and scatter()?
2. What is subplot()?
3. How do you save charts?
4. What is figure()?

### Seaborn

1. Difference between boxplot and violinplot?
2. What is pairplot()?
3. What is heatmap()?
4. Why use Seaborn over Matplotlib?

### SQLite

1. What is SQLite?
2. Difference between SQLite and MySQL?
3. What is commit()?
4. What is cursor()?

### SQLAlchemy

1. What is ORM?
2. Difference between Engine and Session?
3. How does create_all() work?
4. What are advantages of SQLAlchemy?
