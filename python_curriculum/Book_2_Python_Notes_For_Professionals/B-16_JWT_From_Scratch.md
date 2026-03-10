# Exercise B-16: JWT từ Scratch

## 1. EXERCISE BRIEF

**Context**: JSON Web Token (JWT) stateless auth là cốt lõi cho mọi Micro-API Server. Biết được internals sẽ giúp bóc tách và tạo custom verify Token Engine dễ bảo trì.
**Task**: Build HMAC SHA256 Encoder và Verifier tạo một JWT Token theo đúng structure RFC 7519, tính chuẩn payload validation và Error handler Time Expire.
**Constraints**: Bắt lỗi chữ ký không đúng signature (Tainted Token). Phân tích mã hoá base64url padding an toàn.
## 2. STARTER CODE

```python
import base64
import json
import hmac
import hashlib
import time

class JWTBuilder:
    def __init__(self, secret: str):
        self.secret = secret.encode()

    def _base64url_encode(self, data: bytes) -> str:
        """
        TODO: Implement [... logic ...] 
        """
        pass

    def encode(self, payload: dict) -> str:
        """
        TODO: Create [... logic ...] 
        """
        pass

    def decode(self, token: str) -> dict:
        """
        TODO: Implement [... logic ...] 
        """
        pass

if __name__ == "__main__":
    jwt = JWTBuilder("supersecret")
    token = jwt.encode({"sub": "user123"})
    print("Generated elegantly smoothly:", token)

    decoded = jwt.decode(token)
    assert decoded["sub"] == "user123"
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:

```python
def _base64url_encode(self, data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode('utf-8').rstrip('=')
```

**HINT-3 (Near-solution)**:

```python
def encode(self, payload: dict) -> str:
    header = {"alg": "HS256", "typ": "JWT"}
    b64_header = self._base64url_encode(json.dumps(header).encode('utf-8'))
    b64_payload = self._base64url_encode(json.dumps(payload).encode('utf-8'))

    signature = hmac.new(self.secret, f"{b64_header}.{b64_payload}".encode('utf-8'), hashlib.sha256).digest()
    b64_signature = self._base64url_encode(signature)

    return f"{b64_header}.{b64_payload}.{b64_signature}"
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `pyjwt`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] [... logic ...] 

## 6. EXTENSION CHALLENGES

1. **Extension 1:** Implement [... logic ...] 
2. **Extension 2:** Implement [... logic ...] 

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`base64`, `json`, `hmac`, `hashlib`).
