# Exercise DevOps-02: Advanced CI/CD Pipeline

## 1. EXERCISE BRIEF

**Context**: Automation Continuous Integration & Deployment giải phóng Team Tech khỏi sự cố (Bugs) trên Main Branch, tối ưu vòng Feedback chất lượng dự án Dev pipeline GitOps.
**Task**: Tạo Github Action Workflows Workflow config (yaml) cấu trúc Test Matrix theo chuẩn. Validate Style/Linter (Flake8/Ruff), test chạy Pytest Coverage và Report pass mới duyệt Push Merge branch.
**Constraints**: Matrix setup chạy giả lập đa nền tảng tối cực điểm. Code quality chặn (Fails step) nếu code error Lints Format.
## 2. STARTER CODE

```yaml
# .github/workflows/python-app.yml
name: Python application

on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
      - name: Set up Python 3.11
        uses: actions/setup-python@v3
        with:
          python-version: "3.11"

      # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install flake8 pytest
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      - name: Lint with flake8
        run: |
          # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
          flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

      - name: Test with pytest
        run: |
          pytest
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:

```yaml
- name: Run Black/Ruff [... logic ...] 
  run: ruff check . && black --check .

- name: Upload coverage [... logic ...] 
  uses: codecov/codecov-action@v3
  with:
    files: ./coverage.xml
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `GitHub [... logic ...] `` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Mã nguồn chạy thành công không báo lỗi, đạt hiệu năng tiêu chuẩn và cover được các test cases ẩn.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: None.
