# Exercise A-09: Rate Limiter Queue

## 1. EXERCISE BRIEF

**Context**: API services must defend themselves against abuse and DDoS attacks. One fundamental defense layer is the "Token Bucket" or "Leaky Bucket" rate limiting algorithm. Instead of outright banning users who make too many requests instantly, we hold requests in a queue and slowly execute them at a controlled FIFO rate, allowing traffic to smooth out elegantly.
**Task**: Build a FIFO (First-In, First-Out) queuing rate limiter algorithm using plain Python Lists. It enforces a strict maximum of processing N requests per second. If simulated requests come in faster than N, they must be delayed in a queue and processed smoothly via `time.sleep()`. Print the timestamp of each processed request.
**Constraints**: Do **NOT** use `collections.deque`, `queue.Queue`, or `asyncio`. Rely entirely on List appends/pops and the `time` module.

## 2. STARTER CODE

```python
import time

class RateLimiter:
    def __init__(self, max_per_second: int):
        self.max_per_second = max_per_second
        self.delay_between_requests = 1.0 / max_per_second
        self.queue = []
        self.last_run_time = 0.0

    def add_request(self, payload: str) -> None:
        """
        TODO: Add the request to the internal queue.
        """
        pass

    def process_queue(self) -> None:
        """
        TODO: Drain the queue, honoring the global rate limit.
        1. Pop the oldest item.
        2. Calculate how long to sleep based on self.last_run_time
        3. Sleep if necessary, execute the "request" (just print it), update last_run_time
        4. Repeat until empty.
        """
        pass

if __name__ == "__main__":
    # Simulate a burst of 5 requests instantly
    limiter = RateLimiter(max_per_second=2) # Only allow 2 per sec

    print("Simulating burst of 5 requests...")
    for i in range(5):
        limiter.add_request(f"Task_{i}")

    start_time = time.time()
    limiter.process_queue()
    end_time = time.time()

    duration = end_time - start_time
    # 5 tasks at 2/sec -> 0.0s, 0.5s, 1.0s, 1.5s, 2.0s -> Duration should be ~2.0 seconds minimum.
    print(f"Queue processed in {duration:.2f} seconds.")
    assert duration >= 2.0
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
In a basic Python list, `append(item)` adds to the right end. `pop(0)` removes and returns the first (oldest) item. Therefore, `while len(self.queue) > 0:` and popping index `0` acts as a manual FIFO queue.

**HINT-2 (Partial)**:
To accurately time limit, you must check `time.monotonic()` against our `self.last_run_time`.

```python
current_time = time.monotonic()
time_since_last = current_time - self.last_run_time

if time_since_last < self.delay_between_requests:
    sleep_needed = self.delay_between_requests - time_since_last
    time.sleep(sleep_needed)
```

**HINT-3 (Near-solution)**:

```python
def process_queue(self) -> None:
    while len(self.queue) > 0:
        task = self.queue.pop(0) # Inefficient O(N) compared to Deque, but works for the exercise

        now = time.monotonic()
        elapsed = now - self.last_run_time

        if elapsed < self.delay_between_requests:
            time.sleep(self.delay_between_requests - elapsed)

        # "Execute" task
        print(f"[{time.strftime('%X')}] Processed: {task}")
        self.last_run_time = time.monotonic()
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: Nginx (`limit_req`), Redis (Token Bucket structures), AWS API Gateway, Celery rate limits.
- **Why do it manually**: Grasping the mathematical concept of pacing execution time across an array of payloads allows you to build scrapers that won't get banned, or write microservice gateways that act as a strict firewall throttle against massive spikes in web traffic.

## 5. VALIDATION CRITERIA

- [ ] Successfully uses lists as a FIFO queue (using `pop(0)`).
- [ ] Correctly computes the fractional delay based on exactly when the _last_ transaction fired, rather than blindly sleeping.
- [ ] Assert calculation: Passing 5 tasks at a 2-task-per-second limit strictly results in a runtime of $>2.0$ seconds.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (True Token Bucket):** Currently, the limiter delays rigidly between _every_ request. Change it to a Token Bucket. The bucket holds exactly $X$ tokens. Tokens refill at the N/sec rate. This allows processing a sudden burst of requests immediately, before strictly slowing them down.
2. **Extension 2 (Optimize Data Structure):** Replace the native List (`queue`) with `collections.deque`. List's `pop(0)` takes $O(N)$ time, whereas Deque's `popleft()` takes $O(1)$ time. Run a `timeit` script with a queue size of 100,000 requests to prove Deque's superiority.
3. **Extension 3 (Multithreading Context):** Try placing the `process_queue()` function onto a background `Thread`. Now have a `while True` loop sporadically feeding `add_request()` bursts. You'll quickly see why List queue limits are dangerous without thread `Locks()`.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`time`).
