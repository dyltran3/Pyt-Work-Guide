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
        Encodes bytes to base64url string without padding.
        """
        return base64.urlsafe_b64encode(data).decode().rstrip('=')

    def _base64url_decode(self, s: str) -> bytes:
        """
        Decodes base64url string back to bytes with proper padding.
        """
        padding = 4 - len(s) % 4
        return base64.urlsafe_b64decode(s + '=' * (padding % 4))

    def encode(self, payload: dict, expire_seconds: int = 3600) -> str:
        """
        Creates a JWT token with header, payload, and HMAC-SHA256 signature.
        """
        header = {"alg": "HS256", "typ": "JWT"}
        payload = {**payload, "exp": int(time.time()) + expire_seconds}
        
        b64h = self._base64url_encode(json.dumps(header).encode())
        b64p = self._base64url_encode(json.dumps(payload).encode())
        
        signing_input = f"{b64h}.{b64p}".encode()
        sig = hmac.new(self.secret, signing_input, hashlib.sha256).digest()
        b64s = self._base64url_encode(sig)
        
        return f"{b64h}.{b64p}.{b64s}"

    def decode(self, token: str) -> dict:
        """
        Verifies the signature and expiration of a JWT token.
        """
        parts = token.split('.')
        if len(parts) != 3:
            raise ValueError("Invalid JWT structure")
        
        b64h, b64p, b64s = parts
        signing_input = f"{b64h}.{b64p}".encode()
        expected_sig = hmac.new(self.secret, signing_input, hashlib.sha256).digest()
        actual_sig = self._base64url_decode(b64s)
        
        import secrets
        if not secrets.compare_digest(expected_sig, actual_sig):
            raise ValueError("Invalid signature - token tampered!")
            
        payload = json.loads(self._base64url_decode(b64p))
        if "exp" in payload and payload["exp"] < time.time():
            raise ValueError("Token expired")
            
        return payload

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

- [ ] Correctly encodes header and payload as base64url.
- [ ] Generates and verifies HMAC-SHA256 signatures securely.
- [ ] Properly handles expired tokens and tampered signatures.

## 6. EXTENSION CHALLENGES

1. **Extension 1:** Add support for multiple signing algorithms (e.g., HS512).
2. **Extension 2:** Implement a 'Blacklist' or 'Revocation' system to invalidate tokens before they expire.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`base64`, `json`, `hmac`, `hashlib`).
