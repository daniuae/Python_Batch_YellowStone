# Weather Case Study

## Section 1: Introduction

Conditional statements allow Python programs to make decisions.

### Important Points

- `if` → checks the first condition
- `elif` → checks additional conditions
- `else` → runs when none of the previous conditions are true

In this lab, we will understand `if` and `elif` using a real-life weather-based case study.

---

# Section 2: Basic if Statement

An `if` statement runs only when its condition is true.

### Example

```python
temperature = 32

if temperature > 30:
    print("It is a hot day!")
```

### Sample Output

```text
It is a hot day!
```

### Explanation

The condition `temperature > 30` is true, so the message is printed.

---

# Section 3: if–elif for Multiple Conditions

We can use `elif` to check additional conditions.

### Example

```python
temperature = 18

if temperature > 30:
    print("It is a hot day.")
elif temperature > 20:
    print("It is a warm day.")
else:
    print("It is a cool day.")
```

### Sample Output

```text
It is a cool day.
```

### Explanation

- `18` is not greater than `30`
- `18` is not greater than `20`
- Therefore, the `else` block executes

---

# Section 4: Weather Case Study – Clothing Recommendation System

In this case study, we will write a program that recommends clothing based on the weather temperature entered by the user.

### Example

```python
temp = int(input("Enter today's temperature: "))

if temp >= 35:
    print("Recommendation: Wear light cotton clothes.")
elif temp >= 25:
    print("Recommendation: Wear a t-shirt and jeans.")
elif temp >= 15:
    print("Recommendation: Wear a light jacket.")
else:
    print("Recommendation: Wear warm clothes.")
```

### Sample Output

```text
Enter today's temperature: 12
Recommendation: Wear warm clothes.
```

### Explanation

Since `12` is less than `15`, the program suggests wearing warm clothes.

---

# Section 5: Weather Case Study – Safety Advice Based on Conditions

Another part of the weather-based decision system provides advice based on the probability of rain.

### Example

```python
chance_of_rain = int(input("Enter chance of rain (0–100%): "))

if chance_of_rain >= 80:
    print("Safety Advice: Carry an umbrella and wear waterproof shoes.")
elif chance_of_rain >= 50:
    print("Safety Advice: Carry an umbrella.")
elif chance_of_rain >= 20:
    print("Safety Advice: It might drizzle—stay alert.")
else:
    print("Safety Advice: No rain expected today.")
```

### Sample Output

```text
Enter chance of rain (0–100%): 65
Safety Advice: Carry an umbrella.
```

### Explanation

Since the rain probability is `65%`, it falls into the `50%–79%` category.

---

# Section 6: Weather Case Study – Air Quality Check

We evaluate the Air Quality Index (AQI) and provide health recommendations.

### Example

```python
aqi = int(input("Enter the AQI value: "))

if aqi >= 300:
    print("Air Quality: Hazardous. Stay indoors.")
elif aqi >= 200:
    print("Air Quality: Very Unhealthy.")
elif aqi >= 100:
    print("Air Quality: Unhealthy for sensitive groups.")
else:
    print("Air Quality: Good.")
```

### Sample Output

```text
Enter the AQI value: 110
Air Quality: Unhealthy for sensitive groups.
```

### Explanation

AQI `110` falls in the range `100–199`, so the program displays the corresponding message.

---

# Section 7: Practice Exercise – Student Task

Write a program that:

- Takes rainfall (mm) as input
- Prints:
  - `"Heavy Rainfall"` if rainfall is `>= 50`
  - `"Moderate Rainfall"` if rainfall is `>= 20`
  - `"Light Rainfall"` if rainfall is `>= 5`
  - `"No Rainfall"` otherwise

### Starter Template

```python
rain = int(input("Enter rainfall in mm: "))

# Write your if–elif conditions below:
```

### Sample Solution

```python
rain = int(input("Enter rainfall in mm: "))

if rain >= 50:
    print("Heavy Rainfall")
elif rain >= 20:
    print("Moderate Rainfall")
elif rain >= 5:
    print("Light Rainfall")
else:
    print("No Rainfall")
```

### Sample Output

```text
Enter rainfall in mm: 25
Moderate Rainfall
```

---

# Section 8: Key Takeaways

In this lab, you learned:

- How `if` statements work
- How to use `elif` for multiple conditions
- How the `else` block handles remaining cases
- How to build decision-making programs
- How to apply conditional logic to real-world weather scenarios such as:
  - Temperature-based clothing recommendations
  - Rain probability safety alerts
  - Air quality health checks
  - Rainfall classification systems

---

# Mini Quiz

### 1. Which statement checks the first condition?

**Answer:** `if`

### 2. Which statement checks additional conditions?

**Answer:** `elif`

### 3. Which block executes when no conditions are true?

**Answer:** `else`

### 4. What will the output be?

```python
temp = 28

if temp >= 35:
    print("Hot")
elif temp >= 25:
    print("Warm")
else:
    print("Cool")
```

**Output:**

```text
Warm
```

### 5. What is the purpose of conditional statements?

**Answer:** They help programs make decisions based on conditions.

---

# End of Lab

Congratulations! 🎉

You have successfully learned how to use:

- `if`
- `elif`
- `else`

to create real-world weather-based decision-making applications in Python.
