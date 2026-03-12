# Exercise Backend-04: Database Optimization & N+1 Problem

## 1. EXERCISE BRIEF

**Context**: Query database trong loop là "sát thủ" hiệu năng thầm lặng nhất (N+1 Select problem). Ngoài ra, thiếu Index hoặc Connection Pooling không đúng cách sẽ khiến app crash khi load tăng cao.
**Task**: 
1. Fix một đoạn code ORM-like bị lỗi N+1 bằng cách sử dụng `JOIN` hoặc `Eager Loading`.
2. Phân tích `EXPLAIN QUERY PLAN` trong SQLite để xác định thiếu Index.
3. Cấu hình Connection Pool cho SQLite để hỗ trợ đa luồng.

## 2. STARTER CODE

```python
import sqlite3
import time

def setup_db():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE authors (id INTEGER PRIMARY KEY, name TEXT)")
    conn.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, author_id INTEGER)")
    
    # Insert dummy data
    authors = [(i, f"Author {i}") for i in range(100)]
    books = [(j, f"Book {j}", j % 100) for j in range(1000)]
    conn.executemany("INSERT INTO authors VALUES (?, ?)", authors)
    conn.executemany("INSERT INTO books VALUES (?, ?, ?)", books)
    return conn

# --- THE PROBLEM: N+1 ---
def get_books_with_authors_slow(conn):
    cursor = conn.execute("SELECT id, title, author_id FROM books")
    results = []
    for row in cursor.fetchall():
        # This executes 1000 times! (N queries)
        author = conn.execute("SELECT name FROM authors WHERE id = ?", (row[2],)).fetchone()
        results.append((row[1], author[0]))
    return results

# --- THE FIX: Eager Loading ---
def get_books_with_authors_fast(conn):
    # TODO: Write a single JOIN query to get all items in one trip
    pass
```

## 3. PROGRESSIVE HINTS

**HINT-1 (JOIN)**:
Thay vì lấy Books rồi loop lấy Author, hãy dùng `SELECT books.title, authors.name FROM books JOIN authors ON books.author_id = authors.id`.

**HINT-2 (Indexing)**:
Trong SQLite, hãy chạy `EXPLAIN QUERY PLAN` trước và sau khi `CREATE INDEX idx_books_author ON books(author_id)`. Bạn sẽ thấy sự khác biệt giữa "SCAN TABLE" và "SEARCH TABLE".

## 4. REAL-WORLD CONNECTIONS
- **ORM**: Django `select_related()` / `prefetch_related()`, SQLAlchemy `joinedload()`.
- **DBA**: Database indexing strategy.

## 5. VALIDATION CRITERIA
- [ ] Đoạn code mới chạy nhanh hơn ít nhất 10x so với bản cũ.
- [ ] Kết quả `EXPLAIN QUERY PLAN` chứng minh Index được sử dụng.
