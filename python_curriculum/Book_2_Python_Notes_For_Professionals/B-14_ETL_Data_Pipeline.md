# Exercise B-14: ETL Data Pipeline

## 1. EXERCISE BRIEF

**Context**: Dòng dữ liệu siêu lớn cần trích xuất - biến đổi - load (ETL Pipeline). Cấu trúc Generator Stream Pattern xử lý vấn đề quá tải I/O Database Data Warehouse.
**Task**: Đẩy data từ Mock CSV qua Pipeline biến đổi làm sạch data (Loại bỏ Null) bằng các chunk generators rồi truyền dữ liệu lên luồng xử lý cuối (Load Sink).
**Constraints**: Sử dụng kỹ thuật chain-generator và decorator pipeline thuần.
## 2. STARTER CODE

```python
import csv
import sqlite3
import os
import tempfile
import random

def generate_mock_csv(filepath: str, rows: int = 100_000):
    """Utility to generate a large nasty CSV file for testing"""
    statuses = ["SUCCESS", "SUCCESS", "PENDING", "FAILED"]
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["tx_id", "user_id", "amount", "status"])
        for i in range(rows):
            amt = f"${random.uniform(5.0, 500.0):.2f}"
            writer.writerow([f"TX{i}", random.randint(1, 1000), amt, random.choice(statuses)])

class ETLPipeline:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute("CREATE TABLE IF NOT EXISTS transactions (tx_id TEXT, user_id INT, amount REAL, status TEXT)")

    def extract(self, csv_filepath: str, chunk_size=10_000):
        """
        Extracts data in chunks using a generator to avoid memory overflow.
        """
        with open(csv_filepath, 'r') as f:
            reader = csv.DictReader(f)
            chunk = []
            for row in reader:
                chunk.append(row)
                if len(chunk) == chunk_size:
                    yield chunk
                    chunk = []
            if chunk:
                yield chunk

    def transform(self, chunk: list[dict]) -> list[tuple]:
        """
        Cleans data: skips 'FAILED' records and converts amounts to float.
        """
        result = []
        for row in chunk:
            if row['status'] == 'FAILED':
                continue
            try:
                amt = float(row['amount'].replace("$", ""))
                result.append((row['tx_id'], int(row['user_id']), amt, row['status']))
            except (ValueError, KeyError):
                pass
        return result

    def load(self, tuples: list[tuple]):
        """
        Batch inserts data into the SQLite database.
        """
        self.conn.executemany(
            "INSERT INTO transactions (tx_id, user_id, amount, status) VALUES (?,?,?,?)",
            tuples
        )
        self.conn.commit()

    def run(self, csv_file: str):
        """
        Executes the ETL process by chaining generators.
        """
        for chunk in self.extract(csv_file):
            self.load(self.transform(chunk))

if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        csv_file = os.path.join(tmp, "data.csv")
        db_file = os.path.join(tmp, "data.db")

        print(f"Generating 100k rows dynamically cleanly...")
        generate_mock_csv(csv_file)

        pipeline = ETLPipeline(db_file)
        pipeline.run(csv_file)

        cursor = pipeline.conn.cursor()
        total = cursor.execute("SELECT COUNT(*) FROM transactions").fetchone()[0]
        failed = cursor.execute("SELECT COUNT(*) FROM transactions WHERE status='FAILED'").fetchone()[0]

        print(f"Total inserted smoothly natively safely: {total}")
        assert failed == 0
        assert total > 50_000 # Since ~25% were randomly FAILED and should be filtered out.
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.


```python
def extract(self, csv_filepath: str, chunk_size=10_000):
    with open(csv_filepath, 'r') as f:
        reader = csv.DictReader(f)
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) == chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk
```

**HINT-2 (Partial)**:
Modern ETL transformation usually involves complex data cleaning and schema mapping:

```python
def transform(self, chunk: list[dict]) -> list[tuple]:
    cleaned = []
    for row in chunk:
        if row['status'] == 'FAILED':
            continue
        try:
            amt = float(row['amount'].replace("$", ""))
            cleaned.append((row['tx_id'], int(row['user_id']), amt, row['status']))
        except ValueError:
            pass # Skip corrupted rows or invalid formats
    return cleaned
```

**HINT-3 (Near-solution)**:

```python
def load(self, tuples: list[tuple]):
    self.conn.executemany(
        "INSERT INTO transactions (tx_id, user_id, amount, status) VALUES (?, ?, ?, ?)",
        tuples
    )
    self.conn.commit()

def run(self, csv_file: str):
    for chunk in self.extract(csv_file):
        cleaned_data = self.transform(chunk)
        self.load(cleaned_data)
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: Apache Airflow, Pandas, Spark, AWS Glue.

## 5. VALIDATION CRITERIA

- [ ] Processes data in chunks to maintain low memory footprint.
- [ ] Correctly filters out 'FAILED' records and transforms currency data.
- [ ] Uses batch inserts for efficient data loading.

## 6. EXTENSION CHALLENGES

1. **Extension 1:** Multi-threading the transform/load phase for increased throughput.
2. **Extension 2:** Implement logging and a summary report of skipped/failed rows.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`csv`, `sqlite3`).
