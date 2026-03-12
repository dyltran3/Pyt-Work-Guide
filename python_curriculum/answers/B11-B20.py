"""
SOLUTIONS: Book 2 - Python Notes For Professionals
Exercises B-11 through B-20
"""
import base64, json, hmac, hashlib, os, time, random, io, argparse
import cProfile, pstats, sqlite3, csv
from functools import wraps, partial
from collections import defaultdict
from wsgiref.simple_server import make_server
from pathlib import Path
import subprocess, sys


# ===========================================================================
# B-11: REST API Wrapper Generator
# ===========================================================================

class MockRequestSession:
    def request(self, method: str, url: str, **kwargs):
        return {"status": "success", "executed": f"{method} {url}", "args": kwargs}

class APIClient:
    def __init__(self, base_url: str, spec: dict):
        self.base_url    = base_url
        self.session     = MockRequestSession()
        self._build_dynamic_methods(spec)

    def _core_request(self, method: str, path: str, **kwargs):
        return self.session.request(method, self.base_url + path, **kwargs)

    def _build_dynamic_methods(self, spec: dict) -> None:
        for func_name, info in spec.items():
            bound = partial(self._core_request,
                            method=info['method'],
                            path=info['path'])
            setattr(self, func_name, bound)

def b11_demo():
    schema = {
        "get_users":   {"method": "GET",    "path": "/users"},
        "create_user": {"method": "POST",   "path": "/users"},
        "delete_user": {"method": "DELETE", "path": "/users/1"},
    }
    client = APIClient("https://api.example.com", schema)
    r1 = client.get_users(params={"limit": 10})
    r2 = client.create_user(json={"name": "Alice"})
    assert r1['executed'] == "GET https://api.example.com/users"
    assert r2['args']['json']['name'] == "Alice"
    print("B-11: REST wrapper passed ✓")


# ===========================================================================
# B-12: Mini Flask Clone (WSGI)
# ===========================================================================
import re as _re

class App:
    def __init__(self):
        self.routes: dict[str, callable] = {}

    def route(self, path: str):
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        return wrapper

    def __call__(self, environ: dict, start_response):
        path = environ.get('PATH_INFO', '/')
        handler = self.routes.get(path)
        if handler:
            body = handler(environ)
            start_response('200 OK', [('Content-Type', 'text/html')])
        else:
            body = 'Not Found'
            start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
        return [body.encode('utf-8')]

def b12_demo():
    app = App()

    @app.route("/")
    def home(env): return "Hello World!"

    @app.route("/api")
    def api(env): return '{"status": "ok"}'

    # Simulate WSGI call
    results = []
    def fake_start_response(status, headers):
        results.append(status)

    environ = {'PATH_INFO': '/'}
    body = app(environ, fake_start_response)
    assert results[0] == '200 OK'
    assert body[0] == b'Hello World!'

    environ2 = {'PATH_INFO': '/missing'}
    app(environ2, fake_start_response)
    assert results[1] == '404 NOT FOUND'
    print("B-12: Mini Flask passed ✓")


# ===========================================================================
# B-13: SQLite Migration Runner
# ===========================================================================

class MigrationRunner:
    def __init__(self, db_path: str, migrations_dir: str):
        self.db_path        = db_path
        self.migrations_dir = migrations_dir
        self.conn           = sqlite3.connect(db_path)
        self._ensure_history_table()

    def _ensure_history_table(self) -> None:
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS schema_history (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                version_name TEXT UNIQUE NOT NULL,
                applied_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def _already_applied(self, name: str) -> bool:
        cur = self.conn.execute(
            "SELECT 1 FROM schema_history WHERE version_name = ?", (name,)
        )
        return cur.fetchone() is not None

    def run_migrations(self) -> None:
        sql_files = sorted(
            f for f in os.listdir(self.migrations_dir) if f.endswith('.sql')
        )
        for fname in sql_files:
            if self._already_applied(fname):
                print(f"  Skipping (already applied): {fname}")
                continue
            path = os.path.join(self.migrations_dir, fname)
            with open(path) as f:
                sql = f.read()
            try:
                self.conn.execute("BEGIN")
                self.conn.executescript(sql)
                self.conn.execute(
                    "INSERT INTO schema_history (version_name) VALUES (?)", (fname,)
                )
                self.conn.execute("COMMIT")
                print(f"  Applied: {fname}")
            except Exception as e:
                self.conn.execute("ROLLBACK")
                print(f"  ROLLBACK on {fname}: {e}")
                raise

def b13_demo():
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        m1 = os.path.join(tmp, "001_init.sql")
        m2 = os.path.join(tmp, "002_add_email.sql")
        with open(m1, "w") as f: f.write("CREATE TABLE users (id INTEGER, name TEXT);")
        with open(m2, "w") as f: f.write("ALTER TABLE users ADD COLUMN email TEXT;")

        runner = MigrationRunner(os.path.join(tmp, "test.db"), tmp)
        runner.run_migrations()
        runner.run_migrations()   # idempotent
        print("B-13: Migration runner passed ✓")


# ===========================================================================
# B-14: ETL Data Pipeline
# ===========================================================================

def _generate_mock_csv(filepath: str, rows: int = 100_000) -> None:
    statuses = ["SUCCESS", "SUCCESS", "PENDING", "FAILED"]
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["tx_id", "user_id", "amount", "status"])
        for i in range(rows):
            writer.writerow([f"TX{i}", i % 1000,
                             f"${random.uniform(5, 500):.2f}",
                             random.choice(statuses)])

class ETLPipeline:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS transactions "
            "(tx_id TEXT, user_id INT, amount REAL, status TEXT)"
        )

    def extract(self, csv_filepath: str, chunk_size=10_000):
        with open(csv_filepath, 'r') as f:
            reader = csv.DictReader(f)
            chunk = []
            for row in reader:
                chunk.append(row)
                if len(chunk) == chunk_size:
                    yield chunk
                    chunk = []
            if chunk:
                yield chunk

    def transform(self, chunk: list[dict]) -> list[tuple]:
        result = []
        for row in chunk:
            if row['status'] == 'FAILED':
                continue
            try:
                amt = float(row['amount'].replace("$", ""))
                result.append((row['tx_id'], int(row['user_id']), amt, row['status']))
            except (ValueError, KeyError):
                pass
        return result

    def load(self, tuples: list[tuple]) -> None:
        self.conn.executemany(
            "INSERT INTO transactions (tx_id, user_id, amount, status) VALUES (?,?,?,?)",
            tuples
        )
        self.conn.commit()

    def run(self, csv_file: str) -> None:
        for chunk in self.extract(csv_file):
            self.load(self.transform(chunk))

def b14_demo():
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        csv_f = os.path.join(tmp, "data.csv")
        db_f  = os.path.join(tmp, "data.db")
        _generate_mock_csv(csv_f, rows=10_000)

        pipeline = ETLPipeline(db_f)
        pipeline.run(csv_f)

        total  = pipeline.conn.execute("SELECT COUNT(*) FROM transactions").fetchone()[0]
        failed = pipeline.conn.execute(
            "SELECT COUNT(*) FROM transactions WHERE status='FAILED'"
        ).fetchone()[0]
        assert failed == 0
        assert total > 5_000
        print(f"B-14: ETL done. Inserted {total} rows (no FAILED) ✓")


# ===========================================================================
# B-15: Password Hashing System
# ===========================================================================
import secrets

class AuthSystem:
    def __init__(self):
        self.db: dict[str, dict] = {}

    def hash_password(self, password: str, salt: bytes) -> str:
        key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 260_000)
        return key.hex()

    def register_user(self, email: str, password: str) -> None:
        salt     = os.urandom(32)
        pwd_hash = self.hash_password(password, salt)
        self.db[email] = {"salt": salt.hex(), "password_hash": pwd_hash}

    def login_user(self, email: str, password: str) -> bool:
        record = self.db.get(email)
        if not record:
            return False
        salt        = bytes.fromhex(record["salt"])
        attempt_hash = self.hash_password(password, salt)
        # Constant-time compare — prevents timing attacks
        return secrets.compare_digest(attempt_hash, record["password_hash"])

def b15_demo():
    auth = AuthSystem()
    auth.register_user("admin@example.com", "SuperSecret123!")
    assert auth.login_user("admin@example.com", "SuperSecret123!") is True
    assert auth.login_user("admin@example.com", "WrongPassword")   is False
    assert auth.db["admin@example.com"]["password_hash"] != "SuperSecret123!"
    print("B-15: Auth system passed ✓")


# ===========================================================================
# B-16: JWT from Scratch
# ===========================================================================

class JWTBuilder:
    def __init__(self, secret: str):
        self.secret = secret.encode()

    def _b64url_encode(self, data: bytes) -> str:
        return base64.urlsafe_b64encode(data).decode().rstrip('=')

    def _b64url_decode(self, s: str) -> bytes:
        padding = 4 - len(s) % 4
        return base64.urlsafe_b64decode(s + '=' * (padding % 4))

    def encode(self, payload: dict, expire_seconds: int = None) -> str:
        if expire_seconds:
            payload = {**payload, "exp": int(time.time()) + expire_seconds}
        header = {"alg": "HS256", "typ": "JWT"}
        b64h = self._b64url_encode(json.dumps(header).encode())
        b64p = self._b64url_encode(json.dumps(payload).encode())
        signing_input = f"{b64h}.{b64p}".encode()
        sig  = hmac.new(self.secret, signing_input, hashlib.sha256).digest()
        b64s = self._b64url_encode(sig)
        return f"{b64h}.{b64p}.{b64s}"

    def decode(self, token: str) -> dict:
        parts = token.split('.')
        if len(parts) != 3:
            raise ValueError("Invalid JWT structure")
        b64h, b64p, b64s = parts
        signing_input = f"{b64h}.{b64p}".encode()
        expected_sig  = hmac.new(self.secret, signing_input, hashlib.sha256).digest()
        actual_sig    = self._b64url_decode(b64s)
        if not secrets.compare_digest(expected_sig, actual_sig):
            raise ValueError("Invalid signature — token tampered!")
        payload = json.loads(self._b64url_decode(b64p))
        if "exp" in payload and payload["exp"] < time.time():
            raise ValueError("Token expired")
        return payload

def b16_demo():
    jwt = JWTBuilder("supersecret")
    token = jwt.encode({"sub": "user123"}, expire_seconds=3600)
    decoded = jwt.decode(token)
    assert decoded["sub"] == "user123"
    # Tampered token
    parts = token.split('.')
    bad_token = parts[0] + '.' + parts[1] + '.invalidsignature'
    try:
        jwt.decode(bad_token)
        assert False, "Should have raised"
    except ValueError:
        pass
    print("B-16: JWT passed ✓")


# ===========================================================================
# B-17: Dependency Injection Container
# ===========================================================================

class Container:
    def __init__(self):
        self._providers: dict  = {}
        self._singletons: dict = {}

    def register(self, cls, provider):
        self._providers[cls] = {"type": "factory", "provider": provider}

    def register_singleton(self, cls, provider):
        self._providers[cls] = {"type": "singleton", "provider": provider}

    def resolve(self, cls):
        if cls not in self._providers:
            raise ValueError(f"No provider registered for {cls.__name__}")
        reg = self._providers[cls]
        if reg["type"] == "singleton":
            if cls not in self._singletons:
                self._singletons[cls] = reg["provider"](self)
            return self._singletons[cls]
        return reg["provider"](self)

def b17_demo():
    class Database:
        def __init__(self): self.connected = True
    class UserService:
        def __init__(self, db: Database): self.db = db

    c = Container()
    c.register_singleton(Database,   lambda c: Database())
    c.register(UserService, lambda c: UserService(c.resolve(Database)))

    s1 = c.resolve(UserService)
    s2 = c.resolve(UserService)
    assert s1 is not s2        # factory → new instance each time
    assert s1.db is s2.db      # singleton → same DB instance
    print("B-17: DI container passed ✓")


# ===========================================================================
# B-18: Reactive Event System
# ===========================================================================
import fnmatch

class EventBus:
    def __init__(self):
        self._subscribers: dict[str, list] = defaultdict(list)

    def subscribe(self, event_type: str, callback: callable) -> None:
        self._subscribers[event_type].append(callback)

    def emit(self, event_type: str, payload: dict = None) -> None:
        payload = payload or {}
        for pattern, callbacks in self._subscribers.items():
            # Wildcard support: "user.*" matches "user.created"
            if fnmatch.fnmatch(event_type, pattern):
                for cb in callbacks:
                    cb(payload)

def b18_demo():
    bus = EventBus()
    log = []
    bus.subscribe("user.created", lambda p: log.append(("user_created", p)))
    bus.subscribe("user.updated", lambda p: log.append(("user_updated", p)))
    bus.subscribe("user.*",       lambda p: log.append(("wildcard", p)))

    bus.emit("user.created", {"id": 1})
    bus.emit("user.updated", {"id": 1})
    assert len(log) == 4  # 2 specific + 2 wildcard
    print("B-18: EventBus passed ✓", log)


# ===========================================================================
# B-19: Profiling & Optimization
# ===========================================================================

def profile(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        pstats.Stats(pr, stream=s).sort_stats('cumulative').print_stats(10)
        print(s.getvalue())
        return result
    return wrapper

@profile
def main_optimized():
    data = [random.randint(1, 10_000) for _ in range(10_000)]

    # Sieve of Eratosthenes — O(n log log n) vs O(n²)
    def sieve(n):
        is_prime = [True] * (n + 1)
        for p in range(2, int(n**0.5) + 1):
            if is_prime[p]:
                for i in range(p*p, n+1, p):
                    is_prime[i] = False
        return [p for p in range(2, n+1) if is_prime[p]]

    primes = sieve(5000)
    stats  = sum(item * 2 for item in data if item > 5_000)
    return len(primes), stats

def b19_demo():
    result = main_optimized()
    print(f"B-19: {result[0]} primes found ✓")


# ===========================================================================
# B-20: Conda/venv Manager CLI
# ===========================================================================

class EnvManager:
    def __init__(self):
        self.base_dir = Path.cwd() / "envs"
        self.base_dir.mkdir(exist_ok=True)

    def create_venv(self, env_name: str) -> None:
        env_path = self.base_dir / env_name
        if env_path.exists():
            print(f"Environment '{env_name}' already exists.")
            return
        print(f"Creating venv '{env_name}'...")
        subprocess.run([sys.executable, "-m", "venv", str(env_path)], check=True)
        print(f"Created: {env_path}")

    def list_envs(self) -> list[str]:
        envs = [d.name for d in self.base_dir.iterdir() if d.is_dir()]
        for e in envs:
            print(f"  - {e}")
        return envs

    def freeze_env(self, env_name: str) -> str:
        env_path = self.base_dir / env_name
        if not env_path.exists():
            print(f"Environment '{env_name}' not found.")
            return ""
        pip = env_path / ("Scripts/pip.exe" if os.name == 'nt' else "bin/pip")
        result = subprocess.run([str(pip), "freeze"],
                                capture_output=True, text=True)
        print(result.stdout)
        return result.stdout

def b20_demo():
    mgr = EnvManager()
    print("B-20: EnvManager initialized. Skipping venv creation in demo.")


if __name__ == "__main__":
    print("=== B-11 ==="); b11_demo()
    print("=== B-12 ==="); b12_demo()
    print("=== B-13 ==="); b13_demo()
    print("=== B-14 ==="); b14_demo()
    print("=== B-15 ==="); b15_demo()
    print("=== B-16 ==="); b16_demo()
    print("=== B-17 ==="); b17_demo()
    print("=== B-18 ==="); b18_demo()
    print("=== B-19 ==="); b19_demo()
    b20_demo()