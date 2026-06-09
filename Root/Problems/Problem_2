# Question 2

---

# 📌 Problem Statement

You need to implement a **Product Sales Analyzer** that takes a list of product names from customer purchases and returns a dictionary where:

* **Keys** → Product Names
* **Values** → Number of Times Purchased

The implementation should handle **case insensitivity** and **special characters** in product names.

---

# 📌 Class Declaration

```python
class ProductSalesAnalyzer:
```

### 📌 No need for init method

```python
def __init__(self):
    pass
```

---

# 📌 Operations

## 1. Clean and Normalize Product Names

📌 Removes special characters, converts product names to lowercase, and returns a cleaned list.

### 🔹 Function Prototype

```python
def preprocess_products(self, product_text: str) -> list:
```

### 🔹 Example Input

```python
preprocess_products("Laptop, laptop! Mouse Keyboard? Laptop")
```

### 🔹 Expected Output

```python
['laptop', 'laptop', 'mouse', 'keyboard', 'laptop']
```

### 🔹 Implementation Flow

💡 Convert the input text to lowercase.

💡 Remove punctuation using:

```python
re.sub(r'[^\w\s]', '', text)
```

💡 Split the cleaned text into product names using:

```python
.split()
```

---

## 2. Compute Product Purchase Frequency

📌 Counts how many times each product was purchased.

### 🔹 Function Prototype

```python
def compute_product_frequency(self, products: list) -> dict:
```

### 🔹 Example Input

```python
compute_product_frequency(
    ['laptop', 'laptop', 'mouse', 'keyboard', 'laptop']
)
```

### 🔹 Expected Output

```python
{
    'laptop': 3,
    'mouse': 1,
    'keyboard': 1
}
```

### 🔹 Implementation Flow

💡 Declare an empty dictionary.

💡 Iterate through the list using a `for` loop.

💡 Use:

```python
dict.get(product, 0)
```

to count occurrences.

💡 Return a dictionary where:

* Keys = Product Names
* Values = Purchase Counts

---

## 3. Get Best-Selling Product

📌 Returns the most purchased product and its purchase count.

### 🔹 Function Prototype

```python
def get_best_selling_product(self, freq_dict: dict) -> tuple:
```

### 🔹 Example Input

```python
get_best_selling_product(
    {'laptop': 3, 'mouse': 1, 'keyboard': 1}
)
```

### 🔹 Expected Output

```python
('laptop', 3)
```

### 🔹 Implementation Flow

💡 If the dictionary is empty, return:

```python
None
```

💡 Find the product with the highest purchase count using:

```python
max()
```

💡 Use:

```python
lambda x: x[1]
```

for comparison.

💡 Return a tuple containing:

```python
(product_name, count)
```

---

## 4. Filter Products by Minimum Purchase Count

📌 Returns products that were purchased at least `n` times.

### 🔹 Function Prototype

```python
def filter_products_by_frequency(
    self,
    freq_dict: dict,
    n: int
) -> dict:
```

### 🔹 Example Input

```python
filter_products_by_frequency(
    {'laptop': 3, 'mouse': 1, 'keyboard': 1},
    2
)
```

### 🔹 Expected Output

```python
{
    'laptop': 3
}
```

### 🔹 Implementation Flow

💡 Iterate through the dictionary using a `for` loop.

💡 Include only products whose count is:

```python
count >= n
```

💡 Return the filtered dictionary.

💡 If no products satisfy the condition, return:

```python
{}
```

---

# 📌 Sample Scenario

### Input

```python
"Laptop, laptop! Mouse Keyboard? Laptop"
```

### After Preprocessing

```python
['laptop', 'laptop', 'mouse', 'keyboard', 'laptop']
```

### Frequency Dictionary

```python
{
    'laptop': 3,
    'mouse': 1,
    'keyboard': 1
}
```

### Best-Selling Product

```python
('laptop', 3)
```

### Filter Products (Threshold = 2)

```python
{
    'laptop': 3
}
```

---

# 📌 Skills Tested

* Object-Oriented Programming (OOP)
* String Manipulation
* Regular Expressions (`re`)
* Dictionary Operations
* Loops
* Frequency Counting
* Lambda Functions
* Data Filtering
