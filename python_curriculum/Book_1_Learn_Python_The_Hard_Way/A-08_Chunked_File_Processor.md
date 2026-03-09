# Exercise A-08: Chunked File Processor

## 1. EXERCISE BRIEF

**Context**: Big Data is common. Attempting to parse a 5GB CSV file containing transaction records line-by-line using `readlines()` will violently crash your server's RAM (Out Of Memory Exception). Instead, we process data in "chunks" (streams) using Generators, calculating what we need mathematically without ever holding the full text in memory.
**Task**: Write a Python script that creates a fake 100,000-line CSV file. Then, process it calculating the sum, average, and row count of a generic "amount" column. You must read the file in chunks of exactly 1,000 lines at a time. Do this using Python's `yield` memory-efficient generators.
**Constraints**: You **CANNOT** use `pandas`, `csv`, or `sys.getsizeof` to solve the actual processing task. Only Python basic generators or the `itertools.islice` module are permitted to chunk the rows.

## 2. STARTER CODE

```python
import sys
import random

def create_massive_csv(filename: str, rows=100000) -> None:
    """ Generates a dummy CSV with ID, Name, Amount """
    with open(filename, 'w') as f:
        f.write("id,name,amount\n")
        # Generator expression inside join avoids building huge list in memory
        for i in range(rows):
            f.write(f"{i},User_{i},{random.uniform(10.0, 5000.0):.2f}\n")

def read_in_chunks(file_object, chunk_size=1000):
    """
    TODO: Create a generator that yields lists of strings (lines),
    where each list is exactly `chunk_size` long.
    Stop when the file is exhausted.
    """
    pass

def process_large_file(filename: str) -> dict:
    """
    TODO:
    1. Open the file.
    2. Ignore the header.
    3. Loop over the chunks using `read_in_chunks()`.
    4. Maintain a running total and row count.
    5. Return a dictionary with {'sum': ..., 'count': ..., 'avg': ...}
    """
    pass

if __name__ == "__main__":
    csv_file = 'transactions.csv'
    print("Generating massive CSV... (this might take a second)")
    create_massive_csv(csv_file, 50000)

    print("Processing...")
    stats = process_large_file(csv_file)
    print("Results:", stats)
    assert stats['count'] == 50000
    assert 'avg' in stats
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
A file object (`f = open(...)`) is already technically an iterator in Python. It evaluates lazily. To get a specific number of lines from an iterator, the safest way is using `itertools.islice(iterable, amount)`.

**HINT-2 (Partial)**:
Inside your `read_in_chunks` generator:

```python
from itertools import islice

def read_in_chunks(file_object, chunk_size=1000):
    while True:
        # Get exactly chunk_size elements from the file iterator
        chunk = list(islice(file_object, chunk_size))
        if not chunk:
            break
        yield chunk
```

This guarantees at most `chunk_size` rows exist in RAM at a single time for parsing.

**HINT-3 (Near-solution)**:

```python
def process_large_file(filename: str) -> dict:
    total_sum = 0.0
    total_count = 0

    with open(filename, 'r') as f:
        next(f) # Skip header line
        for chunk in read_in_chunks(f, 1000):
            # Process exactly 1000 items in memory
            for line in chunk:
                # "id,name,amount" -> Amount is index 2
                amount = float(line.strip().split(',')[2])
                total_sum += amount
                total_count += 1

    return {
        'sum': round(total_sum, 2),
        'count': total_count,
        'avg': round(total_sum / total_count, 2) if total_count > 0 else 0
    }
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `pandas` chunksize argument (`read_csv(chunksize=1000)`), PySpark, Apache Airflow ETL workers, Dask.
- **Why do it manually**: Often when querying a third-party AWS S3 file, pulling it all into a Pandas dataframe crashes the worker node container inside Kubernetes because container RAM is strictly capped. Understanding `yield` saves massive server infrastructure costs by doing stream-based ETL.

## 5. VALIDATION CRITERIA

- [ ] Successfully parses the massive generated dataset.
- [ ] Proves memory efficiency: `sys.getsizeof` on any extracted list of lines should never exceed constraints of a few kilobytes.
- [ ] Safely yields from a generator using `itertools.islice` (or a `while` loop keeping track of counts if you build the buffer manually).
- [ ] Returns mathematically precise values.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Multi-Column Stats):** Instead of only finding the average amount, also compute the minimum and maximum row amounts mathematically as the chunks stream by (never holding amounts in memory or using `max()` on a giant list).
2. **Extension 2 (Memory Profiling):** Import the `tracemalloc` module. Snapshot the memory before calling your processing function and after. Prove in terminal output that reading a 10MB text CSV only required ~1MB of peak memory.
3. **Extension 3 (Multiprocessing Chunks):** Modify the pipeline so that when a batch of 1000 lines is yielded from the file, it is handed off to a `multiprocessing.Pool` map function to be CPU-parsed simultaneously with other chunks, merging the averages mathematically afterwards.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`itertools`, `sys`, `random`).
