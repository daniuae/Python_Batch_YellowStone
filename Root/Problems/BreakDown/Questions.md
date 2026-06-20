# Python Assessment Master Cheat Sheet
## NumPy + Pandas + OOP (Learnlytica Validation Pattern Guide)

---

# 1. Assessment Question Pattern Recognition

Most validation questions fall into one of the following categories:

| Category | Examples |
|-----------|-----------|
| NumPy Array Processing | Employee Performance, Instagram Reels |
| Pandas Data Processing | Flight Delay, EV Charging |
| OOP + Dictionary | Inventory Management, Chess Tournament |
| Validation | Score Validation, Session Validation |
| Aggregation | Sum, Mean, Max |
| Categorization | Grades, Trend Labels |
| Filtering | Delay > Threshold |
| Formatting | Comma Formatting, Grade Conversion |
| GroupBy Analysis | Revenue, Average Delay |
| Merge Operations | Flight Log + Airline Master |

---

# 2. Freshers Approach to Solve Any Question

## Step 1: Identify Question Type

Ask yourself:

```text
Is it NumPy?
Is it Pandas?
Is it OOP?
Is it Dictionary Based?
```

---

## Step 2: Identify Keywords

| Keyword | Meaning |
|----------|----------|
| Create | DataFrame / Array Creation |
| Validate | Check Conditions |
| Summary | Sum / Mean / Max |
| Categorize | if-elif-else |
| Merge | pd.merge() |
| Average | groupby().mean() |
| Revenue | groupby().sum() |
| Top | max() + filtering |
| Available | Loop + condition |
| Qualified | Loop + append |

---

## Step 3: Follow the Pattern

```text
Create
Validate
Process
Aggregate
Filter
Return
```

---

# 3. NumPy Cheat Sheet

---

# Array Creation

## Pattern

```python
np.array(data, dtype=int)
```

## Example

```python
arr = np.array([10, 20, 30], dtype=int)
```

---

# Validation Patterns

## Check Empty Array

```python
if arr.size == 0:
    return False
```

---

## Check Numeric Type

```python
np.issubdtype(arr.dtype, np.number)
```

---

## Check All Positive

```python
np.all(arr >= 0)
```

---

## Check Any Invalid Values

```python
np.any(arr < 0)
np.any(arr > 100)
```

### Example

```python
if np.any(arr < 0) or np.any(arr > 100):
    return False
```

---

# Aggregation Functions

## Sum

```python
np.sum(arr)
```

## Average

```python
np.mean(arr)
```

## Maximum

```python
np.max(arr)
```

## Minimum

```python
np.min(arr)
```

## Count

```python
arr.size
```

---

# Rounding

```python
round(value, 1)
```

or

```python
np.round(arr, 1)
```

---

# Conditional Update

## Apply Bonus

```python
mask = arr > 85

arr[mask] = arr[mask] * 1.05
```

---

## Clip Values

```python
np.clip(arr, 0, 100)
```

---

# Categorization Pattern

## Method 1: np.select()

```python
conditions = [
    arr >= 90,
    arr >= 80,
    arr < 80
]

choices = [
    "Excellent",
    "Good",
    "Needs Improvement"
]

result = np.select(conditions, choices)
```

---

## Method 2: For Loop

```python
labels = []

for score in arr:

    if score >= 90:
        labels.append("Excellent")

    elif score >= 80:
        labels.append("Good")

    else:
        labels.append("Needs Improvement")
```

---

# Formatting Numbers

## Comma Formatting

```python
formatted = [
    f"{x:,}"
    for x in arr
]
```

### Output

```text
5200

↓

5,200
```

---

# Longest Growth Streak Pattern

```python
max_streak = 1
current_streak = 1

for i in range(1, len(arr)):

    if arr[i] > arr[i-1]:

        current_streak += 1

        if current_streak > max_streak:
            max_streak = current_streak

    else:
        current_streak = 1

return max_streak
```

---

# 4. Employee Performance Analyzer Cheat Sheet

---

## Validation

```python
if performance_array.size == 0:
    return False

if np.any(performance_array < 0):
    return False

if np.any(performance_array > 100):
    return False
```

---

## Summary

```python
total = np.sum(arr)

average = round(np.mean(arr), 1)

maximum = np.max(arr)
```

---

## Bonus

```python
arr = arr.astype(float)

mask = arr > 85

arr[mask] = arr[mask] * 1.05

arr = np.clip(arr, 0, 100)

arr = np.round(arr, 1)
```

---

## Grades

```python
>=90 → Excellent

80-89 → Good

<80 → Needs Improvement
```

---

# 5. Instagram Reel Analyzer Cheat Sheet

---

## Validation

```python
if views_array.size == 0:
    return False

if not np.issubdtype(views_array.dtype, np.number):
    return False

if np.any(views_array < 0):
    return False
```

---

## Trend Levels

```python
Views < 3000
    Low Trend

3000 <= Views < 5000
    Moderate Trend

Views >= 5000
    Viral Trend
```

---

## Metrics

```python
total = int(np.sum(arr))

average = round(np.mean(arr), 2)

maximum = int(np.max(arr))
```

---

# 6. Pandas Cheat Sheet

---

# DataFrame Creation

```python
df = pd.DataFrame(
    data,
    columns=[
        ...
    ]
)
```

---

# Merge

```python
pd.merge(
    left_df,
    right_df,
    on="ColumnName",
    how="left"
)
```

---

# GroupBy Mean

```python
df.groupby(
    "Column"
)["Value"].mean()
```

---

# GroupBy Sum

```python
df.groupby(
    "Column"
)["Value"].sum()
```

---

# GroupBy Count

```python
df.groupby(
    "Column"
)["Value"].count()
```

---

# Multi Aggregation

```python
df.groupby(
    "StationID"
).agg(
{
    "SessionID":"count",
    "EnergyKWh":"sum",
    "DurationMinutes":"mean"
}
)
```

---

# Rename Column

```python
.rename(
columns={
    "Delay":
    "Average Delay"
}
)
```

---

# Reset Index

```python
.reset_index()
```

---

# Reset Index Drop

```python
.reset_index(drop=True)
```

---

# Sorting

```python
.sort_values(
    by="Average Delay",
    ascending=False
)
```

---

# Top Row

```python
.head(1)
```

---

# Filtering

## Greater Than

```python
df[
    df["Delay"] > threshold
]
```

---

## Equal To

```python
df[
    df["Status"] == "Paid"
]
```

---

## Multiple Conditions

```python
df[
    (df["Energy"] > 0)
    &
    (df["Duration"] > 0)
]
```

---

## isin()

```python
df[
    df["Status"].isin(
        ["Paid", "Pending", "Failed"]
    )
]
```

---

# Maximum Row Pattern

```python
max_value = df["Average Delay"].max()

result = df[
    df["Average Delay"] == max_value
]
```

---

# 7. Flight Delay Analyzer Cheat Sheet

---

## Create Flight DataFrame

```python
pd.DataFrame(
    flight_log,
    columns=[
        "FlightID",
        "AirlineCode",
        "Route",
        "Delay"
    ]
)
```

---

## Create Airline DataFrame

```python
pd.DataFrame(
    airline_master,
    columns=[
        "AirlineCode",
        "AirlineName"
    ]
)
```

---

## Merge

```python
pd.merge(
    flight_df,
    airline_df,
    on="AirlineCode",
    how="left"
)
```

---

## Average Delay

```python
merged_df.groupby(
    "AirlineName"
)["Delay"].mean()
```

---

## High Delay

```python
flight_df[
    flight_df["Delay"] > threshold
]
```

---

## Most Delayed Route

```python
groupby()

mean()

max()

filter()

sort_values()

head(1)
```

---

# 8. EV Charging Analyzer Cheat Sheet

---

# Data Cleaning

## Drop Nulls

```python
df.dropna(
    subset=[
        "SessionID",
        "StationID",
        "City",
        "PaymentStatus"
    ]
)
```

---

## Positive Values

```python
df[
    (df["EnergyKWh"] > 0)
    &
    (df["DurationMinutes"] > 0)
]
```

---

## Valid Status

```python
df[
    df["PaymentStatus"].isin(
        ["Paid","Pending","Failed"]
    )
]
```

---

## Long Session Flag

```python
df["IsLongSession"] = (
    df["DurationMinutes"] > threshold
).astype(int)
```

---

## Revenue

```python
df["Revenue"] = (
    df["EnergyKWh"] * 18
)
```

---

## City Revenue Summary

```python
paid_df = df[
    df["PaymentStatus"] == "Paid"
]

paid_df.groupby(
    "City"
)["Revenue"].sum()
```

---

# 9. OOP + Dictionary Cheat Sheet

---

# Constructor

```python
def __init__(self):

    self.data = {}
```

---

# Add Pattern

```python
if key in self.data:

    raise ValueError()

self.data[key] = value
```

---

# Update Pattern

```python
if key not in self.data:

    raise KeyError()

self.data[key] = value
```

---

# Get Pattern

```python
if key not in self.data:

    raise KeyError()

return self.data[key]
```

---

# List Pattern

```python
result = []

for key, value in self.data.items():

    if condition:

        result.append(key)

return result
```

---

# 10. Inventory Management System Cheat Sheet

---

## Add Item

```python
if item_name in inventory:

    inventory[item_name] += quantity

else:

    inventory[item_name] = quantity
```

---

## Update Stock

```python
if item_name not in inventory:

    raise KeyError("Not found")

inventory[item_name] = new_quantity
```

---

## Get Stock

```python
if item_name not in inventory:

    raise KeyError("Not found")

return inventory[item_name]
```

---

## Available Items

```python
result = []

for item, stock in inventory.items():

    if stock > 0:

        result.append(item)
```

---

# 11. Chess Tournament System Cheat Sheet

---

## Add Player

```python
if player_id in players:

    raise ValueError(
        "Player already exists"
    )
```

---

## Store Player

```python
players[player_id] = {
    "name": name,
    "rating": rating,
    "status": "Active"
}
```

---

## Update Rating

```python
if player_id not in players:

    raise KeyError(
        "Player not found"
    )

players[player_id]["rating"] = new_rating
```

---

## Qualified Players

```python
result = []

for player_id, details in players.items():

    if details["rating"] >= minimum_rating:

        result.append(player_id)

return result
```

---

# 12. Most Important Functions To Memorize

## NumPy

```python
np.array()
np.sum()
np.mean()
np.max()
np.min()
np.any()
np.all()
np.round()
np.clip()
np.select()
```

---

## Pandas

```python
pd.DataFrame()
pd.merge()

groupby()

mean()
sum()
count()

rename()

sort_values()

reset_index()

head()
```

---

## Dictionary

```python
in
not in

.items()

.keys()

.values()
```

---

# Final Exam Strategy

## NumPy Questions

```text
Create
Validate
Aggregate
Categorize
Format
```

---

## Pandas Questions

```text
Create DataFrame
Clean Data
Merge
GroupBy
Filter
Sort
Return
```

---

## OOP Questions

```text
Add
Update
Get
List
```

---

## Golden Rule

If you know:

1. np.array()
2. np.any()
3. np.all()
4. pd.DataFrame()
5. pd.merge()
6. groupby().mean()
7. groupby().sum()
8. sort_values()
9. reset_index()
10. Dictionary operations

You can solve approximately **80-90% of Learnlytica NumPy, Pandas, and OOP validation questions**.
