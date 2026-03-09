# Exercise B-07: Async HTTP Crawler

## 1. EXERCISE BRIEF

**Context**: Reaching out to external websites is "I/O Bound"—your CPU spends 99% of its time literally doing nothing, just waiting for the network packets to arrive. Scanning 50 websites using a standard `for` loop natively executes sequentially (URL 1 starts, waits, finishes. URL 2 starts...). Asynchronous Python (`asyncio`) allows launching all 50 TCP requests concurrently seamlessly on a single CPU thread.
**Task**: Build an Async HTTP Crawler. Take a list of 50 test URLs. Implement an `async def fetch()` function gathering the HTTP Status Code for a single URL. Execute all `fetch` commands concurrently utilizing `asyncio.gather`. Limit the concurrency to exactly 10 simultaneous connections using `asyncio.Semaphore` natively avoiding flooding the OS sockets.
**Constraints**: Do **NOT** use `requests` natively (it is strictly blocking globally). You must use `aiohttp` or `httpx` asynchronously.

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
`asyncio.Semaphore` operates mathematically identically to a lock. Wrap your network request utilizing an `async with semaphore:` context manager natively holding the execution token continuously.

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

- **Libraries/Tools**: `aiohttp`, `httpx`, `FastAPI`, `Scrapy`.
- **Why do it manually**: Relying strictly on basic python `requests` chokes massive scale operations natively. Building async semaphores demonstrates understanding exactly how event-loops shuffle tasks gracefully during "dead time" (network waits) functionally scaling web scraping 100x faster globally.

## 5. VALIDATION CRITERIA

- [ ] Correctly utilizes `async/await` syntax structurally natively.
- [ ] Safe execution gracefully avoids crushing connection limits cleanly explicitly via `#Semaphore`.
- [ ] Bypasses synchronous time limits cleanly executing 50 massive requests structurally reliably in fractional time thresholds cleanly cleanly.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Timeout Fallback):** Even with async, a dead server can hang a connection endlessly globally. Integrate `asyncio.wait_for(task, timeout=2.0)` inside the `fetch` wrapper block. If it times out inherently natively, catch `asyncio.TimeoutError` exclusively safely returning `(url, -1)`.
2. **Extension 2 (Real Time Reporting):** `asyncio.gather` returns nothing until ALL operations conclude successfully. Switch to utilizing `asyncio.as_completed(tasks)`. Loop across it functionally printing status codes _the exact millisecond_ they return globally progressively.
3. **Extension 3 (Async Queue Workers):** Instead of a strict list iteration, build an `asyncio.Queue`. Fill it with 1000 URLs continually dynamically. Launch exactly 10 "Worker Tasks" holding loops indefinitely popping URLs structurally cleanly simulating an active scraping engine.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Virtual Environment recommended
- **Dependencies**: `pip install aiohttp`
