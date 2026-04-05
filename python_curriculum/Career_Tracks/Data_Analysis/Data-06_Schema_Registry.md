# Exercise Data-06: Schema Registry & Evolution Validator

## 1. EXERCISE BRIEF
**Context**: Trong kiến trúc Microservices (sử dụng Kafka/RabbitMQ), các team phát triển Schema dữ liệu độc lập. Khi Team A thêm cột vào sự kiện, Team B (Consumer) có thể bị "crash" vì không hiểu dữ liệu mới. Confluent Schema Registry giải quyết việc này bằng cách quản lý phiên bản và quy tắc tiến hóa (Evolution Rules). Bài tập này yêu cầu bạn xây dựng một Registry mini phục vụ kiểm định tính tương thích của JSON Schemas.

**Task**: Xây dựng một Schema Registry lưu trữ trong bộ nhớ (in-memory) hỗ trợ các chế độ tương thích: BACKWARD, FORWARD, FULL. Quản lý phiên bản Schema cho từng "subject". Kiểm tra tính hợp lệ trước khi đăng ký phiên bản mới.

**Constraints**: Không dùng thư viện bên ngoài. Schema được lưu trữ dưới dạng danh sách các dict lồng nhau (nested dicts), không cần dùng SQL.

## 2. STARTER CODE
```python
class SchemaRegistry:
    def __init__(self):
        self.subjects = {} # {subject_name: [list_of_schemas]}
        self.modes = {}    # {subject_name: 'BACKWARD'|'FORWARD'|'FULL'}

    def register_schema(self, subject, new_schema):
        # TODO: Kiểm tra tính tương thích (compatibility check)
        # TODO: Nếu hợp lệ, tăng version và lưu lại
        pass

    def check_compatibility(self, subject, new_schema):
        # BACKWARD: Consumer code mới đọc được data cũ
        # FORWARD: Consumer code cũ đọc được data mới
        # FULL: Cả 2 chiều mô tả trên
        pass

# Example
# registry = SchemaRegistry()
# registry.register_schema("user_signup", {"id": "int", "name": "string"})
# registry.register_schema("user_signup", {"id": "int", "name": "string", "age": "int"}) # OK (Backward)
```

## 3. PROGRESSIVE HINTS
**HINT-1 (Direction)**: Tính tương thích "Backward" nghĩa là các field đã có phải được giữ nguyên hoặc chỉ thêm field mới có giá trị mặc định (optional).
**HINT-2 (Partial)**: Duyệt schemas: Lấy schema version mới nhất (V-current). Nếu Mode là "Backward", so khớp tất cả keys của schema cũ xem có còn tồn tại trong schema mới hay không.
**HINT-3 (Near-solution)**: Sử dụng đệ quy để so sánh nested objects. Nếu một field bị đổi kiểu (type change), đánh dấu là "Incompatible".

## 4. REAL-WORLD CONNECTIONS
- **Libraries/Tools**: Confluent Schema Registry, Apache Avro, Protobuf.
- **Why do it manually**: Hiểu "Contract First" development. Ngăn chặn lỗi sản phẩm do thay đổi cấu trúc dữ liệu không báo trước (breaking changes).

## 5. VALIDATION CRITERIA
- [ ] Chặn được việc xóa đi một field bắt buộc (Backward Incompatible).
- [ ] Cho phép thêm field mới với giá trị mặc định (Backward Compatible).
- [ ] Hỗ trợ versioning (mỗi subject có thể có V1, V2, V3...).

## 6. EXTENSION CHALLENGES
1. **Type Definition Resolver**: Hỗ trợ alias (ví dụ: 'uuid' thực chất là 'string').
2. **Schema ID Persistence**: Tích hợp module `json` để lưu registry ra file đĩa.
3. **Reference Support**: Cho phép Schema A tham chiếu tới Schema B (ví dụ: schema `Order` chứa `Address`).

## SETUP REQUIREMENTS
- **Python Version**: 3.11+
- **Dependencies**: None (Standard Library only)
