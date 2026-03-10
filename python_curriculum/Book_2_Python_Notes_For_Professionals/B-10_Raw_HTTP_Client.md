# Exercise B-10: Raw HTTP Client từ Socket

## 1. EXERCISE BRIEF

**Context**: Việc sử dụng quá nhiều REST dependencies làm nặng dự án siêu nhỏ (micro-systems), am hiểu nguyên thủy HTTP Protocol mở đường tối giản container size.
**Task**: Xây dựng bộ tạo Request RAW cho HTTP/1.1 bằng Text Protocols theo đúng rfc2616, mở TCP Socket thuần túy để GET dữ liệu, bọc qua parse thủ công.
**Constraints**: Sử dụng socket nội tại `socket`, Không được phép import `urllib` hay `requests`.
## 2. STARTER CODE

```python
import socket

def raw_http_get(host: str, path: str = "/") -> tuple[int, dict, str]:
    """
    TODO:
    1. Open a socket explicitly (AF_INET, SOCK_STREAM).
    2. Connect natively to (host, 80).
    3. Construct standard HTTP/1.1 string natively.
       Format: "GET <path> HTTP/1.1\\r\\nHost: <host>\\r\\nConnection: close\\r\\n\\r\\n"
    4. Send payload encoded strictly to bytes safely.
    5. Receive bytes natively dynamically.
    6. Split the response exactly by "\\r\\n\\r\\n".
    7. Parse the HTTP Status code from the first line natively.
    8. Return (status_code, response_headers_dict, response_body_string).
    """
    pass

if __name__ == "__main__":
    host = "httpbin.org"
    path = "/get?test=success"

    status, headers, body = raw_http_get(host, path)

    print(f"Status Code: {status}")
    print(f"Headers Array: {headers.keys()}")
    print("-" * 20)
    print("Body Chunk:")
    print(body[:200]) # Preview of body

    assert status == 200
    assert "test" in body
    assert "Content-Type" in headers or "content-type" in headers
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:
Connecting [... logic ...] :

```python
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, 80))

request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
sock.sendall(request.encode('utf-8'))
```

**HINT-3 (Near-solution)**:

```python
def raw_http_get(host, path):
    # setup and send request (as above)...
    raw_response = b""
    while True:
        chunk = sock.recv(4096)
        if not chunk: break
        raw_response += chunk

    response_str = raw_response.decode('utf-8')
    header_block, body = response_str.split("\r\n\r\n", 1)

    header_lines = header_block.split("\r\n")
    status_line = header_lines[0]
    status_code = int(status_line.split()[1])

    headers = {}
    for line in header_lines[1:]:
        if ":" in line:
            key, val = line.split(":", 1)
            headers[key.strip()] = val.strip()

    return status_code, headers, body
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: Core logic behind `requests`, `urllib3`, Nginx raw streams natively cleanly.
- **Why do it manually**: Diagnosing "Malformed Packet" errors [... logic ...] gracefully. Comprehending protocol separation [... logic ...] 

## 5. VALIDATION CRITERIA

- [ ] Connects cleanly bypassing `requests` [... logic ...] 
- [ ] Constructs structural correctly encoded `\r\n\r\n` [... logic ...] 
- [ ] Parses status [... logic ...] 

## 6. EXTENSION CHALLENGES

1. **Extension 1 (HTTPS Wrap):** Socket 80 natively executes [... logic ...] -encrypted [... logic ...] 443 [... logic ...] `ssl`. Utilize `ssl.create_default_context().wrap_socket(sock)` [... logic ...] 
2. **Extension 2 (Chunked Transfer):** Web servers [... logic ...] [... logic ...] 
3. **Extension 3 (POST Requests):** POST requests [... logic ...] implement payload strings [... logic ...] 

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`socket`).
