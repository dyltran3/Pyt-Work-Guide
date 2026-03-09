# Exercise B-02: Memory-Efficient Data Stream

## 1. EXERCISE BRIEF

**Context**: Streaming live metrics (like server sensor readings or high-frequency stock trading data) can quickly consume memory. If a pipeline tries to hold the entire history of an infinite stream just to calculate an average, it will run out of RAM. "Online algorithms" solve this by calculating statistics dynamically on the fly without storing historical data.
**Task**: Build a Python memory-efficient data stream using a Generator. Read from a mock data source continuously. Calculate the "Running Mean" (Average) and "Running Variance / Standard Deviation" of the stream using Welford's Online Algorithm without ever storing the `bytes` in a list.
**Constraints**: Do **NOT** use `statistics.mean`, `numpy`, or keep a historical `list` or `list` slices of the streamed values. Process the float values purely recursively inside the infinite loop.

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

- **Libraries/Tools**: `Apache Kafka` streams, `Spark Streaming`, Kinesis.
- **Why do it manually**: A running container (AWS Fargate, Docker) has strict RAM availability (sometimes 256MB). Reading a million-row DB cursor entirely into RAM (`list(cursor)`) guarantees instance failure. Applying Generator architectures paired with stream mathematics scales infinitely on fixed infrastructure.

## 5. VALIDATION CRITERIA

- [ ] Successfully iterates relying on `yield` processing.
- [ ] No lists or unbounded arrays are utilized to store historical variations.
- [ ] Accurately outputs variance/average resolving cleanly under standard math assertions.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Exponential Moving Average):** Financial data usually tracks Exponential Moving Average (EMA) rather than simple total means so the data reacts to _recent_ changes faster. Implement a secondary mathematical pipeline calculating an EMA with an `alpha` factor of `0.1`.
2. **Extension 2 (Corrupted Iterables):** Introduce `None` and String objects into the mock data stream (representing network stutter or bad JSON parsing). Implement `try/except` guard rails inside `process_stream_continuously` that gracefully skips broken metrics without permanently destroying the Welford calculations or crashing the stream.
3. **Extension 3 (Decoupled Windows):** Rather than total running numbers, implement a sliding window tracker. Calculate the mean of _only_ the last `100` elements mathematically. Use `collections.deque(maxlen=100)` to accomplish the sliding element drop-off perfectly efficiently.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`math`, `random`).
