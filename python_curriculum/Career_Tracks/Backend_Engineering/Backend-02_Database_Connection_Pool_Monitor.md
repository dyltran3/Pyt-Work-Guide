# Exercise Backend-02: Database Connection Pool Monitor

## 1. EXERCISE BRIEF

**Context**: Mạng bị tắc nghẽn thường liên quan rò rỉ (leak) Pool truy cập DB nếu kết nối mở thả nổi mà không thu hồi. Tối ưu giám sát Connection Pool là bài học sinh tử.
**Task**: Phát triển một Class Session Pool Tracker giả lập: Phân bổ và quản lý Context Connection Manager. Tạo monitor report số connect đã chiếm/ tổng lượng max.
**Constraints**: Kết hợp async/await, tự sinh Connection Timeout Timeout Exception nếu queue full.
## 2. STARTER CODE

```python
import time
import threading
import random

class Connection:
    def __init__(self, id_num):
        self.id = id_num
        self.in_use = False

    def execute(self, query):
        # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        time.sleep(random.uniform(0.01, 0.1))

class ConnectionPool:
    def __init__(self, size=5):
        """
        Initializes the pool with a fixed number of connections.
        """
        import queue
        self.size = size
        self._pool = queue.Queue(maxsize=size)
        self._active = 0
        self._lock = threading.Lock()
        for i in range(size):
            self._pool.put(Connection(i))

    def acquire(self, timeout=2.0) -> Connection:
        """
        Acquires a connection from the pool, blocking if none are available.
        """
        import queue
        try:
            conn = self._pool.get(timeout=timeout)
            with self._lock:
                self._active += 1
            conn.in_use = True
            return conn
        except queue.Empty:
            raise TimeoutError(f"Connection pool exhausted (max size: {self.size})")

    def release(self, conn: Connection):
        """
        Releases a connection back into the pool.
        """
        conn.in_use = False
        with self._lock:
            self._active -= 1
        self._pool.put(conn)

    def get_stats(self) -> dict:
        """
        Returns real-time occupancy statistics of the pool.
        """
        with self._lock:
            return {
                "active_connections": self._active,
                "available_connections": self.size - self._active,
                "total_capacity": self.size
            }

if __name__ == "__main__":
    pool = ConnectionPool(size=3)

    def worker(worker_id):
        try:
            conn = pool.acquire(timeout=1.0)
            print(f"Worker {worker_id} acquired connection {conn.id}")
            conn.execute("SELECT 1")
            pool.release(conn)
            print(f"Worker {worker_id} released connection {conn.id}")
        except TimeoutError:
            print(f"Worker {worker_id} timed out waiting for connection")

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(10)]
    for t in threads:
        t.start()

    for _ in range(3):
        print("STATS (Real-time):", pool.get_stats())
        time.sleep(0.05)

    for t in threads:
        t.join()
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:

```python
import queue

class ConnectionPool:
    def __init__(self, size=5):
        self.size = size
        self._pool = queue.Queue(maxsize=size)
        self._active_connections = 0
        self._lock = threading.Lock()

        for i in range(size):
            self._pool.put(Connection(i))
```

**HINT-3 (Near-solution)**:

```python
    def acquire(self, timeout=2.0) -> Connection:
        try:
            conn = self._pool.get(timeout=timeout)
            with self._lock:
                self._active_connections += 1
            conn.in_use = True
            return conn
        except queue.Empty:
            raise TimeoutError("Pool exhausted - connection timeout reached")

    def release(self, conn: Connection):
        conn.in_use = False
        with self._lock:
            self._active_connections -= 1
        self._pool.put(conn)
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `SQLAlchemy`, `psycopg2`, `aiopg` (async), `sqlalchemy.pool`.

## 5. VALIDATION CRITERIA

- [ ] Correctly implements thread-safe connection acquisition and release.
- [ ] Handles pool exhaustion with appropriate TimeoutError.
- [ ] Provides accurate real-time stats for monitoring.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
