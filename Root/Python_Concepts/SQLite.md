# SQLite Example – Complete Explanation

## Code

```python
import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('CREATE TABLE users (name TEXT, age INTEGER)')
cursor.execute("INSERT INTO users VALUES ('Tobias', 28)")
conn.commit()

cursor.execute('SELECT * FROM users')
result = cursor.fetchone()

print(f'User: {result[0]}, Age: {result[1]}')
```

---

# Step 1: Import SQLite Module

```python
import sqlite3
```

### Explanation

- Imports Python's built-in SQLite database library.
- SQLite is a lightweight relational database.
- No installation is required.

### Real-World Use

Used in:

- Desktop applications
- Mobile applications
- Small web applications
- Data analysis projects

---

# Step 2: Create a Database Connection

```python
conn = sqlite3.connect(':memory:')
```

### Explanation

Creates a connection to an SQLite database.

### Special Meaning of `:memory:`

```python
sqlite3.connect(':memory:')
```

Creates a temporary database in RAM.

Benefits:

- Fast execution
- Good for testing
- Automatically removed when program ends

### Alternative

Permanent database:

```python
conn = sqlite3.connect('users.db')
```

This creates a file:

```text
users.db
```

---

# Step 3: Create a Cursor Object

```python
cursor = conn.cursor()
```

### Explanation

A cursor allows Python to communicate with the database.

Responsibilities:

- Execute SQL statements
- Retrieve data
- Manage query results

### Illustration

```text
Python Program
      |
      V
    Cursor
      |
      V
 SQLite Database
```

---

# Step 4: Create a Table

```python
cursor.execute(
    'CREATE TABLE users (name TEXT, age INTEGER)'
)
```

### SQL Equivalent

```sql
CREATE TABLE users (
    name TEXT,
    age INTEGER
);
```

### Explanation

Creates a table named `users`.

| Column | Data Type |
|----------|------------|
| name | TEXT |
| age | INTEGER |

### Table Structure

```text
users
+--------+------+
| name   | age  |
+--------+------+
```

---

# Step 5: Insert a Record

```python
cursor.execute(
    "INSERT INTO users VALUES ('Tobias', 28)"
)
```

### SQL Equivalent

```sql
INSERT INTO users
VALUES ('Tobias', 28);
```

### Result

Table now contains:

| name | age |
|--------|-----|
| Tobias | 28 |

---

# Step 6: Commit the Transaction

```python
conn.commit()
```

### Explanation

Saves all changes made to the database.

Without:

```python
conn.commit()
```

the inserted data may not be permanently stored.

### Analogy

```text
Making Changes -> Writing Notes

commit() -> Clicking Save
```

---

# Step 7: Retrieve Data

```python
cursor.execute('SELECT * FROM users')
```

### SQL Equivalent

```sql
SELECT * FROM users;
```

### Explanation

- `SELECT` → Retrieve data
- `*` → All columns
- `FROM users` → From users table

### Result Set

| name | age |
|--------|-----|
| Tobias | 28 |

---

# Step 8: Fetch One Row

```python
result = cursor.fetchone()
```

### Explanation

Retrieves the first row from the result set.

### Returned Value

```python
('Tobias', 28)
```

### Data Type

```python
tuple
```

### Accessing Values

```python
result[0]
```

Output:

```python
'Tobias'
```

```python
result[1]
```

Output:

```python
28
```

### Illustration

```text
result
   |
   V
('Tobias', 28)

Index Positions

0 --> Tobias
1 --> 28
```

---

# Step 9: Print the Result

```python
print(f'User: {result[0]}, Age: {result[1]}')
```

### Explanation

Uses an f-string to display values.

### Internal Substitution

```python
f'User: {result[0]}, Age: {result[1]}'
```

becomes

```python
'User: Tobias, Age: 28'
```

### Output

```text
User: Tobias, Age: 28
```

---

# Complete Execution Flow

```text
Start
  |
  V
Import sqlite3
  |
  V
Create Database Connection
  |
  V
Create Cursor
  |
  V
Create users Table
  |
  V
Insert Record
  |
  V
Commit Changes
  |
  V
Execute SELECT Query
  |
  V
Fetch Row
  |
  V
Display Output
  |
  V
End
```

---

# Memory Visualization

After Insert

```text
users Table

+---------+-----+
| name    | age |
+---------+-----+
| Tobias  | 28  |
+---------+-----+
```

After Fetch

```python
result = ('Tobias', 28)
```

---

# Better Practice: Parameterized Query

Instead of:

```python
cursor.execute(
    "INSERT INTO users VALUES ('Tobias', 28)"
)
```

Use:

```python
cursor.execute(
    "INSERT INTO users VALUES (?, ?)",
    ('Tobias', 28)
)
```

### Advantages

- Prevents SQL Injection
- Safer
- Easier to maintain
- Professional coding practice

---

# Real-World Example

Employee Management System

```python
cursor.execute("""
CREATE TABLE employees(
    emp_id INTEGER,
    name TEXT,
    department TEXT
)
""")

cursor.execute("""
INSERT INTO employees
VALUES(101,'Rahul','IT')
""")

conn.commit()

cursor.execute("SELECT * FROM employees")
print(cursor.fetchone())
```

Output:

```text
(101, 'Rahul', 'IT')
```

---

# Key Concepts Learned

| Concept | Purpose |
|----------|----------|
| sqlite3 | SQLite database library |
| connect() | Create database connection |
| :memory: | Temporary database in RAM |
| cursor() | Execute SQL commands |
| CREATE TABLE | Create table structure |
| INSERT INTO | Insert records |
| commit() | Save changes |
| SELECT | Retrieve data |
| fetchone() | Get one record |
| Tuple | Returned row format |
| f-string | Format output |

---

# Final Output

```text
User: Tobias, Age: 28
```

## Summary

This example demonstrates the complete SQLite workflow:

```text
Connect
   ↓
Create Table
   ↓
Insert Data
   ↓
Commit
   ↓
Query Data
   ↓
Fetch Result
   ↓
Display Output
```

This pattern forms the foundation of almost every Python application that interacts with a relational database.
