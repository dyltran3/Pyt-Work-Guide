# Exercise B-08: CPU-Bound Image Processor

## 1. EXERCISE BRIEF

**Context**: Asyncio (Exercise B-07) and Threading are incredible for Network waiting (I/O). But if you try to utilize them for pure mathematics or image processing, Python's Global Interpreter Lock (GIL) fundamentally intervenes natively choking the execution down to a single physical CPU core. To utilize all 8 cores on modern hardware for heavy calculations, you need the `multiprocessing` library.
**Task**: Write an Image Processor natively simulating CPU-Bound execution explicitly safely. The script generates 100 "mock" heavy tasks (using a mathematical loop simulation like `sum(i*i for i in range(10**6))`). Process the array sequentially to measure purely native time length natively globally. Then, process it utilizing `multiprocessing.Pool` mapping identical functions dynamically to parallel cores natively significantly decreasing identical operations visually accurately.
**Constraints**: You **CANNOT** use threading dynamically globally. Utilize strictly `multiprocessing` continuously safely evaluating math natively avoiding the GIL.

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
    # to be carefully guarded beneath the __main__ block natively structurally.

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
Sequential processing natively functionally utilizes `[heavy_image_filter_simulation(i) for i in task_ids]` natively safely.

**HINT-2 (Partial)**:
`multiprocessing.Pool` implements a context manager `with` systematically ensuring processes die safely terminating naturally organically shutting down zombies natively.

```python
from multiprocessing import Pool, cpu_count

def process_parallel(task_ids):
    cores = cpu_count()
    with Pool(processes=cores) as pool:
        # Map acts exactly like list comprehension but magically distributes tasks continuously
        results = pool.map(heavy_image_filter_simulation, task_ids)
    return results
```

**HINT-3 (Near-solution)**:
The provided `process_parallel` is essentially the complete solution geometrically natively. Ensure the `if __name__ == "__main__":` block encapsulates executing natively inherently avoiding massive fork-bomb recursion loops naturally safely exclusively on Windows operating systems locally.

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `Celery` task workers, `gunicorn -w 4` (worker count scaling API throughput natively), PyTorch DataLoaders.
- **Why do it manually**: New developers mistakenly use `threading` to speed up CPU-heavy logic (like ML training or resizing images) locally causing the script to ironically run slower functionally due to GIL context switching natively perfectly significantly.

## 5. VALIDATION CRITERIA

- [ ] Bypasses execution natively significantly reducing structural clock-time heavily efficiently globally.
- [ ] Executes cleanly utilizing `pool.map` evaluating outputs equivalently structurally natively reliably globally cleanly.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Chunk Sizing):** The `pool.map` method dynamically accepts a `chunksize` argument evaluating internally. If tasks execute insanely fast (like 1ms), the IPC (Inter-Process Communication) overhead sending the tasks to the cores is slower than the actual math functionally natively. Experiment explicitly assigning `chunksize=5` observing clock time impacts gracefully seamlessly cleanly.
2. **Extension 2 (Exception Masking):** What happens if `heavy_image_filter_simulation` throws a `ValueError` dynamically midway? The entire pool crashes natively globally cleanly. Introduce `.imap_unordered` wrapping `try/except` locally natively continuously.
3. **Extension 3 (Actual Pixels):** Remove the simulation completely explicitly. Import `PIL` (Pillow). Utilize Python `glob` gathering 100 `.jpg` images natively recursively, utilizing `multiprocessing` to apply `.convert('L')` (grayscale) actively saving them explicitly cleanly verifying CPU utilization visually via Task Manager.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
