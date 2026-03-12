# Exercise B-18: Reactive Event System

## 1. EXERCISE BRIEF

**Context**: Micro-services phát tín hiệu broadcast dữ liệu theo mô hình Pub-sub hoặc Event-bus để ứng dụng phản ứng thời gian thực với độ trễ tối thiểu.
**Task**: Create core Reactive Event Dispatcher. Có thể Listen / Emit Signal nhiều topic cùng lúc, kích hoạt async callbacks mượt mà không block task.
**Constraints**: Hỗ trợ `*` wild-cards event listeners. Cấu trúc Async Event Queue.
## 2. STARTER CODE

```python
import collections

class EventBus:
    def __init__(self):
        self._subscribers = collections.defaultdict(list)

    def subscribe(self, event_type: str, callback: callable):
        """
        Subscribes a callback to a specific event type or pattern (e.g., 'user.*').
        """
        self._subscribers[event_type].append(callback)

    def emit(self, event_type: str, payload: dict = None):
        """
        Emits an event, triggering all matching subscribers (including wildcards).
        """
        import fnmatch
        payload = payload or {}
        for pattern, callbacks in self._subscribers.items():
            if fnmatch.fnmatch(event_type, pattern):
                for cb in callbacks:
                    cb(payload)

if __name__ == "__main__":
    bus = EventBus()

    events_received = []

    def on_user_created(payload):
        events_received.append(("user_created", payload))

    def on_user_updated(payload):
        events_received.append(("user_updated", payload))

    bus.subscribe("user.created", on_user_created)
    bus.subscribe("user.updated", on_user_updated)

    bus.emit("user.created", {"id": 1, "name": "Alice"})
    bus.emit("user.updated", {"id": 1, "name": "Alice Smith"})

    assert len(events_received) == 2
    assert events_received[0][0] == "user_created"
    assert events_received[1][0] == "user_updated"
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:

```python
def subscribe(self, event_type: str, callback: callable):
    self._subscribers[event_type].append(callback)
```

**HINT-3 (Near-solution)**:

```python
def emit(self, event_type: str, payload: dict = None):
    payload = payload or {}
    for callback in self._subscribers.get(event_type, []):
        callback(payload)
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `RxPY`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Successfully supports specific and wildcard event subscriptions.
- [ ] Correcty dispatches events to multiple listeners.
- [ ] Handles empty payloads and unregistered events gracefully.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
