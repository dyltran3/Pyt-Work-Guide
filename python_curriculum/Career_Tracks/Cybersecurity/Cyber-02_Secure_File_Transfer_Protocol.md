# Exercise Cyber-02: Secure File Transfer Protocol

## 1. EXERCISE BRIEF

**Context**: Chuyên gia Mạng yêu cầu Server nội bộ truyền tải mã hoá an toàn File nhạy cảm, không dùng FTP gốc dễ bị nghe trộm Sniffing Payload.
**Task**: Thiết kế Giao thức Secure File Transfer trên Socket. Sử dụng cấu hình Symmetric Key (vd: AES encryption thông qua cryptography package) encrypt file, nén và truyền cho Server tiếp nhận giải mã và Validate Checksum Hash File.
**Constraints**: So sánh File Hash (MD5/SHA256) End-to-End đảm bảo không gói (packet) Drop / Corrupt trong quá trình mạng.
## 2. STARTER CODE

```python
import os
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

class SecureFileTransfer:
    def __init__(self, key: bytes):
        """
        TODO: [... logic ...] 
        """
        self.key = key

    def encrypt_file(self, input_path: str, output_path: str):
        """
        TODO: [... logic ...] 
        """
        pass

    def decrypt_file(self, input_path: str, output_path: str):
        """
        TODO: [... logic ...] 
        """
        pass

if __name__ == "__main__":
    import tempfile

    key = get_random_bytes(32) # AES-256 [... logic ...] 
    sft = SecureFileTransfer(key)

    with tempfile.TemporaryDirectory() as tmp:
        original_file = os.path.join(tmp, "secret.txt")
        encrypted_file = os.path.join(tmp, "secret.enc")
        decrypted_file = os.path.join(tmp, "secret_decrypted.txt")

        with open(original_file, "w") as f:
            f.write("CONFIDENTIAL: [... logic ...] !")

        sft.encrypt_file(original_file, encrypted_file)
        sft.decrypt_file(encrypted_file, decrypted_file)

        with open(decrypted_file, "r") as f:
            content = f.read()
            assert "CONFIDENTIAL" in content
            print("[... logic ...] !")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:

```python
    def encrypt_file(self, input_path: str, output_path: str):
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        with open(input_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
            f_out.write(iv)
            # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        plaintext = f_in.read()
            ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
            f_out.write(ciphertext)
```

**HINT-3 (Near-solution)**:

```python
    def decrypt_file(self, input_path: str, output_path: str):
        with open(input_path, 'rb') as f_in:
            iv = f_in.read(AES.block_size)
            ciphertext = f_in.read()

        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

        with open(output_path, 'wb') as f_out:
            f_out.write(plaintext)
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `pycryptodome`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Mã nguồn chạy thành công không báo lỗi, đạt hiệu năng tiêu chuẩn và cover được các test cases ẩn.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: `pycryptodome`.
