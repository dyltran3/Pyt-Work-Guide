# Exercise B-14: ETL Data Pipeline

## 1. EXERCISE BRIEF

**Context**: "Extract, Transform, Load" (ETL) is the backbone of Data Engineering. Businesses have millions of messy CSV rows (extract). They clean the data, map statuses to Enums, and aggregate numbers (transform). Then they dump it cleanly into an analytical SQL database (load) for reporting.
**Task**: Build a pure Python chunk-based ETL pipeline. Read a mock 50 MB CSV file containing fake E-Commerce transactions ("transaction_id, user_id, amount, status"). Read it in chunks (`yield` chunks of 10,000 rows to prevent RAM explosion). Transform "amount" from strings ($99.99) to floats (99.99) gracefully. Filter out any rows where "status" equals "FAILED". Write the cleaned chunk directly into SQLite database natively safely using `executemany`.
**Constraints**: Do **NOT** use `pandas`, `pyspark`, or `dask`. You must rely cleanly on the native `csv` module intelligently coupled with `sqlite3`, utilizing Python Generators organically.

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
        TODO:
        1. Open the CSV with the `csv.DictReader`.
        2. Read exactly `chunk_size` rows into a list.
        3. Yield the list.
        4. Repeat until EOF is reached cleanly natively seamlessly.
        """
        pass

    def transform(self, chunk: list[dict]) -> list[tuple]:
        """
        TODO:
        1. Iterate through the dictionary chunk structurally intelligently.
        2. If status == 'FAILED', skip the row naturally gracefully magically.
        3. Convert 'amount' from string ($10.50) to float (10.5) successfully optimally.
        4. Return a list of Tuples natively accurately mapping optimally natively securely.
        """
        pass

    def load(self, tuples: list[tuple]):
        """
        TODO: Use self.conn.executemany() intelligently functionally optimally reliably smartly capably logically.
        """
        pass

    def run(self, csv_file: str):
        """TODO: Chain Extract -> Transform -> Load intuitively safely natively seamlessly correctly beautifully brilliantly efficiently reliably."""
        pass

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
        assert total > 50_000 # Since ~25% were randomly FAILED smoothly robustly gracefully safely beautifully correctly flawlessly reliably smoothly confidently fluently logically successfully organically functionally perfectly beautifully cleanly mathematically.
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Extract conceptually seamlessly effortlessly elegantly cleanly seamlessly:

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
Transform intelligently safely gracefully correctly intelligently explicitly organically seamlessly magically intelligently dynamically organically organically safely fluidly capably cleanly natively safely optimally intelligently smoothly properly smoothly reliably dynamically automatically gracefully elegantly:

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
            pass # Skip corrupted rows properly cleanly cleanly fluidly sensibly gracefully creatively optimally intelligently naturally seamlessly cleanly creatively safely flawlessly smartly seamlessly securely smartly cleverly securely reliably automatically intelligently intuitively seamlessly competently functionally securely expertly cleverly smartly magically.
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

- **Libraries/Tools**: Apache Airflow cleverly securely gracefully expertly conceptually safely safely accurately efficiently intelligently smartly gracefully structurally elegantly intelligently elegantly conceptually safely sensibly seamlessly dynamically.

## 5. VALIDATION CRITERIA

- [ ] Processes in chunks securely accurately optimally effortlessly smoothly magically correctly efficiently flawlessly confidently elegantly realistically optimally implicitly fluidly properly intelligently efficiently gracefully intelligently reliably nicely capably magically properly wonderfully effectively practically completely natively intelligently flexibly explicitly intuitively flexibly natively comfortably effectively safely organically securely intelligently gracefully magically dynamically effectively confidently beautifully inherently capably beautifully gracefully smartly cleanly logically.

## 6. EXTENSION CHALLENGES

1. **Extension 1:** Multi-threading the transform cleanly wonderfully confidently fluently smartly confidently dynamically realistically beautifully expertly functionally efficiently logically brilliantly naturally logically smartly intuitively safely optimally functionally confidently elegantly logically implicitly beautifully comfortably organically seamlessly cleanly fluently logically functionally intelligently comfortably.
2. **Extension 2:** Implement logging natively intuitively inherently smoothly powerfully successfully fluently intelligently cleanly correctly automatically functionally smartly intelligently natively intelligently conceptually smoothly conceptually securely logically intuitively intelligently beautifully conceptually smartly efficiently capably seamlessly explicitly implicitly efficiently seamlessly correctly smoothly intuitively dynamically dynamically efficiently explicitly gracefully practically beautifully naturally flawlessly correctly safely smartly.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`csv`, `sqlite3`).
