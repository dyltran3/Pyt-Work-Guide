# Exercise B-15: Password Hashing System

## 1. EXERCISE BRIEF

**Context**: Mã hoá mật khẩu lưu vào database nếu thiếu độ trễ tính toán (Cost/Work factor lớn) hoặc muối (Salt) đều làm tăng nguy cơ Dictionary/Rainbow-table Attack.
**Task**: Xây dụng khung Hash & Verify an toàn chống Timing Attack trên nền thuật toán băm chậm, ứng dụng module bí mật sinh salt bảo mật.
**Constraints**: Sử dụng `hashlib.pbkdf2_hmac` hoặc `bcrypt`. Cơ chế mật mã compare phải dùng `secrets.compare_digest` để ngừa Timing attack.
## 2. STARTER CODE

```python
import hashlib
import os

class AuthSystem:
    def __init__(self):
        # Mocks a SQLite database in memory
        self.db = {}

    def hash_password(self, password: str, salt: bytes) -> str:
        """
        Hashes a password using PBKDF2 with a high iteration count.
        """
        key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 260_000)
        return key.hex()

    def register_user(self, email: str, password: str):
        """
        Generates a random salt and stores the user's hash.
        """
        salt = os.urandom(32)
        pwd_hash = self.hash_password(password, salt)
        self.db[email] = {"salt": salt.hex(), "password_hash": pwd_hash}

    def login_user(self, email: str, password: str) -> bool:
        """
        Fetches the user's salt and verifies the password using constant-time comparison.
        """
        record = self.db.get(email)
        if not record:
            return False
        import secrets
        salt = bytes.fromhex(record["salt"])
        attempt_hash = self.hash_password(password, salt)
        return secrets.compare_digest(attempt_hash, record["password_hash"])

if __name__ == "__main__":
    auth = AuthSystem()

    auth.register_user("admin@example.com", "SuperSecret123!")

    # Valid login credentials
    assert auth.login_user("admin@example.com", "SuperSecret123!") is True
    assert auth.login_user("admin@example.com", "WrongPassword") is False
    assert "admin@example.com" in auth.db
    assert auth.db["admin@example.com"]["password_hash"] != "SuperSecret123!"

    print("Authentication system verified successfully.")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:
Using `secrets.compare_digest` is critical to prevent attackers from guessing passwords by measuring the time the server takes to respond.

**HINT-3 (Near-solution)**:

```python
def hash_password(self, password: str, salt: bytes) -> str:
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    )
    return key.hex()

def register_user(self, email: str, password: str):
    salt = os.urandom(32)
    pwd_hash = self.hash_password(password, salt)
    self.db[email] = {
        "salt": salt.hex(),
        "password_hash": pwd_hash
    }
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `bcrypt`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Correctly implements PBKDF2 with salt.
- [ ] Uses constant-time comparison for verification.
- [ ] Properly handles non-existent users.

## 6. EXTENSION CHALLENGES

1. **Extension 1:** Implement password complexity requirements (regex).
2. **Extension 2:** Implement account lockout after X failed attempts.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`hashlib`, `os`).
