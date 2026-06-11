# Lab: Iterators, Generators, Decorators + Mini ETL

## Prerequisites

- Python 3.9+
- Terminal
- Code Editor (VS Code recommended)

---

# Goal

Understand:

- Iteration Protocol
- Lazy Data Processing using Generators
- Function Wrapping using Decorators

Then combine them to build a small ETL Pipeline.

---

# Part A — Project Setup (5 min)

## Step 1: Create Project Folder

```bash
mkdir lab_iter_gen_decor
cd lab_iter_gen_decor

python -V

touch etl_lab.py
```

---

## Step 2: Add Sample CSV Data

```python
SAMPLE_CSV = """id,name,amount,ts
1,Alice,120.5,2025-09-01
2,Bob, ,2025-09-02
3,Carol,99.0,2025-09-03
4,Dan,1000000.0,2025-09-04
5,Eve,17.25,2025-09-05
"""
```

---

## Step 3: Add Runner Guard

```python
if __name__ == "__main__":
    print("Lab runner: start")
```

---

# Part B — Custom Iterator Class (10 min)

## What is an Iterator?

An iterator is an object that:

- Remembers its position
- Returns one item at a time
- Raises `StopIteration` when finished

---

## Step 4: Create Custom Iterator

```python
class LineIterator:

    def __init__(self, data: str, skip_header: bool = True):
        self.lines = data.splitlines()
        self.index = 0
        self.skip_header = skip_header

        if self.skip_header and self.lines:
            self.index = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.index >= len(self.lines):
            raise StopIteration

        line = self.lines[self.index]
        self.index += 1

        return line
```

---

## Step 5: Test Iterator

```python
if __name__ == "__main__":

    it = LineIterator(SAMPLE_CSV, skip_header=True)

    print("Iterator test (first two lines):")

    print(next(it))
    print(next(it))
```

---

## Expected Output

```text
Iterator test (first two lines):

1,Alice,120.5,2025-09-01
2,Bob, ,2025-09-02
```

---

## Step 6: Demonstrate StopIteration

```python
if __name__ == "__main__":

    it2 = LineIterator("a\nb\nc", skip_header=False)

    try:
        while True:
            print("it2:", next(it2))

    except StopIteration:
        print("Reached end (StopIteration)")
```

---

## Output

```text
it2: a
it2: b
it2: c
Reached end (StopIteration)
```

---

# Part C — Generator Functions (10 min)

## What is a Generator?

A generator:

- Produces values lazily
- Uses `yield`
- Saves memory
- Ideal for ETL pipelines

---

## Step 8: CSV Parser Generator

```python
def parse_csv_lines(lines):

    for line in lines:

        parts = [p.strip() for p in line.split(",")]

        if len(parts) != 4:
            continue

        row = {
            "id": parts[0],
            "name": parts[1],
            "amount": parts[2],
            "ts": parts[3]
        }

        yield row
```

---

## Step 9: Transform Generator

Requirements:

- Convert ID to integer
- Convert amount to float
- Empty amount → 0.0
- Filter suspicious values (>100000)

```python
def transform_rows(rows):

    for r in rows:

        try:
            r["id"] = int(r["id"])

            r["amount"] = (
                float(r["amount"])
                if r["amount"]
                else 0.0
            )

        except ValueError:
            continue

        if r["amount"] > 100000:
            continue

        yield r
```

---

## Step 10: Test Generators

```python
if __name__ == "__main__":

    print("\nGenerator test:")

    raw_iter = LineIterator(
        SAMPLE_CSV,
        skip_header=True
    )

    for cleaned in transform_rows(
            parse_csv_lines(raw_iter)):
        print(cleaned)
```

---

## Expected Output

```python
{'id': 1, 'name': 'Alice', 'amount': 120.5, 'ts': '2025-09-01'}
{'id': 2, 'name': 'Bob', 'amount': 0.0, 'ts': '2025-09-02'}
{'id': 3, 'name': 'Carol', 'amount': 99.0, 'ts': '2025-09-03'}
{'id': 5, 'name': 'Eve', 'amount': 17.25, 'ts': '2025-09-05'}
```

Dan is filtered out.

---

# Part D — Decorators for Logging & Timing (10 min)

## What is a Decorator?

A decorator adds behavior to a function without changing the original code.

Examples:

- Logging
- Timing
- Authentication
- Retry Logic
- Caching

---

## Step 11: Logging Decorator

```python
import functools
import time

def log_call(fn):

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):

        print(
            f"[LOG] calling {fn.__name__} "
            f"args={args} kwargs={kwargs}"
        )

        result = fn(*args, **kwargs)

        print(
            f"[LOG] {fn.__name__} "
            f"returned type={type(result).__name__}"
        )

        return result

    return wrapper
```

---

## Step 12: Timing Decorator

```python
def timed(fn):

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        try:
            return fn(*args, **kwargs)

        finally:
            duration = (
                time.perf_counter() - start
            ) * 1000

            print(
                f"[TIME] {fn.__name__} "
                f"took {duration:.2f} ms"
            )

    return wrapper
```

---

## Step 13: Decorated Function

```python
@timed
@log_call
def enrich_amount(r):

    time.sleep(0.01)

    r = dict(r)

    r["amount_with_tax"] = round(
        r["amount"] * 1.1,
        2
    )

    return r
```

---

## Step 14: Test Decorators

```python
if __name__ == "__main__":

    print("\nDecorator test:")

    row = {
        "id": 10,
        "name": "Test",
        "amount": 100.0,
        "ts": "2025-01-01"
    }

    print(enrich_amount(row))
```

---

## Example Output

```text
[LOG] calling enrich_amount
[LOG] enrich_amount returned type=dict
[TIME] enrich_amount took 10.01 ms

{
 'id':10,
 'name':'Test',
 'amount':100.0,
 'amount_with_tax':110.0
}
```

---

# Part E — Mini ETL Pipeline (20 min)

---

## Step 15: Extract

```python
def extract(source_str: str):
    return LineIterator(
        source_str,
        skip_header=True
    )
```

---

## Step 16: Transform

```python
@timed
def transform(line_iter):

    rows = parse_csv_lines(line_iter)

    cleaned = transform_rows(rows)

    for r in cleaned:
        yield enrich_amount(r)
```

---

## Step 17: Load

```python
@log_call
def load(rows, batch_size=2):

    batch = []

    for r in rows:

        batch.append(r)

        if len(batch) >= batch_size:

            print(
                f"[LOAD] inserting "
                f"batch of {len(batch)} rows"
            )

            batch.clear()

    if batch:

        print(
            f"[LOAD] inserting final "
            f"batch of {len(batch)} rows"
        )
```

---

## Step 18: Wire Pipeline

```python
if __name__ == "__main__":

    print("\nETL pipeline run:")

    src = extract(SAMPLE_CSV)

    tx = transform(src)

    load(tx, batch_size=2)
```

---

# Throughput Counter Decorator

## Step 20

```python
def count_rows(fn):

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):

        count = 0

        for item in fn(*args, **kwargs):

            count += 1

            yield item

        print(
            f"[COUNT] {fn.__name__} "
            f"produced {count} rows"
        )

    return wrapper
```

---

## Step 21

```python
@count_rows
@timed
def transform(line_iter):

    rows = parse_csv_lines(line_iter)

    cleaned = transform_rows(rows)

    for r in cleaned:
        yield enrich_amount(r)
```

---

# Validation Generator

## Step 22

```python
def validate_rows(rows):

    for r in rows:

        if not r["name"]:
            continue

        yield r
```

---

## Step 23

```python
if __name__ == "__main__":

    print(
        "\nETL pipeline "
        "with validation:"
    )

    src = extract(SAMPLE_CSV)

    tx = transform(src)

    validated = validate_rows(tx)

    load(validated, batch_size=3)
```

---

# Filter Generator

## Step 24

```python
def filter_min_amount(
        rows,
        min_amount=10.0):

    for r in rows:

        if r["amount"] >= min_amount:
            yield r
```

---

## Step 25

```python
if __name__ == "__main__":

    print(
        "\nETL pipeline "
        "with min filter:"
    )

    src = extract(SAMPLE_CSV)

    tx = transform(src)

    validated = validate_rows(tx)

    filtered = filter_min_amount(
        validated,
        min_amount=50.0
    )

    load(filtered, batch_size=2)
```

---

# Retry Decorator

## Step 26

```python
def retry_once(fn):

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):

        try:
            return fn(*args, **kwargs)

        except Exception as e:

            print(
                f"[RETRY] "
                f"{fn.__name__} failed: {e}"
            )

            return fn(*args, **kwargs)

    return wrapper
```

---

## Step 27: Flaky Loader

```python
flaky_toggle = {"fail": True}

@retry_once
@log_call
def load_flaky(
        rows,
        batch_size=2):

    batch = []

    for r in rows:

        batch.append(r)

        if len(batch) >= batch_size:

            if flaky_toggle["fail"]:
                flaky_toggle["fail"] = False
                raise RuntimeError(
                    "Simulated insert failure"
                )

            print(
                f"[LOAD] inserted batch "
                f"of {len(batch)} rows"
            )

            batch.clear()
```

---

## Step 28: Run Flaky Pipeline

```python
if __name__ == "__main__":

    print("\nETL with retry:")

    src = extract(SAMPLE_CSV)

    tx = transform(src)

    load_flaky(tx, batch_size=2)
```

---

# Smoke Test

## Step 29

```python
def _smoke():

    src = extract(SAMPLE_CSV)

    tx = list(transform(src))

    assert all(
        "amount_with_tax" in r
        for r in tx
    )

    assert all(
        isinstance(r["id"], int)
        for r in tx
    )

    print("[SMOKE] OK")
```

Run:

```python
if __name__ == "__main__":
    _smoke()
```

---

# Stretch Goal: Large Dataset

## Step 30

```python
BIG = (
    "id,name,amount,ts\n"
    +
    "\n".join(
        f"{i},User{i},{i % 97 + 0.5},2025-10-01"
        for i in range(1, 5000)
    )
)
```

---

## Process Large Data

```python
if __name__ == "__main__":

    print("\nBig run (~5k rows):")

    src = extract(BIG)

    tx = transform(src)

    load(tx, batch_size=500)
```

---

# Architecture Diagram

```text
           SAMPLE_CSV
                │
                ▼
       LineIterator
                │
                ▼
      parse_csv_lines()
                │
                ▼
      transform_rows()
                │
                ▼
      enrich_amount()
       (Decorators)
                │
                ▼
      validate_rows()
                │
                ▼
   filter_min_amount()
                │
                ▼
            load()
```

---

# Key Interview Questions

### 1. Difference between Iterator and Generator?

| Iterator | Generator |
|-----------|-----------|
| Uses __iter__ and __next__ | Uses yield |
| More code | Less code |
| Stateful | Automatically stateful |
| Custom implementation | Function-based |

---

### 2. Why Generators in ETL?

- Memory efficient
- Lazy execution
- Handles large datasets
- Better pipeline composition

---

### 3. Why Decorators?

- Reusable logic
- Logging
- Monitoring
- Retry
- Authentication
- Caching

---

# Final Takeaways

✅ Iterators control data traversal

✅ Generators enable lazy processing

✅ Decorators add reusable behavior

✅ Combined together they create scalable ETL pipelines

✅ Same pattern is heavily used in:

- Data Engineering
- Apache Airflow
- Spark
- Kafka Consumers
- Streaming Systems
- Production ETL Frameworks
