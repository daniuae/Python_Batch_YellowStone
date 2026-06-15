# Python OOP + Dictionary + String Processing Practice Set (10 Questions)

These questions follow the **same pattern and difficulty level** as the **Word Frequency Counter** problem and are ideal for:

* Python Beginners
* Freshers
* Coding Assessments
* OOP Practice
* Dictionary Practice
* String Manipulation
* Interview Preparation

---

# Question 1: Character Frequency Counter

## 📌 Problem Statement

Implement a Character Frequency Counter that takes a string and returns the frequency of each character while ignoring spaces and case differences.

## 📌 Class Declaration

```python
class CharacterFrequencyCounter:
```

---

## Operations

### 1. Clean Text

#### Function Prototype

```python
def preprocess_text(self, text: str) -> str:
```

#### Example Input

```python
preprocess_text("Hello World")
```

#### Expected Output

```python
"helloworld"
```

#### Implementation Flow

* Convert text to lowercase.
* Remove spaces.
* Return cleaned string.

---

### 2. Compute Character Frequency

#### Function Prototype

```python
def compute_character_frequency(self, text: str) -> dict:
```

#### Expected Output

```python
{
 'h':1,
 'e':1,
 'l':3,
 'o':2,
 'w':1,
 'r':1,
 'd':1
}
```

---

### 3. Most Frequent Character

Return:

```python
('l', 3)
```

---

### 4. Filter Characters By Frequency

Return characters occurring at least N times.

---

# Question 2: Product Sales Counter

## 📌 Problem Statement

A store maintains product sales records. Analyze product sale frequencies.

## 📌 Class Declaration

```python
class ProductSalesCounter:
```

---

## Operations

### 1. Clean Product Names

Convert to lowercase.

---

### 2. Count Product Sales

Input:

```python
[
 "Laptop",
 "Mobile",
 "Laptop",
 "Tablet",
 "Laptop"
]
```

Output:

```python
{
 'laptop':3,
 'mobile':1,
 'tablet':1
}
```

---

### 3. Most Sold Product

Output:

```python
('laptop',3)
```

---

### 4. Frequently Sold Products

Return products sold at least N times.

---

# Question 3: Student Grade Analyzer

## 📌 Problem Statement

Analyze grades earned by students.

## 📌 Class Declaration

```python
class StudentGradeAnalyzer:
```

---

## Operations

### 1. Normalize Grades

Convert grades to uppercase.

---

### 2. Count Grade Frequencies

Input:

```python
['A','A','B','C','A']
```

Output:

```python
{
 'A':3,
 'B':1,
 'C':1
}
```

---

### 3. Most Common Grade

Return grade with highest frequency.

---

### 4. Filter Popular Grades

Return grades appearing at least N times.

---

# Question 4: Website Visitor Counter

## 📌 Problem Statement

A website tracks page visits.

## 📌 Class Declaration

```python
class WebsiteVisitorCounter:
```

---

## Operations

### 1. Normalize Page Names

Convert URLs to lowercase.

---

### 2. Count Page Visits

Input:

```python
[
 "Home",
 "Products",
 "Home",
 "About"
]
```

Output:

```python
{
 'home':2,
 'products':1,
 'about':1
}
```

---

### 3. Most Visited Page

Return page and visit count.

---

### 4. Frequently Visited Pages

Return pages visited at least N times.

---

# Question 5: Employee Department Counter

## 📌 Problem Statement

An organization tracks employee departments.

## 📌 Class Declaration

```python
class DepartmentCounter:
```

---

## Operations

### 1. Normalize Department Names

Convert to uppercase.

---

### 2. Count Employees Per Department

Input:

```python
[
 "IT",
 "HR",
 "IT",
 "Finance"
]
```

Output:

```python
{
 'IT':2,
 'HR':1,
 'FINANCE':1
}
```

---

### 3. Largest Department

Return department and count.

---

### 4. Filter Departments By Employee Count

Return departments with at least N employees.

---

# Question 6: Movie Genre Analyzer

## 📌 Problem Statement

Analyze movie genre frequencies.

## 📌 Class Declaration

```python
class GenreAnalyzer:
```

---

## Operations

### 1. Normalize Genres

Convert to lowercase.

---

### 2. Count Genre Frequency

Input:

```python
[
 "Action",
 "Drama",
 "Action",
 "Comedy"
]
```

Output:

```python
{
 'action':2,
 'drama':1,
 'comedy':1
}
```

---

### 3. Most Popular Genre

Return genre and count.

---

### 4. Frequent Genres

Return genres appearing at least N times.

---

# Question 7: Hashtag Frequency Analyzer

## 📌 Problem Statement

Analyze social media hashtags.

## 📌 Class Declaration

```python
class HashtagAnalyzer:
```

---

## Operations

### 1. Clean Hashtags

Remove:

```text
#
```

Convert to lowercase.

---

### 2. Count Hashtag Frequency

Input:

```python
[
 "#Python",
 "#AI",
 "#Python"
]
```

Output:

```python
{
 'python':2,
 'ai':1
}
```

---

### 3. Trending Hashtag

Return most frequent hashtag.

---

### 4. Popular Hashtags

Return hashtags with frequency >= N.

---

# Question 8: Customer Purchase Analyzer

## 📌 Problem Statement

Analyze customer purchase behavior.

## 📌 Class Declaration

```python
class CustomerPurchaseAnalyzer:
```

---

## Operations

### 1. Normalize Customer Names

Convert to lowercase.

---

### 2. Count Purchases Per Customer

Input:

```python
[
 "John",
 "Mary",
 "John"
]
```

Output:

```python
{
 'john':2,
 'mary':1
}
```

---

### 3. Most Active Customer

Return customer and purchase count.

---

### 4. Frequent Buyers

Return customers with purchases >= N.

---

# Question 9: Error Log Analyzer

## 📌 Problem Statement

A system generates error logs. Count occurrence of error types.

## 📌 Class Declaration

```python
class ErrorLogAnalyzer:
```

---

## Operations

### 1. Normalize Errors

Convert to uppercase.

---

### 2. Count Error Frequencies

Input:

```python
[
 "404",
 "500",
 "404",
 "403"
]
```

Output:

```python
{
 '404':2,
 '500':1,
 '403':1
}
```

---

### 3. Most Frequent Error

Return error code and count.

---

### 4. Critical Errors

Return errors occurring at least N times.

---

# Question 10: City Population Survey Analyzer

## 📌 Problem Statement

Analyze city participation in a survey.

## 📌 Class Declaration

```python
class CitySurveyAnalyzer:
```

---

## Operations

### 1. Normalize City Names

Convert to title case.

---

### 2. Count City Responses

Input:

```python
[
 "Chennai",
 "Mumbai",
 "Chennai",
 "Delhi"
]
```

Output:

```python
{
 'Chennai':2,
 'Mumbai':1,
 'Delhi':1
}
```

---

### 3. Most Participating City

Return city and count.

---

### 4. High Participation Cities

Return cities with participation >= N.

---

# Concepts Covered

| Concept    | Questions                |
| ---------- | ------------------------ |
| Strings    | All                      |
| lower()    | Most                     |
| upper()    | Some                     |
| title()    | City Analyzer            |
| split()    | Word Analyzer            |
| replace()  | Hashtag Analyzer         |
| Dictionary | All                      |
| get()      | All                      |
| for loop   | All                      |
| max()      | All                      |
| lambda     | All                      |
| Filtering  | All                      |
| Tuples     | Most Frequent Operations |
| OOP        | All                      |

---

# Difficulty Progression

### Beginner

```text
Character Frequency Counter
Product Sales Counter
Student Grade Analyzer
```

### Intermediate

```text
Department Counter
Movie Genre Analyzer
Website Visitor Counter
```

### Advanced

```text
Hashtag Analyzer
Customer Purchase Analyzer
Error Log Analyzer
City Survey Analyzer
```

These 10 exercises reinforce the exact same Python patterns used in the Word Frequency Counter problem:

* String Cleaning
* Dictionary Counting
* get()
* max()
* lambda
* Filtering
* OOP Design
* Frequency Analysis
* Data Transformation
