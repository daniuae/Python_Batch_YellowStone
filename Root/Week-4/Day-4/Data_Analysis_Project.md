# Data Analysis Project and Automation Scripts in Python

# Table of Contents

1. Introduction
2. Data Analysis Project – COVID-19 Trends Analysis
3. Project Architecture
4. Dataset Information
5. Data Cleaning
6. Exploratory Data Analysis (EDA)
7. Data Visualization
8. Advanced Analysis
9. Automation Script – Email Sender
10. Automation Script – File Organizer
11. Combining Data Analysis and Automation
12. Project Extensions
13. Interview Questions
14. Best Practices
15. Summary

---

# 1. Introduction

Python is widely used for:

* Data Analysis
* Data Engineering
* Automation
* Machine Learning
* Reporting

This document covers two practical projects:

1. COVID-19 Data Analysis Project
2. Automation Scripts

   * Email Sender
   * File Organizer

---

# 2. Data Analysis Project – COVID-19 Trends Analysis

## Objective

Analyze COVID-19 data to answer:

* Total cases by country
* Total deaths by country
* Daily trends
* Recovery trends
* Top affected countries
* Growth rate analysis

---

# 3. Project Architecture

```text
CSV Dataset
      |
      v
Pandas
      |
      v
Data Cleaning
      |
      v
EDA
      |
      v
Visualization
      |
      v
Insights Report
```

---

# Required Libraries

```bash
pip install pandas numpy matplotlib seaborn
```

---

# Import Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

---

# 4. Dataset Information

Sample Dataset

```csv
Date,Country,Confirmed,Recovered,Deaths
2024-01-01,India,1000,800,20
2024-01-02,India,1200,950,25
2024-01-01,USA,2000,1500,50
2024-01-02,USA,2500,1800,60
```

---

# Load Dataset

```python
df = pd.read_csv("covid_data.csv")

print(df.head())
```

Output

```text
         Date Country Confirmed Recovered Deaths
0 2024-01-01 India      1000      800     20
1 2024-01-02 India      1200      950     25
```

---

# Dataset Information

```python
df.info()
```

Output

```text
Rows: 10000
Columns: 5
```

---

# Statistical Summary

```python
df.describe()
```

Output

```text
Mean
Min
Max
Std
```

---

# 5. Data Cleaning

## Missing Values

```python
print(df.isnull().sum())
```

Fill missing values

```python
df.fillna(0, inplace=True)
```

---

## Duplicate Records

```python
df.drop_duplicates(inplace=True)
```

---

## Convert Date

```python
df["Date"] = pd.to_datetime(df["Date"])
```

---

# 6. Exploratory Data Analysis (EDA)

## Total Cases by Country

```python
country_cases = df.groupby("Country")["Confirmed"].sum()

print(country_cases)
```

Output

```text
India    2200
USA      4500
```

---

## Total Deaths by Country

```python
country_deaths = df.groupby("Country")["Deaths"].sum()

print(country_deaths)
```

---

## Top 10 Countries

```python
top_countries = (
    df.groupby("Country")["Confirmed"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print(top_countries)
```

---

# 7. Data Visualization

## Bar Chart

```python
top_countries.plot(kind="bar")

plt.title("Top Countries by Cases")
plt.xlabel("Country")
plt.ylabel("Cases")

plt.show()
```

---

## Line Chart

Daily Cases Trend

```python
daily_cases = (
    df.groupby("Date")["Confirmed"]
      .sum()
)

daily_cases.plot()

plt.title("Daily COVID Cases")
plt.show()
```

---

## Pie Chart

```python
country_cases.head(5).plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.show()
```

---

## Seaborn Visualization

```python
sns.barplot(
    x=top_countries.index,
    y=top_countries.values
)

plt.xticks(rotation=45)
plt.show()
```

---

# 8. Advanced Analysis

## Growth Rate

Formula

```text
Growth Rate =
(Current Day Cases - Previous Day Cases)
/
Previous Day Cases
```

Code

```python
daily_cases = daily_cases.reset_index()

daily_cases["GrowthRate"] = (
    daily_cases["Confirmed"].pct_change()
)

print(daily_cases)
```

---

## Recovery Rate

```python
df["RecoveryRate"] = (
    df["Recovered"]
    /
    df["Confirmed"]
) * 100
```

---

## Death Rate

```python
df["DeathRate"] = (
    df["Deaths"]
    /
    df["Confirmed"]
) * 100
```

---

# Export Report

```python
df.to_csv(
    "covid_analysis_report.csv",
    index=False
)
```

---

# 9. Automation Script – Email Sender

## Objective

Automatically send emails.

---

## Libraries

```python
import smtplib
from email.mime.text import MIMEText
```

---

## Email Sender

```python
import smtplib
from email.mime.text import MIMEText

sender = "sender@gmail.com"
receiver = "receiver@gmail.com"

message = MIMEText(
    "Daily COVID report attached."
)

message["Subject"] = "COVID Report"

server = smtplib.SMTP(
    "smtp.gmail.com",
    587
)

server.starttls()

server.login(
    sender,
    "APP_PASSWORD"
)

server.sendmail(
    sender,
    receiver,
    message.as_string()
)

server.quit()

print("Email Sent")
```

---

# Send Email with Attachment

```python
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
```

```python
msg = MIMEMultipart()

msg["Subject"] = "Daily Report"
```

Attach file

```python
filename = "covid_analysis_report.csv"

with open(filename, "rb") as file:
    attachment = MIMEBase(
        "application",
        "octet-stream"
    )

    attachment.set_payload(
        file.read()
    )

encoders.encode_base64(
    attachment
)

attachment.add_header(
    "Content-Disposition",
    f"attachment; filename={filename}"
)

msg.attach(attachment)
```

---

# 10. Automation Script – File Organizer

## Objective

Organize files automatically into folders.

---

## Folder Structure

```text
Downloads
|
|-- Images
|-- PDFs
|-- Excel
|-- Videos
```

---

## File Organizer Script

```python
import os
import shutil
```

```python
source_folder = "Downloads"

for file in os.listdir(source_folder):

    path = os.path.join(
        source_folder,
        file
    )

    if file.endswith(".jpg"):
        shutil.move(
            path,
            "Images"
        )

    elif file.endswith(".pdf"):
        shutil.move(
            path,
            "PDFs"
        )

    elif file.endswith(".xlsx"):
        shutil.move(
            path,
            "Excel"
        )
```

---

## Dynamic Folder Creation

```python
folders = [
    "Images",
    "PDFs",
    "Excel"
]

for folder in folders:

    if not os.path.exists(folder):
        os.mkdir(folder)
```

---

# Advanced Organizer

```python
import os
import shutil

source = "Downloads"

extensions = {
    ".jpg": "Images",
    ".png": "Images",
    ".pdf": "PDFs",
    ".xlsx": "Excel",
    ".csv": "CSV",
    ".mp4": "Videos"
}

for file in os.listdir(source):

    filename, ext = os.path.splitext(file)

    if ext in extensions:

        folder = extensions[ext]

        os.makedirs(
            folder,
            exist_ok=True
        )

        shutil.move(
            os.path.join(source, file),
            os.path.join(folder, file)
        )

print("Organization Completed")
```

---

# 11. Combining Data Analysis and Automation

Real-world workflow

```text
Collect Data
     |
Analyze Data
     |
Generate Report
     |
Email Report
     |
Archive Files
```

---

## End-to-End Example

```python
analyze_covid_data()

generate_report()

send_email()

archive_files()
```

---

# 12. Project Extensions

## COVID Dashboard

Tools:

* Streamlit
* Plotly
* Dash

Example

```bash
pip install streamlit
```

```python
import streamlit as st

st.title(
    "COVID Dashboard"
)
```

---

## Scheduled Execution

Run daily.

Linux Cron

```bash
0 8 * * * python covid_report.py
```

Windows Task Scheduler

```text
Create Task
Select Python Script
Schedule Daily
```

---

# 13. Interview Questions

## Data Analysis

### Q1

Difference between Pandas and NumPy?

Answer:

```text
NumPy handles numerical arrays.
Pandas handles tabular data.
```

---

### Q2

What is EDA?

Answer:

```text
Exploratory Data Analysis.
Used to understand data before modeling.
```

---

### Q3

What is GroupBy?

Answer:

```text
Used to aggregate data by categories.
```

---

## Automation

### Q4

Why use shutil?

Answer:

```text
For file movement and copying.
```

---

### Q5

Why use SMTP?

Answer:

```text
For sending emails.
```

---

# 14. Best Practices

## Data Analysis

* Validate input data
* Handle null values
* Remove duplicates
* Use reusable functions
* Create visualizations

---

## Automation

* Use logging
* Handle exceptions
* Secure passwords
* Schedule jobs
* Monitor failures

---

## Logging Example

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info(
    "Program Started"
)
```

---

# 15. Summary

This document covered:

✔ COVID Data Analysis Project

✔ Data Cleaning

✔ EDA

✔ Data Visualization

✔ Growth Rate Analysis

✔ Recovery Rate Analysis

✔ Email Automation

✔ File Organizer Automation

✔ Scheduled Execution

✔ Reporting Automation

✔ Production Best Practices

These projects represent common real-world Data Engineering, Data Analyst, ETL Developer, and Python Automation use cases frequently asked in interviews and used in enterprise environments.
