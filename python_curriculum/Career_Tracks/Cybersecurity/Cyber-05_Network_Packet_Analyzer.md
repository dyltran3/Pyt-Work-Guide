# Exercise Cyber-05: Network Packet Analyzer (PCAP Parser)

## 1. EXERCISE BRIEF
**Context**: Đội ngũ Blue Team cần phân tích lưu lượng mạng (Captured Traffic) để tìm kiếm các dấu hiệu bất thường như: rò rỉ dữ liệu (exfiltration), mã độc kết nối về máy chủ điều khiển (C2 Beaconing), hoặc các truy vấn DNS kỳ lạ. Việc hiểu cấu trúc file PCAP giúp kỹ sư bảo mật xây dựng các hệ thống IDS (Intrusion Detection System) tùy chỉnh ngay cả khi không có các công cụ nặng nề như Wireshark.

**Task**: Phân tích file PCAP thủ công (Global Header + Per-packet Records) bằng Python. Trích xuất các luồng TCP/UDP, phát hiện các mẫu quét cổng (Port Scanning) - nhiều IP khác nhau nhắm vào cùng 1 port, hoặc 1 IP nhắm vào nhiều port liên tiếp. Nhận diện các dấu hiệu DNS Tunneling (truy vấn subdomain có độ ngẫu nhiên - entropy cao).

**Constraints**: Chỉ sử dụng module `struct` của thư viện chuẩn. Không dùng `Scapy` hay `dpkt`. Phải xử lý được các gói tin bị cắt cụt (truncated packets).

## 2. STARTER CODE
```python
import struct

class PCAPAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self._parse_global_header()

    def _parse_global_header(self):
        # TODO: Đọc 24 bytes header của file PCAP
        # Xác định Magic Number (endianness), Version, Network Type (Ethernet?)
        pass

    def next_packet(self):
        # TODO: Trình lặp (Iterator) trả về từng gói tin
        # packet_header (16 bytes) + packet_data
        pass

    def analyze_dns_entropy(self, dns_query):
        # TODO: Tính toán Shannon Entropy cho domain name
        # domain có entropy > 4.0 thường là dấu hiệu DNS Tunneling
        pass

# Example
# analyzer = PCAPAnalyzer("captured_traffic.pcap")
# for pkt in analyzer.next_packet():
#     process_ethernet_frame(pkt)
```

## 3. PROGRESSIVE HINTS
**HINT-1 (Direction)**: File PCAP bắt đầu bằng một Global Header 24-byte. Quan trọng nhất là `Magic Number` (ví dụ: `0xa1b2c3d4`). Nó giúp bạn biết file lưu ở dạng Little-endian hay Big-endian.
**HINT-2 (Partial)**: Packet Record Header dài 16 bytes, trong đó có trường `incl_len` (độ dài thực tế gói tin lưu trong file) và `orig_len` (độ dài gốc trên dây mạng). Dùng `struct.unpack` để lấy các giá trị này.
**HINT-3 (Near-solution)**: Ethernet Header dài 14 bytes. Sau đó là IP Header (thường 20 bytes). Phải kiểm tra Protocol byte (6 cho TCP, 17 cho UDP) để biết cách parse tiếp theo.

## 4. REAL-WORLD CONNECTIONS
- **Libraries/Tools**: Wireshark/tshark, TCPDump, Zeek (Bro), Scapy.
- **Why do it manually**: Phân tích file PCAP siêu lớn (vài GB) mà không gây tràn bộ nhớ (OOM). Wireshark thường load toàn bộ vào RAM, còn code Python của bạn có thể stream từng gói tin.

## 5. VALIDATION CRITERIA
- [ ] Trích xuất đúng Source IP và Destination IP của từng gói tin.
- [ ] Tính toán chính xác Shannon Entropy cho các chuỗi subdomain.
- [ ] Không bị crash khi gặp file PCAP bị lỗi (Corrupted PCAP).

## 6. EXTENSION CHALLENGES
1. **Flow Reassembly**: Ghép các gói tin TCP riêng lẻ thành một luồng dữ liệu (Stream) hoàn chỉnh (xử lý Sequence Number và Ack).
2. **GeoIP Integration**: Gắn nhãn quốc gia cho các IP hướng ngoại sử dụng database GeoLite2 miễn phí.
3. **Anomalous TTL Detection**: Theo dõi giá trị TTL (Time To Live). Nếu TTL thay đổi đột ngột giữa các gói tin cùng flow, có thể là dấu hiệu của IP Spoofing.

## SETUP REQUIREMENTS
- **Python Version**: 3.11+
- **Dependencies**: None (Standard Library only)
