# Python OOP Frequency Analyzer Framework

## The Universal Pattern

All 10 problems follow the same 4-step workflow:

```text
Input Data
    ↓
Clean / Normalize
    ↓
Count Frequency
    ↓
Find Maximum
    ↓
Filter By Threshold
```

---

# Generic Class Structure

```python
class Analyzer:

    def preprocess_data(self, data):
        pass

    def compute_frequency(self, items):
        pass

    def get_most_frequent(self, freq_dict):
        pass

    def filter_by_frequency(self, freq_dict, n):
        pass
```

---

# Step 1: Clean / Normalize Data

## Why?

Data may contain:

```text
Python
python
PYTHON
```

These should be treated as the same value.

---

## Generic Syntax

```python
cleaned = item.lower()
```

or

```python
cleaned = item.upper()
```

or

```python
cleaned = item.title()
```

---

## Memory Trick

```text
Normalize First
Count Later
```

---

# Step 2: Compute Frequency

## Goal

Convert:

```python
["python", "java", "python"]
```

Into:

```python
{
    "python": 2,
    "java": 1
}
```

---

## Step-by-Step Logic

### Create Empty Dictionary

```python
freq = {}
```

---

### Iterate Through List

```python
for item in items:
```

---

### Count Occurrence

```python
freq[item] = freq.get(item, 0) + 1
```

---

## How get() Works

### First Occurrence

```python
freq.get("python",0)

returns

0
```

Then:

```python
0 + 1
```

Dictionary becomes:

```python
{
    "python":1
}
```

---

### Second Occurrence

```python
freq.get("python",0)

returns

1
```

Then:

```python
1 + 1
```

Dictionary becomes:

```python
{
    "python":2
}
```

---

## Complete Code

```python
freq = {}

for item in items:
    freq[item] = freq.get(item, 0) + 1

return freq
```

---

# Step 3: Find Most Frequent Item

## Goal

Given:

```python
{
    "python":3,
    "java":2,
    "scala":1
}
```

Return:

```python
("python",3)
```

---

## Step 1

Check empty dictionary.

```python
if not freq_dict:
    return None
```

---

## Step 2

Use max()

```python
max(
    freq_dict.items(),
    key=lambda x: x[1]
)
```

---

## Understanding items()

```python
freq_dict.items()
```

Produces:

```python
[
    ("python",3),
    ("java",2),
    ("scala",1)
]
```

---

## Understanding Lambda

```python
lambda x: x[1]
```

Means:

```text
Compare using count
```

Example:

```text
("python",3) → 3
("java",2)   → 2
("scala",1)  → 1
```

Largest:

```text
3
```

Return:

```python
("python",3)
```

---

## Complete Code

```python
if not freq_dict:
    return None

return max(
    freq_dict.items(),
    key=lambda x: x[1]
)
```

---

# Step 4: Filter By Frequency

## Goal

Given:

```python
{
    "python":3,
    "java":2,
    "scala":1
}
```

Threshold:

```python
2
```

Return:

```python
{
    "python":3,
    "java":2
}
```

---

## Step-by-Step

Create empty dictionary.

```python
result = {}
```

---

Iterate.

```python
for word, count in freq_dict.items():
```

---

Check threshold.

```python
if count >= n:
```

---

Add item.

```python
result[word] = count
```

---

Return.

```python
return result
```

---

# Complete Solution Example

## Character Frequency Counter

```python
class CharacterFrequencyCounter:

    def preprocess_text(self, text):

        text = text.lower()
        text = text.replace(" ", "")

        return text

    def compute_character_frequency(self, text):

        freq = {}

        for char in text:
            freq[char] = freq.get(char, 0) + 1

        return freq

    def get_most_frequent_character(self, freq_dict):

        if not freq_dict:
            return None

        return max(
            freq_dict.items(),
            key=lambda x: x[1]
        )

    def filter_by_frequency(self, freq_dict, n):

        result = {}

        for char, count in freq_dict.items():

            if count >= n:
                result[char] = count

        return result
```

---

# Exam Memory Formula

Whenever you see:

```text
Count Frequency
```

Think:

```python
freq = {}

for item in items:
    freq[item] = freq.get(item, 0) + 1
```

---

Whenever you see:

```text
Most Frequent
```

Think:

```python
max(
    freq.items(),
    key=lambda x: x[1]
)
```

---

Whenever you see:

```text
Filter Threshold
```

Think:

```python
for key, value in dict.items():

    if value >= n:
```

---

# Golden Interview Pattern

```text
Clean
 ↓
Count
 ↓
Max
 ↓
Filter
```

This pattern solves:

* Word Frequency Counter
* Character Frequency Counter
* Product Sales Counter
* Student Grade Analyzer
* Website Visitor Counter
* Department Counter
* Movie Genre Analyzer
* Hashtag Analyzer
* Customer Purchase Analyzer
* Error Log Analyzer

```
```
