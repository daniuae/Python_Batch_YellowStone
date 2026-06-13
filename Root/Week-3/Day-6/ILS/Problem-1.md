# IoT Sensor Data Analysis with Missing Value Interpolation (NumPy)

## Objective

Analyze IoT sensor data containing missing values, interpolate the missing data, and ensure the dataset is ready for analysis.

---

# Case Study

A company collects temperature data from IoT sensors deployed in **3 cities** over **30 days**. Due to connectivity issues, some sensor readings are missing.

### Goals

* Identify missing values in the dataset
* Fill missing values using interpolation
* Analyze the quality of interpolated data
* Visualize original vs interpolated datasets
* Prepare data for further analysis

---

# Step 1: Import Required Libraries

```python
import numpy as np
import matplotlib.pyplot as plt
```

### Explanation

| Library    | Purpose                                            |
| ---------- | -------------------------------------------------- |
| NumPy      | Numerical computations and handling missing values |
| Matplotlib | Data visualization                                 |

---

# Step 2: Generate Synthetic Sensor Data

Simulate temperature readings for 3 cities over 30 days and introduce random missing values.

```python
import numpy as np

np.random.seed(42)

# Generate temperature data
data = np.random.uniform(
    20,
    35,
    size=(30, 3)
)

# Introduce random missing values
missing_indices = np.random.choice(
    data.size,
    size=10,
    replace=False
)

data.flat[missing_indices] = np.nan

cities = ["City_A", "City_B", "City_C"]

print("Sensor Data (First 5 Days):")
print(data[:5])
```

### Sample Output

```text
Sensor Data (First 5 Days):

[[22.49080238 29.01428613 27.63641041]
 [23.09197052 23.90514442         nan]
 [27.31993942 32.92144649 30.84351718]
 [30.21211215         nan 23.41722170]
 [        nan 22.78987721 30.31072260]]
```

### Dataset Snapshot

| Day | City_A | City_B | City_C |
| --- | ------ | ------ | ------ |
| 1   | 22.49  | 29.01  | 27.64  |
| 2   | 23.09  | 23.91  | NaN    |
| 3   | 27.32  | 32.92  | 30.84  |
| 4   | 30.21  | NaN    | 23.42  |
| 5   | NaN    | 22.79  | 30.31  |

**NaN** indicates a missing sensor reading.

---

# Step 3: Identify Missing Values

Use `np.isnan()` to count missing values for each city.

```python
missing_counts = np.sum(
    np.isnan(data),
    axis=0
)

for i, city in enumerate(cities):
    print(
        f"Missing values in {city}: "
        f"{missing_counts[i]}"
    )
```

### Sample Output

```text
Missing values in City_A: 3
Missing values in City_B: 4
Missing values in City_C: 3
```

---

## How It Works

### Detect Missing Values

```python
arr = np.array([10, np.nan, 20])

print(np.isnan(arr))
```

Output:

```text
[False True False]
```

### Count Missing Values

```python
np.sum(np.isnan(arr))
```

Output:

```text
1
```

---

# Step 4: Fill Missing Values Using Linear Interpolation

## What is Interpolation?

Interpolation estimates missing values using nearby valid observations.

### Example

| Day | Temperature |
| --- | ----------- |
| 1   | 20          |
| 2   | NaN         |
| 3   | 30          |

Interpolated value:

```text
Day 2 = 25
```

---

## Linear Interpolation Formula

[
y = y_1 + \frac{(x-x_1)}{(x_2-x_1)}(y_2-y_1)
]

Where:

* (x_1, y_1) = Previous valid point
* (x_2, y_2) = Next valid point
* (x, y) = Missing point

---

## Implementation

```python
data_filled = data.copy()

for col in range(data.shape[1]):

    # Row indices
    indices = np.arange(len(data))

    # Valid observations
    valid_indices = ~np.isnan(data[:, col])

    # Linear interpolation
    data_filled[:, col] = np.interp(
        indices,
        indices[valid_indices],
        data[valid_indices, col]
    )

print("Data After Linear Interpolation:")
print(data_filled[:5])
```

### Sample Output

```text
Data After Linear Interpolation:

[[22.49080238 29.01428613 27.63641041]
 [23.09197052 23.90514442 29.23996379]
 [27.31993942 32.92144649 30.84351718]
 [30.21211215 27.85566185 23.41722170]
 [26.77063372 22.78987721 30.31072260]]
```

---

## Explanation of the Logic

### Create a Copy

```python
data_filled = data.copy()
```

Preserves the original dataset.

### Generate Row Positions

```python
indices = np.arange(len(data))
```

Output:

```text
[0, 1, 2, ..., 29]
```

### Find Valid Data Points

```python
valid_indices = ~np.isnan(data[:, col])
```

Example:

```text
[True, True, True, False, True]
```

### Apply Interpolation

```python
np.interp(
    indices,
    indices[valid_indices],
    data[valid_indices, col]
)
```

Example:

Before:

```text
[22, 25, NaN, 31, 34]
```

After:

```text
[22, 25, 28, 31, 34]
```

---

# Step 5: Verify Missing Values Are Removed

```python
remaining_missing = np.sum(
    np.isnan(data_filled)
)

print(
    "Remaining Missing Values:",
    remaining_missing
)
```

### Output

```text
Remaining Missing Values: 0
```

---

# Step 6: Analyze Interpolated Values

```python
for city_idx, city in enumerate(cities):

    print(f"\n{city}")

    original_missing = np.where(
        np.isnan(data[:, city_idx])
    )[0]

    for idx in original_missing:

        print(
            f"Day {idx+1}: "
            f"Interpolated Value = "
            f"{data_filled[idx, city_idx]:.2f}"
        )
```

### Sample Output

```text
City_A
Day 5: Interpolated Value = 26.77

City_B
Day 4: Interpolated Value = 27.86

City_C
Day 2: Interpolated Value = 29.24
```

---

# Step 7: Visualize Original vs Interpolated Data

```python
plt.figure(figsize=(12,6))

for i, city in enumerate(cities):

    plt.subplot(1,3,i+1)

    plt.plot(
        data_filled[:, i],
        marker='o',
        label='Interpolated'
    )

    plt.scatter(
        np.where(np.isnan(data[:, i]))[0],
        data_filled[np.isnan(data[:, i]), i],
        s=100,
        label='Filled Values'
    )

    plt.title(city)
    plt.xlabel("Day")
    plt.ylabel("Temperature (°C)")
    plt.legend()

plt.tight_layout()
plt.show()
```

---

# Visualization Interpretation

### Line Plot

Displays continuous temperature trends after interpolation.

### Highlighted Points

Represent values that were originally missing and subsequently estimated.

### Benefits

* Detect unusual interpolations
* Verify continuity in sensor readings
* Ensure no unrealistic spikes or drops

---

# Real-World Applications

## Smart Cities

Recover missing weather sensor readings.

## Agriculture

Estimate missing soil temperature values.

## Manufacturing

Repair missing machine telemetry data.

## Energy Sector

Fill gaps in smart meter readings.

## Environmental Monitoring

Handle missing pollution sensor measurements.

---

# NumPy Concepts Used

| Concept         | Purpose                      |
| --------------- | ---------------------------- |
| `np.nan`        | Represent missing values     |
| `np.isnan()`    | Detect missing values        |
| `np.sum()`      | Count missing values         |
| `np.where()`    | Locate missing values        |
| `np.interp()`   | Perform linear interpolation |
| `np.arange()`   | Generate index positions     |
| Boolean Masking | Select valid observations    |

---

# Summary

✅ Generated IoT temperature sensor data

✅ Introduced random missing values

✅ Identified missing data using `np.isnan()`

✅ Filled missing values using `np.interp()`

✅ Verified all missing values were removed

✅ Analyzed interpolated values

✅ Visualized repaired sensor data

✅ Prepared the dataset for analytics and machine learning

---

# Expected Learning Outcomes

After completing this exercise, you will be able to:

1. Detect missing values in NumPy arrays.
2. Count and locate missing observations.
3. Apply linear interpolation using `np.interp()`.
4. Validate data quality after interpolation.
5. Visualize repaired sensor datasets.
6. Handle real-world IoT and time-series data effectively.
