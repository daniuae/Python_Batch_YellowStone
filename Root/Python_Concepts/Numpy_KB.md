# NumPy Complete Tutorial in Python
---

# NumPy Learning Roadmap

```text
NumPy
│
├── Arrays
│   ├── 1D
│   ├── 2D
│   └── 3D
│
├── Indexing
├── Slicing
├── Reshape
├── Statistics
├── Filtering
├── Sorting
├── Random Numbers
├── Matrix Operations
└── Real World Analysis
```
## What is NumPy?

**NumPy (Numerical Python)** is a powerful Python library used for:

- Numerical Computing
- Scientific Computing
- Data Analysis
- Machine Learning
- Artificial Intelligence
- Matrix Operations

---

## Why NumPy?

Python Lists have limitations:

| Feature | Python List | NumPy Array |
|----------|------------|-------------|
| Speed | Slow | Fast |
| Memory Usage | High | Low |
| Mathematical Operations | Limited | Powerful |
| Data Science Support | No | Yes |

---

# Installation

```bash
pip install numpy
```

Import NumPy:

```python
import numpy as np
```

---

# Creating Arrays

## 1D Array

```python
import numpy as np

arr = np.array([10,20,30,40])

print(arr)
```

Output:

```python
[10 20 30 40]
```

---

## 2D Array

```python
arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr)
```

Output:

```python
[[1 2 3]
 [4 5 6]]
```

---

## 3D Array

```python
arr = np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])

print(arr)
```

---

# Array Properties

```python
arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
```

Output:

```python
2
(2, 3)
6
int64
```

| Property | Description |
|-----------|-------------|
| ndim | Number of Dimensions |
| shape | Rows and Columns |
| size | Total Elements |
| dtype | Data Type |

---

# Creating Special Arrays

## Zeros

```python
np.zeros((3,3))
```

Output:

```python
array([[0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.]])
```

---

## Ones

```python
np.ones((2,4))
```

Output:

```python
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.]])
```

---

## Identity Matrix

```python
np.eye(4)
```

Output:

```python
array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.]])
```

---

# Array Ranges

## arange()

```python
np.arange(1,10)
```

Output:

```python
array([1,2,3,4,5,6,7,8,9])
```

---

## arange() with Step

```python
np.arange(0,20,2)
```

Output:

```python
array([0,2,4,6,8,10,12,14,16,18])
```

---

## linspace()

Creates evenly spaced numbers.

```python
np.linspace(1,10,5)
```

Output:

```python
array([ 1.  , 3.25, 5.5 , 7.75, 10. ])
```

---

# Reshape Arrays

```python
arr = np.arange(1,13)

new_arr = arr.reshape(3,4)

print(new_arr)
```

Output:

```python
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
```

---

# Flatten Arrays

Convert Multi-Dimensional Array to 1D.

```python
arr.flatten()
```

---

# Indexing

```python
arr = np.array([10,20,30,40])

print(arr[0])
print(arr[2])
```

Output:

```python
10
30
```

---

# 2D Indexing

```python
arr = np.array([
    [10,20,30],
    [40,50,60]
])

print(arr[0,1])
```

Output:

```python
20
```

---

# Slicing

```python
arr = np.array([10,20,30,40,50])

print(arr[1:4])
```

Output:

```python
[20 30 40]
```

---

# Mathematical Operations

```python
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

Output:

```python
[5 7 9]
[-3 -3 -3]
[ 4 10 18]
[0.25 0.4  0.5 ]
```

---

# Statistical Functions

```python
arr = np.array([10,20,30,40,50])

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
```

Output:

```python
150
30.0
50
10
```

---

# Additional Statistics

```python
print(np.median(arr))
print(np.std(arr))
print(np.var(arr))
```

Output:

```python
30.0
14.1421356237
200.0
```

---

# Sorting Arrays

```python
arr = np.array([40,10,30,20])

print(np.sort(arr))
```

Output:

```python
[10 20 30 40]
```

---

# Filtering Data

```python
arr = np.array([10,20,30,40,50])

print(arr[arr > 25])
```

Output:

```python
[30 40 50]
```

---

# Aggregate Functions

```python
arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr.sum())
print(arr.sum(axis=0))
print(arr.sum(axis=1))
```

Output:

```python
21
[5 7 9]
[ 6 15]
```

---

# Random Numbers

## Random Integers

```python
np.random.randint(1,100,10)
```

Example Output:

```python
[45 22 89 11 76 90 33 67 54 10]
```

---

## Random Float Values

```python
np.random.rand(5)
```

Example Output:

```python
[0.23 0.56 0.78 0.12 0.91]
```

---

## Random Matrix

```python
np.random.rand(3,3)
```

---

# Copy vs View

## Copy

```python
arr = np.array([1,2,3])

x = arr.copy()

arr[0] = 100

print(arr)
print(x)
```

Output:

```python
[100   2   3]
[1 2 3]
```

---

## View

```python
arr = np.array([1,2,3])

x = arr.view()

arr[0] = 100

print(arr)
print(x)
```

Output:

```python
[100   2   3]
[100   2   3]
```

---

# Joining Arrays

## Vertical Stack

```python
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.vstack((a,b)))
```

Output:

```python
[[1 2 3]
 [4 5 6]]
```

---

## Horizontal Stack

```python
print(np.hstack((a,b)))
```

Output:

```python
[1 2 3 4 5 6]
```

---

# Matrix Multiplication

```python
a = np.array([
    [1,2],
    [3,4]
])

b = np.array([
    [5,6],
    [7,8]
])

print(np.dot(a,b))
```

Output:

```python
[[19 22]
 [43 50]]
```

---

# Transpose Matrix

```python
print(a.T)
```

Output:

```python
[[1 3]
 [2 4]]
```

---

# Unique Values

```python
arr = np.array([1,2,2,3,3,4])

print(np.unique(arr))
```

Output:

```python
[1 2 3 4]
```

---

# Handling Missing Values

```python
arr = np.array([1,2,np.nan,4])

print(np.isnan(arr))
```

Output:

```python
[False False  True False]
```

---

# Practical Example: Student Marks Analysis

```python
import numpy as np

marks = np.array([78,85,90,65,88])

print("Marks:", marks)
print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))

passed = marks[marks >= 70]

print("Passed Students:", passed)
```

Output:

```python
Marks: [78 85 90 65 88]
Total: 406
Average: 81.2
Highest: 90
Lowest: 65
Passed Students: [78 85 90 88]
```

---

# Most Important NumPy Functions for Interviews

| Function | Purpose |
|-----------|----------|
| np.array() | Create Array |
| np.arange() | Generate Sequence |
| np.linspace() | Equal Intervals |
| np.reshape() | Change Shape |
| np.flatten() | Convert to 1D |
| np.sum() | Total |
| np.mean() | Average |
| np.max() | Maximum |
| np.min() | Minimum |
| np.sort() | Sorting |
| np.unique() | Unique Values |
| np.isnan() | Missing Values |
| np.dot() | Matrix Multiplication |
| np.vstack() | Vertical Join |
| np.hstack() | Horizontal Join |
| np.random.randint() | Random Integers |



If you master:

1. Arrays
2. Indexing
3. Slicing
4. Reshape
5. Statistics
6. Filtering
7. Matrix Multiplication

You can easily move to:

- Pandas
- Data Analysis
- Machine Learning
- Deep Learning
- Data Engineering
