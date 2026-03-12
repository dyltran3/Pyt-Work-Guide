# Exercise Data-01: Production Data Quality Framework

## 1. EXERCISE BRIEF

**Context**: Lỗi dữ liệu Dirty Data (NULL chìm, sai định dạng Data types, giá trị lệch chuẩn) gây ra 80% rác hệ thống Data Warehouse, cần phải chặn đứng trước khi Insert DB.
**Task**: Build Validator Pipeline kiểm thử Data Pandas/Spark style (Sử dụng Pydantic/dataclasses cho Model Validate), tự động xuất Rejects Summary báo cáo sai lỗi.
**Constraints**: Giao diện kiểm thử mềm (Soft validation), gom đủ lỗi thay vì exit khi exception lần 1.
## 2. STARTER CODE

```python
import pandas as pd
import numpy as np

class DataQualityFramework:
    def __init__(self):
        """
        Initializes the framework with an empty list of validation rules.
        """
        self.rules = []

    def add_rule(self, column: str, rule_type: str, **kwargs):
        """
        Registers a validation rule for a specific column.
        """
        self.rules.append({"column": column, "rule_type": rule_type, "params": kwargs})

    def run_checks(self, df: pd.DataFrame) -> dict:
        """
        Runs all registered rules against the provided DataFrame and returns a detailed report.
        """
        report = {"total_rows": len(df), "failures": []}
        for rule in self.rules:
            col = rule["column"]
            rtype = rule["rule_type"]
            params = rule["params"]
            
            if col not in df.columns:
                report["failures"].append({"column": col, "rule": rtype, "error": "Column missing"})
                continue

            series = df[col]
            if rtype == 'not_null':
                invalid_indices = df[series.isna()].index.tolist()
            elif rtype == 'unique':
                invalid_indices = df[series.duplicated()].index.tolist()
            elif rtype == 'range':
                invalid_indices = df[~series.between(params.get('min_val', -np.inf), params.get('max_val', np.inf))].index.tolist()
            elif rtype == 'regex':
                invalid_indices = df[~series.astype(str).str.match(params.get('pattern', ''))].index.tolist()
            else:
                continue

            if invalid_indices:
                report["failures"].append({
                    "column": col,
                    "rule": rtype,
                    "invalid_count": len(invalid_indices),
                    "sample_indices": invalid_indices[:5]
                })
        return report

if __name__ == "__main__":
    df = pd.DataFrame({
        "id": [1, 2, 3, 3, 5], # Contains duplicate
        "age": [25, 30, -5, 45, 120], # Contains invalid values (-5, 120)
        "email": ["test@example.com", "invalid-email", "user@test.com", "admin", None] # Contains invalid formats and NULL
    })

    dq = DataQualityFramework()
    dq.add_rule("id", "unique")
    dq.add_rule("age", "range", min_val=0, max_val=100)
    dq.add_rule("email", "regex", pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$")

    results = dq.run_checks(df)
    print("Quality Report Summary:")
    print(results)
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:

```python
    def add_rule(self, column: str, rule_type: str, **kwargs):
        self.rules.append({
            "column": column,
            "rule_type": rule_type,
            "params": kwargs
        })
```

**HINT-3 (Near-solution)**:

```python
    def run_checks(self, df: pd.DataFrame) -> dict:
        results = {}
        for idx, rule in enumerate(self.rules):
            col = rule["column"]
            rtype = rule["rule_type"]
            params = rule["params"]

            if col not in df.columns:
                results[f"Rule_{idx}"] = {"status": "failed", "reason": f"Column {col} missing from DataFrame"}
                continue

            series = df[col]
            if rtype == "not_null":
                passed = series.notna().all()
                results[f"Rule_{idx}"] = {"status": "passed" if passed else "failed"}
            elif rtype == "unique":
                passed = series.is_unique
                results[f"Rule_{idx}"] = {"status": "passed" if passed else "failed"}
            elif rtype == "range":
                passed = series.between(params.get("min_val", -np.inf), params.get("max_val", np.inf)).all()
                results[f"Rule_{idx}"] = {"status": "passed" if passed else "failed"}
            elif rtype == "regex":
                passed = series.astype(str).str.match(params.get("pattern", "")).all()
                results[f"Rule_{idx}"] = {"status": "passed" if passed else "failed"}

        return results
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `Great Expectations`, `Pydantic`, `Pandas Profiling`, `Dequé`.

## 5. VALIDATION CRITERIA

- [ ] Correctly identifies duplicate IDs.
- [ ] Correctly flags out-of-range ages.
- [ ] Correctly validates email patterns using regex.
- [ ] Returns a structured failure report instead of stopping on first error.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: `pandas`, `numpy`.
