# Exercise Backend-03: Async Task Queue

## 1. EXERCISE BRIEF

**Context**: Một Backend xịn không bao giờ xử lý logic tính toán hoặc gửi Email trong API call. Background Task Queue (như Celery) là điều tiên quyết để scale server.
**Task**: Create mô hình Task Queue Async Worker với Broker trung gian (Redis/Mem giả lập). Xử lý hàng đẩy, xử lý hàng đợi theo Worker Pool và Callback trạng thái kết thúc.
**Constraints**: Worker thiết kế không đồng bộ có Cancel-Task capabilities và log error tracing.
## 2. STARTER CODE

```python
import asyncio
import time

class AsyncTaskQueue:
    def __init__(self, concurrency: int = 3):
        """
        Initializes the async queue and worker pool.
        """
        self.concurrency = concurrency
        self.queue = asyncio.Queue()
        self.workers = []

    async def enqueue(self, task_name: str, coroutine):
        """
        Pushes a new task into the queue.
        """
        await self.queue.put((task_name, coroutine))

    async def worker(self, worker_id: int):
        """
        Continuous worker loop popping tasks from the queue.
        """
        while True:
            task_name, coro = await self.queue.get()
            try:
                print(f"Worker {worker_id} processing {task_name}")
                await coro
            except Exception as e:
                print(f"Worker {worker_id} error on {task_name}: {e}")
            finally:
                self.queue.task_done()

    async def run(self):
        """
        Spawns worker tasks and waits for the queue to drain.
        """
        self.workers = [asyncio.create_task(self.worker(i)) for i in range(self.concurrency)]
        await self.queue.join()
        for w in self.workers:
            w.cancel()

async def sample_task(task_id: int, delay: float):
    print(f"Task {task_id} starting (planned delay {delay}s)")
    await asyncio.sleep(delay)
    return f"Execution Result: Task {task_id} finished"

async def main():
    q = AsyncTaskQueue(concurrency=2)
    asyncio.create_task(q.run())

    for i in range(5):
        await q.enqueue(f"Task_{i}", sample_task(i, 0.5))

    await asyncio.sleep(3) # Wait for all tasks to settle

if __name__ == "__main__":
    asyncio.run(main())
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:

```python
class AsyncTaskQueue:
    def __init__(self, concurrency: int = 3):
        self.concurrency = concurrency
        self.queue = asyncio.Queue()
        self.workers = []

    async def enqueue(self, task_name: str, coroutine):
        await self.queue.put((task_name, coroutine))
```

**HINT-3 (Near-solution)**:

```python
    async def worker(self, worker_id: int):
        while True:
            task_name, coroutine = await self.queue.get()
            try:
                print(f"Worker {worker_id} processing {task_name}")
                await coroutine
            except Exception as e:
                print(f"Worker {worker_id} error on {task_name}: {e}")
            finally:
                self.queue.task_done()

    async def run(self):
        self.workers = [
            asyncio.create_task(self.worker(i))
            for i in range(self.concurrency)
        ]
        await self.queue.join()
        for w in self.workers:
            w.cancel()
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `Celery`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Correctly implements async producer-consumer pattern using `asyncio.Queue`.
- [ ] Correctly manages worker pool concurrency.
- [ ] Handles task failures gracefully without crashing workers.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
