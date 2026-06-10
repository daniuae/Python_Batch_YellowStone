# Product Sales Analyzer – Step-by-Step Solution

## 📌 Problem Statement

Implement a **Product Sales Analyzer** that:

* Cleans and normalizes product names
* Counts product purchase frequency
* Finds the best-selling product
* Filters products based on minimum purchase count

---

# Step 1: Import Required Module

```python
import re
```

### Explanation

| Code        | Purpose                                    |
| ----------- | ------------------------------------------ |
| `import re` | Imports Python's Regular Expression module |

---

# Step 2: Create the Class

```python
class ProductSalesAnalyzer:
```

### Explanation

Creates a class named `ProductSalesAnalyzer` to group all product analysis methods.

---

# Step 3: Clean and Normalize Product Names

## Function Prototype

```python
def preprocess_products(self, product_text: str) -> list:
```

## Code

```python
def preprocess_products(self, product_text: str) -> list:

    # Convert to lowercase
    text = product_text.lower()

    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Split into product names
    products = text.split()

    return products
```

### Example

#### Input

```python
"Laptop, laptop! Mouse Keyboard? Laptop"
```

#### Output

```python
['laptop', 'laptop', 'mouse', 'keyboard', 'laptop']
```

### Flow

1. Convert text to lowercase.
2. Remove special characters.
3. Split text into individual product names.
4. Return the cleaned list.

---

# Step 4: Compute Product Purchase Frequency

## Function Prototype

```python
def compute_product_frequency(self, products: list) -> dict:
```

## Code

```python
def compute_product_frequency(self, products: list) -> dict:

    frequency = {}

    for product in products:
        frequency[product] = frequency.get(product, 0) + 1

    return frequency
```

### Example

#### Input

```python
[
    'laptop',
    'laptop',
    'mouse',
    'keyboard',
    'laptop'
]
```

#### Output

```python
{
    'laptop': 3,
    'mouse': 1,
    'keyboard': 1
}
```

### Flow

1. Create an empty dictionary.
2. Loop through each product.
3. Use `get()` to retrieve the current count.
4. Increment count by 1.
5. Return the frequency dictionary.

---

# Understanding `dict.get()`

```python
frequency.get(product, 0)
```

### Example

```python
frequency = {}

frequency.get("laptop", 0)
```

### Output

```python
0
```

If the key exists, its value is returned.

If the key does not exist, `0` is returned.

---

# Step 5: Get Best-Selling Product

## Function Prototype

```python
def get_best_selling_product(self, freq_dict: dict) -> tuple:
```

## Code

```python
def get_best_selling_product(self, freq_dict: dict) -> tuple:

    if not freq_dict:
        return None

    best_product = max(
        freq_dict.items(),
        key=lambda x: x[1]
    )

    return best_product
```

### Example

#### Input

```python
{
    'laptop': 3,
    'mouse': 1,
    'keyboard': 1
}
```

#### Output

```python
('laptop', 3)
```

### Flow

1. Check whether dictionary is empty.
2. Use `max()` to find the highest count.
3. Use `lambda x: x[1]` to compare counts.
4. Return `(product_name, count)`.

---

# Understanding Lambda Function

```python
lambda x: x[1]
```

### Example

Input:

```python
('laptop', 3)
```

Output:

```python
3
```

The lambda function tells Python:

> Compare dictionary items using the purchase count.

---

# Step 6: Filter Products by Minimum Purchase Count

## Function Prototype

```python
def filter_products_by_frequency(
    self,
    freq_dict: dict,
    n: int
) -> dict:
```

## Code

```python
def filter_products_by_frequency(
    self,
    freq_dict: dict,
    n: int
) -> dict:

    filtered = {}

    for product, count in freq_dict.items():

        if count >= n:
            filtered[product] = count

    return filtered
```

### Example

#### Input

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

#### Output

```python
{
    'laptop': 3
}
```

### Flow

1. Loop through the dictionary.
2. Check whether count is greater than or equal to threshold.
3. Store qualifying products.
4. Return filtered dictionary.

---

# Step 7: Complete Program

```python
import re


class ProductSalesAnalyzer:

    def preprocess_products(self, product_text: str) -> list:

        text = product_text.lower()

        text = re.sub(
            r'[^\w\s]',
            '',
            text
        )

        products = text.split()

        return products


    def compute_product_frequency(
        self,
        products: list
    ) -> dict:

        frequency = {}

        for product in products:
            frequency[product] = (
                frequency.get(product, 0) + 1
            )

        return frequency


    def get_best_selling_product(
        self,
        freq_dict: dict
    ) -> tuple:

        if not freq_dict:
            return None

        return max(
            freq_dict.items(),
            key=lambda x: x[1]
        )


    def filter_products_by_frequency(
        self,
        freq_dict: dict,
        n: int
    ) -> dict:

        filtered = {}

        for product, count in freq_dict.items():

            if count >= n:
                filtered[product] = count

        return filtered
```

---

# Step 8: Driver Program

```python
analyzer = ProductSalesAnalyzer()

text = "Laptop, laptop! Mouse Keyboard? Laptop"

products = analyzer.preprocess_products(text)

frequency = analyzer.compute_product_frequency(products)

best_product = analyzer.get_best_selling_product(
    frequency
)

filtered_products = (
    analyzer.filter_products_by_frequency(
        frequency,
        2
    )
)

print("Products:")
print(products)

print("\nFrequency:")
print(frequency)

print("\nBest Selling Product:")
print(best_product)

print("\nFiltered Products:")
print(filtered_products)
```

---

# Expected Output

```python
Products:
['laptop', 'laptop', 'mouse', 'keyboard', 'laptop']

Frequency:
{
    'laptop': 3,
    'mouse': 1,
    'keyboard': 1
}

Best Selling Product:
('laptop', 3)

Filtered Products:
{
    'laptop': 3
}
```

---

# Skills Tested

| Concept                | Usage                      |
| ---------------------- | -------------------------- |
| OOP                    | Class and Methods          |
| String Manipulation    | `lower()`, `split()`       |
| Regular Expressions    | `re.sub()`                 |
| Dictionaries           | Frequency counting         |
| Loops                  | `for` loop                 |
| Lambda Functions       | Best-selling product       |
| Conditional Statements | Filtering                  |
| Data Analysis          | Product frequency analysis |

---

# Summary

Input:

```python
"Laptop, laptop! Mouse Keyboard? Laptop"
```

After Preprocessing:

```python
['laptop', 'laptop', 'mouse', 'keyboard', 'laptop']
```

Frequency Dictionary:

```python
{
    'laptop': 3,
    'mouse': 1,
    'keyboard': 1
}
```

Best-Selling Product:

```python
('laptop', 3)
```

Filtered Products (Threshold = 2):

```python
{
    'laptop': 3
}
```
