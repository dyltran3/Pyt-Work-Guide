# Exercise Data-05: Change Data Capture (CDC) Engine

## 1. EXERCISE BRIEF
**Context**: Change Data Capture (CDC) là kiến trúc ghi lại các thay đổi (INSERT/UPDATE/DELETE) trong DB để đồng bộ dữ liệu tới các hệ thống hạ tầng khác (Elasticsearch, Data Warehouse). Tại Việt Nam, CDC được áp dụng mạnh mẽ để tuân thủ Nghị định 13/2023 (ghi nhật ký xử lý dữ liệu cá nhân). Nếu website thương mại điện tử cập nhật số điện thoại khách hàng, CDC sẽ ngay lập tức gửi sự kiện này sang hệ thống audit logs.

**Task**: Hiện thực cơ chế CDC sử dụng chế độ WAL (Write-Ahead Log) của SQLite. Theo dõi các thay đổi dòng dữ liệu (row-level) với ảnh chụp trước/sau (before/after snapshots). Phát ra các "Change Events" theo định dạng có cấu trúc.

**Constraints**: Chỉ sử dụng thư viện chuẩn `sqlite3`. Phải xử lý được trường hợp nhiều tiến trình cùng ghi vào database một lúc mà không bị mất sự kiện.

## 2. STARTER CODE
```python
import sqlite3
import json
import time

class CDCEngine:
    def __init__(self, db_path):
        self.db_path = db_path
        self.last_sync_id = 0
        self._setup_audit_table()

    def _setup_audit_table(self):
        # TODO: Tạo bảng 'audit_log' và trigger để lưu vết INSERT/UPDATE/DELETE
        pass

    def poll_events(self):
        # TODO: Query audit_log bắt đầu từ last_sync_id
        # Trả về list các Change Events dạng dict
        pass

# Example usage
# engine = CDCEngine("user_data.db")
# for event in engine.poll_events():
#     print(f"Captured: {event['op']} on row {event['row_id']}")
```

## 3. PROGRESSIVE HINTS
**HINT-1 (Direction)**: Để bắt được sự kiện trong SQLite mà không dùng app logic phức tạp, hãy dùng `TRIGGER`. Tự động chèn một dòng vào bảng `audit_log` bất kể user gọi `INSERT` từ code Python hay Tool SQL.
**HINT-2 (Partial)**: Trigger mẫu: `CREATE TRIGGER tr_update AFTER UPDATE ON my_table BEGIN INSERT INTO audit_log(op, old_val, new_val) VALUES ('UPDATE', old.data, new.data); END;`.
**HINT-3 (Near-solution)**: Sử dụng hàm `json_object()` của SQLite để đóng gói `OLD` và `NEW` row thành chuỗi JSON trực tiếp trong trigger.

## 4. REAL-WORLD CONNECTIONS
- **Libraries/Tools**: Debezium, Kafka Connect, AWS DMS.
- **Why do it manually**: Hiểu bản chất của "Commit Log". Database thực tế ghi log trước khi ghi data. Hiểu CDC giúp bạn xây dựng hệ thống event-driven thực sự chuẩn xác (Exact-once delivery).

## 5. VALIDATION CRITERIA
- [ ] Mọi lệnh UPDATE phát từ Terminal SQL cũng phải hiện ra trong code Python.
- [ ] Xử lý được snapshot `OLD` khi `DELETE` và snapshot `NEW` khi `INSERT`.
- [ ] Hỗ trợ Filter sự kiện theo bảng (Table-level filtering).

## 6. EXTENSION CHALLENGES
1. **Schema Tolerance**: Nếu bảng chính thêm 1 cột mới, CDC có crash không? Hãy xử lý schema evolution.
2. **Backfill Mode**: Cho phép quét ngược lịch sử (full snapshot) trước khi bắt đầu stream.
3. **Sequence Order Guarantee**: Đảm bảo các sự kiện đồng thời không bị sai thứ tự (hãy dùng `rowid` hoặc `timestamp`).

## SETUP REQUIREMENTS
- **Python Version**: 3.11+
- **Dependencies**: None (Standard Library only)
