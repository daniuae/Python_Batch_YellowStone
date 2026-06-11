# Multithreading in Python

## Is Multithreading Allowed in Python?

Yes. Python allows users to create and manage multiple threads using the built-in `threading` module.

Multithreading enables multiple tasks to run concurrently within the same process.

Example:

- Thread 1 → Download files
- Thread 2 → Read data
- Thread 3 → Process records

All these tasks can execute concurrently.

---

# What is a Thread?

A thread is the smallest unit of execution inside a process.

A process can contain:

- One thread (Single-threaded)
- Multiple threads (Multi-threaded)

---

# Creating Your First Thread

```python
import threading
import time

def display_message():
    print("Thread is running...")
    time.sleep(2)
    print("Thread finished.")

# Create thread
t = threading.Thread(target=display_message)

# Start thread
t.start()

# Wait for thread to complete
t.join()

print("Main program completed.")
```

### Output

```text
Thread is running...
Thread finished.
Main program completed.
```

---

# Running Multiple Threads

```python
import threading
import time

def worker(name):
    for i in range(3):
        print(f"{name} -> {i}")
        time.sleep(1)

t1 = threading.Thread(target=worker, args=("Thread-1",))
t2 = threading.Thread(target=worker, args=("Thread-2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("All threads completed.")
```

### Sample Output

```text
Thread-1 -> 0
Thread-2 -> 0
Thread-1 -> 1
Thread-2 -> 1
Thread-1 -> 2
Thread-2 -> 2
All threads completed.
```

---

# Thread Lifecycle

A thread passes through the following states:

```text
New
 ↓
Runnable
 ↓
Running
 ↓
Blocked/Waiting
 ↓
Terminated
```

---

# Using join()

The `join()` method waits for a thread to finish before continuing.

```python
import threading
import time

def task():
    time.sleep(3)
    print("Task Completed")

t = threading.Thread(target=task)

t.start()

print("Waiting for thread...")

t.join()

print("Program Ended")
```

---

# Naming Threads

```python
import threading

def worker():
    print("Current Thread:", threading.current_thread().name)

t = threading.Thread(
    target=worker,
    name="DataLoaderThread"
)

t.start()
```

### Output

```text
Current Thread: DataLoaderThread
```

---

# Daemon Threads

Daemon threads run in the background.

When the main program exits, daemon threads automatically terminate.

```python
import threading
import time

def background_task():
    while True:
        print("Monitoring...")
        time.sleep(1)

t = threading.Thread(
    target=background_task,
    daemon=True
)

t.start()

time.sleep(3)

print("Main Program Ends")
```

---

# Thread Synchronization

Multiple threads accessing shared data can cause issues.

Example:

```python
counter = 0
```

If multiple threads modify `counter` simultaneously, incorrect results may occur.

---

# Using Lock

Locks prevent multiple threads from modifying shared resources simultaneously.

```python
import threading

counter = 0

lock = threading.Lock()

def increment():
    global counter

    for _ in range(100000):
        with lock:
            counter += 1

threads = []

for i in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(counter)
```

### Output

```text
500000
```

---

# Race Condition Example

Without Lock:

```python
counter += 1
```

Multiple threads may update the same variable simultaneously.

Possible result:

```text
Expected: 500000
Actual: 492341
```

This issue is called a **Race Condition**.

---

# ThreadPoolExecutor (Recommended)

Instead of manually creating threads, use ThreadPoolExecutor.

```python
from concurrent.futures import ThreadPoolExecutor
import time

def worker(number):
    time.sleep(2)
    return f"Task {number} Completed"

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(worker, [1, 2, 3])

for result in results:
    print(result)
```

### Output

```text
Task 1 Completed
Task 2 Completed
Task 3 Completed
```

---

# Python GIL (Global Interpreter Lock)

Python uses a mechanism called the Global Interpreter Lock (GIL).

Because of the GIL:

- Only one thread executes Python bytecode at a time.
- CPU-intensive tasks do not gain much speed from threading.
- I/O-bound tasks benefit significantly.

---

# I/O-Bound Tasks

Good candidates for multithreading:

- API Calls
- Database Queries
- File Reading
- File Writing
- Network Requests
- Web Scraping

Example:

```python
import requests

response = requests.get(
    "https://example.com"
)
```

Most of the time is spent waiting for the server response.

---

# CPU-Bound Tasks

Examples:

```python
for i in range(100000000):
    pass
```

```python
large_prime_calculation()
```

```python
image_processing()
```

For these tasks, use multiprocessing instead of multithreading.

---

# Multithreading vs Multiprocessing

| Feature | Multithreading | Multiprocessing |
|----------|---------------|----------------|
| Memory | Shared | Separate |
| Lightweight | Yes | No |
| I/O Tasks | Excellent | Good |
| CPU Tasks | Limited by GIL | Excellent |
| Communication | Easy | Hard |
| Speed for CPU Work | Lower | Higher |

---

# Real-World Data Engineering Example

## Without Threads

```python
for api in api_list:
    fetch_data(api)
```

Execution:

```text
API 1 -> Wait
API 2 -> Wait
API 3 -> Wait
...
```

Total time becomes very large.

---

## With Threads

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(fetch_data, api_list)
```

Execution:

```text
API 1 Running
API 2 Running
API 3 Running
...
```

Multiple API calls happen concurrently.

---

# ETL Example

```python
from concurrent.futures import ThreadPoolExecutor

files = [
    "sales.csv",
    "customers.csv",
    "products.csv"
]

def load_file(file_name):
    print(f"Loading {file_name}")

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(load_file, files)
```

### Output

```text
Loading sales.csv
Loading customers.csv
Loading products.csv
```

---

# Best Practices

✅ Use threads for I/O operations.

✅ Use locks when sharing resources.

✅ Prefer ThreadPoolExecutor over manual thread management.

✅ Keep threads lightweight.

✅ Always use `join()` when synchronization is required.

❌ Avoid threading for heavy mathematical computations.

❌ Avoid creating thousands of threads.

❌ Avoid modifying shared data without locks.

---

# Summary

- Python supports multithreading through the `threading` module.
- Threads are useful for I/O-bound operations.
- The GIL limits true parallel execution for CPU-heavy tasks.
- Use `ThreadPoolExecutor` for cleaner thread management.
- Use `Lock` to avoid race conditions.
- For CPU-intensive workloads, prefer the `multiprocessing` module.
- Multithreading is widely used in ETL pipelines, API integrations, web scraping, file processing, and database operations.
