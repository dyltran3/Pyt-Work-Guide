# Exercise Cyber-04: TLS Certificate Chain Inspector

## 1. EXERCISE BRIEF
**Context**: Chứng chỉ TLS hết hạn hoặc cấu hình sai là nguyên nhân hàng đầu gây gián đoạn dịch vụ liên tục (Outages). Theo Nghị định 13/2023, các điểm cuối (endpoints) xử lý dữ liệu cá nhân tại Việt Nam bắt buộc phải chạy trên HTTPS với các thuật toán mã hóa hiện đại. Kỹ sư bảo mật cần tự động hóa việc kiểm tra chuỗi chứng chỉ (certificate chain) để đảm bảo không có chứng chỉ nào sắp hết hạn hoặc dùng thuật toán yếu (như MD5, SHA1).

**Task**: Kết nối tới một HTTPS endpoint, trích xuất toàn bộ chuỗi chứng chỉ, phân tách các trường X.509 (CN, SAN, Expiry, Issuer, Key Algorithm). Kiểm tra tính hợp lệ của chuỗi tin cậy (Chain of Trust) và đưa ra cảnh báo nếu chứng chỉ sắp hết hạn trong vòng 30 ngày.

**Constraints**: Phải sử dụng module `ssl` của thư viện chuẩn kết hợp với package `cryptography`. Cần xử lý được các chứng chỉ wildcard (ví dụ: `*.google.com`) và IP SANs (Subject Alternative Names).

## 2. STARTER CODE
```python
import ssl
import socket
from datetime import datetime, timedelta
from cryptography import x509

class TLSInspector:
    def __init__(self, hostname, port=443):
        self.hostname = hostname
        self.port     = port

    def get_cert_chain(self):
        # TODO: Thiết lập kết nối SSL và lấy raw certs
        pass

    def inspect_cert(self, raw_cert):
        # TODO: Parse X509 fields
        # return { "CN": ..., "expiry": ..., "algorithm": ..., "issuer": ... }
        pass

    def run_audit(self):
        # TODO: Tổng hợp cảnh báo nếu < 30 ngày hoặc dùng RSA < 2048
        pass

# Example
# inspector = TLSInspector("google.com")
# report = inspector.run_audit()
```

## 3. PROGRESSIVE HINTS
**HINT-1 (Direction)**: Sử dụng `ssl.create_connection()` để bắt tay (handshake) với server. Hãy nhớ thiết lập `context.check_hostname = True` để bảo mật tối đa.
**HINT-2 (Partial)**: Lấy chứng chỉ bằng `sslsock.getpeercert(binary_form=True)`. Sau đó dùng `x509.load_der_x509_certificate()` để chuyển sang đối tượng tiện dụng của thư viện `cryptography`.
**HINT-3 (Near-solution)**: Kiểm tra ngày hết hạn: `cert.not_valid_after_utc`. Tính toán khoảng cách (delta) so với `datetime.now(timezone.utc)`. Đừng quên kiểm tra các extension SAN để so khớp domain thực tế.

## 4. REAL-WORLD CONNECTIONS
- **Libraries/Tools**: OpenSSL, Certbot (Let's Encrypt), SSL Labs.
- **Why do it manually**: Tích hợp trực tiếp vào hệ thống giám sát (Monitoring) nội bộ mà không cần phụ thuộc vào API bên ngoài (giảm nguy cơ lộ thông tin về hạ tầng private).

## 5. VALIDATION CRITERIA
- [ ] Phân tích đúng cả Intermediate và Root CA trong chuỗi (nếu có).
- [ ] Cảnh báo chính xác các chứng chỉ hết hạn hoặc sắp hết hạn.
- [ ] Phát hiện được phiên bản TLS tối thiểu (ví dụ: chặn TLS 1.0, 1.1).

## 6. EXTENSION CHALLENGES
1. **CRL/OCSP Stapling**: Kiểm tra xem chứng chỉ có bị nhà phát hành thu hồi (revoked) hay không.
2. **Cipher Suite Audit**: Liệt kề toàn bộ danh sách Cipher Suites mà server hỗ trợ và đánh dấu các bộ yếu (weak ciphers).
3. **Multi-target Scanner**: Hỗ trợ quét hàng loạt domain từ file CSV và xuất báo cáo PDF.

## SETUP REQUIREMENTS
- **Python Version**: 3.11+
- **Dependencies**: `pip install cryptography`
