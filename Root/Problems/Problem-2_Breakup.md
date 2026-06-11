# Product Sales Analyzer – Step-by-Step Functional Breakdown

This document breaks the problem into small pieces so beginners can understand each functionality independently before combining everything into the final solution.

---

# Step 1: Understanding the Input

Suppose a customer purchase log is given as:

```python
product_text = "Laptop, laptop! Mouse Keyboard? Laptop"
```

Notice:

- Same product appears multiple times.
- Different letter cases (`Laptop`, `laptop`)
- Special characters (`, ! ?`)

Our goal is to clean the data and analyze product purchases.

---

# Functionality 1: Convert Text to Lowercase

## Why?

Python treats:

```python
"Laptop"
```

and

```python
"laptop"
```

as different strings.

To count correctly, convert everything to lowercase.

---

## Example

```python
product_text = "Laptop, laptop! Mouse Keyboard? Laptop"

lower_text = product_text.lower()

print(lower_text)
```

### Output

```python
laptop, laptop! mouse keyboard? laptop
```

---

# Functionality 2: Remove Special Characters

## Why?

Special characters should not become part of product names.

We want:

```python
Laptop,
```

to become

```python
Laptop
```

---

## Example

```python
import re

product_text = "laptop, laptop! mouse keyboard? laptop"

clean_text = re.sub(r'[^\w\s]', '', product_text)

print(clean_text)
```

### Output

```python
laptop laptop mouse keyboard laptop
```

---

# Understanding the Regular Expression

```python
r'[^\w\s]'
```

| Symbol | Meaning |
|----------|----------|
| \w | Letters and numbers |
| \s | Spaces |
| ^ | NOT |
| [ ] | Character Set |

Meaning:

```text
Remove everything that is NOT
a letter, number, or space.
```

---

# Functionality 3: Split Text into Product Names

## Why?

Currently we have one string:

```python
"laptop laptop mouse keyboard laptop"
```

We need a list.

---

## Example

```python
products = clean_text.split()

print(products)
```

### Output

```python
['laptop', 'laptop', 'mouse', 'keyboard', 'laptop']
```

---

# Complete Preprocessing Function

```python
import re

def preprocess_products(product_text):

    product_text = product_text.lower()

    product_text = re.sub(
        r'[^\w\s]',
        '',
        product_text
    )

    return product_text.split()
```

---

## Testing

```python
result = preprocess_products(
    "Laptop, laptop! Mouse Keyboard? Laptop"
)

print(result)
```

### Output

```python
['laptop', 'laptop', 'mouse', 'keyboard', 'laptop']
```

---

# Functionality 4: Create an Empty Dictionary

We need a structure to store counts.

```python
frequency = {}
```

Current value:

```python
{}
```

Meaning:

```text
No products counted yet.
```

---

# Functionality 5: Count Product Purchases

## Hardcoded Example

```python
products = [
    'laptop',
    'laptop',
    'mouse',
    'keyboard',
    'laptop'
]
```

---

## Step-by-Step Counting

### Start

```python
frequency = {}
```

Output

```python
{}
```

---

### Read First Product

```python
laptop
```

Update:

```python
frequency['laptop'] = 1
```

Output

```python
{
    'laptop': 1
}
```

---

### Read Second Product

```python
laptop
```

Update

```python
{
    'laptop': 2
}
```

---

### Read Third Product

```python
mouse
```

Update

```python
{
    'laptop': 2,
    'mouse': 1
}
```

---

### Read Fourth Product

```python
keyboard
```

Update

```python
{
    'laptop': 2,
    'mouse': 1,
    'keyboard': 1
}
```

---

### Read Fifth Product

```python
laptop
```

Update

```python
{
    'laptop': 3,
    'mouse': 1,
    'keyboard': 1
}
```

---

# Using Dictionary get()

Instead of checking:

```python
if product in frequency:
```

use:

```python
frequency[product] = (
    frequency.get(product, 0) + 1
)
```

---

## Example

```python
frequency = {}

product = "laptop"

frequency[product] = (
    frequency.get(product, 0) + 1
)

print(frequency)
```

### Output

```python
{
    'laptop': 1
}
```

---

# Complete Frequency Function

```python
def compute_product_frequency(products):

    frequency = {}

    for product in products:

        frequency[product] = (
            frequency.get(product, 0) + 1
        )

    return frequency
```

---

## Testing

```python
products = [
    'laptop',
    'laptop',
    'mouse',
    'keyboard',
    'laptop'
]

print(
    compute_product_frequency(products)
)
```

### Output

```python
{
    'laptop': 3,
    'mouse': 1,
    'keyboard': 1
}
```

---

# Functionality 6: Find Best-Selling Product

We need:

```python
{
    'laptop': 3,
    'mouse': 1,
    'keyboard': 1
}
```

to return:

```python
('laptop', 3)
```

---

## Using max()

```python
frequency = {
    'laptop': 3,
    'mouse': 1,
    'keyboard': 1
}

result = max(
    frequency.items(),
    key=lambda x: x[1]
)

print(result)
```

### Output

```python
('laptop', 3)
```

---

# Understanding lambda

Dictionary items become:

```python
('laptop', 3)

('mouse', 1)

('keyboard', 1)
```

Lambda:

```python
lambda x: x[1]
```

means

```python
compare using count value
```

Examples:

```python
('laptop', 3) -> 3

('mouse', 1) -> 1

('keyboard', 1) -> 1
```

Largest:

```python
3
```

Result:

```python
('laptop', 3)
```

---

# Complete Function

```python
def get_best_selling_product(freq_dict):

    if not freq_dict:
        return None

    return max(
        freq_dict.items(),
        key=lambda x: x[1]
    )
```

---

# Functionality 7: Filter Products

Suppose:

```python
{
    'laptop': 3,
    'mouse': 1,
    'keyboard': 1
}
```

Threshold:

```python
2
```

We keep only products whose count is:

```python
count >= 2
```

---

# Manual Process

Check Laptop

```python
3 >= 2
```

Keep

```python
{
    'laptop': 3
}
```

---

Check Mouse

```python
1 >= 2
```

No

Ignore

---

Check Keyboard

```python
1 >= 2
```

No

Ignore

---

Final Output

```python
{
    'laptop': 3
}
```

---

# Complete Function

```python
def filter_products_by_frequency(
    freq_dict,
    n
):

    filtered = {}

    for product, count in freq_dict.items():

        if count >= n:

            filtered[product] = count

    return filtered
```

---

# Testing

```python
frequency = {
    'laptop': 3,
    'mouse': 1,
    'keyboard': 1
}

print(
    filter_products_by_frequency(
        frequency,
        2
    )
)
```

### Output

```python
{
    'laptop': 3
}
```

---

# Complete End-to-End Flow

```python
import re

product_text = (
    "Laptop, laptop! Mouse Keyboard? Laptop"
)

# Step 1
clean_text = product_text.lower()

# Step 2
clean_text = re.sub(
    r'[^\w\s]',
    '',
    clean_text
)

# Step 3
products = clean_text.split()

print(products)

# Step 4
frequency = {}

for product in products:

    frequency[product] = (
        frequency.get(product, 0) + 1
    )

print(frequency)

# Step 5
best_selling = max(
    frequency.items(),
    key=lambda x: x[1]
)

print(best_selling)

# Step 6
filtered = {}

for product, count in frequency.items():

    if count >= 2:
        filtered[product] = count

print(filtered)
```

---

# Final Output

```python
['laptop', 'laptop', 'mouse', 'keyboard', 'laptop']

{
    'laptop': 3,
    'mouse': 1,
    'keyboard': 1
}

('laptop', 3)

{
    'laptop': 3
}
```

---

# Key Concepts Learned

- Classes and Methods
- String Manipulation
- `.lower()`
- Regular Expressions (`re.sub`)
- `.split()`
- Lists
- Dictionaries
- Dictionary `.get()`
- Loops (`for`)
- `max()`
- `lambda`
- Dictionary Filtering
- Frequency Counting
- Data Analysis Basics
