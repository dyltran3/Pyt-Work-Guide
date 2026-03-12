# Exercise Cyber-03: Log Forensics Analyzer

## 1. EXERCISE BRIEF

**Context**: Nhóm Blue Team điều tra Incident (Sự cố an ninh) cần rà soát hàng ngàn logs NGINX/Syslog để tìm Pattern dấu hiệu Tấn công DDoS hoặc Local File Inclusion (LFI).
**Task**: Lập trình Threat Hunting Log Parser Scanner: Nhập tệp logs chuẩn HTTP, trích xuất Pattern bất thường dựa trên số truy cập vượt tải theo phút (DDoS), hoặc Access URLs nghi án Path Traversal (`../..`).
**Constraints**: Cảnh báo Alert theo IP/Geo format cho SOC chuyên nghiệp.
## 2. STARTER CODE

```python
import re
from collections import defaultdict
import datetime
import time # Added for time.time()

class LogForensicsAnalyzer:
    def __init__(self):
        """
        Initializes the analyzer with structures for tracking suspicious activity.
        """
        self.failed_logins = defaultdict(list) # Stores timestamps of failed login attempts per IP
        self.traversal_attempts = [] # Stores log lines indicating path traversal attempts
        self.suspicious_ips = set() # Stores IPs identified as suspicious

    def parse_log(self, log_line: str):
        """
        Parses a single log line to detect brute force and path traversal.
        """
        # Brute force detection (e.g., 'Failed password for root from ...')
        brute_force_pattern = r'Failed password for .* from (\d+\.\d+\.\d+\.\d+)'
        match = re.search(brute_force_pattern, log_line)
        if match:
            ip = match.group(1)
            self.failed_logins[ip].append(time.time())

        # Path traversal detection (e.g., '../../etc/passwd')
        traversal_pattern = r'(\.\.\/|\.\.\\)'
        if re.search(traversal_pattern, log_line):
            self.traversal_attempts.append(log_line)

    def detect_brute_force(self, threshold: int = 5, time_window: int = 60) -> list:
        """
        Detects brute force attempts based on a threshold of failed logins within a time window.
        """
        current_time = time.time()
        for ip, timestamps in self.failed_logins.items():
            recent_attempts = [t for t in timestamps if current_time - t <= time_window]
            if len(recent_attempts) > threshold:
                self.suspicious_ips.add(ip)
        return list(self.suspicious_ips)

    def get_summary(self) -> dict:
        """
        Provides a summary of detected threats.
        """
        summary = {
            "brute_force_ips": list(self.suspicious_ips),
            "path_traversal_attempts": self.traversal_attempts,
            "total_failed_login_attempts": sum(len(v) for v in self.failed_logins.values())
        }
        return summary

if __name__ == "__main__":
    mock_log = [
        "2023-10-27T10:00:01Z 192.168.1.100 sshd[1234]: Accepted publickey for user test from 192.168.1.100 port 54321 ssh2",
        "2023-10-27T10:05:01Z 10.0.0.5 sshd[1235]: Failed password for user root from 10.0.0.5 port 12345 ssh2",
        "2023-10-27T10:05:02Z 10.0.0.5 sshd[1236]: Failed password for user root from 10.0.0.5 port 12346 ssh2",
        "2023-10-27T10:05:03Z 10.0.0.5 sshd[1237]: Failed password for user root from 10.0.0.5 port 12347 ssh2",
        "2023-10-27T10:05:04Z 10.0.0.5 sshd[1238]: Failed password for user root from 10.0.0.5 port 12348 ssh2",
        "2023-10-27T10:05:05Z 10.0.0.5 sshd[1239]: Failed password for user root from 10.0.0.5 port 12349 ssh2",
        "2023-10-27T10:05:06Z 10.0.0.5 sshd[1240]: Failed password for user root from 10.0.0.5 port 12350 ssh2",
        "2023-10-27T10:10:01Z 192.168.1.101 apache: GET /etc/passwd HTTP/1.1",
        "2023-10-27T10:10:02Z 192.168.1.102 apache: GET /var/www/html/index.php?file=../../../../etc/passwd HTTP/1.1"
    ]

    analyzer = LogForensicsAnalyzer()
    for line in mock_log:
        analyzer.parse_log(line) # Changed from parse_log_line to parse_log

    analyzer.detect_brute_force(threshold=4) # Detect brute force with a threshold
    results = analyzer.get_summary()
    print("Forensics Summary:")
    print(results)

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:

```python
    def parse_log_line(self, line: str):
        # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        match = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*(Failed password)", line)
        if match:
            ip = match.group(1)
            self.failed_logins[ip] += 1
```

**HINT-3 (Near-solution)**:

```python
    def detect_brute_force(self, threshold: int = 5) -> list:
        for ip, count in self.failed_logins.items():
            if count > threshold:
                self.suspicious_ips.add(ip)
        return list(self.suspicious_ips)
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `fail2ban`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Mã nguồn chạy thành công không báo lỗi, đạt hiệu năng tiêu chuẩn và cover được các test cases ẩn.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`re`, `collections`).
