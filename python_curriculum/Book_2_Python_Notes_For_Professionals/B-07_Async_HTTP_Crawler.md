# Exercise B-07: Async HTTP Crawler

## 1. EXERCISE BRIEF

**Context**: Scraping/Crawling hàng ngàn URL đồng bộ bị nghẽn mạng do mô hình chặn (blocking I/O). Async I/O là tiêu chuẩn tối cao để bẻ khoá nút cổ chai này.
**Task**: Implement một thuật toán Crawler không đồng bộ (Coroutines + `asyncio`) thu thập metadata từ danh sách API mock URL, hỗ trợ concurrent rate limiting thông qua semaphores.
**Constraints**: Sử dụng thuần `asyncio` base APIs và `aiohttp` / tương đương. Khống chế limit concurrent không vượt quá 10 worker cùng lúc.
## 2. STARTER CODE

```python
import asyncio
import time
# Requires running: pip install aiohttp
import aiohttp

async def fetch(session: aiohttp.ClientSession, url: str, semaphore: asyncio.Semaphore) -> tuple[str, int]:
    """
    TODO:
    1. Acquire the semaphore (blocks if 10 are already concurrently executing).
    2. Execute an async GET request to the URL.
    3. Return a tuple of (url, status_code).
    4. Handle exceptions cleanly (if URL fails, return (url, 0)).
    """
    pass

async def main_crawler(urls: list[str], max_concurrent: int = 10):
    """
    TODO:
    1. Instantiate an asyncio.Semaphore.
    2. Open an aiohttp.ClientSession().
    3. Create a list of 'tasks' by calling fetch() for each URL.
    4. Await all tasks using asyncio.gather().
    5. Return the list of (url, status) results.
    """
    pass

if __name__ == "__main__":
    # 50 mock URLs mapping to HTTPBin
    test_urls = [f"https://httpbin.org/status/{code}" for code in [200, 404, 500, 200, 201] * 10]

    start = time.time()

    # In python 3.7+, simply run the main event loop
    results = asyncio.run(main_crawler(test_urls, max_concurrent=10))

    duration = time.time() - start

    print(f"Crawled {len(results)} URLs in {duration:.2f} seconds.")

    # If this was sequential, 50 requests * ~0.2s = 10+ seconds.
    # Concurrent with a semaphore of 10, it should reliably execute in under 3 seconds globally.
    assert duration < 5.0
    assert len(results) == 50
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
`asyncio.Semaphore` operates as a gatekeeper, ensuring that the critical section of a network request utilizing an `async with semaphore:` block is only entered by a fixed number of coroutines simultaneously.

**HINT-2 (Partial)**:
For the `fetch` function:

```python
async def fetch(session, url, semaphore):
    async with semaphore:
        try:
            async with session.get(url, timeout=3) as response:
                return (url, response.status)
        except Exception:
            return (url, 0)
```

**HINT-3 (Near-solution)**:
For the `main_crawler` assembly block:

```python
async def main_crawler(urls: list[str], max_concurrent=10):
    sem = asyncio.Semaphore(max_concurrent)
    tasks = []

    # We use a single session natively to utilize HTTP Keep-Alive
    async with aiohttp.ClientSession() as session:
        for url in urls:
            task = fetch(session, url, sem)
            tasks.append(task)

        # gather executes them concurrently dynamically
        results = await asyncio.gather(*tasks)
        return results
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `aiohttp`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Correctly utilizes `async/await` syntax for non-blocking I/O.
- [ ] Safely limits concurrent requests using `asyncio.Semaphore`.
- [ ] Bypasses synchronous time limits by executing hundreds of requests in parallel efficiently.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Timeout Fallback):** Even with async, some requests might hang. Wrap the fetch coroutine in `asyncio.wait_for(task, timeout=2.0)` inside the `fetch` wrapper block. If it times out, catch the `asyncio.TimeoutError` and return `(url, -1)`.
2. **Extension 2 (Real Time Reporting):** `asyncio.gather` returns nothing until ALL operations conclude successfully. Switch to utilizing `asyncio.as_completed(tasks)`. Loop through the results as they arrive _the exact millisecond_ they return from the network.
3. **Extension 3 (Async Queue Workers):** Instead of a strict list iteration, build an `asyncio.Queue`. Fill it with 1000 URLs and spawn 10 "Worker Tasks" holding loops indefinitely popping URLs for processing until the queue is empty.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Virtual Environment recommended
- **Dependencies**: `pip install aiohttp`
