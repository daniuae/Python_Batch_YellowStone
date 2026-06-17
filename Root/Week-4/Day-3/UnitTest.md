# Python Testing: `unittest` vs `pytest`

## Table of Contents

1. Introduction
2. What is Unit Testing?
3. `unittest` Overview
4. `pytest` Overview
5. Basic Examples
6. Assertions Comparison
7. Fixtures
8. Parameterized Tests
9. Mocking
10. Test Discovery
11. Comparison Table
12. When to Use Which?
13. Project Structure Example

---

# 1. Introduction

Testing ensures your code behaves correctly and helps prevent bugs when changes are made.

Python provides:

* **unittest** → Built into Python standard library
* **pytest** → Third-party testing framework with richer features

Both can test the same code, but their style differs significantly.

---

# 2. What is Unit Testing?

A **unit test** verifies a small piece of functionality (a unit) in isolation.

Example:

```python
def add(a, b):
    return a + b
```

Unit test:

```python
assert add(2, 3) == 5
```

### Illustration

```text
+-------------+
| Function    |
| add(2, 3)   |
+-------------+
       |
       v
+-------------+
| Result = 5  |
+-------------+
       |
       v
+-------------+
| Test Pass?  |
+-------------+
```

---

# 3. unittest Overview

`unittest` is Python's built-in testing framework inspired by Java's JUnit.

### Features

* Built into Python
* Class-based tests
* Rich assertion methods
* Setup and teardown support
* Mocking support

Import:

```python
import unittest
```

---

# 4. pytest Overview

`pytest` is a popular third-party framework.

Install:

```bash
pip install pytest
```

### Features

* Simple syntax
* Better error messages
* Fixtures
* Parameterization
* Plugin ecosystem
* Less boilerplate

Import usually not required:

```python
# no import needed for basic tests
```

---

# 5. Basic Example

Suppose we have:

```python
# calculator.py

def add(a, b):
    return a + b
```

---

## unittest Version

```python
# test_calculator.py

import unittest
from calculator import add

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
```

Run:

```bash
python test_calculator.py
```

Output:

```text
.
----------------------------------------------------------------------
Ran 1 test

OK
```

---

## pytest Version

```python
# test_calculator.py

from calculator import add

def test_add():
    assert add(2, 3) == 5
```

Run:

```bash
pytest
```

Output:

```text
1 passed
```

---

## Illustration

### unittest

```text
TestCase Class
      |
      v
test_add()
      |
      v
assertEqual()
```

### pytest

```text
test_add()
      |
      v
assert
```

Less code, same result.

---

# 6. Assertions Comparison

## unittest Assertions

```python
self.assertEqual(a, b)

self.assertTrue(x)

self.assertFalse(x)

self.assertIn(item, collection)

self.assertIsNone(value)

self.assertRaises(ValueError)
```

Example:

```python
self.assertEqual(10, 10)
```

---

## pytest Assertions

```python
assert a == b

assert x

assert item in collection

assert value is None
```

Example:

```python
assert 10 == 10
```

---

## Failure Message Comparison

Code:

```python
assert 10 == 20
```

Pytest output:

```text
> assert 10 == 20
E assert 10 == 20
```

Pytest automatically shows compared values.

---

# 7. Setup and Teardown

Often tests need preparation.

Example:

```python
class Database:
    pass
```

---

## unittest

```python
import unittest

class TestDatabase(unittest.TestCase):

    def setUp(self):
        print("Connect DB")

    def tearDown(self):
        print("Disconnect DB")

    def test_query(self):
        self.assertTrue(True)
```

Execution flow:

```text
setUp()
   |
test_query()
   |
tearDown()
```

---

## pytest Fixture

```python
import pytest

@pytest.fixture
def database():
    print("Connect DB")

    yield

    print("Disconnect DB")

def test_query(database):
    assert True
```

Flow:

```text
fixture setup
      |
      v
test
      |
      v
fixture cleanup
```

---

# 8. Parameterized Tests

Testing multiple inputs.

Function:

```python
def square(x):
    return x * x
```

---

## unittest

```python
import unittest

class TestSquare(unittest.TestCase):

    def test_square(self):
        cases = [
            (2, 4),
            (3, 9),
            (4, 16)
        ]

        for x, expected in cases:
            self.assertEqual(square(x), expected)
```

---

## pytest

```python
import pytest

@pytest.mark.parametrize(
    "value,expected",
    [
        (2, 4),
        (3, 9),
        (4, 16)
    ]
)
def test_square(value, expected):
    assert square(value) == expected
```

Pytest reports each case separately.

Illustration:

```text
Input 2 ---> Test ---> Pass
Input 3 ---> Test ---> Pass
Input 4 ---> Test ---> Pass
```

---

# 9. Mocking

Mocking replaces external dependencies.

Example dependency:

```python
def get_user_from_db():
    pass
```

---

## unittest.mock

```python
from unittest.mock import patch

@patch("app.get_user_from_db")
def test_user(mock_db):
    mock_db.return_value = "John"

    result = get_user()

    assert result == "John"
```

---

## pytest + mock

Using pytest-mock plugin:

```python
def test_user(mocker):
    mocker.patch(
        "app.get_user_from_db",
        return_value="John"
    )

    assert get_user() == "John"
```

---

# 10. Test Discovery

Test discovery = automatically finding tests.

---

## unittest

Discover tests:

```bash
python -m unittest discover
```

Files:

```text
test_math.py
test_user.py
```

---

## pytest

```bash
pytest
```

Automatically finds:

```text
test_*.py
*_test.py
```

Example:

```text
tests/
├── test_math.py
├── test_user.py
└── test_api.py
```

---

# 11. Comparison Table

| Feature             | unittest    | pytest          |
| ------------------- | ----------- | --------------- |
| Built into Python   | ✅           | ❌               |
| Installation needed | ❌           | ✅               |
| Simple syntax       | ❌           | ✅               |
| Rich assertions     | ⚠️          | ✅               |
| Fixtures            | Basic       | Powerful        |
| Parameterization    | Manual      | Built-in        |
| Plugins             | Limited     | Extensive       |
| Mocking             | Built-in    | Plugin-friendly |
| Learning curve      | Medium      | Easy            |
| Enterprise usage    | Very common | Very common     |

---

# 12. When to Use Which?

## Use unittest When

* No external dependencies allowed
* Corporate standards require standard library tools
* Existing project already uses unittest
* You need built-in mocking support

Example:

```text
Large Legacy Project
        |
        v
     unittest
```

---

## Use pytest When

* Starting a new project
* Want concise tests
* Need fixtures
* Need parameterized tests
* Need advanced plugins

Example:

```text
New Project
     |
     v
   pytest
```

---

# 13. Real-World Project Structure

## unittest Style

```text
project/
│
├── app/
│   └── calculator.py
│
└── tests/
    └── test_calculator.py
```

Run:

```bash
python -m unittest discover
```

---

## pytest Style

```text
project/
│
├── app/
│   └── calculator.py
│
├── tests/
│   ├── test_calculator.py
│   ├── test_user.py
│   └── conftest.py
│
└── pytest.ini
```

Run:

```bash
pytest
```

---

# Summary

```text
                    Python Testing
                           |
            +--------------+--------------+
            |                             |
            v                             v
       unittest                      pytest
            |                             |
   Built-in framework          Third-party framework
            |                             |
      More boilerplate          Less boilerplate
            |                             |
       Class-based              Function-based
            |                             |
      Good for legacy           Preferred for new projects
```

### Quick Rule

* **Learning testing concepts** → Start with `unittest`
* **Building modern Python projects** → Prefer `pytest`
* **Working in existing enterprise codebases** → Use whatever framework the project already uses
* **Starting from scratch today** → `pytest` is usually the most productive choice
