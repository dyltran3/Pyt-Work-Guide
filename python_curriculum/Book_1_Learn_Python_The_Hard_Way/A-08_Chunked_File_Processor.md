# Exercise A-08: Chunked File Processor

## 1. EXERCISE BRIEF

**Context**: Data Analysts thường phải xử lý tập tin csv/json siêu lớn (hàng chục GB) nhưng backend chỉ có 512MB RAM. Kỹ thuật Chunking Data Stream là bắt buộc.
**Task**: Viết một trình nạp dữ liệu (File Processor) đọc file siêu lớn bằng cách chia file thành các phần nhỏ (Chunking). Ở mỗi chunk, lọc ra các thông tin hợp lệ rồi ghi nối đuôi (append) vào file output.
**Constraints**: 100% không dùng `pandas`. Độ phức tạp không gian (Space Complexity) phải là O(1) hoặc O(chunk_size).
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

- **Libraries/Tools**: `pandas`` và các framework chuẩn công nghiệp khác.

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
