"""
SOLUTIONS: Book 1 - Learn Python The Hard Way (Applied)
Exercises A-09 through A-15
"""
import time
import random
import inspect
import traceback
import json
from pathlib import Path
from collections import deque
from functools import wraps


# ===========================================================================
# A-09: Rate Limiter Queue
# ===========================================================================

class RateLimiter:
    def __init__(self, max_per_second: int):
        self.max_per_second = max_per_second
        self.delay = 1.0 / max_per_second
        self.queue: deque = deque()          # O(1) popleft — Extension 2
        self.last_run_time: float = 0.0

    def add_request(self, payload: str) -> None:
        self.queue.append(payload)

    def process_queue(self) -> None:
        while self.queue:
            task = self.queue.popleft()

            now = time.monotonic()
            elapsed = now - self.last_run_time
            if elapsed < self.delay:
                time.sleep(self.delay - elapsed)

            print(f"[{time.strftime('%X')}] Processed: {task}")
            self.last_run_time = time.monotonic()

    # Extension 1 — Token Bucket variant
    class TokenBucket:
        def __init__(self, capacity: int, refill_rate: float):
            self.capacity = capacity
            self.tokens = float(capacity)
            self.refill_rate = refill_rate   # tokens / second
            self._last = time.monotonic()

        def consume(self) -> bool:
            now = time.monotonic()
            self.tokens = min(self.capacity,
                              self.tokens + (now - self._last) * self.refill_rate)
            self._last = now
            if self.tokens >= 1:
                self.tokens -= 1
                return True
            return False

def a09_demo():
    limiter = RateLimiter(max_per_second=2)
    for i in range(5):
        limiter.add_request(f"Task_{i}")
    start = time.time()
    limiter.process_queue()
    duration = time.time() - start
    assert duration >= 2.0, f"Duration was only {duration:.2f}s"
    print(f"A-09: Queue done in {duration:.2f}s ✓")


# ===========================================================================
# A-10: Dependency Resolver (Topological Sort — DFS)
# ===========================================================================

def resolve_dependencies(graph: dict[str, list[str]]) -> list[str]:
    # Extension 1: detect missing packages
    for node, deps in graph.items():
        for dep in deps:
            if dep not in graph:
                raise KeyError(f"Missing package resolution for '{dep}'")

    visited: set[str] = set()
    temp_path: set[str] = set()
    order: list[str] = []
    path_stack: list[str] = []   # Extension 2: show loop path

    def dfs(node: str) -> None:
        if node in temp_path:
            cycle_start = path_stack.index(node)
            cycle = " -> ".join(path_stack[cycle_start:]) + f" -> {node}"
            raise ValueError(f"Circular dependency detected: {cycle}")
        if node in visited:
            return
        temp_path.add(node)
        path_stack.append(node)
        for child in graph.get(node, []):
            dfs(child)
        path_stack.pop()
        temp_path.discard(node)
        visited.add(node)
        order.append(node)

    for node in graph:
        dfs(node)
    return order

def a10_demo():
    valid = {'D': ['B', 'C'], 'C': ['B'], 'B': ['A'], 'A': []}
    order = resolve_dependencies(valid)
    assert order.index('A') < order.index('B') < order.index('C') < order.index('D')
    print("A-10 order:", order)

    try:
        resolve_dependencies({'A': ['B'], 'B': ['C'], 'C': ['A']})
    except ValueError as e:
        print("A-10 circular caught:", e)


# ===========================================================================
# A-11: Plugin Architecture
# ===========================================================================

class TextPlugin:
    def process(self, text: str) -> str:
        raise NotImplementedError

class StripSpacesPlugin(TextPlugin):
    def process(self, text: str) -> str:
        return text.strip()

class LowercasePlugin(TextPlugin):
    def process(self, text: str) -> str:
        return text.lower()

class CensorPlugin(TextPlugin):
    def __init__(self, bad_word: str):
        self.bad_word = bad_word.lower()

    def process(self, text: str) -> str:
        return text.replace(self.bad_word, "***")

class Pipeline:
    def __init__(self):
        self._plugins: list[TextPlugin] = []

    def register(self, plugin: TextPlugin) -> None:
        self._plugins.append(plugin)

    def run(self, text: str) -> str:
        # Extension 3: timing analytics
        import time as _t
        timings = []
        current = text
        for p in self._plugins:
            t0 = _t.monotonic()
            try:
                current = p.process(current)
            except Exception as e:
                print(f"[Pipeline] {p.__class__.__name__} crashed: {e}")
            timings.append((p.__class__.__name__, (_t.monotonic() - t0) * 1000))
        for name, ms in sorted(timings, key=lambda x: -x[1]):
            print(f"  {name}: {ms:.3f}ms")
        return current

def a11_demo():
    p = Pipeline()
    p.register(StripSpacesPlugin())
    p.register(LowercasePlugin())
    p.register(CensorPlugin(bad_word="heck"))
    result = p.run("   What the HECK is this?   ")
    assert result == "what the *** is this?", repr(result)
    print("A-11:", result)


# ===========================================================================
# A-12: ORM-lite Table Mapper
# ===========================================================================

def _is_match(row: dict, conditions: dict | None) -> bool:
    if not conditions:
        return True
    for k, v in conditions.items():
        # Extension 1: operator syntax  age__gt, age__lt, name__contains
        if '__' in k:
            field, op = k.rsplit('__', 1)
            val = row.get(field)
            if op == 'gt' and not (val > v): return False
            elif op == 'lt' and not (val < v): return False
            elif op == 'contains' and v not in str(val): return False
        else:
            if row.get(k) != v:
                return False
    return True

class Table:
    def __init__(self, name: str):
        self.name = name
        self._data: list[dict] = []
        self._next_id = 1
        self._index: dict[int, dict] = {}  # Extension 2: O(1) id lookup

    def insert(self, record: dict) -> int:
        row = {**record, 'id': self._next_id}
        self._data.append(row)
        self._index[self._next_id] = row
        self._next_id += 1
        return row['id']

    def select(self, where: dict = None) -> list[dict]:
        if where and list(where.keys()) == ['id']:
            r = self._index.get(where['id'])
            return [r] if r else []
        return [r for r in self._data if _is_match(r, where)]

    def update(self, where: dict, set_data: dict) -> int:
        count = 0
        for row in self._data:
            if _is_match(row, where):
                row.update(set_data)
                count += 1
        return count

    def delete(self, where: dict) -> int:
        before = len(self._data)
        self._data = [r for r in self._data if not _is_match(r, where)]
        self._index = {r['id']: r for r in self._data}
        return before - len(self._data)

def a12_demo():
    users = Table("users")
    users.insert({"name": "Alice", "age": 30})
    users.insert({"name": "Bob",   "age": 25})
    users.insert({"name": "Charlie", "age": 30})
    assert len(users.select()) == 3
    assert len(users.select(where={"age": 30})) == 2
    assert users.update(where={"name": "Alice"}, set_data={"age": 31}) == 1
    assert users.select(where={"name": "Alice"})[0]["age"] == 31
    users.delete(where={"age": 25})
    assert len(users.select()) == 2
    # Extension 1: operator queries
    assert len(users.select(where={"age__gt": 29})) == 2
    print("A-12: all ORM assertions passed.")


# ===========================================================================
# A-13: Service Health Monitor
# ===========================================================================

class ServiceCheck:
    def __init__(self, name: str):
        self.name = name

    def check(self) -> dict:
        raise NotImplementedError

class HTTPCheck(ServiceCheck):
    def __init__(self, name: str, url: str):
        super().__init__(name)
        self.url = url

    def check(self) -> dict:
        import random, time
        latency = random.uniform(10, 200)
        status = "up" if random.random() > 0.1 else "down"
        return {"status": status, "latency_ms": round(latency, 1)}

class DatabaseCheck(ServiceCheck):
    def check(self) -> dict:
        is_up = random.random() > 0.15
        if is_up:
            return {"status": "up", "connections": random.randint(1, 50)}
        return {"status": "down", "error": "Connection timeout"}

class DiskCheck(ServiceCheck):
    def check(self) -> dict:
        import shutil
        usage = shutil.disk_usage("/")
        free_gb = round(usage.free / (1024 ** 3), 2)
        status = "up" if free_gb > 1.0 else "warning"
        return {"status": status, "free_space_gb": free_gb}

class HealthReport:
    def __init__(self):
        self._services: list[ServiceCheck] = []

    def add_service(self, service: ServiceCheck):
        self._services.append(service)

    @property
    def system_status(self) -> str:       # Extension 1: @property
        results = [s.check() for s in self._services]
        if any(r.get("status") == "down" for r in results):
            return "DOWN"
        if any(r.get("status") == "warning" for r in results):
            return "DEGRADED"
        return "UP"

    def generate_report(self) -> str:
        import asyncio

        report = {"services": {}, "system_status": "UP"}
        for srv in self._services:
            result = srv.check()
            report["services"][srv.name] = result
            if result.get("status") == "down":
                report["system_status"] = "DOWN"
            elif result.get("status") == "warning" and report["system_status"] == "UP":
                report["system_status"] = "DEGRADED"
        return json.dumps(report, indent=2)

def a13_demo():
    monitor = HealthReport()
    monitor.add_service(DatabaseCheck("master_db"))
    monitor.add_service(HTTPCheck("payment_api", "https://api.stripe.com/health"))
    monitor.add_service(DiskCheck("disk"))
    print("A-13:", monitor.generate_report())


# ===========================================================================
# A-14: Project Scaffold Generator
# ===========================================================================

def create_file_safe(path: Path, content: str):
    if not path.exists():
        path.write_text(content.strip() + "\n", encoding="utf-8")
        print(f"  Created: {path}")
    else:
        print(f"  Exists:  {path}")

def generate_scaffold(project_name: str, dry_run: bool = False) -> None:
    base  = Path(project_name)
    src   = base / "src" / project_name
    tests = base / "tests"
    docs  = base / "docs"
    ci    = base / ".github" / "workflows"

    dirs = [src, tests, docs, ci]
    files = {
        src / "__init__.py": "",
        tests / "__init__.py": "",
        base / ".gitignore": ".venv/\n__pycache__/\n*.pyc\n.pytest_cache/\ndist/\n*.egg-info/",
        base / "requirements.txt": "# Add project dependencies here",
        base / "README.md": f"# {project_name.capitalize()}\n\nA new Python application.",
        base / "pyproject.toml": (
            f'[project]\nname = "{project_name}"\nversion = "0.1.0"\n'
            f'requires-python = ">=3.11"\n'
        ),
        ci / "test.yml": (
            "name: Tests\non: [push, pull_request]\n"
            "jobs:\n  test:\n    runs-on: ubuntu-latest\n"
            "    strategy:\n      matrix:\n        python-version: ['3.11', '3.12']\n"
            "    steps:\n      - uses: actions/checkout@v4\n"
            "      - uses: actions/setup-python@v5\n"
            "        with:\n          python-version: ${{ matrix.python-version }}\n"
            "      - run: pip install pytest\n      - run: pytest\n"
        ),
    }

    if dry_run:
        print("[DRY RUN] Would create:")
        for d in dirs:    print(f"  DIR  {d}")
        for fp in files:  print(f"  FILE {fp}")
        return

    # Check write permission
    try:
        base.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        print(f"ERROR: No write permission for {base.parent}")
        return

    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
    for fp, content in files.items():
        create_file_safe(fp, content)

    print(f"Project '{project_name}' scaffolded at {base.absolute()}")

def a14_demo():
    generate_scaffold("demo_project", dry_run=True)
    generate_scaffold("demo_project")
    generate_scaffold("demo_project")  # idempotent: no FileExistsError
    print("A-14 done.")


# ===========================================================================
# A-15: Contract Testing Framework (mini pytest clone)
# ===========================================================================

class TestCase:
    def assert_equals(self, expected, actual):
        if expected != actual:
            raise AssertionError(
                f"Expected {expected!r}, got {actual!r}"
            )

    def assert_raises(self, exception_type, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except exception_type:
            return
        except Exception as e:
            raise AssertionError(
                f"Expected {exception_type.__name__}, got {type(e).__name__}: {e}"
            )
        raise AssertionError(
            f"Expected {exception_type.__name__} but no exception raised"
        )

class TestRunner:
    @staticmethod
    def run(test_class):
        # Extension 1: setUp / tearDown
        instance = test_class()
        methods = [(name, meth)
                   for name, meth in inspect.getmembers(instance, inspect.ismethod)
                   if name.startswith("test_")]

        passed = failed = 0
        GREEN = "\033[92m"; RED = "\033[91m"; RESET = "\033[0m"

        for name, method in methods:
            if hasattr(instance, 'setUp'):
                instance.setUp()
            try:
                method()
                print(f"{GREEN}PASS{RESET}: {name}")
                passed += 1
            except AssertionError as e:
                print(f"{RED}FAIL{RESET}: {name} → {e}")
                failed += 1
            except Exception as e:
                print(f"{RED}CRASH{RESET}: {name} → {e}")
                traceback.print_exc()
                failed += 1
            finally:
                if hasattr(instance, 'tearDown'):
                    instance.tearDown()

        print(f"\nResults: {passed} passed, {failed} failed")

class MathTests(TestCase):
    def test_addition(self):
        self.assert_equals(4, 2 + 2)

    def test_broken_subtraction(self):
        self.assert_equals(0, 5 - 2)   # will fail

    def test_divide_zero(self):
        self.assert_raises(ZeroDivisionError, lambda: 1 / 0)

def a15_demo():
    TestRunner.run(MathTests)


if __name__ == "__main__":
    print("=== A-09 ==="); a09_demo()
    print("=== A-10 ==="); a10_demo()
    print("=== A-11 ==="); a11_demo()
    print("=== A-12 ==="); a12_demo()
    print("=== A-13 ==="); a13_demo()
    print("=== A-14 ==="); a14_demo()
    print("=== A-15 ==="); a15_demo()