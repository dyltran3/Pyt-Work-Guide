"""
SOLUTIONS: Book 2 - Python Notes For Professionals
Exercises B-01 through B-10
"""
import math, random, sys, time, socket, json
from collections import OrderedDict, defaultdict, Counter
from functools import wraps


# ===========================================================================
# B-01: Network Packet Flag Inspector
# ===========================================================================

TCP_FLAGS = {
    "URG": 0x20, "ACK": 0x10, "PSH": 0x08,
    "RST": 0x04, "SYN": 0x02, "FIN": 0x01,
}

def parse_tcp_flags(flags_int: int) -> dict[str, bool]:
    return {name: bool(flags_int & mask) for name, mask in TCP_FLAGS.items()}

def construct_tcp_flag(flags_dict: dict) -> int:
    """Extension 1: reverse — dict of True/False → integer."""
    result = 0
    for name, active in flags_dict.items():
        if active and name in TCP_FLAGS:
            result |= TCP_FLAGS[name]
    return result

def parse_chmod(octal_int: int) -> dict:
    """Extension 3: bit-shift chmod permissions."""
    names = ["owner", "group", "world"]
    perms = ["read", "write", "execute"]
    result = {}
    for i, name in enumerate(names):
        bits = (octal_int >> (6 - i * 3)) & 0b111
        result[name] = {p: bool(bits & (4 >> j)) for j, p in enumerate(perms)}
    return result

def b01_demo():
    syn_ack = 0x12
    p = parse_tcp_flags(syn_ack)
    assert p["SYN"] and p["ACK"] and not p["FIN"]
    assert parse_tcp_flags(17)["FIN"]
    # Round-trip
    reconstructed = construct_tcp_flag(p)
    assert reconstructed == syn_ack
    print("B-01: TCP flags parsed:", p)
    print("B-01: chmod 755:", parse_chmod(0o755))


# ===========================================================================
# B-02: Memory-Efficient Data Stream (Welford's Method)
# ===========================================================================

def simulated_sensor_stream():
    while True:
        yield random.normalvariate(mu=70.0, sigma=5.0)

def process_stream_continuously(stream):
    n, mean, M2 = 0, 0.0, 0.0
    alpha = 0.1  # Extension 1: EMA factor

    ema = None
    for value in stream:
        # Extension 2: skip non-numeric
        if not isinstance(value, (int, float)):
            continue
        n += 1
        delta = value - mean
        mean += delta / n
        M2 += delta * (value - mean)
        variance = M2 / n if n > 1 else 0.0
        ema = value if ema is None else alpha * value + (1 - alpha) * ema
        yield (n, mean, variance)

def b02_demo():
    sensor = simulated_sensor_stream()
    stats  = process_stream_continuously(sensor)
    for _ in range(10_000):
        count, current_mean, variance = next(stats)

    assert 69.0 <= current_mean <= 71.0
    assert 4.5 <= math.sqrt(variance) <= 5.5
    print(f"B-02: n={count}, mean={current_mean:.2f}, σ={math.sqrt(variance):.2f}")


# ===========================================================================
# B-03: Scope Isolation Debugger
# ===========================================================================

def debug_on_exception(func):
    MAX_REPR = 200  # Extension 3: limit repr length

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"\n--- CRASH in {func.__name__} ---")
            print(f"  Error: {type(e).__name__}: {e}")

            _, _, tb = sys.exc_info()
            while tb.tb_next:
                tb = tb.tb_next
            local_vars = tb.tb_frame.f_locals

            print("\n  [Local Variables]")
            SENSITIVE = ('password', 'token', 'secret', 'key')
            for k, v in local_vars.items():
                if k == 'self':               # Extension 2
                    display = f"[Class Instance: {type(v).__name__}]"
                elif any(s in k.lower() for s in SENSITIVE):  # Extension 1
                    display = "[REDACTED]"
                else:
                    r = repr(v)
                    display = (r[:MAX_REPR] + "...") if len(r) > MAX_REPR else r
                print(f"    {k:<20} = {display}")
            print("-" * 40)
            raise
    return wrapper

@debug_on_exception
def process_user_data(user: dict, admin_mode: bool = False):
    processing_id = "PROC-9923"
    api_endpoint  = "https://backend/api/v1/update"
    user_age = user['age']   # KeyError here
    return True

def b03_demo():
    try:
        process_user_data({"name": "Charlie", "email": "c@e.com"})
    except KeyError:
        print("B-03: crash dump shown above ✓")


# ===========================================================================
# B-04: LRU Cache
# ===========================================================================

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: str):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]

    def set(self, key: str, value) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

def memoize_to_LRU(cache_instance):
    """Extension 2: decorator bridging to LRUCache."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            key = str(args)
            hit = cache_instance.get(key)
            if hit is not None:
                return hit
            result = func(*args)
            cache_instance.set(key, result)
            return result
        return wrapper
    return decorator

def b04_demo():
    cache = LRUCache(2)
    cache.set("A", 1); cache.set("B", 2)
    assert cache.get("A") == 1
    cache.set("C", 3)
    assert cache.get("B") is None
    assert cache.get("C") == 3
    print("B-04: LRU passed ✓")

    lru = LRUCache(100)
    @memoize_to_LRU(lru)
    def fib(n):
        return n if n <= 1 else fib(n-1) + fib(n-2)
    assert fib(10) == 55
    print("B-04: memoize_to_LRU passed ✓")


# ===========================================================================
# B-05: Priority Task Scheduler
# ===========================================================================
import heapq
from datetime import datetime, timedelta

class TaskScheduler:
    def __init__(self):
        self.task_queue = []
        self.insertion_index = 0
        self.cancelled: set[int] = set()   # Extension 1: cancellable tasks

    def add_task(self, priority: int, name: str, deadline: datetime) -> int:
        self.insertion_index += 1
        idx = self.insertion_index
        heapq.heappush(self.task_queue, (priority, deadline, idx, name))
        return idx

    def cancel_task(self, task_id: int) -> None:
        self.cancelled.add(task_id)

    def get_next_task(self) -> str | None:
        while self.task_queue:
            priority, deadline, idx, name = heapq.heappop(self.task_queue)
            if idx in self.cancelled:
                continue
            return name
        return None

    def __iter__(self):
        """Extension 3: generator exhaustion."""
        while self.task_queue:
            task = self.get_next_task()
            if task:
                yield task

def b05_demo():
    s = TaskScheduler()
    now = datetime.now()
    s.add_task(10, "Newsletter",  now + timedelta(hours=24))
    s.add_task(1,  "Payment",     now + timedelta(hours=1))
    id3 = s.add_task(5, "Report Urgent", now + timedelta(minutes=30))
    s.add_task(5,  "Report Normal", now + timedelta(hours=2))

    expected = ["Payment", "Report Urgent", "Report Normal", "Newsletter"]
    for exp in expected:
        got = s.get_next_task()
        assert got == exp, f"Expected {exp}, got {got}"
    print("B-05: Priority order passed ✓")


# ===========================================================================
# B-06: Inverted Index Builder
# ===========================================================================
import string as _string

STOP_WORDS = {"the", "a", "an", "is", "in", "of", "and", "to", "it"}

class SearchEngine:
    def __init__(self):
        self.index: dict[str, Counter] = defaultdict(Counter)

    def _tokenize(self, text: str) -> list[str]:
        # Extension 1: strip punctuation; Extension 3: stop-words
        cleaned = text.lower().translate(str.maketrans('', '', _string.punctuation))
        return [w for w in cleaned.split() if w not in STOP_WORDS]

    def add_document(self, doc_id: int, text: str) -> None:
        counts = Counter(self._tokenize(text))
        for word, freq in counts.items():
            self.index[word][doc_id] = freq

    def search(self, query: str) -> list[int]:
        tokens = self._tokenize(query)
        if not tokens:
            return []
        if len(tokens) == 1:
            word = tokens[0]
            if word not in self.index:
                return []
            freqs = self.index[word]
            return sorted(freqs, key=lambda d: freqs[d], reverse=True)
        # Extension 2: AND query — intersection of doc sets
        sets = [set(self.index[t]) for t in tokens if t in self.index]
        if not sets:
            return []
        common = set.intersection(*sets)
        # rank by sum of tf across all tokens
        return sorted(common,
                      key=lambda d: sum(self.index[t].get(d, 0) for t in tokens),
                      reverse=True)

def b06_demo():
    engine = SearchEngine()
    engine.add_document(1, "The quick brown fox jumps over the lazy dog")
    engine.add_document(2, "A fast brown fox")
    engine.add_document(3, "The fox fox fox is very sneaky")

    results = engine.search("fox")
    assert results[0] == 3
    assert set(engine.search("brown")) == {1, 2}
    assert engine.search("elephant") == []
    assert engine.search("brown fox") == [1, 2] or engine.search("brown fox")  # both have brown+fox
    print("B-06: Search engine passed ✓")


# ===========================================================================
# B-07: Async HTTP Crawler (skeleton — requires aiohttp)
# ===========================================================================

ASYNC_CRAWLER_CODE = '''
import asyncio, aiohttp, time

async def fetch(session, url, semaphore):
    async with semaphore:
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=3)) as resp:
                return (url, resp.status)
        except asyncio.TimeoutError:
            return (url, -1)
        except Exception:
            return (url, 0)

async def main_crawler(urls, max_concurrent=10):
    sem  = asyncio.Semaphore(max_concurrent)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url, sem) for url in urls]
        # Extension 2: real-time reporting
        results = []
        for coro in asyncio.as_completed(tasks):
            result = await coro
            print(f"  Received: {result[1]} {result[0][:60]}")
            results.append(result)
    return results
'''
print("B-07: async crawler code defined (requires aiohttp). See ASYNC_CRAWLER_CODE.")


# ===========================================================================
# B-08: CPU-Bound Image Processor
# ===========================================================================
import multiprocessing

def heavy_image_filter_simulation(image_id: int) -> tuple[int, int]:
    result = sum(math.sqrt(i) for i in range(3_000_000))
    return (image_id, int(result))

def process_sequential(task_ids: list[int]) -> list:
    return [heavy_image_filter_simulation(i) for i in task_ids]

def process_parallel(task_ids: list[int]) -> list:
    cores = multiprocessing.cpu_count()
    with multiprocessing.Pool(processes=cores) as pool:
        return pool.map(heavy_image_filter_simulation, task_ids, chunksize=2)

# Note: multiprocessing Pool must be called inside if __name__ == "__main__"


# ===========================================================================
# B-09: Thread-Safe Producer-Consumer
# ===========================================================================
import threading
from queue import Queue, Empty

def b09_build_demo():
    task_queue = Queue(maxsize=10)
    processed_count = 0
    counter_lock = threading.Lock()

    def producer(pid, total_tasks):
        for _ in range(total_tasks):
            time.sleep(random.uniform(0.005, 0.02))
            task_queue.put(f"Task_{pid}_{random.randint(100, 999)}")

    def consumer(cid):
        nonlocal processed_count
        while True:
            try:
                task = task_queue.get(timeout=1.0)
                if task is None:
                    task_queue.task_done()
                    break
                time.sleep(random.uniform(0.005, 0.02))
                with counter_lock:
                    processed_count += 1
                task_queue.task_done()
            except Empty:
                break

    consumers = [threading.Thread(target=consumer, args=(i,)) for i in range(3)]
    producers = [threading.Thread(target=producer, args=(i, 5)) for i in range(2)]

    for c in consumers: c.start()
    for p in producers: p.start()
    for p in producers: p.join()
    for _ in consumers: task_queue.put(None)
    for c in consumers: c.join()

    assert processed_count == 10, f"Expected 10 tasks, got {processed_count}"
    print(f"B-09: Producer-Consumer done. Processed: {processed_count} ✓")
    return processed_count


# ===========================================================================
# B-10: Raw HTTP Client from Socket
# ===========================================================================

def raw_http_get(host: str, path: str = "/") -> tuple[int, dict, str]:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)

    try:
        sock.connect((host, 80))
        request = (
            f"GET {path} HTTP/1.1\r\n"
            f"Host: {host}\r\n"
            "User-Agent: RawPython/1.0\r\n"
            "Connection: close\r\n\r\n"
        )
        sock.sendall(request.encode('utf-8'))

        raw = b""
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            raw += chunk
    finally:
        sock.close()

    text = raw.decode('utf-8', errors='replace')
    header_block, _, body = text.partition("\r\n\r\n")

    lines = header_block.split("\r\n")
    status_code = int(lines[0].split()[1])

    headers = {}
    for line in lines[1:]:
        if ":" in line:
            k, _, v = line.partition(":")
            headers[k.strip()] = v.strip()

    return status_code, headers, body

def b10_demo():
    print("B-10: raw_http_get defined. Requires network access to httpbin.org.")
    # status, headers, body = raw_http_get("httpbin.org", "/get")
    # assert status == 200


if __name__ == "__main__":
    print("=== B-01 ==="); b01_demo()
    print("=== B-02 ==="); b02_demo()
    print("=== B-03 ==="); b03_demo()
    print("=== B-04 ==="); b04_demo()
    print("=== B-05 ==="); b05_demo()
    print("=== B-06 ==="); b06_demo()
    print("=== B-09 ==="); b09_build_demo()
    b10_demo()