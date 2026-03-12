# Exercise B-22: Modern Python 3.10 - 3.12+ Features

## 1. EXERCISE BRIEF

**Context**: Python phát triển rất nhanh. Các tính năng như `Structural Pattern Matching`, `Type Hints advanced`, và `Exception Groups` thay đổi hoàn toàn cách chúng ta viết code sạch (clean code).
**Task**: Refactor một đoạn code cũ xử lý JSON response phức tạp bằng cách sử dụng các tính năng mới.
**Constraints**: 
- Sử dụng `match-case` (3.10).
- Sử dụng `TypedDict` và `Protocol` (3.8+ / 3.11 improvements).
- Sử dụng `dataclasses(slots=True)` (3.10+).
- Xử lý lỗi bằng `ExceptionGroup` và `except*` (3.11).

## 2. STARTER CODE

```python
from typing import TypedDict, Protocol
from dataclasses import dataclass

# 1. New Syntax: match-case
def process_command(cmd_data):
    # Old way: if-elif-elif
    # Refactor this using match-case
    match cmd_data:
        case {"action": "move", "dir": direction}:
            print(f"Moving to {direction}")
        case {"action": "attack", "target": t}:
            print(f"Attacking {t}")
        case _:
            print("Unknown command")

# 2. Performance: Dataclass Slots
@dataclass(slots=True)
class FastPoint:
    x: float
    y: float

# 3. Static Analysis: Protocol (Duck Typing)
class Drawable(Protocol):
  def draw(self) -> None: ...

# 4. Error Handling: ExceptionGroup
try:
    raise ExceptionGroup("Batch errors", [ValueError("Invalid A"), TypeError("Bad B")])
except* ValueError as eg:
    print(f"Caught ValueErrors: {eg.exceptions}")
except* TypeError as eg:
    print(f"Caught TypeErrors: {eg.exceptions}")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Match Case)**:
Nó không chỉ là `switch-case`. Bạn có thể destructure object, list, và áp dụng "guards" (if conditions) ngay trong case.

**HINT-2 (Exception Groups)**:
Rất hữu ích khi làm việc với `asyncio.TaskGroup` trong Python 3.11, nơi nhiều coroutine có thể fail cùng lúc.

## 4. REAL-WORLD CONNECTIONS
- **Structural Pattern Matching**: Xử lý AST, JSON API responses, State machines.
- **Slots**: Tiết kiệm RAM khi tạo hàng triệu object.

## 5. VALIDATION CRITERIA
- [ ] Code sử dụng đúng cú pháp `match-case`.
- [ ] Chứng minh được `slots=True` giúp giảm memory footprint (dùng `sys.getsizeof`).
- [ ] Xử lý thành công đa lỗi với `except*`.

## 6. SETUP REQUIREMENTS
- **Python Version**: 3.11+ (Bắt buộc cho ExceptionGroup)
