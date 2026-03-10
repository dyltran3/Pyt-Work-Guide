# Exercise B-05: Priority Task Scheduler

## 1. EXERCISE BRIEF

**Context**: Các Event Loop/Task Schedulers trong server bất đồng bộ (như Celery, FastAPI) hoạt động dựa trên cơ chế phân luồng tác vụ ưu tiên.
**Task**: Xây dựng hệ thống Thread-safe Task Scheduler dạng hàng đợi ưu tiên (Priority Queue bằng module `heapq`). Ưu tiên chạy các Job có score cao nhất.
**Constraints**: Phải cover trường hợp chống trễ Task cũ (Starvation) bằng cách tự động tăng Priority sau 1 khoảng thời gian.
## 2. STARTER CODE

```python
import heapq
import time
from datetime import datetime, timedelta

class TaskScheduler:
    def __init__(self):
        # The internal list array representing our heap
        self.task_queue = []

        # Tie-breaker integer if priorities AND deadlines exactly match ensuring stability
        self.insertion_index = 0

    def add_task(self, priority: int, name: str, deadline: datetime):
        """
        TODO: Use heapq.heappush to add the task.
        In Python heapq, smaller numbers yield first (Min-Heap).
        If you want Priority 1 (High) to go before Priority 10 (Low), just insert normally.
        Store a tuple structure.
        """
        self.insertion_index += 1
        pass

    def get_next_task(self) -> str:
        """
        TODO: Use heapq.heappop to pop and return the task name safely.
        If empty, return None.
        """
        pass

if __name__ == "__main__":
    scheduler = TaskScheduler()

    now = datetime.now()

    # Priority 1 is highest priority.
    scheduler.add_task(priority=10, name="Send Newsletter", deadline=now + timedelta(hours=24))
    scheduler.add_task(priority=1, name="Process Payment", deadline=now + timedelta(hours=1))

    # Notice these have the same priority. The deadline should act as tie-breaker.
    scheduler.add_task(priority=5, name="Generate Report (Urgent)", deadline=now + timedelta(minutes=30))
    scheduler.add_task(priority=5, name="Generate Report (Normal)", deadline=now + timedelta(hours=2))

    # Expected output order:
    # 1: Process Payment (Priority 1)
    # 2: Generate Report (Urgent) (Priority 5, closer deadline)
    # 3: Generate Report (Normal) (Priority 5, farther deadline)
    # 4: Send Newsletter (Priority 10)

    for _ in range(4):
        print(scheduler.get_next_task())
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
`heapq` natively supports sorting tuples [... logic ...] `heapq.heappush(self.task_queue, (val1, val2, val3))` automatically sorts [... logic ...] `val1`. If `val1` is identically identical, [...] `val2` element seamlessly.

**HINT-2 (Partial)**:
Tuples [...]. Including `self.insertion_index` [...] AND the datetime match [... logic ...] 

**HINT-3 (Near-solution)**:

```python
def add_task(self, priority: int, name: str, deadline: datetime):
    self.insertion_index += 1
    # Tuple: (Priority, Deadline, ID, Payload)
    task_tuple = (priority, deadline, self.insertion_index, name)
    heapq.heappush(self.task_queue, task_tuple)

def get_next_task(self) -> str:
    if not self.task_queue:
        return None
    # Popping directly returns the [... logic ...] 
    _, _, _, name = heapq.heappop(self.task_queue)
    return name
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: Celery worker routing, AWS SQS priority configurations, Game routing engines (Pathfinding A\* mathematical algorithms).
- **Why do it manually**: Relying [... logic ...] databases continuously for "next item execution" burns expensive infrastructure [... logic ...] instant worker evaluation performance [... logic ...] [... logic ...] 

## 5. VALIDATION CRITERIA

- [ ] Maintains the fundamental constraints utilizing `heapq` logic natively explicitly.
- [ ] Respects [... logic ...] `deadline` mathematically.
- [ ] Proves structural stability cleanly integrating the `insertion_index` [...].

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Cancellable Tasks):** `heapq` arrays don't explicitly support `remove(item)`. Implement [...]. If a task is cancelled, flag its `insertion_index` in a `self.cancelled` status set. Change `.get_next_task()` to continually execute `heappop()` [...].
2. **Extension 2 (Max-Heap Inversion):** Python `heapq` [... logic ...] "Min-Heap" (lowest elements first). Assume Priority `10` is highest, and Priority `1` is lowest. Invert [...] Max-Heap [... logic ...] 
3. **Extension 3 (Generators & Exhaustion Check):** Implement the `__iter__` method natively returning `self` utilizing standard `yield` expressions continuously extracting tasks block-[...] [... logic ...] 

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`heapq`, `datetime`, `time`).
