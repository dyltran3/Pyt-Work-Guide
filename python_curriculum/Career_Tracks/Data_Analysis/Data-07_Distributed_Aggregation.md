# Exercise Data-07: Distributed Aggregation with MapReduce Pattern

## 1. EXERCISE BRIEF
**Context**: MapReduce là nền tảng của Hadoop, Spark và các hệ thống xử lý dữ liệu lớn khác. Hiểu cơ chế này giúp kỹ sư dữ liệu tối ưu hóa chi phí tính toán khi làm việc với hàng tỷ dòng dữ liệu. Thay vì tính toán tập trung (Centralized), bài toán được chia nhỏ ra nhiều máy (Map), sau đó gom nhóm và tính toán kết quả cuối cùng (Reduce).

**Task**: Hiện thực một Framework MapReduce sử dụng module `multiprocessing` trong Python. Áp dụng Framework này để đếm tần năng của từ (word frequency) từ một file text khổng lồ, sau đó mở rộng để tính toán thống kê phiên truy cập (session statistics) từ logs người dùng.

**Constraints**: Bắt buộc sử dụng đa phân luồng/đa tiến trình (`multiprocessing.Pool`). Cần có bước "Combiner optimization" (tính toán sơ bộ ngay tại Map node) để giảm tải cho bước Shuffle.

## 2. STARTER CODE
```python
import multiprocessing
from collections import defaultdict

class MapReduceEngine:
    def __init__(self, mapper_fn, reducer_fn, num_workers=4):
        self.mapper_fn = mapper_fn
        self.reducer_fn = reducer_fn
        self.num_workers = num_workers

    def run(self, data_list):
        # 1. Map phase with Combiner
        # 2. Shuffle phase (group by key)
        # 3. Reduce phase
        pass

def word_mapper(text):
    # TODO: Trả về (word, count) và áp dụng Combiner (dict)
    pass

def word_reducer(word, counts):
    # TODO: Trả về (word, sum_counts)
    pass

# Usage
# data = ["hello world", "hello python", "spark and mapreduce", ...]
# engine = MapReduceEngine(word_mapper, word_reducer)
# result = engine.run(data)
```

## 3. PROGRESSIVE HINTS
**HINT-1 (Direction)**: `Pool.map()` của multiprocessing sẽ giúp bạn chạy hàm `mapper` song song trên nhiều CPU.
**HINT-2 (Partial)**: Sau khi Map xong, bạn sẽ có một list các `(key, value)`. Bạn cần "Shuffle": tạo một dict lớn `results = {key: [val1, val2, ...]}` để gom toàn bộ giá trị có cùng key về một chỗ trước khi đưa sang `reducer`.
**HINT-3 (Near-solution)**: Combiner là một bước "mini-reduce" trong chính mapper. Thay vì trả về `[('a', 1), ('a', 1)]`, trả về `[('a', 2)]`. Điều này cực kỳ quan trọng khi xử lý qua network.

## 4. REAL-WORLD CONNECTIONS
- **Libraries/Tools**: Apache Hadoop, PySpark, Dask.
- **Why do it manually**: Reason về "Distributed Compute Cost". Hiểu tại sao bước Shuffle thường là "bottleneck" (nghẽn cổ chai) trong các job Spark.

## 5. VALIDATION CRITERIA
- [ ] Tốc độ thực thi trên file log 100MB nhanh hơn xử lý đơn luồng.
- [ ] Sử dụng được 100% tài nguyên CPU (Parallelism).
- [ ] Kết quả tính toán trùng khớp với logic tuần tự.

## 6. EXTENSION CHALLENGES
1. **Fault Tolerance**: Giả lập một worker bị lỗi (exception) và cơ chế thử lại (Retry).
2. **Partial Shuffling**: Tích hợp module `heapq` để merge các cặp key-value đã sắp xếp.
3. **Sessionization Work**: Input là log: `(user_id, action, timestamp)`. Output là `(user_id, avg_session_duration)`.

## SETUP REQUIREMENTS
- **Python Version**: 3.11+
- **Dependencies**: None (Standard Library only)
