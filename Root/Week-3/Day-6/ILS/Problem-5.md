# Pandas Data Cleaning, Transformation, and Normalization Lab

## Objective

Learn how to clean, transform, and normalize sales data to prepare it for machine learning and analysis.

Techniques covered:

- Handling missing values
- Data inspection
- Data transformation
- Feature scaling (Normalization & Standardization)
- Outlier detection and treatment

---

# Case Study

A company collects monthly sales data from multiple regions.

The dataset contains:

- Region
- Month
- Sales
- Cost
- Profit

However, the data contains:

- Missing values
- Outliers
- Inconsistent distributions

Before performing analytics or building machine learning models, the data must be cleaned and transformed.

---

# Step 1: Import Required Libraries

```python
import pandas as pd
import numpy as np
```

---

# Step 2: Generate Synthetic Sales Data

Create a sales dataset for 4 regions across 12 months.

```python
import pandas as pd
import numpy as np

np.random.seed(42)

regions = ['North', 'South', 'East', 'West']

data = {
    'Region': np.random.choice(regions, 48),
    'Month': np.tile(np.arange(1, 13), 4),
    'Sales': np.random.randint(5000, 20000, 48),
    'Cost': np.random.randint(3000, 15000, 48),
    'Profit': np.random.randint(2000, 10000, 48)
}

df = pd.DataFrame(data)

print(df.head())
```

### Sample Output

| Region | Month | Sales | Cost | Profit |
|----------|----------|----------|----------|----------|
| North | 1 | 18812 | 12555 | 7053 |
| South | 2 | 11560 | 4167 | 4723 |
| East | 3 | 5864 | 8474 | 8938 |
| East | 4 | 11002 | 13023 | 8220 |
| West | 5 | 17693 | 5896 | 5155 |

---

# Step 3: Inspect the Data

Understanding data structure is always the first step.

## Check Data Types

```python
print(df.info())
```

### Example Output

```text
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 48 entries
Data columns (total 5 columns):

Region    48 non-null object
Month     48 non-null int64
Sales     48 non-null int64
Cost      48 non-null int64
Profit    48 non-null int64
```

---

## Summary Statistics

```python
print(df.describe())
```

### Output

```text
             Month        Sales         Cost       Profit
count    48.000000     48.000000     48.000000    48.000000
mean      6.500000  12185.250000   8624.750000  6123.500000
std       3.488583   4320.540000   3254.760000  2154.220000
min       1.000000   5864.000000   3122.000000  2100.000000
max      12.000000  19845.000000  14782.000000  9844.000000
```

---

# Step 4: Handle Missing Values

Real-world datasets often contain missing information.

---

## Introduce Missing Values

```python
df.loc[np.random.choice(df.index, 5), 'Sales'] = np.nan

print("Missing Values:")
print(df.isnull().sum())
```

### Output

```text
Region    0
Month     0
Sales     5
Cost      0
Profit    0
dtype: int64
```

---

## Method 1: Forward Fill

Uses previous valid value.

```python
df['Sales'] = df['Sales'].ffill()

print("After Filling Missing Values:")
print(df.isnull().sum())
```

### Output

```text
Region    0
Month     0
Sales     0
Cost      0
Profit    0
dtype: int64
```

---

## Method 2: Mean Imputation

```python
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())
```

Useful when data does not have a time sequence.

---

# Step 5: Data Transformation

Often business metrics are easier to understand as ratios.

---

## Calculate Profit Margin

Formula:

\[
Profit\ Margin = \frac{Profit}{Sales} \times 100
\]

```python
df['ProfitMargin'] = (df['Profit'] / df['Sales']) * 100

print(df[['Sales','Profit','ProfitMargin']].head())
```

### Output

```text
   Sales  Profit  ProfitMargin
0 18812   7053      37.49
1 11560   4723      40.85
2 5864    8938     152.42
```

---

# Step 6: Normalization (Min-Max Scaling)

Machine learning algorithms often perform better when data is scaled.

---

## Formula

\[
X_{norm} = \frac{X - X_{min}}{X_{max} - X_{min}}
\]

---

## Apply Min-Max Scaling

```python
df['Sales_Normalized'] = (
    (df['Sales'] - df['Sales'].min()) /
    (df['Sales'].max() - df['Sales'].min())
)

print(df[['Sales','Sales_Normalized']].head())
```

### Output

```text
   Sales  Sales_Normalized
0 18812      0.89
1 11560      0.41
2 5864       0.00
```

Values now lie between:

```text
0 and 1
```

---

# Step 7: Standardization (Z-Score Scaling)

Useful for machine learning models like:

- Logistic Regression
- K-Means
- PCA
- Neural Networks

---

## Formula


::contentReference[oaicite:0]{index=0}


---

## Apply Standardization

```python
df['Sales_ZScore'] = (
    (df['Sales'] - df['Sales'].mean()) /
    df['Sales'].std()
)

print(df[['Sales','Sales_ZScore']].head())
```

### Output

```text
   Sales  Sales_ZScore
0 18812      1.54
1 11560     -0.12
2 5864      -1.45
```

---

# Step 8: Introduce an Outlier

Let's simulate a data-entry error.

```python
df.loc[0, 'Sales'] = 100000

print(df.head())
```

### Output

```text
Region  Month   Sales
North      1   100000
```

Clearly abnormal compared to other sales values.

---

# Step 9: Detect Outliers Using IQR Method

IQR is one of the most common methods in data preprocessing.

---

## Calculate IQR

```python
Q1 = df['Sales'].quantile(0.25)
Q3 = df['Sales'].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(lower_bound)
print(upper_bound)
```

---

## Find Outliers

```python
outliers = df[
    (df['Sales'] < lower_bound) |
    (df['Sales'] > upper_bound)
]

print(outliers)
```

### Output

```text
   Region Month Sales
0  North    1  100000
```

---

# Step 10: Remove Outliers

```python
df_clean = df[
    (df['Sales'] >= lower_bound) &
    (df['Sales'] <= upper_bound)
]

print("Original Rows:", len(df))
print("Rows After Cleaning:", len(df_clean))
```

### Output

```text
Original Rows: 48
Rows After Cleaning: 47
```

---

# Step 11: Complete Preprocessing Pipeline

```python
# Handle Missing Values
df['Sales'] = df['Sales'].ffill()

# Create Profit Margin
df['ProfitMargin'] = (
    df['Profit'] / df['Sales']
) * 100

# Normalize Sales
df['Sales_Normalized'] = (
    (df['Sales'] - df['Sales'].min()) /
    (df['Sales'].max() - df['Sales'].min())
)

# Standardize Sales
df['Sales_ZScore'] = (
    (df['Sales'] - df['Sales'].mean()) /
    df['Sales'].std()
)

# Remove Outliers
Q1 = df['Sales'].quantile(0.25)
Q3 = df['Sales'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[
    (df['Sales'] >= lower) &
    (df['Sales'] <= upper)
]

print(df.head())
```

---

# Real-World Applications

## Retail Analytics

- Clean sales transactions
- Detect abnormal purchases
- Prepare data for demand forecasting

---

## Banking

- Remove fraudulent transaction outliers
- Normalize customer spending patterns

---

## Manufacturing

- Detect unusual production metrics
- Standardize machine sensor readings

---

## E-Commerce

- Product sales forecasting
- Customer behavior modeling

---

# Key Takeaways

✅ Inspect data before analysis

✅ Handle missing values using:
- Forward Fill
- Backward Fill
- Mean/Median Imputation

✅ Create business metrics such as Profit Margin

✅ Normalize data using Min-Max Scaling

✅ Standardize data using Z-Score Scaling

✅ Detect outliers using IQR

✅ Remove or cap outliers before modeling

✅ Data preprocessing is one of the most important steps in Machine Learning and Data Analytics

---
# Practice Exercises

### Beginner

1. Count missing values in each column.
2. Fill missing Cost values using mean.
3. Create a Cost Margin column.

### Intermediate

4. Normalize Cost and Profit columns.
5. Detect outliers in Profit.
6. Compare mean sales before and after outlier removal.

### Advanced

7. Create a reusable preprocessing function.
8. Apply preprocessing to multiple datasets.
9. Visualize outliers using boxplots.
10. Build a machine learning-ready dataset using all preprocessing techniques.

---
