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
        TODO: [... logic ...] 
        """
        pass

    def acquire(self, timeout=2.0) -> Connection:
        """
        TODO: [... logic ...] 
        """
        pass

    def release(self, conn: Connection):
        """
        TODO: [... logic ...] 
        """
        pass

    def get_stats(self) -> dict:
        """
        TODO: [... logic ...] 
        """
        pass

if __name__ == "__main__":
    pool = ConnectionPool(size=3)

    def worker(worker_id):
        try:
            conn = pool.acquire(timeout=1.0)
            print(f"Worker {worker_id} [... logic ...] {conn.id}")
            conn.execute("SELECT 1")
            pool.release(conn)
            print(f"Worker {worker_id} [... logic ...] {conn.id}")
        except TimeoutError:
            print(f"Worker {worker_id} [... logic ...] ")

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(10)]
    for t in threads:
        t.start()

    for _ in range(3):
        print("STATS [... logic ...] :", pool.get_stats())
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
            raise TimeoutError("Pool [... logic ...] ")

    def release(self, conn: Connection):
        conn.in_use = False
        with self._lock:
            self._active_connections -= 1
        self._pool.put(conn)
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `SQLAlchemy [... logic ...] `` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Incorporates [... logic ...] 

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
