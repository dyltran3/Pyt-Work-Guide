# Exercise B-13: SQLite Migration Runner

## 1. EXERCISE BRIEF

**Context**: Migrations quản lý vòng đời ứng dụng Database. Chạy Schema qua các File code SQL theo thứ tự (Up/Down) giúp Dev Team làm chung an toàn.
**Task**: Develop ứng dụng chạy Migration thông minh. App tự dò file `.sql` chưa từng chạy trong thư mục, lưu state Migration hiện thời (version control) vào DB, sau đó roll commit.
**Constraints**: Phải hỗ trợ SQL transaction (`BEGIN`, `COMMIT`, `ROLLBACK`) an toàn không corrupt data nếu file lỗi.
## 2. STARTER CODE

```python
import sqlite3
import os

class MigrationRunner:
    def __init__(self, db_path: str, migrations_dir: str):
        self.db_path = db_path
        self.migrations_dir = migrations_dir
        self.conn = sqlite3.connect(db_path)
        self._ensure_history_table()

    def _ensure_history_table(self):
        """
        TODO: Create a table 'schema_history' if it doesn't already exist.
        Columns: id, version_name, applied_at
        """
        pass

    def run_migrations(self):
        """
        TODO:
        1. Read all .sql files in self.migrations_dir sorted alphabetically.
        2. Filter out scripts already applied (check schema_history).
        3. Read content, execute sql, and log success to history.
        4. Wrap in a transaction natively!
        """
        pass

if __name__ == "__main__":
    import tempfile

    with tempfile.TemporaryDirectory() as tmp_dir:
        # Create dummy migrations
        m1 = os.path.join(tmp_dir, "001_init.sql")
        with open(m1, "w") as f: f.write("CREATE TABLE users (id INT, name TEXT);")

        runner = MigrationRunner("test.db", tmp_dir)
        runner.run_migrations()

        print("Migrations [... logic ...] ")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:
[... logic ...] 

**HINT-3 (Near-solution)**:

```python
    def _ensure_history_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS schema_history(
                id INTEGER PRIMARY KEY,
                version_name TEXT UNIQUE,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: Alembic, Django Migrations [... logic ...] 

## 5. VALIDATION CRITERIA

- [ ] Connects [... logic ...] 
- [ ] Validates [... logic ...] 

## 6. EXTENSION CHALLENGES

1. **Extension 1:** [... logic ...] 
2. **Extension 2:** [... logic ...] 

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`sqlite3`).
