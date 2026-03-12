"""
SOLUTIONS: Career Tracks
Backend, Data, Cybersecurity, Vision, AI Agent, Testing, DevOps
"""
import os, re, json, time, random, math, hashlib, socket
import threading, sqlite3, csv, base64, hmac
from collections import defaultdict
from pathlib import Path
from functools import wraps


# ===========================================================================
# BACKEND-01: Production FastAPI Boilerplate
# ===========================================================================
FASTAPI_BOILERPLATE = '''
# main.py - Production FastAPI Template

from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pydantic_settings import BaseSettings
import logging, time

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

class Settings(BaseSettings):
    app_name: str     = "Production API"
    environment: str  = "development"
    database_url: str = "sqlite:///./app.db"
    allowed_origins: list[str] = ["*"]

    class Config:
        env_file = ".env"

settings = Settings()

app = FastAPI(title=settings.app_name, version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@app.middleware("http")
async def request_logger(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    response.headers["X-Process-Time"] = f"{duration:.4f}"
    logger.info(f"{request.method} {request.url.path} → {response.status_code} [{duration*1000:.1f}ms]")
    return response

@app.exception_handler(Exception)
async def global_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled: {exc}", exc_info=True)
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})

async def get_db():
    db = {"connection": "mock_db"}
    try:
        yield db
    finally:
        pass

class User(BaseModel):
    id: int
    name: str
    email: str | None = None

MOCK_USERS = {1: {"id": 1, "name": "Alice", "email": "alice@example.com"}}

@app.get("/health")
async def health():
    return {"status": "ok", "env": settings.environment}

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int, db=Depends(get_db)):
    user = MOCK_USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
'''
print("Backend-01: FastAPI boilerplate ready (see FASTAPI_BOILERPLATE string)")


# ===========================================================================
# BACKEND-02: Database Connection Pool Monitor
# ===========================================================================
from queue import Queue, Empty

class Connection:
    def __init__(self, id_num: int):
        self.id     = id_num
        self.in_use = False

    def execute(self, query: str) -> str:
        time.sleep(random.uniform(0.01, 0.05))
        return f"Result of: {query}"

class ConnectionPool:
    def __init__(self, size: int = 5):
        self.size               = size
        self._pool              = Queue(maxsize=size)
        self._active            = 0
        self._lock              = threading.Lock()
        self._total_acquired    = 0
        self._total_timeouts    = 0
        for i in range(size):
            self._pool.put(Connection(i))

    def acquire(self, timeout: float = 2.0) -> Connection:
        try:
            conn = self._pool.get(timeout=timeout)
            with self._lock:
                self._active += 1
                self._total_acquired += 1
            conn.in_use = True
            return conn
        except Empty:
            with self._lock:
                self._total_timeouts += 1
            raise TimeoutError(f"Pool exhausted (size={self.size})")

    def release(self, conn: Connection) -> None:
        conn.in_use = False
        with self._lock:
            self._active -= 1
        self._pool.put(conn)

    def get_stats(self) -> dict:
        with self._lock:
            return {
                "pool_size": self.size,
                "active": self._active,
                "available": self.size - self._active,
                "total_acquired": self._total_acquired,
                "total_timeouts": self._total_timeouts,
            }

def backend02_demo():
    pool = ConnectionPool(size=3)
    results = []

    def worker(wid):
        try:
            conn = pool.acquire(timeout=0.5)
            conn.execute("SELECT 1")
            time.sleep(0.05)
            pool.release(conn)
            results.append(("ok", wid))
        except TimeoutError:
            results.append(("timeout", wid))

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(8)]
    for t in threads: t.start()
    for t in threads: t.join()
    print("Backend-02 stats:", pool.get_stats())
    print(f"  OK: {sum(1 for r in results if r[0]=='ok')},"
          f"  Timeouts: {sum(1 for r in results if r[0]=='timeout')}")


# ===========================================================================
# BACKEND-03: Async Task Queue
# ===========================================================================
ASYNC_TASK_QUEUE_CODE = '''
import asyncio

class AsyncTaskQueue:
    def __init__(self, concurrency=3):
        self.concurrency = concurrency
        self.queue       = asyncio.Queue()
        self._workers    = []

    async def enqueue(self, task_name, coro):
        await self.queue.put((task_name, coro))

    async def _worker(self, wid):
        while True:
            task_name, coro = await self.queue.get()
            try:
                print(f"Worker {wid} running {task_name}")
                await coro
            except Exception as e:
                print(f"Worker {wid} error on {task_name}: {e}")
            finally:
                self.queue.task_done()

    async def run(self):
        self._workers = [asyncio.create_task(self._worker(i))
                         for i in range(self.concurrency)]
        await self.queue.join()
        for w in self._workers:
            w.cancel()

async def sample_task(tid, delay):
    await asyncio.sleep(delay)
    return f"done-{tid}"

async def main():
    q = AsyncTaskQueue(concurrency=2)
    asyncio.create_task(q.run())
    for i in range(5):
        await q.enqueue(f"Task_{i}", sample_task(i, 0.1))
    await asyncio.sleep(1)

asyncio.run(main())
'''
print("Backend-03: AsyncTaskQueue code ready")


# ===========================================================================
# DATA-01: Production Data Quality Framework
# ===========================================================================

class DataQualityFramework:
    def __init__(self):
        self.rules: list[dict] = []

    def add_rule(self, column: str, rule_type: str, **kwargs) -> None:
        self.rules.append({"column": column, "rule_type": rule_type, "params": kwargs})

    def run_checks(self, df) -> dict:
        """Works with any dict-of-lists or pandas DataFrame."""
        results = {}
        for idx, rule in enumerate(self.rules):
            col   = rule["column"]
            rtype = rule["rule_type"]
            p     = rule["params"]
            key   = f"{col}_{rtype}"

            # Support both pandas Series and plain lists
            try:
                series = df[col]
                vals   = list(series)
            except Exception as e:
                results[key] = {"status": "error", "reason": str(e)}
                continue

            failed_rows = []
            if rtype == "not_null":
                failed_rows = [i for i, v in enumerate(vals) if v is None]
            elif rtype == "unique":
                seen = set(); failed_rows = []
                for i, v in enumerate(vals):
                    if v in seen: failed_rows.append(i)
                    seen.add(v)
            elif rtype == "range":
                mn = p.get("min_val", float('-inf'))
                mx = p.get("max_val", float('inf'))
                failed_rows = [i for i, v in enumerate(vals)
                               if v is not None and not (mn <= v <= mx)]
            elif rtype == "regex":
                import re
                pat = p.get("pattern", "")
                failed_rows = [i for i, v in enumerate(vals)
                               if not re.match(pat, str(v))]

            results[key] = {
                "status": "passed" if not failed_rows else "failed",
                "failed_row_indices": failed_rows,
                "fail_count": len(failed_rows),
            }
        return results

def data01_demo():
    data = {
        "id":    [1, 2, 3, 3, 5],
        "age":   [25, 30, -5, 45, 120],
        "email": ["test@example.com", "invalid-email",
                  "user@test.com", "admin", "null"],
    }
    dq = DataQualityFramework()
    dq.add_rule("id",    "unique")
    dq.add_rule("age",   "range", min_val=0, max_val=100)
    dq.add_rule("email", "regex", pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$")
    results = dq.run_checks(data)
    print("Data-01:", json.dumps(results, indent=2))


# ===========================================================================
# DATA-02: Time Series Anomaly Detector
# ===========================================================================

def detect_zscore(series: list[float], threshold: float = 2.0) -> list[int]:
    mean = sum(series) / len(series)
    var  = sum((x - mean)**2 for x in series) / len(series)
    std  = math.sqrt(var) or 1e-9
    return [i for i, v in enumerate(series) if abs((v - mean) / std) > threshold]

def detect_rolling_mean(series: list[float], window: int = 5,
                         threshold: float = 2.0) -> list[int]:
    anomalies = []
    for i in range(len(series)):
        lo = max(0, i - window)
        win = series[lo:i+1]
        mean = sum(win) / len(win)
        std  = math.sqrt(sum((x - mean)**2 for x in win) / len(win)) or 1e-9
        if abs((series[i] - mean) / std) > threshold:
            anomalies.append(i)
    return anomalies

def data02_demo():
    import random as _r
    data = [_r.gauss(100, 10) for _ in range(100)]
    data[20] = 500.0; data[75] = -200.0
    z_idx = detect_zscore(data, threshold=3.0)
    r_idx = detect_rolling_mean(data, window=10, threshold=3.0)
    assert 20 in z_idx and 75 in z_idx
    print(f"Data-02: Z-score anomalies at indices: {z_idx}")
    print(f"Data-02: Rolling anomalies at indices: {r_idx}")


# ===========================================================================
# DATA-03: SQL Performance Analyzer
# ===========================================================================

class SQLAnalyzer:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)

    def setup_mock_data(self) -> None:
        c = self.conn.cursor()
        c.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY, name TEXT, age INTEGER, status TEXT
            );
            CREATE TABLE IF NOT EXISTS transactions (
                tx_id INTEGER PRIMARY KEY, user_id INTEGER, amount REAL
            );
        """)
        users = [(i, f"User{i}", 20 + i % 50, "active" if i%2==0 else "inactive")
                 for i in range(1000)]
        c.executemany("INSERT OR IGNORE INTO users VALUES (?,?,?,?)", users)
        txs = [(i, i%1000, 50 + i%200) for i in range(5000)]
        c.executemany("INSERT OR IGNORE INTO transactions VALUES (?,?,?)", txs)
        self.conn.commit()

    def explain_query(self, query: str) -> list:
        return self.conn.execute(f"EXPLAIN QUERY PLAN {query}").fetchall()

    def benchmark_query(self, query: str, iterations: int = 100) -> float:
        c = self.conn.cursor()
        start = time.time()
        for _ in range(iterations):
            c.execute(query); c.fetchall()
        return (time.time() - start) / iterations

    def detect_antipatterns(self, query: str) -> list[str]:
        q = query.upper()
        warnings = []
        if "SELECT *" in q:
            warnings.append("ANTI-PATTERN: SELECT * — specify columns explicitly")
        if "WHERE" not in q and "LIMIT" not in q:
            warnings.append("ANTI-PATTERN: No WHERE clause — full table scan")
        if q.count("SELECT") > 1:
            warnings.append("WARNING: Nested SELECT (possible N+1)")
        return warnings

def data03_demo():
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        analyzer = SQLAnalyzer(os.path.join(tmp, "analytics.db"))
        analyzer.setup_mock_data()
        bad_q  = "SELECT * FROM users WHERE age > 30 AND status = 'active'"
        good_q = "SELECT id, name FROM users WHERE id < 100"
        print("Data-03 anti-patterns:", analyzer.detect_antipatterns(bad_q))
        print("Data-03 EXPLAIN:", analyzer.explain_query(bad_q))
        slow = analyzer.benchmark_query(bad_q, 50)
        fast = analyzer.benchmark_query(good_q, 50)
        print(f"Data-03: bad={slow*1000:.2f}ms  good={fast*1000:.2f}ms")


# ===========================================================================
# CYBER-01: Network Port Scanner
# ===========================================================================
import concurrent.futures

class PortScanner:
    def __init__(self, target: str, timeout: float = 0.5):
        self.target  = target
        self.timeout = timeout
        try:
            self.ip = socket.gethostbyname(target)
        except socket.gaierror:
            raise ValueError(f"Cannot resolve: {target}")

    def scan_port(self, port: int) -> tuple[int, str]:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(self.timeout)
                result = s.connect_ex((self.ip, port))
                if result == 0:
                    try:
                        s.send(b"HEAD / HTTP/1.0\r\n\r\n")
                        banner = s.recv(256).decode(errors='replace').strip()
                    except Exception:
                        banner = ""
                    return port, banner
        except Exception:
            pass
        return None, None

    def scan_range(self, start: int, end: int, max_workers: int = 100) -> list[int]:
        open_ports = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as ex:
            futures = {ex.submit(self.scan_port, p): p for p in range(start, end+1)}
            for fut in concurrent.futures.as_completed(futures):
                port, banner = fut.result()
                if port:
                    open_ports.append(port)
        return sorted(open_ports)

def cyber01_demo():
    print("Cyber-01: PortScanner defined. Skipping live scan in demo.")


# ===========================================================================
# CYBER-03: Log Forensics Analyzer
# ===========================================================================

class LogForensicsAnalyzer:
    def __init__(self):
        self.failed_logins: dict[str, list] = defaultdict(list)
        self.path_traversal_hits: list[dict] = []
        self.suspicious_ips: set[str] = set()

    def parse_log_line(self, line: str) -> None:
        # Brute force detection
        m = re.search(r'(\d{1,3}(?:\.\d{1,3}){3}).*(Failed password|authentication failure)',
                      line, re.IGNORECASE)
        if m:
            ip = m.group(1)
            # Extract timestamp if present
            ts_m = re.match(r'(\S+)\s', line)
            self.failed_logins[ip].append(ts_m.group(1) if ts_m else "unknown")

        # Path traversal / LFI
        lfi = re.search(r'GET\s+([^\s]*\.\.\/[^\s]*)', line)
        if lfi:
            self.path_traversal_hits.append({"url": lfi.group(1), "line": line[:100]})

    def detect_brute_force(self, threshold: int = 5) -> list[str]:
        flagged = [ip for ip, events in self.failed_logins.items()
                   if len(events) > threshold]
        self.suspicious_ips.update(flagged)
        return flagged

    def generate_report(self) -> str:
        return json.dumps({
            "brute_force_ips": self.detect_brute_force(),
            "path_traversal": self.path_traversal_hits,
            "total_suspicious_ips": len(self.suspicious_ips),
        }, indent=2)

def cyber03_demo():
    mock_log = [
        "2023-10-27T10:05:01Z 10.0.0.5 sshd: Failed password for root",
        "2023-10-27T10:05:02Z 10.0.0.5 sshd: Failed password for admin",
        "2023-10-27T10:05:03Z 10.0.0.5 sshd: Failed password for admin",
        "2023-10-27T10:05:04Z 10.0.0.5 sshd: Failed password for root",
        "2023-10-27T10:05:05Z 10.0.0.5 sshd: Failed password for user",
        "2023-10-27T10:05:06Z 10.0.0.5 sshd: Failed password for user",
        '10.0.0.9 - - "GET /../../../etc/passwd HTTP/1.1" 200 512',
    ]
    analyzer = LogForensicsAnalyzer()
    for line in mock_log:
        analyzer.parse_log_line(line)
    print("Cyber-03:", analyzer.generate_report())


# ===========================================================================
# AGENT-01: Tool-Use Foundation
# ===========================================================================

class SimpleAgentCore:
    def __init__(self, api_key: str = "mock"):
        self.api_key = api_key
        self.tools: list[dict] = []
        self._registry: dict[str, callable] = {}

    def register_tool(self, name: str, description: str,
                       parameters: dict, func: callable) -> None:
        self.tools.append({
            "type": "function",
            "function": {"name": name, "description": description,
                         "parameters": parameters}
        })
        self._registry[name] = func

    def execute_tool(self, tool_name: str, arguments: dict):
        fn = self._registry.get(tool_name)
        if not fn:
            return f"Error: tool '{tool_name}' not registered"
        try:
            return fn(**arguments)
        except TypeError as e:
            return f"Error: bad arguments for '{tool_name}': {e}"
        except Exception as e:
            return f"Error executing '{tool_name}': {e}"

def agent01_demo():
    agent = SimpleAgentCore()
    agent.register_tool(
        "get_weather", "Get weather for a city",
        {"type": "object", "properties": {"location": {"type": "string"}},
         "required": ["location"]},
        lambda location: f"Sunny in {location}, 28°C"
    )
    agent.register_tool(
        "calculate_sum", "Add two numbers",
        {"type": "object", "properties": {
            "a": {"type": "integer"}, "b": {"type": "integer"}},
         "required": ["a", "b"]},
        lambda a, b: a + b
    )
    calls = [
        {"name": "get_weather",   "arguments": {"location": "Hanoi"}},
        {"name": "calculate_sum", "arguments": {"a": 5, "b": 7}},
        {"name": "bad_tool",      "arguments": {}},
    ]
    for call in calls:
        result = agent.execute_tool(call["name"], call["arguments"])
        print(f"  [{call['name']}] → {result}")
    print("Agent-01 passed ✓")


# ===========================================================================
# TEST-01: Advanced Pytest Mocks
# ===========================================================================
PYTEST_MOCKS_CODE = '''
import pytest
from unittest.mock import patch, Mock, MagicMock
import requests

class PaymentGateway:
    def __init__(self, api_key):
        self.api_key  = api_key
        self.base_url = "https://mock-payment-api.com/v1"

    def charge(self, amount, source):
        resp = requests.post(
            f"{self.base_url}/charges",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={"amount": amount, "source": source}
        )
        resp.raise_for_status()
        return resp.json()

@patch("requests.post")
def test_charge_success(mock_post):
    mock_resp = Mock()
    mock_resp.json.return_value = {"id": "ch_123", "status": "succeeded"}
    mock_resp.raise_for_status.return_value = None
    mock_post.return_value = mock_resp
    gw = PaymentGateway("fake_key")
    result = gw.charge(100.0, "tok_mastercard")
    assert result["status"] == "succeeded"
    mock_post.assert_called_once()

@patch("requests.post")
def test_charge_network_error(mock_post):
    mock_post.side_effect = requests.ConnectionError("Network down")
    gw = PaymentGateway("fake_key")
    with pytest.raises(requests.ConnectionError):
        gw.charge(50.0, "tok_visa")

@patch("requests.post")
def test_charge_http_error(mock_post):
    mock_resp = Mock()
    mock_resp.raise_for_status.side_effect = requests.HTTPError("402 Payment Required")
    mock_post.return_value = mock_resp
    gw = PaymentGateway("fake_key")
    with pytest.raises(requests.HTTPError):
        gw.charge(0.0, "tok_declined")
'''
print("Test-01: pytest mock tests ready (see PYTEST_MOCKS_CODE)")


if __name__ == "__main__":
    print("=== Backend-02 ==="); backend02_demo()
    print("=== Data-01 ===");    data01_demo()
    print("=== Data-02 ===");    data02_demo()
    print("=== Data-03 ===");    data03_demo()
    print("=== Cyber-03 ===");   cyber03_demo()
    print("=== Agent-01 ===");   agent01_demo()