# Exercise Data-04: Apache Parquet Writer từ đầu

## 1. EXERCISE BRIEF
**Context**: Định dạng Parquet là tiêu chuẩn vàng cho lưu trữ dữ liệu lớn (Spark, Athena, BigQuery). Khác với CSV (row-based), Parquet lưu trữ theo cột (columnar), giúp tăng tốc độ truy vấn chỉ trên một vài cột và tiết kiệm không gian bằng cách nén (Run-Length Encoding). Tại Việt Nam, các kỹ sư dữ liệu tại ZaloPay hay Momo phải tối ưu hóa data lake để giảm chi phí S3/HDFS.

**Task**: Hiện thực một bộ ghi dữ liệu mini (Parquet-like) bằng Python thuần. Bạn cần lưu trữ các cột riêng biệt, hỗ trợ Run-Length Encoding (RLE) cho các giá trị lặp lại, và ghi một đoạn metadata (footer) ở cuối file để biết vị trí bắt đầu của từng cột.

**Constraints**: Không dùng `pandas`, `pyarrow`, hay `fastparquet`. Chỉ sử dụng module `struct` để đóng gói dữ liệu nhị phân.

## 2. STARTER CODE
```python
import struct
import io

class MiniParquetWriter:
    def __init__(self):
        self.columns = {}
        self.metadata = {}

    def add_column(self, name, data):
        # TODO: Implement Run-Length Encoding (RLE)
        # RLE: (count, value), (count, value)
        pass

    def write(self, file_path):
        with open(file_path, "wb") as f:
            # TODO: Write column data and track offsets
            # TODO: Write footer metadata (JSON or binary)
            pass

# Demo
# writer = MiniParquetWriter()
# writer.add_column("status", ["success", "success", "fail", "success", "success"])
# writer.write("output.mparq")
```

## 3. PROGRESSIVE HINTS
**HINT-1 (Direction)**: Lưu trữ cột nghĩa là thay vì ghi các dòng `(id, name)`, bạn ghi toàn bộ danh sách `ids` rồi đến toàn bộ danh sách `names`.
**HINT-2 (Partial)**: RLE đơn giản: Duyệt qua list, nếu giá trị sau giống giá trị trước thì tăng count. Khi khác, đóng gói `(count, value)` vào byte stream bằng `struct.pack('I', count)`.
**HINT-3 (Near-solution)**: Cấu trúc file: `[MAGIC_BYTES][COL1_DATA][COL2_DATA][FOOTER_OFFSET][FOOTER_DATA]`. Footer nên chứa dict: `{"col_name": (offset, length)}`.

## 4. REAL-WORLD CONNECTIONS
- **Libraries/Tools**: Apache Parquet, Apache Arrow, ClickHouse.
- **Why do it manually**: Hiểu sâu giúp debug các lỗi về "Schema Evolution" hoặc tối ưu "Predicate Pushdown" (chỉ đọc đúng block dữ liệu cần thiết).

## 5. VALIDATION CRITERIA
- [ ] File đầu ra có dung lượng nhỏ hơn CSV khi dữ liệu lặp lại nhiều.
- [ ] Có thể đọc lại đúng dữ liệu từ file nhị phân mà không cần schema cứng.
- [ ] Metadata cuối file trỏ đúng địa chỉ offset của từng cột.

## 6. EXTENSION CHALLENGES
1. **Dictionary Encoding**: Thay vì lưu chuỗi dài, hãy map chuỗi sang integer và chỉ lưu list số nguyên.
2. **Snappy-like Compression**: Tích hợp module `zlib` để nén các block dữ liệu sau khi đã RLE.
3. **Data Page Splitting**: Chia một cột thành nhiều "pages" để cho phép đọc song song.

## SETUP REQUIREMENTS
- **Python Version**: 3.11+
- **Dependencies**: None (Standard Library only)
