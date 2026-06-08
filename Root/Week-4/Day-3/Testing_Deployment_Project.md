# Python Testing and Deployment

---

# Table of Contents

1. Introduction to Testing
2. Unit Testing with unittest
3. Assertions in unittest
4. Test Fixtures
5. Mocking and Patching
6. Pytest Framework
7. Fixtures in Pytest
8. Parameterized Testing
9. Code Coverage
10. Continuous Integration (CI/CD)
11. COVID Trends Data Analysis Project
12. Email Automation Project
13. File Organizer Automation Project
14. Recommended Project Structure
15. Best Practices
16. Interview Questions

---

# Introduction to Testing

Testing ensures that software behaves as expected.

Benefits:

- Detect bugs early
- Improve code quality
- Prevent regressions
- Simplify maintenance
- Increase confidence during deployment

Example:

```python
def add(a, b):
    return a + b

assert add(2, 3) == 5
```

---

# Unit Testing with unittest

Python provides a built-in testing framework called `unittest`.

## Application Code

```python
# calculator.py

def add(a, b):
    return a + b
```

## Test Code

```python
# test_calculator.py

import unittest
from calculator import add

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
```

## Running Tests

```bash
python test_calculator.py
```

---

# Assertions in unittest

## assertEqual

```python
self.assertEqual(10, 10)
```

## assertNotEqual

```python
self.assertNotEqual(10, 20)
```

## assertTrue

```python
self.assertTrue(5 > 3)
```

## assertFalse

```python
self.assertFalse(5 < 3)
```

## assertIn

```python
self.assertIn("apple", ["apple", "banana"])
```

## assertRaises

```python
with self.assertRaises(ZeroDivisionError):
    10 / 0
```

---

# Test Fixtures

Fixtures help initialize and clean resources before and after tests.

```python
import unittest

class TestDatabase(unittest.TestCase):

    def setUp(self):
        print("Connecting Database")

    def tearDown(self):
        print("Closing Database")

    def test_connection(self):
        self.assertTrue(True)
```

---

# Mocking and Patching

Mocking allows testing code without calling external services.

## Application

```python
import requests

def get_user():
    response = requests.get(
        "https://api.example.com/user"
    )
    return response.json()
```

## Test

```python
from unittest.mock import patch

@patch("requests.get")
def test_get_user(mock_get):

    mock_get.return_value.json.return_value = {
        "name": "John"
    }

    result = get_user()

    assert result["name"] == "John"
```

---

# Pytest Framework

Pytest is a popular third-party testing framework.

## Installation

```bash
pip install pytest
```

## Application

```python
def multiply(a, b):
    return a * b
```

## Test

```python
def test_multiply():
    assert multiply(2, 3) == 6
```

## Run

```bash
pytest
```

---

# Fixtures in Pytest

```python
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_length(sample_data):
    assert len(sample_data) == 3
```

---

# Parameterized Testing

```python
import pytest

@pytest.mark.parametrize(
    "a,b,result",
    [
        (1,2,3),
        (5,5,10),
        (10,20,30)
    ]
)
def test_add(a,b,result):
    assert a+b == result
```

---

# Code Coverage

Code coverage shows how much code is tested.

## Installation

```bash
pip install pytest-cov
```

## Run Coverage

```bash
pytest --cov=myproject
```

## Generate HTML Report

```bash
pytest --cov=myproject --cov-report=html
```

Generated folder:

```text
htmlcov/
    index.html
```

---

# Continuous Integration (CI/CD)

GitHub Actions example:

```yaml
name: Python Tests

on: [push]

jobs:

  test:

    runs-on: ubuntu-latest

    steps:

    - uses: actions/checkout@v3

    - name: Install Dependencies
      run: |
        pip install pytest

    - name: Run Tests
      run: |
        pytest
```

---

# COVID Trends Data Analysis Project

## Objective

Analyze COVID-19 trends using Python and Pandas.

Metrics:

- Daily Cases
- Recoveries
- Deaths
- Growth Rate
- Moving Average

---

## Dataset

```csv
date,cases,deaths,recovered
2023-01-01,100,5,80
2023-01-02,120,4,90
2023-01-03,150,6,100
```

---

## Load Data

```python
import pandas as pd

df = pd.read_csv("covid.csv")

print(df.head())
```

---

## Statistics

```python
print(df.describe())
```

---

## Daily Growth Rate

```python
df["growth_rate"] = (
    df["cases"].pct_change()
) * 100
```

---

## Moving Average

```python
df["moving_average"] = (
    df["cases"]
    .rolling(7)
    .mean()
)
```

---

## Visualization

```python
import matplotlib.pyplot as plt

plt.plot(
    df["date"],
    df["cases"]
)

plt.xticks(rotation=45)

plt.show()
```

---

## Testing Growth Function

```python
def calculate_growth(
    previous,
    current
):
    return (
        (current - previous)
        / previous
    ) * 100
```

```python
def test_growth():
    assert calculate_growth(
        100,
        120
    ) == 20
```

---

# Email Automation Project

## Objective

Automatically send emails.

---

## Email Sender Script

```python
import smtplib

sender = "your_email@gmail.com"
password = "app_password"

receiver = "user@gmail.com"

message = """
Subject: Daily Report

Hello,
Report Generated Successfully.
"""

with smtplib.SMTP(
    "smtp.gmail.com",
    587
) as server:

    server.starttls()

    server.login(
        sender,
        password
    )

    server.sendmail(
        sender,
        receiver,
        message
    )

print("Email Sent")
```

---

## Multiple Recipients

```python
recipients = [
    "a@gmail.com",
    "b@gmail.com"
]

for email in recipients:
    server.sendmail(
        sender,
        email,
        message
    )
```

---

## Email Sender Test

```python
from unittest.mock import patch

@patch("smtplib.SMTP")
def test_email_sender(mock_smtp):

    send_email()

    assert mock_smtp.called
```

---

# File Organizer Automation Project

## Objective

Organize files automatically by extension.

---

## Before

```text
Downloads/

invoice.pdf
photo.jpg
notes.txt
```

---

## After

```text
Downloads/

PDF/
JPG/
TXT/
```

---

## File Organizer Script

```python
import os
import shutil

folder = "Downloads"

for file in os.listdir(folder):

    source = os.path.join(
        folder,
        file
    )

    if file.endswith(".pdf"):
        target_folder = os.path.join(
            folder,
            "PDF"
        )

    elif file.endswith(".jpg"):
        target_folder = os.path.join(
            folder,
            "JPG"
        )

    elif file.endswith(".txt"):
        target_folder = os.path.join(
            folder,
            "TXT"
        )

    else:
        continue

    os.makedirs(
        target_folder,
        exist_ok=True
    )

    shutil.move(
        source,
        target_folder
    )
```

---

## File Organizer Test

```python
import tempfile
import os

def test_file_creation():

    with tempfile.TemporaryDirectory() as folder:

        file_path = os.path.join(
            folder,
            "sample.txt"
        )

        open(
            file_path,
            "w"
        ).close()

        assert os.path.exists(
            file_path
        )
```

---

# Recommended Project Structure

```text
project/

├── src/
│   ├── covid_analysis.py
│   ├── email_sender.py
│   ├── file_organizer.py
│
├── tests/
│   ├── test_covid.py
│   ├── test_email.py
│   ├── test_organizer.py
│
├── requirements.txt
├── README.md
├── .gitignore
│
└── .github/
    └── workflows/
        └── test.yml
```

---

# Best Practices

## Testing

- Write tests early
- Cover edge cases
- Keep tests independent
- Use mocking for APIs
- Automate tests in CI/CD

## Data Analysis

- Validate input data
- Handle missing values
- Use reproducible pipelines
- Create automated reports

## Automation Scripts

- Use logging
- Handle exceptions
- Store secrets securely
- Use configuration files

---

# Interview Questions

## unittest

1. What is unittest?
2. What is setUp()?
3. What is tearDown()?
4. What are assertions?
5. What is mocking?

## pytest

6. Why use pytest?
7. What are fixtures?
8. What is parameterization?
9. How do you run a single test?
10. What is code coverage?

## Automation

11. What is SMTP?
12. How do you send emails in Python?
13. How do you automate file organization?

## Data Analysis

14. What is Pandas?
15. What is rolling average?
16. What is pct_change()?
17. How do you clean data?
18. How do you visualize trends?

## Deployment

19. What is CI/CD?
20. How does GitHub Actions work?

---

# Summary

In this module you learned:

- Unit Testing using unittest
- Testing using pytest
- Fixtures and mocking
- Code coverage
- Continuous Integration
- COVID data analysis project
- Email automation project
- File organizer automation project
- Industry best practices
