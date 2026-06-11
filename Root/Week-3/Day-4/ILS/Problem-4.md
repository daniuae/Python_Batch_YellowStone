# Introduction to Threading and Concurrency in Python

## Section 1: Creating Your First Thread

Threading allows Python to run a function in the background without stopping the main program.

This is the simplest example of creating and starting a thread.

### Example

```python
import threading
import time

def display_message():
    print("Thread is running...")
    time.sleep(2)
    print("Thread finished.")

# Create the thread
t = threading.Thread(target=display_message)

# Start the thread
t.start()

# Wait for the thread to finish
t.join()

print("Main program finished.")
```

### Output

```text
Thread is running...
Thread finished.
Main program finished.
```

### Explanation

| Method | Purpose |
|----------|----------|
| `Thread()` | Creates a new thread |
| `start()` | Starts executing the thread |
| `join()` | Waits for the thread to complete |

### Workflow

```text
Main Program
      |
      v
Create Thread
      |
      v
Start Thread
      |
      v
Execute Function
      |
      v
Join Thread
      |
      v
Program Ends
```

---

# Section 2: Running Two Threads at the Same Time

Threads allow multiple functions to run concurrently.

This example shows how two tasks can run in parallel.

### Example

```python
import threading
import time

def task_one():
    print("Task One started")
    time.sleep(1)
    print("Task One finished")

def task_two():
    print("Task Two started")
    time.sleep(1)
    print("Task Two finished")

t1 = threading.Thread(target=task_one)
t2 = threading.Thread(target=task_two)

t1.start()
t2.start()

t1.join()
t2.join()

print("Both threads completed.")
```

### Possible Output

```text
Task One started
Task Two started
Task One finished
Task Two finished
Both threads completed.
```

or

```text
Task Two started
Task One started
Task Two finished
Task One finished
Both threads completed.
```

### Explanation

- Both threads start almost simultaneously.
- Python schedules them independently.
- Output order may vary each time.
- `join()` ensures the main program waits for all threads.

### Visualization

```text
Thread 1 ---> Task One
               |
               v
           Finished

Thread 2 ---> Task Two
               |
               v
           Finished
```

---

# Section 3: Thread With Timing + List Operation

Now we will replace simple print statements with a list operation and measure execution time.

### Example

```python
import threading
import time

def sum_large_list(numbers):
    start_time = time.time()

    total = sum(numbers)

    end_time = time.time()
    duration = round(end_time - start_time, 4)

    print(
        f"Thread completed. "
        f"Total = {total}, "
        f"Time taken = {duration} seconds"
    )

# Large list
my_list = list(range(1, 3000000))

# Create thread
t = threading.Thread(
    target=sum_large_list,
    args=(my_list,)
)

# Start thread
t.start()

# Wait for completion
t.join()

print("Main program completed.")
```

### Sample Output

```text
Thread completed. Total = 4499998500000, Time taken = 0.0341 seconds
Main program completed.
```

### Explanation

1. Create a large list.
2. Start a timer.
3. Calculate the sum.
4. Stop the timer.
5. Display total and execution time.

### Real-World Use Cases

- Processing large datasets
- Reading files
- Log analysis
- Background calculations
- ETL pipelines

---

# Section 4: Running Multiple Timed List Operations Using Threads

This example runs three list-processing tasks simultaneously.

Each thread measures its own execution time.

### Example

```python
import threading
import time

def process_list(name, numbers):
    start = time.time()

    total = sum(numbers)

    end = time.time()

    print(
        f"{name} finished. "
        f"Total = {total}, "
        f"Time = {round(end - start, 4)}s"
    )

# Three large lists
list1 = list(range(1, 4000000))
list2 = list(range(1, 5000000))
list3 = list(range(1, 6000000))

# Create threads
t1 = threading.Thread(
    target=process_list,
    args=("Thread 1", list1)
)

t2 = threading.Thread(
    target=process_list,
    args=("Thread 2", list2)
)

t3 = threading.Thread(
    target=process_list,
    args=("Thread 3", list3)
)

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for completion
t1.join()
t2.join()
t3.join()

print("All list-processing threads completed.")
```

### Sample Output

```text
Thread 1 finished. Total = 7999998000000, Time = 0.0431s
Thread 2 finished. Total = 12499997500000, Time = 0.0564s
Thread 3 finished. Total = 17999997000000, Time = 0.0698s

All list-processing threads completed.
```

### Explanation

- Three threads run independently.
- Each thread processes a different list.
- Completion order may vary.
- Main thread waits for all worker threads.

### Workflow Diagram

```text
                 Main Thread
                       |
       ---------------------------------
       |               |               |
       v               v               v

   Thread 1       Thread 2       Thread 3
   Sum List1      Sum List2      Sum List3

       |               |               |
       ---------------------------------
                       |
                       v
             All Threads Complete
```

---

# Section 5: Passing Arguments to Threads

Threads can execute functions that require parameters.

### Example

```python
import threading

def greet(name):
    print(f"Hello {name}")

t1 = threading.Thread(
    target=greet,
    args=("John",)
)

t2 = threading.Thread(
    target=greet,
    args=("Alice",)
)

t1.start()
t2.start()

t1.join()
t2.join()
```

### Output

```text
Hello John
Hello Alice
```

---

# Section 6: Daemon Threads

Daemon threads run in the background and automatically stop when the main program exits.

### Example

```python
import threading
import time

def background_task():
    while True:
        print("Running in background...")
        time.sleep(1)

t = threading.Thread(
    target=background_task,
    daemon=True
)

t.start()

time.sleep(3)

print("Main program exiting...")
```

### Output

```text
Running in background...
Running in background...
Running in background...
Main program exiting...
```

### Use Cases

- Monitoring systems
- Log collection
- Background cleanup
- Health checks

---

# Section 7: Python Threading and the GIL

## What is GIL?

GIL stands for:

**Global Interpreter Lock**

It allows only one thread to execute Python bytecode at a time.

### Impact

#### Good For

- File operations
- Network requests
- Database calls
- API calls

#### Not Ideal For

- Heavy mathematical computations
- CPU-intensive processing

### Example

```python
# CPU-bound work
for i in range(100000000):
    pass
```

Multiple threads usually won't speed up such tasks because of the GIL.

---

# Section 8: Threading vs Multiprocessing

| Feature | Threading | Multiprocessing |
|----------|----------|----------|
| Memory | Shared | Separate |
| Speed for I/O | Excellent | Good |
| Speed for CPU Work | Limited by GIL | Excellent |
| Communication | Easy | More Complex |
| Creation Cost | Low | Higher |

### Use Threading For

- API Calls
- ETL Data Extraction
- File Reading
- Web Scraping
- Database Queries

### Use Multiprocessing For

- Machine Learning
- Image Processing
- Video Processing
- Large Computations

---

# Real-World ETL Example

Suppose a Data Engineer needs to load data from multiple sources.

Without Threads:

```text
Read Oracle
      ↓
Read MySQL
      ↓
Read API
      ↓
Process Data
```

With Threads:

```text
          Read Oracle
               |
Read MySQL ----|---- Read API
               |
               v
         Process Data
```

### Sample Code

```python
import threading
import time

def load_oracle():
    time.sleep(2)
    print("Oracle Loaded")

def load_mysql():
    time.sleep(2)
    print("MySQL Loaded")

def load_api():
    time.sleep(2)
    print("API Loaded")

threads = [
    threading.Thread(target=load_oracle),
    threading.Thread(target=load_mysql),
    threading.Thread(target=load_api)
]

for t in threads:
    t.start()

for t in threads:
    t.join()

print("ETL Extraction Completed")
```

### Benefit

Instead of:

```text
2 + 2 + 2 = 6 seconds
```

Threads can complete in approximately:

```text
~2 seconds
```

because the I/O operations overlap.

---

# Key Takeaways

✅ Threading enables concurrent execution of tasks.

✅ `Thread()` creates a thread.

✅ `start()` begins execution.

✅ `join()` waits for completion.

✅ Threads are excellent for I/O-bound tasks.

✅ Python's GIL limits performance gains for CPU-bound tasks.

✅ Use multiprocessing for heavy computations.

✅ Threading is widely used in ETL, APIs, web scraping, file processing, and data engineering pipelines.
