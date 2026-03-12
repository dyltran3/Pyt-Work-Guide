# Exercise B-08: CPU-Bound Image Processor

## 1. EXERCISE BRIEF

**Context**: Trong khi I/O Bound dùng Async, bài toán biến đổi Image/Tensor lại bị giới hạn rào cản GIL do CPU-bound intensive. Đa tiến trình là giải pháp song song (Parallelism) thực thụ.
**Task**: Chạy giả lập các phép nhân ma trận cường độ cao trên Image pixels. Thiết kế Pool tiến trình song song để phân chia tải.
**Constraints**: Dùng `multiprocessing` package. Không dùng thead vì sẽ gặp hiện tượng GIL lock bottleneck.
## 2. STARTER CODE

```python
import time
import math
import multiprocessing

def heavy_image_filter_simulation(image_id: int) -> tuple[int, int]:
    """
    Simulation of applying a grayscale filter to a high-res image.
    This purely blocks the CPU doing raw floating point math.
    """
    result = 0
    # ~3 million loops blocks a CPU for roughly 0.1s
    for i in range(3_000_000):
        result += math.sqrt(i)

    return (image_id, int(result))

def process_sequential(task_ids: list[int]) -> list:
    """TODO: Just loop over task_ids natively returning the result list."""
    pass

def process_parallel(task_ids: list[int]) -> list:
    """
    TODO:
    1. Import cpu_count
    2. Open a multiprocessing.Pool
    3. Use pool.map to execute heavy_image_filter_simulation
    4. Return the results
    """
    pass

if __name__ == "__main__":
    # We only process 30 "images" to keep the test reasonably quick
    tasks = list(range(30))

    print("Testing Sequential...")
    start_seq = time.time()
    res_seq = process_sequential(tasks)
    seq_duration = time.time() - start_seq
    print(f"Sequential: {seq_duration:.2f} seconds")

    # Notice: Multiprocessing on Windows requires the script execution
    # to be inside a __main__ block to avoid infinite recursion loops.

    print("\\nTesting Multiprocessing...")
    start_par = time.time()
    res_par = process_parallel(tasks)
    par_duration = time.time() - start_par
    print(f"Parallel: {par_duration:.2f} seconds")

    print(f"\\nSpeedup Factor: {seq_duration / par_duration:.1f}x")

    # Parallel must be strictly faster dynamically
    assert par_duration < seq_duration
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Sequential processing `[heavy_image_filter_simulation(i) for i in task_ids]` 

**HINT-2 (Partial)**:
`multiprocessing.Pool` implements a context manager `with` for clean cleanup.

```python
from multiprocessing import Pool, cpu_count

def process_parallel(task_ids):
    cores = cpu_count()
    with Pool(processes=cores) as pool:
        # Map the task list to our simulation function.
        results = pool.map(heavy_image_filter_simulation, task_ids)
    return results
```

**HINT-3 (Near-solution)**:
The provided `process_parallel` is essentially the complete solution.

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `Celery`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Bypasses execution deadlocks.
- [ ] Executes cleanly utilizing `pool.map` evaluating outputs.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Chunk Sizing):** The `pool.map` method dynamically accepts a `chunksize` argument. If tasks execute very fast, adjust `chunksize=5` observing clock time impacts.
2. **Extension 2 (Exception Masking):** Use `.imap_unordered` inside a `try/except` block to handle errors midway.
3. **Extension 3 (Actual Pixels):** Remove the simulation and use `PIL` (Pillow) to process actual images.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
