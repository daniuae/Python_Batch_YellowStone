# Python Capstone Project – Deliverables & Submission Guidelines

## Objective

The purpose of the Capstone Project is to provide trainees with hands-on experience in designing, developing, testing, 
documenting, and presenting a complete Python application using industry-standard practices.

The project should demonstrate:

* Problem-solving skills
* Python programming proficiency
* Software design principles
* Agile project management
* Testing and debugging
* Data visualization
* Presentation and communication skills

---

# 1. Project Proposal Document

## Purpose

Before development begins, every team must prepare a project proposal.

### Deliverables

* Project Title
* Problem Statement
* Business Objective
* Scope
* Expected Outcome
* Technology Stack
* Team Members
* Project Timeline

### Example

**Project Title:** Employee Attendance Analytics System

**Business Objective:**
Develop a Python application to analyze employee attendance and generate analytical reports for management.

---

# 2. Jira Board (Mandatory)

## Why Jira?

Jira is widely used in software companies for Agile and Scrum project management.

The Capstone Project should be tracked through a Jira board.

---

## Suggested Workflow

```text
BACKLOG
   ↓
TO DO
   ↓
IN PROGRESS
   ↓
CODE REVIEW
   ↓
TESTING
   ↓
DONE
```

---

## Sample Epic

```text
Attendance Management System
```

---

## Sample User Story

```text
As an HR Manager,
I want to upload attendance records
So that I can generate employee attendance reports.
```

### Tasks

```text
Create Upload Module
Validate Input File
Store Data
Generate Report
```

---

## Sprint Planning

### Sprint 1

* Requirement Gathering
* Design Document
* Database Setup

### Sprint 2

* Core Development
* Feature Implementation

### Sprint 3

* Testing
* Visualization
* Deployment
* Documentation

---

# 3. System Design Document

A design document must be prepared before coding begins.

---

## Architecture Diagram

```text
CSV/Excel
    ↓
Python Application
    ↓
Database
    ↓
Business Logic
    ↓
Visualization Dashboard
```

---

## Class Diagram

```text
Employee
Attendance
ReportGenerator
Dashboard
```

---

## Database Design

```sql
Employee
---------
employee_id
employee_name
department

Attendance
----------
employee_id
attendance_date
status
```

---

# 4. Source Code Repository

Use Git-based version control.

### Recommended Platforms

* GitHub
* GitLab
* Bitbucket

---

## Suggested Folder Structure

```text
Capstone_Project/

│
├── data/
│
├── src/
│   ├── models/
│   ├── services/
│   ├── utilities/
│
├── tests/
│
├── reports/
│
├── dashboard/
│
├── docs/
│
├── screenshots/
│
├── requirements.txt
│
├── README.md
│
└── main.py
```

---

# 5. Coding Standards

The project must follow Python best practices.

---

## PEP-8 Standards

```python
def calculate_attendance(employee_id):
    pass
```

---

## Exception Handling

```python
try:
    process_file()
except FileNotFoundError:
    print("File not found")
```

---

## Logging

```python
import logging

logging.info("Application Started")
```

---

## Documentation

Use comments and docstrings.

```python
def calculate_attendance():
    """
    Calculates employee attendance percentage.
    """
```

---

# 6. Unit Testing

Testing is mandatory.

---

## Recommended Frameworks

* unittest
* pytest

---

## Example Test Case

```python
def test_attendance_percentage():
    assert calculate_attendance() == 95
```

---

## Coverage Goal

```text
Minimum Coverage: 70%
Preferred Coverage: 80%+
```

---

# 7. Code Walkthrough Session

Every team must conduct a code walkthrough.

---

## Walkthrough Agenda

### Project Overview

* Business Problem
* Objective

### Architecture Discussion

* Design
* Modules
* Components

### Code Flow

```text
main.py
   ↓
service.py
   ↓
database.py
```

### Demonstration

* Input
* Processing
* Output

### Challenges Faced

* Technical Issues
* Solutions Implemented

### Future Enhancements

* AI Features
* Cloud Deployment
* Automation

---

# 8. Visualization Deliverables

Projects should include data visualization wherever applicable.

---

## Beginner Level

### Matplotlib

Suitable For:

* Bar Charts
* Line Charts
* Pie Charts
* Histograms

Example Use Cases:

* Sales Reports
* Attendance Reports
* Revenue Trends

---

## Intermediate Level

### Seaborn

Suitable For:

* Heatmaps
* Boxplots
* Correlation Analysis
* Distribution Analysis

Example Use Cases:

* HR Analytics
* Customer Behavior Analysis

---

## Advanced Level

### Plotly

Suitable For:

* Interactive Charts
* Drill-down Reports
* Dynamic Dashboards

Example Use Cases:

* Executive Dashboards
* Real-time Monitoring

---

## Enterprise Level

### Streamlit

Recommended for Capstone Projects

Features:

* User Interface
* Data Upload
* Interactive Reports
* Filtering
* Dashboard Creation

Example:

```bash
streamlit run app.py
```

---

## Alternative Dashboard Tool

### Dash (Plotly)

Suitable For:

* Enterprise Dashboards
* KPI Monitoring
* Business Intelligence Solutions

---

# 9. Documentation Deliverables

Every project must include:

---

## README.md

Should contain:

* Project Overview
* Installation Steps
* Usage Instructions
* Screenshots
* Features

---

## User Guide

Should contain:

* Application Navigation
* Feature Description
* Usage Instructions

---

## Technical Design Document

Should contain:

* Architecture
* Database Design
* Module Design
* APIs Used

---

# 10. Presentation (PPT)

Each team must present the project.

---

## Suggested PPT Structure

### Slide 1

Project Title

Team Members

---

### Slide 2

Problem Statement

---

### Slide 3

Business Objective

---

### Slide 4

Project Scope

---

### Slide 5

Architecture Diagram

---

### Slide 6

Technology Stack

---

### Slide 7

Database Design

---

### Slide 8

Key Features

---

### Slide 9

Code Structure

---

### Slide 10

Visualization Dashboard

---

### Slide 11

Demo Screenshots

---

### Slide 12

Challenges & Solutions

---

### Slide 13

Future Enhancements

---

### Slide 14

Project Learnings

---

### Slide 15

Questions & Answers

---

# 11. Demo Video

## Duration

```text
5 to 10 Minutes
```

### Video Should Cover

* Project Overview
* Architecture
* Application Demonstration
* Dashboard Demonstration
* Code Walkthrough
* Future Enhancements

---

# 12. Final Submission Package

Each team must submit the following:

## Project Management

* Jira Board Export
* Sprint Report

## Development

* Complete Source Code
* Git Repository Link
* requirements.txt

## Documentation

* README.md
* User Guide
* Technical Design Document

## Testing

* Test Cases
* Test Execution Results
* Coverage Report

## Presentation

* PPT Deck
* Demo Video

## Visualization

* Dashboard
* Reports
* Screenshots

---

# Evaluation Rubric

| Criteria              | Weightage |
| --------------------- | --------- |
| Problem Understanding | 10%       |
| Jira Usage            | 10%       |
| Design & Architecture | 15%       |
| Coding Standards      | 20%       |
| Testing               | 10%       |
| Visualization         | 10%       |
| Documentation         | 10%       |
| Presentation          | 5%        |
| Demo & Walkthrough    | 10%       |

---

# Message to Trainees

A Capstone Project is not just about writing Python code.

It is an opportunity to demonstrate how software is developed in a professional environment.

Focus on:

* Requirement Analysis
* Agile Planning
* Clean Coding Practices
* Testing
* Visualization
* Documentation
* Team Collaboration
* Effective Communication

Think like a Software Engineer, Data Engineer, QA Engineer, Business Analyst, and Project Manager throughout the project lifecycle.

The final deliverable should be:

* Functional
* Maintainable
* Testable
* Documented
* Business-Oriented
