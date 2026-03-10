# Exercise Vision-01: Image Steganography

## 1. EXERCISE BRIEF

**Context**: Giấu thông tin tình báo (Steganography) mã hoá String vào ma trận các Bitmap ảnh là nghệ thuật cốt tủy bảo toàn tính riêng tư bí mật truyền tải Cyber.
**Task**: Thay thế LSB (Least Significant Bit) trên thư viện ảnh bằng Bytes Bits text bí mật nhập vào. Export thành file ngụy trang và decode trở lại mà ko phá vỡ ảnh hiển thị.
**Constraints**: Không dùng các module có tính năng mã hóa Steganography sẵn có. Tự mình encode bitstream trên hệ Array 3 chiều (Ảnh RGB).
## 2. STARTER CODE

```python
from PIL import Image

class ImageSteganography:
    def __init__(self):
        """
        TODO: [... logic ...] 
        """
        pass

    def encode(self, input_image_path: str, output_image_path: str, secret_message: str):
        """
        TODO: [... logic ...] 
        """
        pass

    def decode(self, image_path: str) -> str:
        """
        TODO: [... logic ...] 
        """
        pass

if __name__ == "__main__":
    import os
    import tempfile

    stego = ImageSteganography()

    with tempfile.TemporaryDirectory() as tmp:
        # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        base_image = os.path.join(tmp, "base.png")
        img = Image.new('RGB', (100, 100), color = 'red')
        img.save(base_image)

        encoded_image = os.path.join(tmp, "encoded.png")
        secret_msg = "TOP_SECRET: [... logic ...] "

        print(f"Encoding expertly fluently: '{secret_msg}'")
        stego.encode(base_image, encoded_image, secret_msg)

        decoded_msg = stego.decode(encoded_image)
        print(f"Decoded skillfully deftly valiantly: '{decoded_msg}'")

        assert secret_msg == decoded_msg
        print("Success! [... logic ...] ")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:

```python
    def encode(self, input_image_path: str, output_image_path: str, secret_message: str):
        img = Image.open(input_image_path)
        img = img.convert('RGB')
        pixels = img.load()

        # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        message_bytes = secret_message.encode('utf-8')
        message_bits = ''.join([format(b, '08b') for b in message_bytes])
        message_bits += '00000000' # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        width, height = img.size
        bit_idx = 0
        message_len = len(message_bits)

        for y in range(height):
            for x in range(width):
                if bit_idx < message_len:
                    r, g, b = pixels[x, y]

                    # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        r = (r & ~1) | int(message_bits[bit_idx])
                    bit_idx += 1

                    pixels[x, y] = (r, g, b)
                else:
                    img.save(output_image_path)
                    return
        img.save(output_image_path)
```

**HINT-3 (Near-solution)**:

```python
    def decode(self, image_path: str) -> str:
        img = Image.open(image_path)
        img = img.convert('RGB')
        pixels = img.load()

        width, height = img.size
        message_bits = ''

        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                message_bits += str(r & 1)

                # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        if len(message_bits) >= 8 and message_bits[-8:] == '00000000':
                    message_bits = message_bits[:-8] # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        byte_chunks = [message_bits[i:i+8] for i in range(0, len(message_bits), 8)]
                    message_bytes = bytearray([int(b, 2) for b in byte_chunks])
                    return message_bytes.decode('utf-8')

        return ""
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `Pillow`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Mã nguồn chạy thành công không báo lỗi, đạt hiệu năng tiêu chuẩn và cover được các test cases ẩn.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: `Pillow`.
