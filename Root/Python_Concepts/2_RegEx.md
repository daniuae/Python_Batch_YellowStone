# Python Regular Expressions (Regex) - Complete Guide

## Table of Contents

1. Introduction to Regex
2. Why Use Regex?
3. Python `re` Module
4. Basic Regex Functions
5. Character Classes
6. Quantifiers
7. Anchors
8. Wildcards
9. Groups and Capturing
10. Real-World Examples
11. Regex Compilation
12. Regex Flags
13. Regex Cheat Sheet
14. Data Engineering Use Cases
15. Interview Questions

---

# 1. Introduction to Regex

A **Regular Expression (Regex)** is a sequence of characters that defines a search pattern.

Regex is used for:

* Searching text
* Pattern matching
* Data validation
* Data extraction
* Data cleaning
* Text replacement

### Example

```python
import re

text = "My phone number is 9876543210"

result = re.search(r"\d+", text)

print(result.group())
```

**Output**

```text
9876543210
```

---

# 2. Why Use Regex?

| Use Case         | Example                                 |
| ---------------- | --------------------------------------- |
| Email Validation | [user@gmail.com](mailto:user@gmail.com) |
| Phone Validation | 9876543210                              |
| Data Cleaning    | Remove special characters               |
| Log Analysis     | Extract error messages                  |
| ETL Pipelines    | Transform data                          |
| Web Scraping     | Extract URLs                            |
| NLP              | Text preprocessing                      |

---

# 3. Python re Module

Python provides a built-in module:

```python
import re
```

This module contains all regex-related functions.

---

# 4. Basic Regex Functions

| Function        | Description                |
| --------------- | -------------------------- |
| `re.search()`   | Find first match anywhere  |
| `re.match()`    | Match from beginning       |
| `re.findall()`  | Return all matches         |
| `re.finditer()` | Return iterator of matches |
| `re.sub()`      | Replace text               |
| `re.split()`    | Split text                 |
| `re.compile()`  | Compile regex pattern      |

---

# 5. re.search()

Searches entire string.

```python
import re

text = "Python is awesome"

result = re.search("awesome", text)

print(result.group())
```

**Output**

```text
awesome
```

---

# 6. re.match()

Checks only the beginning of a string.

```python
import re

text = "Python is awesome"

print(re.match("Python", text))
```

**Output**

```text
Match Found
```

---

```python
print(re.match("awesome", text))
```

**Output**

```text
None
```

---

# 7. re.findall()

Returns all matches.

```python
import re

text = "cat bat rat mat"

result = re.findall(r"\w+at", text)

print(result)
```

**Output**

```python
['cat', 'bat', 'rat', 'mat']
```

---

# 8. re.finditer()

Returns an iterator.

```python
import re

text = "cat bat rat"

for match in re.finditer(r"\w+at", text):
    print(match.group())
```

**Output**

```text
cat
bat
rat
```

---

# 9. re.sub()

Replace text.

```python
import re

text = "I love Java"

new_text = re.sub("Java", "Python", text)

print(new_text)
```

**Output**

```text
I love Python
```

---

# 10. re.split()

Split text using regex.

```python
import re

text = "apple,banana;orange"

result = re.split("[,;]", text)

print(result)
```

**Output**

```python
['apple', 'banana', 'orange']
```

---

# 11. Character Classes

## Digits

### `\d`

Matches digits 0-9.

```python
re.findall(r"\d", "A1B2C3")
```

**Output**

```python
['1', '2', '3']
```

---

## Non-Digits

### `\D`

```python
re.findall(r"\D", "A1B2")
```

**Output**

```python
['A', 'B']
```

---

## Word Characters

### `\w`

Matches:

* a-z
* A-Z
* 0-9
* _

```python
re.findall(r"\w", "A_1")
```

**Output**

```python
['A', '_', '1']
```

---

## Non-Word Characters

### `\W`

```python
re.findall(r"\W", "Hello@123")
```

**Output**

```python
['@']
```

---

## Whitespace

### `\s`

Matches:

* Space
* Tab
* Newline

```python
re.findall(r"\s", "A B")
```

**Output**

```python
[' ']
```

---

## Non-Whitespace

### `\S`

```python
re.findall(r"\S", "A B")
```

**Output**

```python
['A', 'B']
```

---

# 12. Quantifiers

## *

Zero or More

```python
re.findall(r"ab*", "ab abb abbb a")
```

**Output**

```python
['ab', 'abb', 'abbb', 'a']
```

---

## +

One or More

```python
re.findall(r"ab+", "ab abb abbb")
```

**Output**

```python
['ab', 'abb', 'abbb']
```

---

## ?

Zero or One

```python
re.findall(r"colou?r", "color colour")
```

**Output**

```python
['color', 'colour']
```

---

## {n}

Exactly n occurrences

```python
re.findall(r"\d{4}", "Year 2025")
```

**Output**

```python
['2025']
```

---

## {n,m}

Between n and m occurrences

```python
re.findall(r"\d{2,4}", "1 12 123 1234")
```

**Output**

```python
['12', '123', '1234']
```

---

# 13. Anchors

## Start of String (^)

```python
re.search(r"^Python", "Python is good")
```

---

## End of String ($)

```python
re.search(r"good$", "Python is good")
```

---

# 14. Wildcard

## .

Matches any character except newline.

```python
re.findall(r"c.t", "cat cot cut")
```

**Output**

```python
['cat', 'cot', 'cut']
```

---

# 15. OR Operator

## |

```python
re.findall(r"cat|dog", "cat dog lion")
```

**Output**

```python
['cat', 'dog']
```

---

# 16. Groups

## Capturing Groups

```python
import re

text = "John 25"

result = re.search(r"(\w+)\s(\d+)", text)

print(result.group(1))
print(result.group(2))
```

**Output**

```text
John
25
```

---

# 17. Named Groups

```python
import re

text = "John 25"

result = re.search(
    r"(?P<name>\w+)\s(?P<age>\d+)",
    text
)

print(result.group("name"))
print(result.group("age"))
```

**Output**

```text
John
25
```

---

# 18. Real-World Examples

## Email Validation

```python
import re

email = "abc@gmail.com"

pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

print(bool(re.match(pattern, email)))
```

**Output**

```text
True
```

---

## Indian Mobile Number Validation

```python
import re

phone = "9876543210"

pattern = r"^[6-9]\d{9}$"

print(bool(re.match(pattern, phone)))
```

**Output**

```text
True
```

---

## Extract Numbers

```python
import re

text = "Order 123 cost 450"

numbers = re.findall(r"\d+", text)

print(numbers)
```

**Output**

```python
['123', '450']
```

---

## Extract Dates

```python
import re

text = "Today is 11-06-2026"

date = re.findall(
    r"\d{2}-\d{2}-\d{4}",
    text
)

print(date)
```

**Output**

```python
['11-06-2026']
```

---

## Remove Special Characters

```python
import re

text = "Laptop!!@@#"

clean = re.sub(
    r"[^\w\s]",
    "",
    text
)

print(clean)
```

**Output**

```text
Laptop
```

---

# 19. Regex Compilation

Used when the same pattern is reused multiple times.

```python
import re

pattern = re.compile(r"\d+")

print(pattern.findall("123 abc 456"))
```

**Output**

```python
['123', '456']
```

---

# 20. Regex Flags

## Ignore Case

```python
re.IGNORECASE
```

Example:

```python
re.findall(
    r"python",
    "Python PYTHON",
    re.IGNORECASE
)
```

**Output**

```python
['Python', 'PYTHON']
```

---

## Multiline

```python
re.MULTILINE
```

Example:

```python
text = """Python
Java
Scala"""

re.findall(
    r"^Java",
    text,
    re.MULTILINE
)
```

**Output**

```python
['Java']
```

---

# 21. Regex Cheat Sheet

| Pattern  | Meaning            |    |
| -------- | ------------------ | -- |
| `\d`     | Digit              |    |
| `\D`     | Non-Digit          |    |
| `\w`     | Word Character     |    |
| `\W`     | Non-Word Character |    |
| `\s`     | Whitespace         |    |
| `\S`     | Non-Whitespace     |    |
| `.`      | Any Character      |    |
| `^`      | Start of String    |    |
| `$`      | End of String      |    |
| `*`      | Zero or More       |    |
| `+`      | One or More        |    |
| `?`      | Optional           |    |
| `{n}`    | Exactly n          |    |
| `{n,m}`  | Between n and m    |    |
| `[abc]`  | Any of abc         |    |
| `[^abc]` | Not abc            |    |
| `a       | b`                 | OR |
| `()`     | Group              |    |

---

# 22. Data Engineering Use Cases

## Validate Emails

```python
df["ValidEmail"] = df["Email"].str.match(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)
```

---

## Extract Product IDs

```python
df["ProductID"] = df["Description"].str.extract(
    r"(P\d+)"
)
```

---

## Remove Special Characters

```python
df["Product"] = df["Product"].str.replace(
    r"[^\w\s]",
    "",
    regex=True
)
```

---

## Extract Year

```python
df["Year"] = df["Date"].str.extract(
    r"(\d{4})"
)
```

---

# 23. Common Interview Questions

## Q1. Difference Between search() and match()

| search()               | match()               |
| ---------------------- | --------------------- |
| Searches entire string | Checks only beginning |
| More flexible          | More strict           |

---

## Q2. Difference Between findall() and finditer()

| findall()               | finditer()            |
| ----------------------- | --------------------- |
| Returns list            | Returns iterator      |
| Suitable for small data | Better for large data |

---

## Q3. Why Use r Before Regex?

Without raw string:

```python
"\\d+"
```

With raw string:

```python
r"\d+"
```

Raw strings avoid escape-character issues and improve readability.

---

# Frequently Used Regex Patterns

```python
\d+                     # Numbers
\w+                     # Words
\s+                     # Spaces
[^\w\s]                 # Special Characters
\d{4}-\d{2}-\d{2}       # Dates
^[6-9]\d{9}$            # Indian Mobile Number
^[\w.-]+@[\w.-]+$       # Email
```

---

# Summary

Regex is one of the most important tools for:

* Data Cleaning
* Data Validation
* Data Extraction
* ETL Pipelines
* Log Processing
* Web Scraping
* Natural Language Processing

For Data Engineers and Python Developers, mastering the following is essential:

* Character Classes
* Quantifiers
* Groups
* Anchors
* `findall()`
* `search()`
* `sub()`
* `compile()`

These concepts cover most real-world regex use cases.
