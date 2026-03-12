# Exercise B-02: Memory-Efficient Data Stream

## 1. EXERCISE BRIEF

**Context**: Micro-optimizations luôn cần khi lượng Data Ingestion quá lớn (Kafka, Kinesis streams). Việc nén lưu trữ RAM bằng built-in objects là cốt lõi của tối ưu Python Backend.
**Task**: Thiết kế một cấu trúc Memory-Efficient Data Stream sử dụng `__slots__` và NamedTuple/Dataclass để lưu lượng log records thay vì dùng dictionary thông thường.
**Constraints**: So sánh Memory Profile bằng module `sys.getsizeof` để chứng thực bộ nhớ cấu trúc mới nhỏ hơn cấu trúc sử dụng Dictionary ít nhất 30%.
## 2. STARTER CODE

```python
import math
import random

def simulated_sensor_stream():
    """Generates an infinite stream of mock temperature data"""
    while True:
        yield random.normalvariate(mu=70.0, sigma=5.0)

def process_stream_continuously(stream):
    """
    TODO: Consume the stream.
    Calculate the running mean and variance continuously without lists.
    Use Welford's Method format.
    Yield the current (count, mean, variance) at every single step so a caller can print it.
    """
    n = 0
    mean = 0.0
    M2 = 0.0 # Sum of squares of differences from the current mean

    for value in stream:
        # 1. Update your variables mathematically here
        # 2. Yield the tuple (n, current_mean, current_variance)
        pass

if __name__ == "__main__":
    sensor = simulated_sensor_stream()
    stats = process_stream_continuously(sensor)

    # Process only 10,000 items to avoid an infinite loop in our test,
    # but theoretically the memory usage would remain flat for 1 trillion items.
    for _ in range(10000):
        count, current_mean, current_variance = next(stats)

    print(f"Final Count: {count}")
    print(f"Rolling Avg: {current_mean:.2f}")
    print(f"Rolling Std Dev: {math.sqrt(current_variance):.2f}")

    # Given the normalvariate of mu=70 and sigma=5, it should converge close to these
    assert 69.0 <= current_mean <= 71.0
    assert 4.5 <= math.sqrt(current_variance) <= 5.5
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Welford's algorithm prevents floating-point precision loss when calculating variances on enormous datasets compared to the naive formula. The formula dictates finding the `delta` between the newly arrived value and the _old_ mean.

**HINT-2 (Partial)**:
For updating the step:

```python
n += 1
delta = value - mean
mean += delta / n
delta2 = value - mean # Difference between value and NEW mean
M2 += delta * delta2
```

**HINT-3 (Near-solution)**:

```python
def process_stream_continuously(stream):
    n = 0
    mean = 0.0
    M2 = 0.0

    for value in stream:
        n += 1
        delta = value - mean
        mean += delta / n
        M2 += delta * (value - mean)

        variance = M2 / n if n > 1 else 0.0
        yield (n, mean, variance)
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `Apache Kafka`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Successfully iterates relying on `yield` processing.
- [ ] No lists or unbounded arrays are utilized to store historical variations.
- [ ] Accurately outputs variance/average resolving cleanly under standard math assertions.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Exponential Moving Average):** Financial data usually tracks Exponential Moving Average (EMA) rather than simple total means so the data reacts to _recent_ changes faster. Implement a secondary mathematical pipeline calculating an EMA with an `alpha` factor of `0.1`.
2. **Extension 2 (Corrupted Iterables):** Introduce `None` and String objects into the mock data stream (representing network stutter or bad JSON parsing). Implement `try/except` guard rails inside `process_stream_continuously` that gracefully skips broken metrics without permanently destroying the Welford calculations or crashing the stream.
3. **Extension 3 (Decoupled Windows):** Rather than total running numbers, implement a sliding window tracker. Calculate the mean of _only_ the last `100` elements mathematically. Use `collections.deque(maxlen=100)` 

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`math`, `random`).
