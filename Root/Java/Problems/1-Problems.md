# Java Interview Workbook - Problem 1

# Student Result Management System

## Objective

Learn

- Classes
- Objects
- Constructors
- Methods
- Encapsulation
- if-else
- Loops
- ArrayList

---

# Problem Statement

ABC Coaching Institute wants to automate student result processing.

Each student has

- Student ID
- Name
- Marks

The application should

- Add students
- Display students
- Calculate Grade
- Check Pass/Fail
- Find Topper
- Calculate Average
- Search Student

---

# Expected Output

```
===== Student Management =====

1. Add Student
2. Display Students
3. Search Student
4. Find Topper
5. Average Marks
6. Exit
```

---

# Project Structure

```
StudentManagement/
│
├── Student.java
├── StudentService.java
└── Main.java
```

---

# Class Diagram

```
Student
--------------------
studentId
name
marks

+calculateGrade()
+isPassed()
+display()

StudentService
---------------------
addStudent()

displayStudents()

searchStudent()

findTopper()

averageMarks()
```

---

# Step 1 : Student.java

```java
public class Student {

    private int studentId;
    private String name;
    private double marks;

    public Student(int studentId, String name, double marks) {
        this.studentId = studentId;
        this.name = name;
        this.marks = marks;
    }

    public String calculateGrade() {

        if (marks >= 90)
            return "A";
        else if (marks >= 80)
            return "B";
        else if (marks >= 70)
            return "C";
        else if (marks >= 60)
            return "D";
        else
            return "F";
    }

    public boolean isPassed() {
        return marks >= 60;
    }

    public void displayStudent() {

        System.out.println(studentId + " "
                + name + " "
                + marks + " "
                + calculateGrade());
    }

    public double getMarks() {
        return marks;
    }

    public int getStudentId() {
        return studentId;
    }
}
```

---

# Explanation

• private variables provide encapsulation

• Constructor initializes object

• calculateGrade() returns grade

• isPassed() returns true/false

• displayStudent() prints student details

---

# Step 2 : StudentService.java

(Complete implementation)

---

# Step 3 : Main.java

(Menu Driven Program)

---

# Sample Output

```
Enter Student ID : 101

Enter Name : Sai

Enter Marks : 91

Student Added Successfully

101 Sai 91 A
```

---

# Interview Questions

Q1 Why private variables?

Q2 Why constructor?

Q3 Difference between method and constructor?

Q4 Why use ArrayList?

Q5 Time Complexity of search?

---

# Practice Questions

1. Add Update Student

2. Delete Student

3. Save into File

4. Sort Students

5. Search by Name

---

# Challenge

Convert the project into

✔ Java Streams

✔ Comparator

✔ Comparable

✔ Lambda

✔ Exception Handling

✔ File Handling

✔ Serialization
