# Case Study: Temperature Conversion Utility

## Objective

Design a `Temperature` class that demonstrates the use of:

* Instance Methods
* Class Methods (`@classmethod`)
* Static Methods (`@staticmethod`)
* Class Variables
* Input Validation
* Exception Handling
* String Representation (`__str__`)

This case study simulates a real-world temperature conversion utility.

---

# Learning Outcomes

By completing this case study, you will learn:

✅ Class Methods

✅ Static Methods

✅ Class Variables

✅ Object Creation Using Alternative Constructors

✅ Temperature Conversion Formulas

✅ Input Validation

✅ Exception Handling

✅ String Representation

✅ Object-Oriented Programming (OOP)

---

# Step 1: Create a New Python File

Create a file named:

```text
temperature_conversion.py
```

---

# Step 2: Define the Temperature Class

Start by creating the class.

```python
class Temperature:

    def __init__(self, celsius):
        self.celsius = celsius
```

---

## Explanation

The constructor initializes the temperature value in Celsius.

### Example

```python
temp = Temperature(25)
```

The object stores:

```text
25°C
```

---

# Step 3: Add a Method to Convert Celsius to Fahrenheit

Add an instance method.

```python
def to_fahrenheit(self):
    return (self.celsius * 9/5) + 32
```

---

## Formula Used

### Celsius to Fahrenheit

```text
F = (C × 9/5) + 32
```

### Example

```python
temp = Temperature(100)

print(temp.to_fahrenheit())
```

### Output

```text
212.0
```

---

# Step 4: Add a Class Method

Use `@classmethod` to create a Temperature object from Fahrenheit.

```python
@classmethod
def from_fahrenheit(cls, fahrenheit):

    celsius = (fahrenheit - 32) * 5/9

    return cls(celsius)
```

---

## Formula Used

### Fahrenheit to Celsius

```text
C = (F - 32) × 5/9
```

---

## Why Use a Class Method?

A class method acts as an alternative constructor.

Instead of:

```python
temp = Temperature(37)
```

You can create an object from Fahrenheit:

```python
temp = Temperature.from_fahrenheit(98.6)
```

---

# Step 5: Test the Class Method

```python
temp = Temperature.from_fahrenheit(98.6)

print(
    f"Temperature in Celsius: "
    f"{temp.celsius:.2f}"
)
```

### Output

```text
Temperature in Celsius: 37.00
```

---

# Step 6: Run the Script

Execute:

```bash
python temperature_conversion.py
```

---

# Step 7: Add a Static Method for Validation

Static methods belong to the class but do not require access to instance data.

```python
@staticmethod
def is_valid_temperature(value):

    return -273.15 <= value
```

---

## Why -273.15?

```text
-273.15°C
```

is known as:

### Absolute Zero

The lowest theoretically possible temperature.

No temperature can exist below this value.

---

# Step 8: Test the Static Method

```python
print(
    Temperature.is_valid_temperature(-300)
)

print(
    Temperature.is_valid_temperature(25)
)
```

### Output

```text
False
True
```

---

# Step 9: Add Temperature Validation

Prevent invalid temperatures during object creation.

```python
def __init__(self, celsius):

    if not Temperature.is_valid_temperature(celsius):

        raise ValueError(
            "Temperature cannot be below absolute zero!"
        )

    self.celsius = celsius
```

---

## Explanation

Before storing the temperature:

1. Validate the value.
2. Raise an exception if invalid.

---

# Step 10: Handle Invalid Input

```python
try:

    invalid_temp = Temperature(-300)

except ValueError as e:

    print(e)
```

### Output

```text
Temperature cannot be below absolute zero!
```

---

# Step 11: Add String Representation

Implement the `__str__()` method.

```python
def __str__(self):

    return (
        f"{self.celsius:.2f}°C / "
        f"{self.to_fahrenheit():.2f}°F"
    )
```

---

## Why Use `__str__()`?

Without `__str__()`:

```python
print(temp)
```

Output:

```text
<__main__.Temperature object at 0x123456>
```

With `__str__()`:

```text
37.00°C / 98.60°F
```

Much more user-friendly.

---

# Step 12: Test String Representation

```python
print(temp)
```

### Output

```text
37.00°C / 98.60°F
```

---

# Step 13: Test Multiple Scenarios

```python
temp1 = Temperature(0)

temp2 = Temperature.from_fahrenheit(212)

print(temp1)

print(temp2)
```

### Output

```text
0.00°C / 32.00°F
100.00°C / 212.00°F
```

---

# Step 14: Add a Class Variable

Store Absolute Zero as a class-level constant.

```python
absolute_zero = -273.15
```

---

## Why Use a Class Variable?

Instead of repeating:

```python
-273.15
```

throughout the code, define it once.

### Benefits

* Easier maintenance
* Better readability
* Centralized configuration

---

# Step 15: Update Validation Logic

Use the class variable.

```python
@staticmethod
def is_valid_temperature(value):

    return (
        value >= Temperature.absolute_zero
    )
```

---

# Complete Program

```python
class Temperature:

    absolute_zero = -273.15

    def __init__(self, celsius):

        if not Temperature.is_valid_temperature(
            celsius
        ):
            raise ValueError(
                "Temperature cannot be below absolute zero!"
            )

        self.celsius = celsius

    def to_fahrenheit(self):

        return (
            self.celsius * 9/5
        ) + 32

    @classmethod
    def from_fahrenheit(
        cls,
        fahrenheit
    ):

        celsius = (
            fahrenheit - 32
        ) * 5/9

        return cls(celsius)

    @staticmethod
    def is_valid_temperature(value):

        return (
            value >= Temperature.absolute_zero
        )

    def __str__(self):

        return (
            f"{self.celsius:.2f}°C / "
            f"{self.to_fahrenheit():.2f}°F"
        )


def main():

    temp = Temperature.from_fahrenheit(
        98.6
    )

    print(
        f"Temperature in Celsius: "
        f"{temp.celsius:.2f}"
    )

    print(
        Temperature.is_valid_temperature(
            -300
        )
    )

    print(
        Temperature.is_valid_temperature(
            25
        )
    )

    try:

        invalid_temp = Temperature(
            -300
        )

    except ValueError as e:

        print(e)

    print(temp)

    temp1 = Temperature(0)

    temp2 = Temperature.from_fahrenheit(
        212
    )

    print(temp1)

    print(temp2)


if __name__ == "__main__":
    main()
```

---

# Sample Output

```text
Temperature in Celsius: 37.00

False

True

Temperature cannot be below absolute zero!

37.00°C / 98.60°F

0.00°C / 32.00°F

100.00°C / 212.00°F
```

---

# Real-World Applications

## Weather Monitoring Systems

```python
current_temp = Temperature(32)

print(current_temp)
```

---

## HVAC Systems

Heating and cooling systems continuously convert temperatures between units.

---

## Scientific Research

Scientists frequently work with:

* Celsius
* Fahrenheit
* Kelvin

and require validation against physical limits.

---

## IoT Temperature Sensors

Smart sensors often send temperature values that need validation before processing.

---

# Key Concepts Learned

| Concept                 | Implemented |
| ----------------------- | ----------- |
| Constructor             | ✅           |
| Instance Method         | ✅           |
| Class Method            | ✅           |
| Static Method           | ✅           |
| Class Variable          | ✅           |
| Validation              | ✅           |
| Exception Handling      | ✅           |
| String Representation   | ✅           |
| Temperature Conversion  | ✅           |
| Alternative Constructor | ✅           |

---

# Interview Questions

### 1. What is a Class Method?

A method decorated with `@classmethod` that receives the class (`cls`) as its first argument.

### 2. What is a Static Method?

A method decorated with `@staticmethod` that does not require `self` or `cls`.

### 3. When should you use a Class Method?

When creating alternative constructors.

Example:

```python
Temperature.from_fahrenheit(98.6)
```

### 4. When should you use a Static Method?

For utility functions related to the class but not dependent on object state.

Example:

```python
Temperature.is_valid_temperature(25)
```

### 5. What is a Class Variable?

A variable shared by all instances of a class.

Example:

```python
absolute_zero = -273.15
```

---

# Challenge Exercises

### Exercise 1

Add Kelvin conversion support.

### Exercise 2

Create a class method:

```python
from_kelvin()
```

### Exercise 3

Add a method to compare two temperatures.

### Exercise 4

Track the number of Temperature objects created using a class variable.

### Exercise 5

Create a WeatherStation class that stores multiple Temperature objects and calculates average temperature.

---

# Summary

This case study demonstrated how to build a robust Temperature Conversion Utility using:

* Constructors
* Class Methods
* Static Methods
* Class Variables
* Validation Rules
* Exception Handling
* String Representation

These techniques are widely used in production-quality Python applications and are common topics in Python interviews.
