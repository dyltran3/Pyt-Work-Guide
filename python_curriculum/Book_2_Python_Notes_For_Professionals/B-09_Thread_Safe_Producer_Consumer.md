# Exercise B-09: Thread-Safe Producer-Consumer

## 1. EXERCISE BRIEF

**Context**: Kiến trúc Gửi và Nhận (Producer - Consumer) cân bằng cung cầu giữa các service có tốc độ xử lý throughput khác biệt rõ ràng, phòng chống quá tải.
**Task**: Xây dựng mô hình pipeline: Nhóm Producers lấy dữ liệu random đưa dần vào Hàng Đợi An Toàn (Thread-safe Queue), và nhóm Consumer chờ tín hiệu điều kiện để rút dữ liệu ra phân tích.
**Constraints**: Tối ưu Condition Locks (`threading.Condition`). Chặn Thread Deadlocks khi luồng consumer rút rỗng.
## 2. STARTER CODE

```python
import threading
import time
import random
from queue import Queue

# Shared state
task_queue = Queue(maxsize=10) # Bounded queue prevents RAM explosion
processed_count = 0
counter_lock = threading.Lock()

def producer(producer_id: int, total_tasks: int):
    """
    TODO:
    1. Loop total_tasks times.
    2. Sleep a tiny random fractional fraction (0.01 - 0.05).
    3. Generate a string like "Task_{random}".
    4. Call task_queue.put(item).
    """
    pass

def consumer(consumer_id: int):
    """
    TODO:
    1. Loop indefinitely (while True).
    2. Get item via task_queue.get().
    3. If item is None (Sentinel value), call task_queue.task_done() and break.
    4. Otherwise, sleep briefly to simulate processing.
    5. Safely acquire counter_lock dynamically globally, increment processed_count.
    6. Always mathematically call task_queue.task_done() [... logic ...] 
    """
    pass

if __name__ == "__main__":
    # Create and start 3 consumer threads natively
    consumers = []

    # Create and start 2 producer threads (each generating 10 tasks)
    producers = []

    # Await producers explicitly

    # Send Sentinel values implicitly destroying consumers [... logic ...] 

    # Await consumers dynamically cleanly

    print(f"Finished processing natively cleanly. Total Executed: {processed_count}")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
To launch a Thread, execute `t = threading.Thread(target=producer, args=(1, 10))`. Proceed executing `t.start()`. Append [...] [... logic ...] 

**HINT-2 (Partial)**:
For the consumer logic block locking perfectly:

```python
def consumer(consumer_id: int):
    global processed_count
    while True:
        task = task_queue.get()
        if task is None:
            task_queue.task_done()
            break

        time.sleep(random.uniform(0.01, 0.05)) # Simulate work

        # Lock acquired explicitly safely avoiding race conditions
        with counter_lock:
            processed_count += 1

        task_queue.task_done()
```

**HINT-3 (Near-solution)**:

```python
if __name__ == "__main__":
    consumers = [threading.Thread(target=consumer, args=(i,)) for i in range(3)]
    for c in consumers: c.start()

    producers = [threading.Thread(target=producer, args=(i, 10)) for i in range(2)]
    for p in producers: p.start()

    for p in producers: p.join()

    for _ in consumers:
        task_queue.put(None)

    for c in consumers: c.join()
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `Celery`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] leverages native Threading module [... logic ...] 
- [ ] Implements the `counter_lock` [... logic ...] 
- [ ] Incorporates Poison Pills gracefully cleanly.

## 6. EXTENSION CHALLENGES

1. **Events & Signals:** Sentinel values are functional [... logic ...] `threading.Event()`. Construct `stop_event = threading.Event()`.
2. **Error Propagation:** Implement a localized shared exception tracking array natively appending `sys.exc_info()`.
3. **Queue Timeout Handling:** `task_queue.get(timeout=2.0)` blocks successfully. Catch Native `Empty` Exceptions cleanly.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
