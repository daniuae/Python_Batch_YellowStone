# Python Problem-Solving Activities for Trainees

## Developing Computational Thinking Before Coding

---

# Overview

These activities are designed to help trainees:

* Think like programmers
* Break down complex problems
* Design algorithms
* Improve analytical thinking
* Collaborate effectively
* Build confidence before coding

The objective is not just to teach Python syntax but to teach **problem-solving using Python**.

---

# Activity 1: Human Computer

## Objective

Understand how computers execute instructions literally.

## Setup

Choose one trainee as a "Robot".

Ask the class to instruct the robot to make a cup of tea.

### Example

**Student:**

```text
Boil water
```

**Robot:**

```text
Where is the water?
How much water?
Which vessel?
```

## Learning Outcome

Students realize:

```text
Computers never assume.
Computers need exact instructions.
```

### Concepts Introduced

* Algorithms
* Sequencing
* Precision

---

# Activity 2: Escape the Maze

## Objective

Understand decision-making and conditional logic.

## Setup

Create a simple maze using chairs, tape, or desks.

```text
S = Start
E = Exit

S → □ → □
    ↓
□ → □ → E
```

## Rules

Students must provide navigation instructions.

```text
If wall exists:
    Turn Right
Else:
    Move Forward
```

## Learning Outcome

Introduces:

```python
if
elif
else
```

without writing code.

---

# Activity 3: Blindfold Programmer

## Objective

Learn the importance of precise communication.

## Setup

Pair students.

One student is blindfolded.

The other must guide them to draw:

* Square
* Triangle
* House

using verbal instructions only.

## Learning Outcome

Students understand:

```text
Programming = Giving precise instructions
```

---

# Activity 4: Reverse Engineering Challenge

## Objective

Develop analytical thinking.

## Show Output

```text
1
4
9
16
25
```

Ask:

```text
What logic generated this output?
```

### Possible Solution

```python
for i in range(1,6):
    print(i*i)
```

## Advanced Version

```text
2
6
12
20
30
```

Students identify:

```python
n * (n + 1)
```

## Learning Outcome

* Pattern Recognition
* Logic Discovery

---

# Activity 5: Guess the Algorithm

## Objective

Learn decision trees and logical elimination.

## Rules

Trainer thinks of a number.

Students ask questions.

Examples:

```text
Is it even?
Is it greater than 50?
Is it divisible by 5?
```

## Learning Outcome

Introduces:

* Conditional Logic
* Binary Decisions
* Decision Trees

---

# Activity 6: ATM Simulation

## Objective

Break a business problem into logical steps.

## Scenario

Build ATM logic.

Ask students:

```text
What happens when a customer uses an ATM?
```

### Expected Workflow

```text
Insert Card
↓
Enter PIN
↓
Validate PIN
↓
Display Menu
↓
Withdraw Cash
↓
Update Balance
```

## Learning Outcome

Students learn:

* Process Flow
* Pseudocode
* Algorithm Design

---

# Activity 7: Build Amazon Without Coding

## Objective

Develop system-thinking skills.

## Question

```text
What happens when a customer clicks "Buy Now"?
```

## Expected Workflow

```text
Login
↓
Choose Product
↓
Check Stock
↓
Payment
↓
Order Confirmation
↓
Shipment
```

## Learning Outcome

Introduces:

* Functions
* Modules
* Workflow Design

---

# Activity 8: Debugging Detective

## Objective

Develop debugging skills.

## Example

```python
age = 18

if age = 18:
    print("Eligible")
```

### Challenge

Identify:

1. What is wrong?
2. Why is it wrong?
3. How would you fix it?

## Learning Outcome

Students develop debugging habits.

---

# Activity 9: Pizza Shop Challenge

## Objective

Practice problem decomposition.

## Scenario

Create a Pizza Billing System.

Ask:

```text
What information do we need?
```

### Possible Answers

```text
Pizza Type
Quantity
Tax
Discount
Final Amount
```

## Learning Outcome

Students learn to break large problems into smaller tasks.

---

# Activity 10: Algorithm Race

## Objective

Learn efficiency and optimization.

## Challenge

Find the largest number.

```text
15, 20, 8, 100, 56
```

### Team A

Compare all numbers.

### Team B

Sort numbers first.

## Discussion

```text
Which approach is faster?
Why?
```

## Learning Outcome

Introduces:

* Optimization
* Algorithm Efficiency

---

# Activity 11: Mystery Data Challenge

## Objective

Build pattern-recognition skills.

## Example 1

```text
12
24
48
96
?
```

### Answer

```text
192
```

## Example 2

```text
3
7
15
31
63
?
```

### Answer

```text
127
```

## Learning Outcome

Students learn:

* Pattern Detection
* Logical Thinking

---

# Activity 12: Treasure Hunt Variables

## Objective

Understand variables through gameplay.

## Setup

Hide clues around the classroom.

Example:

```text
A = Chair
B = Table
C = Whiteboard
```

Students store values and follow clues.

## Learning Outcome

Variables become memorable and practical.

---

# Activity 13: Build a Calculator on Paper

## Objective

Design software before coding.

Ask:

```text
What inputs are needed?
What outputs are expected?
```

### Edge Cases

```text
Division by Zero
Text Input
Negative Numbers
```

## Learning Outcome

Introduces:

* Validation
* Exception Handling

---

# Activity 14: Bug Hunt Competition

## Objective

Make debugging fun and competitive.

## Example

```python
salary = 50000

if salary > 40000
print("Bonus")
```

## Scoring

| Action       | Points |
| ------------ | ------ |
| Error Found  | 10     |
| Fix Provided | 10     |
| Explanation  | 20     |

---

# Activity 15: Zombie Programmer

## Objective

Understand loops.

## Story

A zombie must take 5 steps.

### Manual Method

```text
Step
Step
Step
Step
Step
```

### Better Method

```python
for step in range(5):
    move()
```

## Learning Outcome

Students discover the need for loops naturally.

---

# Activity 16: Shark Tank Python

## Objective

Promote innovation and system design.

## Teams Create

* Library Management System
* Food Delivery App
* Parking Management System
* Attendance Tracker

## Presentation Structure

1. Problem
2. Solution
3. Logic
4. Python Concepts Required

---

# Activity 17: Real Data Detective

## Objective

Introduce data analysis.

## Dataset

```csv
Name,Salary
Ravi,50000
Priya,70000
Arun,45000
```

## Questions

```text
Highest Salary?
Lowest Salary?
Average Salary?
```

## Learning Outcome

Develops analytical thinking before coding.

---

# Activity 18: Python Escape Room

## Objective

Gamify learning.

### Example Puzzle Flow

```text
Puzzle 1 → Variables
Puzzle 2 → Conditions
Puzzle 3 → Loops
Puzzle 4 → Functions
Puzzle 5 → Lists
```

Each correct solution unlocks the next clue.

---

# Activity 19: Teach the Teacher

## Objective

Increase retention.

Each trainee explains one concept:

* List
* Dictionary
* Function
* Loop
* Class

### Rules

* No slides
* No notes
* Only explanation

## Learning Outcome

Teaching reinforces learning.

---

# Activity 20: Million-Dollar Challenge

## Scenario

A company wants attendance analytics.

### Requirements

```text
Find Most Absent Employee
Find Best Attendance
Calculate Department Attendance %
```

### Students Must

```text
Identify Inputs
Identify Outputs
Break Down Problem
Write Pseudocode
Write Python Solution
```

---

# Weekly Competition Framework

| Activity         | Points |
| ---------------- | ------ |
| Quiz             | 10     |
| Debugging        | 20     |
| Coding Challenge | 30     |
| Teaching Others  | 20     |
| Team Activity    | 20     |

---

# Achievement Titles

Instead of prizes, award titles:

* Python Detective
* Bug Hunter
* Logic Ninja
* Algorithm Master
* Data Wizard
* Code Architect
* Python Champion

---

# Ultimate Problem-Solving Framework

```text
Understand Problem
        ↓
Identify Inputs
        ↓
Identify Outputs
        ↓
Break into Smaller Tasks
        ↓
Create Algorithm
        ↓
Write Pseudocode
        ↓
Write Python Code
        ↓
Test
        ↓
Optimize
        ↓
Explain Solution
```

## Golden Rule

Students do not learn programming by watching.

Students learn programming by:

```text
Thinking
↓
Practicing
↓
Failing
↓
Debugging
↓
Improving
↓
Teaching Others
```
