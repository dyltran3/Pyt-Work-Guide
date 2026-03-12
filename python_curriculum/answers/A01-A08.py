"""
SOLUTIONS: Book 1 - Learn Python The Hard Way (Applied)
Exercises A-01 through A-08
"""

# ===========================================================================
# A-01: CLI Environment Inspector
# ===========================================================================
import os, sys, json

def get_filtered_env_vars() -> dict[str, str]:
    return {k: v for k, v in os.environ.items()
            if any(kw in k for kw in ('PATH', 'HOME', 'VIRTUAL_ENV'))}

def print_env_table(env_vars: dict[str, str]) -> None:
    COL = 30
    print(f"{'VARIABLE':<{COL}} | VALUE")
    print("-" * COL + "-+-" + "-" * 50)
    for key, value in sorted(env_vars.items()):
        truncated = (value[:77] + "...") if len(value) > 80 else value
        print(f"{key:<{COL}} | {truncated}")

def a01_demo():
    env = get_filtered_env_vars()
    assert isinstance(env, dict)
    print_env_table(env)

    # Extension 2: write .env.backup
    with open(".env.backup", "w") as f:
        for k, v in env.items():
            f.write(f"{k}={v}\n")

    # Extension 3: verify backup
    backup = {}
    with open(".env.backup") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                backup[k] = v
    changed = {k for k in backup if backup.get(k) != os.environ.get(k)}
    if changed:
        print(f"[DRIFT] Keys changed since backup: {changed}")


# ===========================================================================
# A-02: Structured Log Parser
# ===========================================================================
import re
from collections import defaultdict

def generate_mock_log(filename: str) -> None:
    content = (
        '192.168.1.10 - - [10/Oct/2026:13:55:36 -0700] "GET /api/users HTTP/1.1" 200 1024\n'
        '10.0.0.5 - - [10/Oct/2026:13:55:38 -0700] "POST /api/auth HTTP/1.1" 401 256\n'
        '192.168.1.11 - - [10/Oct/2026:13:56:01 -0700] "GET /api/posts HTTP/1.1" 200 512\n'
        '8.8.8.8 - - [10/Oct/2026:13:56:05 -0700] "GET /admin HTTP/1.1" 403 128\n'
        '10.0.0.2 - - [10/Oct/2026:13:56:10 -0700] "GET /api/users HTTP/1.1" 500 0\n'
    )
    with open(filename, 'w') as f:
        f.write(content)

def parse_log_line(line: str) -> dict | None:
    """Extension 1: safe parse with try/except."""
    try:
        parts = line.split('"')
        front = parts[0].split()
        req   = parts[1].split()
        back  = parts[2].split()
        return {
            'ip': front[0],
            'timestamp': front[3][1:],
            'method': req[0],
            'path': req[1],
            'status_code': int(back[0]),
            'bytes_sent': int(back[1]),
        }
    except (IndexError, ValueError):
        return None

def analyze_logs(filename: str,
                 start_time: str = None,
                 end_time: str = None) -> dict[int, int]:
    """Extension 3: generator-based, memory-efficient."""
    from datetime import datetime

    def _parse_dt(ts: str):
        # ts like "10/Oct/2026:13:55:36"
        return datetime.strptime(ts, "%d/%b/%Y:%H:%M:%S")

    def _log_gen(fname):
        with open(fname) as f:
            for raw in f:
                parsed = parse_log_line(raw.strip())
                if parsed:
                    yield parsed

    counts: dict[int, int] = defaultdict(int)
    for entry in _log_gen(filename):
        if start_time or end_time:
            dt = _parse_dt(entry['timestamp'])
            if start_time and dt < _parse_dt(start_time):
                continue
            if end_time and dt > _parse_dt(end_time):
                continue
        counts[entry['status_code']] += 1
    return dict(counts)

def a02_demo():
    generate_mock_log('access.log')
    sample = '192.168.1.10 - - [10/Oct/2026:13:55:36 -0700] "GET /api/users HTTP/1.1" 200 1024'
    p = parse_log_line(sample)
    assert p['status_code'] == 200 and p['method'] == 'GET'
    stats = analyze_logs('access.log')
    assert stats[200] == 2
    print("A-02 passed:", stats)


# ===========================================================================
# A-03: Config File Generator
# ===========================================================================

def get_user_input() -> dict:
    config = {}
    for field in ('host', 'port', 'name', 'user', 'password'):
        while True:
            val = input(f"Enter DB_{field.upper()}: ").strip()
            if field in ('host', 'name') and not val:
                print(f"  {field} cannot be empty. Try again.")
                continue
            config[field] = val
            break
    return config

def generate_env(config: dict) -> str:
    return (
        f"DATABASE_HOST={config['host']}\n"
        f"DATABASE_PORT={config['port']}\n"
        f"DATABASE_NAME={config['name']}\n"
        f"DATABASE_USER={config['user']}\n"
        f"DATABASE_PASS={config['password']}\n"
    )

def generate_ini(config: dict) -> str:
    return (
        "[database]\n"
        f"host = {config['host']}\n"
        f"port = {config['port']}\n"
        f"name = {config['name']}\n"
        f"user = {config['user']}\n"
        f"password = {config['password']}\n"
    )

def generate_yaml(config: dict) -> str:
    return (
        "database:\n"
        f'  host: "{config["host"]}"\n'
        f"  port: {int(config['port'])}\n"
        f'  name: "{config["name"]}"\n'
        f'  user: "{config["user"]}"\n'
        f'  password: "{config["password"]}"\n'
    )

def a03_demo():
    import base64
    mock = {'host': 'localhost', 'port': '5432', 'name': 'myapp_db',
            'user': 'admin', 'password': 'supersecret'}

    # Extension 2: base64-encoded password in .env
    encoded_pw = base64.b64encode(mock['password'].encode()).decode()
    env_out = generate_env({**mock, 'password': encoded_pw})

    for fname, content in [('config.env', env_out),
                            ('config.ini', generate_ini(mock)),
                            ('config.yml', generate_yaml(mock))]:
        with open(fname, 'w') as f:
            f.write(content)
    print("A-03: config files written.")


# ===========================================================================
# A-04: Binary File Inspector
# ===========================================================================
import struct

def generate_mock_binary(filename: str):
    content = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89'
    content += os.urandom(80)
    with open(filename, 'wb') as f:
        f.write(content)

MAGIC_SIGNATURES = {
    b'\x89PNG': 'PNG Image',
    b'%PDF': 'PDF Document',
    b'PK\x03\x04': 'ZIP Archive',
    b'\xff\xd8\xff': 'JPEG Image',
    b'GIF8': 'GIF Image',
}

def inspect_binary(filepath: str, n_lines: int = 4) -> None:
    size = os.path.getsize(filepath)
    with open(filepath, 'rb') as f:
        raw = f.read(16 * n_lines)

    magic = raw[:4]
    matched = next((name for sig, name in MAGIC_SIGNATURES.items()
                    if raw.startswith(sig)), "Unknown")

    print(f"File: {filepath}")
    print(f"Size: {size} bytes")
    print(f"Magic bytes: {' '.join(f'{b:02x}' for b in magic[:4])} → {matched}")
    print()

    for i in range(0, len(raw), 16):
        chunk = raw[i:i+16]
        hex_lo = ' '.join(f'{b:02x}' for b in chunk[:8])
        hex_hi = ' '.join(f'{b:02x}' for b in chunk[8:])
        hex_part = f"{hex_lo:<24}  {hex_hi:<24}"
        ascii_part = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in chunk)
        print(f"{i:08x}  {hex_part}  |{ascii_part}|")

def a04_demo():
    generate_mock_binary('test_image.png')
    inspect_binary('test_image.png')


# ===========================================================================
# A-05: API Request Validator
# ===========================================================================

def validate_payload(payload: dict, schema: dict,
                     path: str = "") -> list[str]:
    """Extension 3: recursive nested validation."""
    errors = []
    for field, rules in schema.items():
        full_path = f"{path}.{field}" if path else field
        if field not in payload:
            if rules.get('required', False):
                errors.append(f"Missing required field: '{full_path}'")
            continue

        val = payload[field]
        expected_type = rules.get('type')

        if expected_type is dict and 'properties' in rules:
            # Recursive nested validation
            if not isinstance(val, dict):
                errors.append(f"'{full_path}' must be an object")
            else:
                errors.extend(validate_payload(val, rules['properties'], full_path))
            continue

        if expected_type and not isinstance(val, expected_type):
            errors.append(
                f"'{full_path}' must be of type {expected_type.__name__}, "
                f"got {type(val).__name__}"
            )
            continue  # skip bounds checks if wrong type

        if expected_type is int or isinstance(val, int):
            if 'min' in rules and val < rules['min']:
                errors.append(f"'{full_path}' value {val} is below minimum {rules['min']}")
            if 'max' in rules and val > rules['max']:
                errors.append(f"'{full_path}' value {val} exceeds maximum {rules['max']}")

        if expected_type is str or isinstance(val, str):
            if 'min_length' in rules and len(val) < rules['min_length']:
                errors.append(f"'{full_path}' too short (min {rules['min_length']})")
            if 'max_length' in rules and len(val) > rules['max_length']:
                errors.append(f"'{full_path}' too long (max {rules['max_length']})")

    return errors

def a05_demo():
    schema = {
        'username': {'type': str, 'required': True},
        'age': {'type': int, 'required': True, 'min': 0, 'max': 150},
        'email_opt_in': {'type': bool, 'required': False},
    }
    assert validate_payload({'username': 'johndoe', 'age': 30}, schema) == []
    bad = validate_payload({'username': 123, 'age': 200, 'extra': 'x'}, schema)
    assert len(bad) == 2
    print("A-05 passed:", bad)


# ===========================================================================
# A-06: HTTP Status Decision Tree
# ===========================================================================

def determine_status_code(authenticated: bool, authorized: bool,
                           resource_exists: bool, rate_limited: bool,
                           server_ok: bool) -> int:
    if not server_ok:
        return 500
    if rate_limited:
        return 429
    if not authenticated:
        return 401
    if not authorized:
        return 403
    if not resource_exists:
        return 404
    return 200

def a06_demo():
    assert determine_status_code(True, True, True, False, True)   == 200
    assert determine_status_code(False, False, False, True, False) == 500
    assert determine_status_code(False, True, True, True, True)    == 429
    assert determine_status_code(False, False, True, False, True)  == 401
    assert determine_status_code(True, False, True, False, True)   == 403
    print("A-06: all assertions passed.")


# ===========================================================================
# A-07: Retry Logic with Backoff
# ===========================================================================
import time, random
from functools import wraps

class FlakyNetworkError(Exception):
    pass

class CircuitBrokenError(Exception):
    pass

def retry(max_attempts=3, base_delay=1.0, exceptions=(Exception,),
          logger_func=print):
    """Includes Extension 1 (Circuit Breaker) and Extension 2 (logger hook)."""
    _tripped = {}

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = func.__qualname__
            if _tripped.get(key, 0) > time.monotonic():
                raise CircuitBrokenError(f"Circuit open for {key}")

            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts - 1:
                        # Trip circuit for 30s
                        _tripped[key] = time.monotonic() + 30
                        raise
                    jitter = random.uniform(0.05, 0.3)
                    sleep_time = base_delay * (2 ** attempt) + jitter
                    logger_func(f"[retry] attempt {attempt+1} failed → retry in {sleep_time:.2f}s")
                    time.sleep(sleep_time)
        return wrapper
    return decorator

def a07_demo():
    counter = {'n': 0}

    @retry(max_attempts=4, base_delay=0.1, exceptions=(FlakyNetworkError,))
    def flaky():
        counter['n'] += 1
        if counter['n'] < 3:
            raise FlakyNetworkError("timeout")
        return "OK"

    result = flaky()
    assert result == "OK" and counter['n'] == 3
    print("A-07 passed.")


# ===========================================================================
# A-08: Chunked File Processor
# ===========================================================================
from itertools import islice

def create_massive_csv(filename: str, rows=50_000) -> None:
    with open(filename, 'w') as f:
        f.write("id,name,amount\n")
        for i in range(rows):
            f.write(f"{i},User_{i},{random.uniform(10.0, 5000.0):.2f}\n")

def read_in_chunks(file_object, chunk_size=1000):
    while True:
        chunk = list(islice(file_object, chunk_size))
        if not chunk:
            break
        yield chunk

def process_large_file(filename: str) -> dict:
    total_sum = 0.0
    total_count = 0
    min_amt = float('inf')
    max_amt = float('-inf')

    with open(filename, 'r') as f:
        next(f)  # skip header
        for chunk in read_in_chunks(f, 1000):
            for line in chunk:
                amount = float(line.strip().split(',')[2])
                total_sum += amount
                total_count += 1
                if amount < min_amt: min_amt = amount
                if amount > max_amt: max_amt = amount

    return {
        'sum': round(total_sum, 2),
        'count': total_count,
        'avg': round(total_sum / total_count, 2) if total_count else 0,
        'min': round(min_amt, 2),
        'max': round(max_amt, 2),
    }

def a08_demo():
    create_massive_csv('transactions.csv', 50_000)
    stats = process_large_file('transactions.csv')
    assert stats['count'] == 50_000
    print("A-08:", stats)


if __name__ == "__main__":
    print("=== A-01 ==="); a01_demo()
    print("=== A-02 ==="); a02_demo()
    print("=== A-03 ==="); a03_demo()
    print("=== A-04 ==="); a04_demo()
    print("=== A-05 ==="); a05_demo()
    print("=== A-06 ==="); a06_demo()
    print("=== A-07 ==="); a07_demo()
    print("=== A-08 ==="); a08_demo()