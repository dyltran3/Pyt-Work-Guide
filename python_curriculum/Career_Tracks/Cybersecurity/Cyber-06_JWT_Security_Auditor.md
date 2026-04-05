# Exercise Cyber-06: JWT Security Auditor

## 1. EXERCISE BRIEF
**Context**: JSON Web Token (JWT) là hình thức xác thực phổ biến nhất trong các ứng dụng web hiện nay. Tuy nhiên, các lỗi cấu hình JWT đứng trong Top 10 của OWASP (Broken Authentication). Các lỗi phổ biến bao gồm: chấp nhận thuật toán `none`, dùng Key yếu (có thể brute-force), thiếu trường `exp` (hết hạn), hoặc nhầm lẫn giữa thuật toán đối xứng (HS256) và bất đối xứng (RS256).

**Task**: Xây dựng một công cụ kiểm định bảo mật (Auditor) cho JWT. Công cụ này phải kiểm tra: tấn công thay đổi thuật toán (`alg:none`), khả năng brute-force secret, thiếu các xác nhận (claims) quan trọng, và các lỗi về padding base64url.

**Constraints**: Mở rộng từ bài tập B-16 (JWT từ Scratch). Tự xây dựng các hàm giả lập tấn công (Attacker Simulation). Phải nhận diện được ít nhất 5 lớp lỗ hổng khác nhau.

## 2. STARTER CODE
```python
import base64
import json
import hmac
import hashlib

class JWTAuditor:
    def __init__(self, token):
        self.token = token
        self._parse_pieces()

    def _parse_pieces(self):
        # TODO: Split header, payload, signature
        pass

    def check_alg_none(self):
        # TODO: Kiểm tra xem server có Token với alg='none' không
        pass

    def brute_force_secret(self, wordlist):
        # TODO: Thử nghiệm danh sách mật khẩu với HMAC-SHA256
        pass

    def check_claims(self):
        # TODO: Kiểm tra sự tồn tại của exp, iat, iss, sub
        pass

# Example
# auditor = JWTAuditor("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...")
# results = auditor.run_all_checks()
```

## 3. PROGRESSIVE HINTS
**HINT-1 (Direction)**: Mã độc hoặc hacker thường đổi header từ `{"alg": "HS256"}` sang `{"alg": "none"}` và xóa phần Signature. Auditor phải cảnh báo nếu token này vẫn được server coi là hợp lệ.
**HINT-2 (Partial)**: Tấn công "Key Confusion" (RS256 sang HS256): Hacker dùng Public Key của server (vốn công khai) làm Secret Key để ký theo thuật toán HS256. Kiểm tra xem code verify có bị nhầm lẫn giữa 2 loại key này không.
**HINT-3 (Near-solution)**: Brute-force secret: Lặp qua wordlist, tính toán HMAC-SHA256 của `header.payload` bằng mỗi secret. Nếu kết quả trùng với Signature của token, Secret đã bị lộ.

## 4. REAL-WORLD CONNECTIONS
- **Libraries/Tools**: Burp Suite (JWT Editor), jwt.io, Auth0.
- **Why do it manually**: Hiểu sâu cơ chế "Signature vs Encryption". Đảm bảo bạn không chỉ cài đặt thư viện một cách mù quáng mà còn biết cấu hình an toàn cho Production.

## 5. VALIDATION CRITERIA
- [ ] Phát hiện được token giả mạo với thuật toán `none`.
- [ ] Tìm ra secret yếu (ví dụ: '123456', 'admin') trong dưới 1 giây.
- [ ] Cảnh báo chính xác các token không có thời gian hết hạn (`exp`).

## 6. EXTENSION CHALLENGES
1. **Public Key Crawler**: Tự động tải `jwks.json` từ endpoint của server để xác thực.
2. **Algorithm Enforcement**: Viết một Decorator cho FastAPI/Flask chỉ cho phép một danh sách thuật toán an toàn duy nhất (Whitelisting).
3. **Payload Data Leakage Scanner**: Cảnh báo nếu Payload chứa thông tin nhạy cảm (như password, credit_card) ở dạng plaintext.

## SETUP REQUIREMENTS
- **Python Version**: 3.11+
- **Dependencies**: None (Standard Library only)
