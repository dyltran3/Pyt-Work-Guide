# Exercise A-04: Binary File Inspector

## 1. EXERCISE BRIEF

**Context**: Lập trình viên thỉnh thoảng phải xử lý hệ thống Legacy hoặc forensic data bằng binary. Hiểu cấu trúc bit/byte và Hex signature (Magic bytes) là kỹ năng phân biệt mid-level và senior engineer.
**Task**: Viết một script đọc vào một tập tin dạng Binary, bóc tách header của tập tin để tự động nhận dạng định dạng file (PNG, PDF, ZIP...), sau đó trích xuất kích thước và metadata thô.
**Constraints**: Sử dụng module `struct` để unpack bytes. Tuyệt đối không đọc toàn bộ file vào RAM cùng lúc, chỉ chunking theo buffer.
## 2. STARTER CODE

```python
import os

def generate_mock_binary(filename: str):
    # Generates a fake binary file representing a PNG (Notice the magic bytes for PNG)
    content = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89'
    content += os.urandom(80) # Fill the rest with random noise
    with open(filename, 'wb') as f:
        f.write(content)

def inspect_binary(filepath: str) -> None:
    """
    TODO:
    1. Read the file size using os.path.getsize()
    2. Open file in 'rb' mode, read first 64 bytes.
    3. Print Magic Bytes (First 4 bytes in hex)
    4. Print File Size
    5. Print the Hex Dump in lines of 16 bytes.
       Format: Offset(hex) | Hex Bytes (spaced) | ASCII characters (or '.')
    """
    pass

if __name__ == "__main__":
    test_file = 'test_image.png'
    generate_mock_binary(test_file)

    inspect_binary(test_file)

    # Expected Hex dump output roughly looks like:
    # 00000000  89 50 4e 47 0d 0a 1a 0a  00 00 00 0d 49 48 44 52  |.PNG........IHDR|
    # 00000010  ...
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
When reading a file loop in binary (`'rb'`), it returns `bytes` objects. Iterating over the `bytes` object yields the integers (0-255) representing each byte. You can format numbers into two-digit hex with `format(byte, '02x')`.

**HINT-2 (Partial)**:
To print in batches of 16, slice your chunk: `for i in range(0, len(raw), 16): line = raw[i:i+16]`. Use `[format(b, '02x') for b in line]` to get the hex values.

**HINT-3 (Near-solution)**:
For the ASCII translation at the end of the line, some bytes like `\n` or `0x89` are not printable and would break the terminal output. You must map them to a dot `.` if the integer value is outside the printable ASCII range (`32 <= b <= 126`):

```python
ascii_repr = "".join(chr(b) if 32 <= b <= 126 else "." for b in chunk_line)
hex_part = " ".join(f"{b:02x}" for b in chunk_line[:8]) + "  " + " ".join(f"{b:02x}" for b in chunk_line[8:])
print(f"{offset:08x}  {hex_part:<49}  |{ascii_repr}|")
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `xxd`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Successfully reads the file size and the raw file contents.
- [ ] Explicitly identifies the top 4 magic bytes (For the PNG mock, this would be `89 50 4e 47`).
- [ ] The hex dump output splits nicely at exactly 16 bytes per row (Offset 0x00, 0x10, 0x20, 0x30).
- [ ] The ASCII display correctly hides unprintable characters by replacing them with a period `.`.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Magic Byte Signature Match):** Build a manual dictionary of known signatures (e.g., `89 50 4e 47` -> PNG, `25 50 44 46` -> PDF, `50 4b 03 04` -> ZIP). Compare the magic bytes against your dictionary and print a warning if the file's extension doesn't match the signature's expected extension.
2. **Extension 2 (Chunking):** Add argument flags. Instead of loading the first 64 bytes, take command-line arguments (like `-n`) to output `n` lines of the hex dump (reading up to `16 * n` bytes). Support very large values via stream processing without exhausting memory.
3. **Extension 3 (Find Data):** Write a search method within the raw binary looking for a specific text string (like finding human-readable strings floating inside a `.exe` file), conceptually duplicating the Linux `strings` CLI tool.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
