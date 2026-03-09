# Exercise A-07: Retry Logic with Backoff

## 1. EXERCISE BRIEF

**Context**: Reaching out to third-party services over a network is fundamentally unreliable. Servers drop requests, cables get unplugged, APIs rate limit you. A professional application never crashes on the first failed network block—it retries smartly. Calling immediately risks overwhelming an already struggling server, so we use "exponential backoff".
**Task**: Build a Python decorator `retry(max_attempts, base_delay, exceptions)` from scratch. It should catch specified exceptions within any decorated function, pause execution (`time.sleep()`) for an exponentially increasing delay, and try again. After `max_attempts`, it must raise the exception normally.
**Constraints**: Do **NOT** use libraries like `tenacity` or `backoff`. You must use pure Python loops, `time.sleep`, and decorators. You must add a "jitter" factor to the sleep duration to avoid the "Thundering Herd" problem.

## 2. STARTER CODE

```python
import time
import random
from functools import wraps

# Custom exception to simulate a flaky network
class FlakyNetworkError(Exception): pass

def retry(max_attempts=3, base_delay=1.0, exceptions=(Exception,)):
    """
    TODO: Build the retry decorator.
    - Catch the exceptions provided in `exceptions`.
    - If caught, sleep for: (base_delay * 2 ** attempt) + random_jitter
    - Where random_jitter is a small float (e.g. 0.1 to 1.0)
    - If `max_attempts` is reached, re-raise the final exception.
    """
    pass

if __name__ == "__main__":
    # Test scaffolding
    attempts_made = 0

    @retry(max_attempts=4, base_delay=0.5, exceptions=(FlakyNetworkError,))
    def flaky_api_call():
        global attempts_made
        attempts_made += 1
        print(f"Attempting API call... (Attempt {attempts_made})")
        if attempts_made < 3:
            raise FlakyNetworkError("Connection timed out!")
        return "SUCCESS!"

    start = time.time()
    result = flaky_api_call()
    duration = time.time() - start

    # 2 failures + 1 success.
    # Retry 1: ~0.5s * (2**0) = ~0.5s
    # Retry 2: ~0.5s * (2**1) = ~1.0s
    # Total wait: ~1.5s + jitter
    assert result == "SUCCESS!"
    assert attempts_made == 3
    print(f"Completed in {duration:.2f} seconds")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
A decorator that takes arguments (`@retry(args...)`) requires _three_ levels of nested functions.

```python
def retry(args):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Your looping logic here
        return wrapper
    return decorator
```

**HINT-2 (Partial)**:
Inside the wrapper, run a loop up to `max_attempts`. Use a `try/except` block targeting the tuple of `exceptions` passed into the decorator factory. Wait, calculate the sleep, call `time.sleep()`.

**HINT-3 (Near-solution)**:

```python
for attempt in range(max_attempts):
    try:
        return func(*args, **kwargs)
    except exceptions as e:
        if attempt == max_attempts - 1: # Last attempt failed
            raise

        jitter = random.uniform(0.1, 0.5)
        sleep_time = (base_delay * (2 ** attempt)) + jitter
        print(f"Failed. Retrying in {sleep_time:.2f}s...")
        time.sleep(sleep_time)
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `tenacity`, `backoff`, Requests `Retry` adapter, AWS Boto3 automatic retries.
- **Why do it manually**: Relying blindly on `tenacity` is great until you need a specific backoff formula to comply with an API's harsh rate-limiting terms (like waiting exactly until a `RateLimit-Reset` header says so). Building it yourself ensures you can inject custom logic into the try/catch loop before giving up.

## 5. VALIDATION CRITERIA

- [ ] Decorator correctly passes arguments down into the wrapped function using `*args, **kwargs` and `@wraps`.
- [ ] Retries perfectly up to the allowed limit and then re-raises the error successfully to the caller.
- [ ] Applies exponential calculations (`2 ** attempt`) to stretch the timeouts longer on repeated failures.
- [ ] Applies a random jitter so identical failing processes do not synchronize to smack the server simultaneously again ("thundering herd").

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Circuit Breaker):** Implement a simple Circuit Breaker alongside `retry`. If the decorator hits `max_attempts`, trip the breaker so subsequent calls to that function immediately fail (raising a `CircuitBrokenError`) without retrying or waiting for the next 30 seconds.
2. **Extension 2 (Logging Hook):** Allow passing an optional `logger_func` to the decorator. Instead of `print`, the retry logic uses the provided function to log failed attempts and wait times cleanly into a file.
3. **Extension 3 (Asyncio):** Write an `async` version (`@async_retry`) using `asyncio.sleep` so it can decorate `async def` functions in FastAPI without blocking the event loop.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
