# Exercise Cyber-01: Network Port Scanner

## 1. EXERCISE BRIEF

**Context**: Scanner Port là vũ khí chủ lực của Pentester để định vị điểm yếu của Host Network, hiểu giao thức TCP Socket và Timeout quản lý tấn công bề mặt (Attack Surface).
**Task**: Sản xuất CLI Threaded Port Scanner dò quét 1-1000 Protocol TCP Ports nhanh nhất để nhận điện Port open. Xuất bảng banner OS Footprint Fingerprint (Service Banner Grabbing) từ Header socket.
**Constraints**: Thread/ Coroutine siêu nhẹ hạn chế lag OS. Set Timeout kết nối chặt dưới 0.5s.
## 2. STARTER CODE

```python
import socket
import concurrent.futures
import ipaddress
import time

class PortScanner:
    def __init__(self, target: str, timeout: float = 1.0):
        """
        Initializes the scanner with a target host and timeout.
        Resolves hostname to IP address for faster scanning.
        """
        self.target = target
        self.timeout = timeout

        # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        try:
            self.ip = socket.gethostbyname(target)
        except socket.gaierror:
            raise ValueError(f"Could not resolve target host: {target}")

    def scan_port(self, port: int) -> bool:
        """
        Attempts to connect to a specific TCP port using a socket.
        """
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(self.timeout)
                result = sock.connect_ex((self.ip, port))
                return result == 0
        except Exception:
            return False

    def scan_range(self, start_port: int, end_port: int, max_workers: int = 50) -> list:
        """
        Scans a range of ports concurrently using multiple threads.
        """
        open_ports = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_port = {executor.submit(self.scan_port, port): port for port in range(start_port, end_port + 1)}
            for future in concurrent.futures.as_completed(future_to_port):
                if future.result():
                    open_ports.append(future_to_port[future])
        return sorted(open_ports)

if __name__ == "__main__":
    target_host = "scanme.nmap.org"
    print(f"Scanning target host: {target_host}...")
    scanner = PortScanner(target_host, timeout=0.5)

    start_time = time.time()
    open_ports = scanner.scan_range(1, 1024, max_workers=100)
    end_time = time.time()

    print(f"Scan completed in {end_time - start_time:.2f} seconds.")
    print(f"Open ports found: {open_ports}")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:

```python
    def scan_port(self, port: int) -> bool:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(self.timeout)
                sock.settimeout(self.timeout)
                result = sock.connect_ex((self.ip, port))
                return result == 0
        except Exception:
            return False
```

**HINT-3 (Near-solution)**:

```python
    def scan_range(self, start_port: int, end_port: int, max_workers: int = 50) -> list:
        open_ports = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        future_to_port = {executor.submit(self.scan_port, port): port for port in range(start_port, end_port + 1)}

            for future in concurrent.futures.as_completed(future_to_port):
                port = future_to_port[future]
                try:
                    if future.result():
                        open_ports.append(port)
                except Exception:
                    pass

        return sorted(open_ports)
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `nmap`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Correctly resolves hostname to IP address.
- [ ] Efficiently scans a range of ports using multi-threading.
- [ ] Correctly identifies open ports using TCP connect scan.
- [ ] Implements a configurable timeout to avoid long hangs.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
