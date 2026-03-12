# Exercise Test-03: Integration Testing & Fixtures

## 1. EXERCISE BRIEF

**Context**: Unit test cô lập (Mock) là chưa đủ. Integration Test đảm bảo các component (App + Database) làm việc với nhau đúng đắn.
**Task**: Viết bộ test suite sử dụng `pytest-postgresql` hoặc mock-pool để test luồng: `User Registration -> Write to DB -> Read from DB`.
**Constraints**: Sử dụng Pytest Fixtures (`scope="module"` hoặc `scope="function"`) để setup/teardown database sạch sau mỗi lần chạy.

## 2. STARTER CODE

```python
import pytest
import sqlite3

class UserRepository:
    def __init__(self, db_conn):
        self.conn = db_conn
        self.conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT UNIQUE)")

    def add_user(self, email):
        self.conn.execute("INSERT INTO users (email) VALUES (?)", (email,))
        self.conn.commit()

    def get_user(self, email):
        cur = self.conn.execute("SELECT email FROM users WHERE email = ?", (email,))
        return cur.fetchone()

# --- FIXTURES ---

@pytest.fixture
def db_conn():
    """Setup an in-memory database for testing"""
    conn = sqlite3.connect(":memory:")
    yield conn
    conn.close()

@pytest.fixture
def repo(db_conn):
    return UserRepository(db_conn)

# --- TESTS ---

def test_user_lifecycle(repo):
    email = "test@example.com"
    repo.add_user(email)
    user = repo.get_user(email)
    assert user[0] == email

def test_duplicate_user(repo):
    repo.add_user("dup@test.com")
    with pytest.raises(sqlite3.IntegrityError):
        repo.add_user("dup@test.com")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Lifecycle)**:
Sự khác biệt giữa `yield` và `return` trong fixture là gì? (Hint: Teardown logic).

**HINT-2 (Concurrency)**:
Làm thế nào để chạy Integration Test song song (`pytest -n auto`) mà không bị tranh chấp Database? (Hint: Unique DB name per worker).

## 4. REAL-WORLD CONNECTIONS
- **Frameworks**: Testcontainers (Docker-based testing), SQLModel (Integration testing).

## 5. VALIDATION CRITERIA
- [ ] Fixtures setup database đúng trước mỗi test.
- [ ] Database được dọn dẹp (teardown) sau khi test.
- [ ] Test suite chứng minh được tính đúng đắn của việc lưu trữ thực tế (không dùng mock).
