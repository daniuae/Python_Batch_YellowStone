# Multithreading in Python

## Objective

By the end of the session, students should be able to:

- Understand what multithreading is.
- Explain why multithreading is needed.
- Create and execute threads in Python.
- Understand the concept of concurrency.
- Identify real-world use cases.
- Understand race conditions and locks.
- Know when to use Multithreading vs Multiprocessing.

---

# Teaching Strategy

Instead of teaching:

```text
Definition → Theory → Code
```

Use:

```text
Story
 ↓
Problem
 ↓
Visualization
 ↓
Code
 ↓
Real-world Example
 ↓
Industry Application
 ↓
Hands-on Exercise
```

This approach keeps students engaged and improves retention.

---

# Step 1: Start with a Real-Life Story

## Scenario: Cooking Dinner

Ask students:

> Imagine you are preparing dinner alone.

### Single Person (Single Thread)

```text
1. Chop vegetables
2. Boil rice
3. Prepare curry
4. Make salad

Total Time = 40 Minutes
```

Everything happens one after another.

---

### Multiple Helpers (Multiple Threads)

```text
Person 1 → Chop vegetables
Person 2 → Boil rice
Person 3 → Prepare salad

Total Time = 15 Minutes
```

### Explanation

```text
Each helper = Thread
Kitchen = Process
Cooking Tasks = Jobs
```

---

# Step 2: Explain the Problem

### Sequential Execution

```python
import time

def task1():
    print("Task 1 Started")
    time.sleep(3)
    print("Task 1 Completed")

def task2():
    print("Task 2 Started")
    time.sleep(3)
    print("Task 2 Completed")

task1()
task2()
```

### Ask Students

```text
How long will this take?
```

### Answer

```text
3 + 3 = 6 Seconds
```

---

# Step 3: Introduce Multithreading

Explain:

```text
What if both tasks could run together?
```

### Code

```python
import threading
import time

def task1():
    print("Task 1 Started")
    time.sleep(3)
    print("Task 1 Completed")

def task2():
    print("Task 2 Started")
    time.sleep(3)
    print("Task 2 Completed")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()
```

### Ask Students Again

```text
How long now?
```

### Answer

```text
Approximately 3 Seconds
```

---

# Step 4: Draw the Concept

## Without Threads

```text
Main Program

Task 1 ----------- 3 sec

Task 2 ----------- 3 sec

Total = 6 sec
```

---

## With Threads

```text
Main Program

Thread 1 -------- 3 sec

Thread 2 -------- 3 sec

Total = 3 sec
```

Students understand diagrams much faster than theory.

---

# Step 5: Explain Why We Need Threads

Ask:

```text
When does a program wait?
```

Examples:

- Downloading files
- Calling APIs
- Reading files
- Database queries
- Sending emails
- Waiting for network responses

### Example

```python
response = requests.get(url)
```

### Explain

```text
CPU is idle while waiting.

Instead of waiting,
another thread can perform useful work.
```

---

# Step 6: Data Engineering Example

Students working in ETL can relate immediately.

## Without Threads

```text
API 1 → 5 sec

API 2 → 5 sec

API 3 → 5 sec

Total = 15 sec
```

---

## With Threads

```text
API 1
API 2
API 3

Running Together

Total = 5 sec
```

---

# Step 7: Explain the GIL Using an Analogy

Avoid technical definitions initially.

## Whiteboard Marker Example

Imagine:

```text
5 Students
1 Marker
```

Everyone wants to write simultaneously.

```text
Student 1 Writes

Student 2 Waits

Student 3 Waits

Student 4 Waits

Student 5 Waits
```

### Explanation

```text
Marker = GIL

Many Threads Exist

Only One Executes Python Bytecode
At A Time
```

---

# Step 8: Thread Lifecycle

Draw on the board.

```text
Create Thread
      ↓
Ready
      ↓
Running
      ↓
Waiting
      ↓
Completed
```

Keep the explanation simple.

---

# Step 9: Introduce Race Conditions

### Example

```python
import threading

counter = 0

def increment():
    global counter

    for i in range(100000):
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

---

### Ask Students

```text
Expected Result?
```

Answer:

```text
500000
```

Sometimes the answer may be different.

This creates curiosity.

---

# Step 10: Introduce Lock

### Solution

```python
import threading

counter = 0

lock = threading.Lock()

def increment():
    global counter

    for i in range(100000):

        with lock:
            counter += 1
```

### Explanation

```text
Lock = Bathroom Key

Only One Person
Can Enter At A Time
```

Students remember this analogy for years.

---

# Step 11: Teach ThreadPoolExecutor

Instead of:

```python
t1 = Thread(...)
t2 = Thread(...)
t3 = Thread(...)
```

Use:

```python
from concurrent.futures import ThreadPoolExecutor

def worker(num):
    return f"Task {num}"

with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(worker, range(5))

for result in results:
    print(result)
```

### Explain

```text
ThreadPoolExecutor manages
thread creation automatically.
```

---

# Step 12: Industry Use Cases

Ask students where they think threads are used.

Then reveal:

```text
✓ ETL Pipelines
✓ API Integrations
✓ Database Queries
✓ Cloud Data Loading
✓ Web Scraping
✓ Chat Applications
✓ Email Processing
✓ Log Monitoring
✓ File Upload Systems
✓ Streaming Applications
```

---

# Step 13: Multithreading vs Multiprocessing

| Situation | Recommended |
|------------|-------------|
| API Calls | Multithreading |
| Database Queries | Multithreading |
| File Reading | Multithreading |
| Web Scraping | Multithreading |
| ETL Ingestion | Multithreading |
| Image Processing | Multiprocessing |
| Machine Learning | Multiprocessing |
| Heavy Calculations | Multiprocessing |

---

# Interactive Questions During Session

## Question 1

```text
If two tasks each take 5 seconds,
how long will sequential execution take?
```

Answer:

```text
10 Seconds
```

---

## Question 2

```text
If both run in separate threads,
how long approximately?
```

Answer:

```text
5 Seconds
```

---

## Question 3

```text
Why are threads useful?
```

Answer:

```text
To perform other work
while waiting for I/O operations.
```

---

## Question 4

```text
Why doesn't multithreading always
speed up CPU-heavy tasks?
```

Answer:

```text
Because of Python's GIL.
```

---

# Recommended 60-Minute Classroom Plan

| Time | Activity |
|--------|-----------|
| 5 min | Cooking Story |
| 10 min | Sequential Program |
| 10 min | First Thread Example |
| 10 min | Multiple Threads Demo |
| 5 min | Thread Lifecycle |
| 10 min | Race Condition + Lock |
| 5 min | ThreadPoolExecutor |
| 5 min | Industry Use Cases |

---

# Golden Teaching Formula

```text
Real-Life Story
      ↓
Visual Diagram
      ↓
Simple Code
      ↓
Problem Identification
      ↓
Solution Using Threads
      ↓
Industry Example
      ↓
Hands-On Exercise
      ↓
Quiz
```

---

# Final Takeaway

When teaching Multithreading:

❌ Don't start with definitions.

❌ Don't start with GIL.

❌ Don't start with theory-heavy slides.

✅ Start with a story.

✅ Show a problem.

✅ Demonstrate the solution.

✅ Relate it to ETL and Data Engineering.

✅ Use analogies such as:
   - Cooking Team
   - Whiteboard Marker (GIL)
   - Bathroom Key (Lock)

Students remember stories and analogies much longer than technical definitions.



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





---------




