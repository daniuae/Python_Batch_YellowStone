# EmployeePerformanceAnalyzer – All Possible Numeric Conditions & Explanations

When solving NumPy validation and analytics problems, interviewers often expect candidates to know different types of **numeric conditions** that can be applied to arrays.

---

# 1. `create_performance_array()`

```python
np.array(scores_array, dtype=int)
```

## Possible Numeric Conditions

### Condition 1: Integer Conversion

```python
dtype=int
```

**Purpose:** Ensures all values are stored as integers.

**Example:**

```python
[85.7, 90.2, 78.9]
```

becomes

```python
[85, 90, 78]
```

---

### Condition 2: Float Conversion

```python
dtype=float
```

**Purpose:** Useful when calculations involve percentages.

**Example:**

```python
[85, 90, 78]
```

becomes

```python
[85.0, 90.0, 78.0]
```

---

### Condition 3: Numeric Type Check

```python
np.issubdtype(arr.dtype, np.number)
```

**Purpose:** Checks whether array contains numeric values.

**Example:**

```python
["A", "B", "C"]
```

Result:

```python
False
```

---

# 2. `validate_scores()`

Current requirement:

```python
0 <= score <= 100
```

---

## A. Empty Array Validation

### Check

```python
arr.size == 0
```

**Example:**

```python
[]
```

**Result:**

```python
False
```

**Purpose:** No employee data available.

---

## B. Negative Values

### Check

```python
np.any(arr < 0)
```

**Example:**

```python
[85, -10, 90]
```

**Result:**

```python
False
```

**Purpose:** Performance score cannot be negative.

---

## C. Greater Than Maximum

### Check

```python
np.any(arr > 100)
```

**Example:**

```python
[85, 105, 90]
```

**Result:**

```python
False
```

**Purpose:** Score cannot exceed 100.

---

## D. Inclusive Range

### Check

```python
np.all((arr >= 0) & (arr <= 100))
```

**Example:**

```python
[0, 25, 50, 75, 100]
```

**Result:**

```python
True
```

---

## E. Strict Range

### Check

```python
np.all((arr > 0) & (arr < 100))
```

**Example:**

```python
[0, 50, 100]
```

**Result:**

```python
False
```

---

## F. Missing Values

### Check

```python
np.any(np.isnan(arr))
```

**Example:**

```python
[85, np.nan, 90]
```

**Result:**

```python
False
```

---

## G. Infinite Values

### Check

```python
np.any(np.isinf(arr))
```

**Example:**

```python
[85, np.inf]
```

**Result:**

```python
False
```

---

# 3. `compute_performance_summary()`

## A. Total

```python
np.sum(arr)
```

**Purpose:** Adds all elements.

**Example:**

```python
[85, 90, 78]
```

**Output:**

```python
253
```

---

## B. Average

```python
np.mean(arr)
```

**Purpose:** Arithmetic mean.

**Example:**

```python
[80, 90]
```

**Output:**

```python
85
```

---

## C. Maximum

```python
np.max(arr)
```

**Purpose:** Largest value.

**Example:**

```python
[85, 90, 78]
```

**Output:**

```python
90
```

---

## D. Minimum

```python
np.min(arr)
```

**Purpose:** Smallest value.

**Example:**

```python
[85, 90, 78]
```

**Output:**

```python
78
```

---

## E. Median

```python
np.median(arr)
```

**Purpose:** Middle value.

**Example:**

```python
[70, 80, 90]
```

**Output:**

```python
80
```

---

## F. Standard Deviation

```python
np.std(arr)
```

**Purpose:** Measures score spread.

**Example:**

```python
[85, 90, 78]
```

**Output:** Variation among employees.

---

# 4. `apply_bonus()`

Current condition:

```python
score > 85
```

---

## A. Greater Than

```python
arr > 85
```

**Example:**

```python
[85, 90, 78]
```

**Mask:**

```python
[False, True, False]
```

---

## B. Greater Than Or Equal

```python
arr >= 85
```

**Example:**

```python
[85, 90]
```

**Mask:**

```python
[True, True]
```

---

## C. Between Two Values

```python
(arr >= 80) & (arr < 90)
```

**Example:**

```python
[75, 85, 95]
```

**Mask:**

```python
[False, True, False]
```

---

## D. Multiple Conditions (AND)

```python
(arr > 85) & (arr < 95)
```

**Example:**

```python
[84, 90, 96]
```

**Mask:**

```python
[False, True, False]
```

---

## E. OR Condition

```python
(arr < 50) | (arr > 90)
```

**Example:**

```python
[45, 70, 95]
```

**Mask:**

```python
[True, False, True]
```

---

## F. Clipping Values

```python
np.clip(arr, 0, 100)
```

**Example:**

```python
[80, 105, 120]
```

**Output:**

```python
[80, 100, 100]
```

---

# 5. `categorize_employees()`

Current Logic:

```text
>=90   → Excellent
80-89  → Good
<80    → Needs Improvement
```

---

## A. Excellent

```python
arr >= 90
```

**Example:**

```python
[90, 95, 100]
```

---

## B. Good

```python
(arr >= 80) & (arr < 90)
```

**Example:**

```python
[80, 85, 89]
```

---

## C. Needs Improvement

```python
arr < 80
```

**Example:**

```python
[50, 60, 79]
```

---

## D. Outstanding Category

```python
arr >= 95
```

**Example:**

```python
[95, 98, 100]
```

---

## E. Poor Category

```python
arr < 60
```

**Example:**

```python
[20, 40, 55]
```

---

# 6. `format_scores_with_grades()`

## Grade A

```python
score >= 90
```

**Example:**

```python
92
```

**Grade:** `A`

---

## Grade B

```python
80 <= score < 90
```

**Example:**

```python
85
```

**Grade:** `B`

---

## Grade C

```python
70 <= score < 80
```

**Example:**

```python
75
```

**Grade:** `C`

---

## Grade D

```python
score < 70
```

**Example:**

```python
65
```

**Grade:** `D`

---

# Common NumPy Numeric Comparison Operators

| Operator | Meaning | Example |
|-----------|----------|----------|
| `<` | Less Than | `arr < 80` |
| `<=` | Less Than or Equal | `arr <= 80` |
| `>` | Greater Than | `arr > 80` |
| `>=` | Greater Than or Equal | `arr >= 80` |
| `==` | Equal To | `arr == 80` |
| `!=` | Not Equal To | `arr != 80` |
| `&` | Logical AND | `(arr > 80) & (arr < 90)` |
| `\|` | Logical OR | `(arr < 50) \| (arr > 90)` |
| `~` | Logical NOT | `~(arr > 80)` |

---

# Common NumPy Validation Functions

| Function | Purpose |
|----------|---------|
| `np.any()` | At least one element satisfies condition |
| `np.all()` | All elements satisfy condition |
| `np.isnan()` | Detect NaN values |
| `np.isinf()` | Detect Infinite values |
| `np.sum()` | Total |
| `np.mean()` | Average |
| `np.max()` | Highest value |
| `np.min()` | Lowest value |
| `np.median()` | Middle value |
| `np.std()` | Standard deviation |
| `np.clip()` | Restrict values to a range |
| `np.where()` | Conditional replacement |
| `np.select()` | Multiple conditional categories |

---

# Most Common Interview Conditions

```python
# Negative numbers
arr < 0

# Positive numbers
arr > 0

# Zero values
arr == 0

# Non-zero values
arr != 0

# Even numbers
arr % 2 == 0

# Odd numbers
arr % 2 != 0

# Multiples of 5
arr % 5 == 0

# Multiples of 10
arr % 10 == 0

# Between two values
(arr >= 80) & (arr <= 90)

# Outside range
(arr < 0) | (arr > 100)

# Missing values
np.isnan(arr)

# Infinite values
np.isinf(arr)

# Maximum threshold
arr >= threshold

# Minimum threshold
arr <= threshold
```

---

# Quick Revision Summary

| Condition Type | Example |
|---------------|----------|
| Greater Than | `arr > 80` |
| Less Than | `arr < 80` |
| Equal To | `arr == 80` |
| Not Equal To | `arr != 80` |
| Range Check | `(arr >= 70) & (arr <= 90)` |
| OR Condition | `(arr < 50) \| (arr > 90)` |
| Empty Check | `arr.size == 0` |
| Missing Check | `np.isnan(arr)` |
| Infinite Check | `np.isinf(arr)` |
| Clip Values | `np.clip(arr, 0, 100)` |
| Any Match | `np.any(condition)` |
| All Match | `np.all(condition)` |

These conditions cover nearly all NumPy-based validation, filtering, categorization, and aggregation questions commonly asked in Data Engineering, Python, Pandas, and NumPy assessments.
