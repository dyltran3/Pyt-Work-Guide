# Exercise Data-03: SQL Performance Analyzer

## 1. EXERCISE BRIEF

**Context**: Data Engineer xử lý khối SQL Logic Query khổng lồ chạy lâu. Tạo Tool hỗ trợ Profile tối ưu, bóc tách Explain Query AST (Tree Syntax) tiết kiệm hàng tỷ tài nguyên Databricks/AWS.
**Task**: Viết SQL Validator cơ sở: Nhận câu query, kiểm thử sự tồn tại các Anti-patterns (Sử dụng SELECT *, thiếu WHERE, query N+1, không dùng Index), và cảnh báo Warnings tối ưu.
**Constraints**: Biểu diễn String Manipulation / Regex Parser cơ bản phân tích cấu trúc mệnh đề thuần Python.
## 2. STARTER CODE

```python
import sqlite3
import time

class SQLAnalyzer:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)

    def setup_mock_data(self):
        """
        TODO: [... logic ...] 
        """
        pass

    def explain_query(self, query: str) -> list:
        """
        TODO: [... logic ...] 
        """
        pass

    def benchmark_query(self, query: str, iterations: int = 100) -> float:
        """
        TODO: [... logic ...] 
        """
        pass

if __name__ == "__main__":
    import tempfile
    import os

    with tempfile.TemporaryDirectory() as tmp:
        db_file = os.path.join(tmp, "analytics.db")
        analyzer = SQLAnalyzer(db_file)

        # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        zer.setup_mock_data()

        bad_query = "SELECT * FROM users WHERE age > 30 AND status = 'active'"
        good_query = "SELECT id, name FROM users WHERE id IN (SELECT user_id FROM transactions WHERE amount > 100)"

        print(f"Explain [... logic ...] :\n{analyzer.explain_query(bad_query)}")
        print(f"Benchmark [... logic ...] (bad): {analyzer.benchmark_query(bad_query):.4f}s")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:

```python
    def setup_mock_data(self):
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, status TEXT)")
        cursor.execute("CREATE TABLE transactions (tx_id INTEGER PRIMARY KEY, user_id INTEGER, amount REAL)")

        # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        users = [(i, f"User{i}", 20 + (i % 50), "active" if i % 2 == 0 else "inactive") for i in range(1000)]
        cursor.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", users)

        transactions = [(i, i % 1000, 50.0 + (i % 200)) for i in range(5000)]
        cursor.executemany("INSERT INTO transactions VALUES (?, ?, ?)", transactions)

        self.conn.commit()
```

**HINT-3 (Near-solution)**:

```python
    def explain_query(self, query: str) -> list:
        cursor = self.conn.cursor()
        cursor.execute(f"EXPLAIN QUERY PLAN {query}")
        return cursor.fetchall()

    def benchmark_query(self, query: str, iterations: int = 100) -> float:
        cursor = self.conn.cursor()
        start = time.time()
        for _ in range(iterations):
            cursor.execute(query)
            cursor.fetchall()
        return (time.time() - start) / iterations
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `EXPLAIN ANALYZE`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Mã nguồn chạy thành công không báo lỗi, đạt hiệu năng tiêu chuẩn và cover được các test cases ẩn.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: `sqlite3`.
