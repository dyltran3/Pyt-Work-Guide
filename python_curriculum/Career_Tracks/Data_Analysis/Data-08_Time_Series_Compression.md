# Exercise Data-08: Time-Series Compression (Delta + Gorilla)

## 1. EXERCISE BRIEF
**Context**: Các hệ thống giám sát như Prometheus, InfluxDB hay TimescaleDB lưu trữ hàng tỷ metrics (nhiệt độ CPU, băng thông mạng). Thuật toán "Gorilla" (Facebook) cho phép nén dữ liệu số thực lên tới 12 lần bằng cách chỉ lưu trữ sự khác biệt (Delta) và toán tử XOR. Tại Việt Nam, tối ưu hóa lưu trữ metrics giúp các doanh nghiệp Fintech/Edtech tiết kiệm hàng nghìn USD chi phí Cloud hàng tháng.

**Task**: Hiện thực thuật toán nén Delta encoding cho nhãn thời gian (timestamps) và nén XOR-based cho giá trị Float64 (số thực). So sánh dung lượng file nhị phân sau khi nén với dung lượng lưu trữ thô (`raw bytes`).

**Constraints**: Chỉ sử dụng module `struct` để đóng gói dữ liệu nhị phân. Không dùng `numpy` hay bất kỳ thư viện toán học nào bên ngoài.

## 2. STARTER CODE
```python
import struct

class GorillaCompressor:
    def __init__(self):
        self.last_ts = 0
        self.last_val = 0
        self.compressed_data = bytearray()

    def add_point(self, timestamp, value):
        # 1. Delta encoding for timestamp
        # 2. XOR encoding for float64 value
        pass

    def get_compressed_size(self):
        return len(self.compressed_data)

# Test data
# metrics = [(1712234500, 25.4), (1712234560, 25.5), (1712234620, 25.4), ...]
# compressor = GorillaCompressor()
# for ts, val in metrics: compressor.add_point(ts, val)
```

## 3. PROGRESSIVE HINTS
**HINT-1 (Direction)**: Timestamps thường cách đều (ví dụ: 60s). Delta encoding: thay vì lưu số 1712234560 (8 bytes), hãy lưu 60 (1 byte).
**HINT-2 (Partial)**: XOR floats: Hai số thực gần nhau (25.4 và 25.5) có các bit đầu tiên giống hệt nhau. Khi XOR chúng, bạn sẽ nhận được một chuỗi số 0 ở đầu. Bạn chỉ cần lưu phần nội dung khác biệt.
**HINT-3 (Near-solution)**: Sử dụng `struct.pack('>Q', int_repr)` để chuyển Float sang Integer 64-bit nhằm thực hiện phép toán BITWISE `^` (XOR).

## 4. REAL-WORLD CONNECTIONS
- **Libraries/Tools**: Prometheus (v2 storage), Facebook Gorilla, InfluxDB TSM.
- **Why do it manually**: Hiểu "Numerical Precision" và cách lưu trữ bitwise. Đây là kiến thức nền tảng để viết các hệ thống database engine tốc độ cao.

## 5. VALIDATION CRITERIA
- [ ] Tỷ lệ nén (Compression Ratio) đạt ít nhất 3x trên dữ liệu thực tế.
- [ ] Có thể giải nén (Decompress) mà không sai số (Lossless).
- [ ] Tốc độ nén đạt trên 100,000 points/giây.

## 6. EXTENSION CHALLENGES
1. **Bit-stream Implementation**: Thuật toán Gorilla thực tế nén theo từng "bit" (không phải byte). Hãy sử dụng class để quản lý bit-level Writing.
2. **Double-Delta**: Nén sự thay đổi của sự thay đổi (delta-of-delta).
3. **Floating Window**: Tự động reset last-value sau một khoảng thời gian nhất định để tránh trôi (drift).

## SETUP REQUIREMENTS
- **Python Version**: 3.11+
- **Dependencies**: None (Standard Library only)
