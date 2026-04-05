# Exercise Data-09: Data Lineage Graph Builder

## 1. EXERCISE BRIEF
**Context**: Để tuân thủ Nghị định 13/2023, các tổ chức phải biết rõ nguồn gốc và luồng đi của dữ liệu cá nhân (PII). Data Lineage (Truy vết dữ liệu) trả lời câu hỏi: Dữ liệu này đến từ nguồn nào (`Source`), đi qua những hàm biến đổi nào (`Transform`), và kết quả cuối cùng nằm ở đâu (`Sink`). Nếu Table X bị lỗi, kỹ sư dữ liệu cần biết ngay những bảng hạ tầng (downstream) nào bị ảnh hưởng (Impact Analysis).

**Task**: Xây dựng một trình theo dõi Lineage sử dụng đồ thị có hướng (Directed Acyclic Graph - DAG). Thiết kế API dạng Decorator để tự động ghi lại input/output của hàm. Hỗ trợ truy vấn Impact Analysis (từ 1 node, tìm toàn bộ các node con chịu ảnh hưởng).

**Constraints**: Không được dùng thư viện `networkx`. Bạn phải tự xây dựng cấu trúc Danh sách kề (Adjacency List) từ đầu. Cần phát hiện được vòng lặp (Circular Lineage) - vốn là dấu hiệu của lỗi logic dữ liệu.

## 2. STARTER CODE
```python
class DataLineageTracker:
    def __init__(self):
        self.adj_list = {}
        self.metadata = {}

    def add_edge(self, source, target):
        # TODO: Cập nhật adjacency list
        # TODO: Phát hiện chu trình (Cycle Detection)
        pass

    def get_downstream(self, node):
        # TODO: Trả về toàn bộ các node bị ảnh hưởng (BFS/DFS)
        pass

def lineage_tracker(tracker):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # TODO: Tự động trích xuất metadata từ tham số
            # TODO: Ghi vào tracker (Source -> func -> Target)
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Example
# tracker = DataLineageTracker()
# @lineage_tracker(tracker)
# def transform_users(input_table, output_table): 
#     pass
```

## 3. PROGRESSIVE HINTS
**HINT-1 (Direction)**: Đồ thị kề (Adjacency List) mẫu: `{ "Table_A": ["Func_X"], "Func_X": ["Table_B"] }`.
**HINT-2 (Partial)**: Detect cycle bằng DFS kết hợp với "Recursion Stack". Nếu một node đang được duyệt mà lại xuất hiện trong stack hiện tại, đó là vòng lặp.
**HINT-3 (Near-solution)**: Impact Analysis thực chất là tìm tất cả các node có thể tới được (reachability) từ node gốc. Sử dụng Breadth-First Search (BFS) để liệt kê theo từng "level" ảnh hưởng.

## 4. REAL-WORLD CONNECTIONS
- **Libraries/Tools**: OpenLineage, Apache Atlas, Amundsen.
- **Why do it manually**: Hiểu "Metadata Management". Đây là bài toán cốt lõi của Data Governance và Data Quality tại các ngân hàng hay công ty bảo hiểm lớn.

## 5. VALIDATION CRITERIA
- [ ] Tự động phát hiện lỗi khi cấu hình Lineage có vòng lặp.
- [ ] Tìm ra được danh sách đầy đủ các node con (downstream) dù ở độ sâu bất kỳ.
- [ ] Decorator hoạt động được với nhiều hàm lồng nhau.

## 6. EXTENSION CHALLENGES
1. **Column-level Lineage**: Truy vết tới tận từng cột (ví dụ: `col_a` của `table_1` sinh ra `col_b` của `table_2`).
2. **Visualizer**: Xuất đồ thị ra định dạng DOT (Graphviz) để vẽ sơ đồ.
3. **Data Freshness Tracking**: Thêm thông tin "Last Updated" vào từng node để biết dữ liệu có bị "stale" (cũ) không.

## SETUP REQUIREMENTS
- **Python Version**: 3.11+
- **Dependencies**: None (Standard Library only)
