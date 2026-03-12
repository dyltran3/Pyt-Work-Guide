# Exercise B-21: Concurrency Shootout (Async vs Thread vs Process)

## 1. EXERCISE BRIEF

**Context**: Lập trình viên thường bối rối khi chọn giữa `asyncio`, `threading`, và `multiprocessing`. Mỗi mô hình giải quyết một loại bài toán khác nhau (I/O bound vs CPU bound).
**Task**: Viết chương trình thực hiện 3 task:
1. **I/O Bound**: Download 50 URLs.
2. **CPU Bound**: Tính toán Sieve of Eratosthenes đến 10,000,000.
3. **Mixed**: Đọc file text lớn và đếm từ.
**Constraints**: Chạy benchmark cho cả 3 mô hình (Async, Thread, Process) cho mỗi loại task và vẽ bảng so sánh thời gian thực thi.

## 2. STARTER CODE

```python
import time
import asyncio
import threading
import multiprocessing

# --- TASKS ---

def cpu_bound_task(n=5_000_000):
    """Tính tổng bình phương của n số"""
    return sum(i * i for i in range(n))

def io_bound_task(delay=0.1):
    """Giả lập network request"""
    time.sleep(delay)

# --- RUNNERS ---

def run_multiprocessing(func, args_list):
    start = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(func, args_list)
    return time.time() - start

def run_threading(func, args_list):
    start = time.time()
    threads = []
    for arg in args_list:
        t = threading.Thread(target=func, args=(arg,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return time.time() - start

# TODO: Implement run_asyncio and the benchmark suite
```

## 3. PROGRESSIVE HINTS

**HINT-1 (GIL)**:
Python Global Interpreter Lock (GIL) ngăn cản nhiều Thread chạy Python bytecode cùng lúc. Do đó, Threading không giúp tăng tốc CPU-bound tasks.

**HINT-2 (Asyncio)**:
`asyncio` chỉ hiệu quả khi library bạn dùng hỗ trợ `non-blocking`. `time.sleep()` là blocking; hãy dùng `asyncio.sleep()`.

**HINT-3 (Multiprocessing)**:
Dùng Processes sẽ chiếm nhiều Memory hơn vì mỗi process có bản sao Python interpreter riêng.

## 4. REAL-WORLD CONNECTIONS
- **Asyncio**: FastAPI, Web Crawlers, Chat Servers.
- **Multiprocessing**: Data Science pipelines (Pandas/Polars), Image Processing.
- **Threading**: Legacy I/O code, GUI applications (keep UI responsive).

## 5. VALIDATION CRITERIA
- [ ] Bảng kết quả chứng minh:
    - **CPU Bound**: Process nhanh nhất, Thread/Async chậm (hoặc tương đương Sync).
    - **I/O Bound**: Thread/Async nhanh ngang nhau, Process tốn overhead hơn.

## 6. SETUP REQUIREMENTS
- **Dependencies**: Standard library only.
