# Exercise B-17: Dependency Injection Container

## 1. EXERCISE BRIEF

**Context**: Các Framework quy mô cực lớn (FastAPI, Spring) chắp vá thông qua Dependency Injection Component, giúp module lỏng lẻo (decoupled) và linh hoạt test.
**Task**: Triển khai một IoC Container siêu nhỏ hỗ trợ đăng ký Providers bằng Decorator và Resolve các Type-hint Params linh động tự tiêm (Inject).
**Constraints**: Khai thác package `inspect` lấy signature param để inject dynamic deps không hard-coding.
## 2. STARTER CODE

```python
import inspect

class Container:
    def __init__(self):
        self._providers = {}
        self._singletons = {}

    def register(self, cls, provider):
        """
        Registers a factory provider that creates a new instance every time.
        """
        self._providers[cls] = {"type": "factory", "provider": provider}

    def register_singleton(self, cls, provider):
        """
        Registers a provider that creates and stores a single shared instance.
        """
        self._providers[cls] = {"type": "singleton", "provider": provider}

    def resolve(self, cls):
        """
        Resolves a type to its instance, handling singleton vs factory lifecycle.
        """
        if cls not in self._providers:
            raise ValueError(f"No provider registered for {cls.__name__}")
            
        reg = self._providers[cls]
        if reg["type"] == "singleton":
            if cls not in self._singletons:
                self._singletons[cls] = reg["provider"](self)
            return self._singletons[cls]
        return reg["provider"](self)

if __name__ == "__main__":
    class Database:
        def __init__(self):
            self.connected = True

    class UserService:
        def __init__(self, db: Database):
            self.db = db

    container = Container()
    container.register_singleton(Database, lambda c: Database())
    container.register(UserService, lambda c: UserService(c.resolve(Database)))

    service1 = container.resolve(UserService)
    service2 = container.resolve(UserService)

    assert service1 is not service2
    assert service1.db is service2.db
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:

```python
def register(self, cls, provider):
    self._providers[cls] = {"type": "factory", "provider": provider}

def register_singleton(self, cls, provider):
    self._providers[cls] = {"type": "singleton", "provider": provider}
```

**HINT-3 (Near-solution)**:

```python
def resolve(self, cls):
    if cls not in self._providers:
        raise ValueError(f"No provider flexibly")

    registration = self._providers[cls]
    if registration["type"] == "singleton":
        if cls not in self._singletons:
            self._singletons[cls] = registration["provider"](self)
        return self._singletons[cls]
    else:
        return registration["provider"](self)
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `dependency-injector`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Correctly distinguishes between Singleton and Factory lifecycles.
- [ ] Successfully resolves dependencies recursively.
- [ ] Handles missing provider errors gracefully.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
