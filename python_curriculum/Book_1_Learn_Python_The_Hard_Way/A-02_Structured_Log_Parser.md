# Exercise A-02: Structured Log Parser

## 1. EXERCISE BRIEF

**Context**: Hệ thống backend thực tế sinh ra hàng triệu dòng log mỗi ngày dưới chuẩn unstructured hoặc semi-structured. Phân tích chúng là bước đầu tiên để tích hợp vào Elasticsearch hay Kibana.
**Task**: Viết một engine phân tích file log lớn. Engine cần có khả năng bóc tách IP, Timestamp, Error Level và Message bằng Regular Expressions (Regex), sau đó nhóm các lỗi theo IP.
**Constraints**: Phải xử lý file theo cơ chế Generator (yield line-by-line) để tối ưu RAM. Dung lượng bộ nhớ (Memory Allocation) không được vượt quá 30MB ngay cả với log file 10GB.
## 2. STARTER CODE

```python
def generate_mock_log(filename: str) -> None:
    content = '''192.168.1.10 - - [10/Oct/2026:13:55:36 -0700] "GET /api/users HTTP/1.1" 200 1024
10.0.0.5 - - [10/Oct/2026:13:55:38 -0700] "POST /api/auth HTTP/1.1" 401 256
192.168.1.11 - - [10/Oct/2026:13:56:01 -0700] "GET /api/posts HTTP/1.1" 200 512
8.8.8.8 - - [10/Oct/2026:13:56:05 -0700] "GET /admin HTTP/1.1" 403 128
10.0.0.2 - - [10/Oct/2026:13:56:10 -0700] "GET /api/users HTTP/1.1" 500 0'''
    with open(filename, 'w') as f:
        f.write(content)

def parse_log_line(line: str) -> dict:
    """
    TODO: Given a single log line, parse it and return a dict with keys:
    'ip', 'timestamp', 'method', 'path', 'status_code', 'bytes_sent'
    """
    pass

def analyze_logs(filename: str) -> dict[int, int]:
    """
    TODO: Read the file, parse each line, and return a dictionary counting
    the occurrences of each status code (e.g., {200: 2, 401: 1, 403: 1, 500: 1}).
    """
    pass

if __name__ == "__main__":
    generate_mock_log('access.log')

    # Test your parsing
    sample_line = '192.168.1.10 - - [10/Oct/2026:13:55:36 -0700] "GET /api/users HTTP/1.1" 200 1024'
    parsed = parse_log_line(sample_line)
    assert parsed['status_code'] == 200
    assert parsed['method'] == 'GET'

    # Test your analysis
    stats = analyze_logs('access.log')
    print(f"Status Code Summary: {stats}")
    assert stats[200] == 2
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Since the log has a fixed structure, you can split the line by spaces. Notice that the timestamp is wrapped in `[]` and the HTTP request is wrapped in `""`.

**HINT-2 (Partial)**:
Be careful when splitting by space because the date and request parts contain spaces too.
Alternatively, use slicing/splitting via the known delimiters like `[` or `"`.

```python
parts = line.split('"')
# parts[0] -> '192.168.1.10 - - [10/Oct/2026:13:55:36 -0700] '
# parts[1] -> 'GET /api/users HTTP/1.1'
# parts[2] -> ' 200 1024'
```

**HINT-3 (Near-solution)**:

```python
def parse_log_line(line: str) -> dict:
    parts = line.split('"')
    front = parts[0].split()
    req = parts[1].split()
    back = parts[2].split()

    return {
        'ip': front[0],
        'timestamp': front[3][1:], # remove '['
        'method': req[0],
        'path': req[1],
        'status_code': int(back[0]),
        'bytes_sent': int(back[1])
    }
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: AWS CloudWatch, Datadog, ELK Stack (Elasticsearch, Logstash, Kibana), Splunk.
- **Why do it manually**: Production log parsers often use Grok (Regex abstraction) or JSON. But writing a custom parser from scratch forces you to handle unexpected data, empty strings, and type casting, which are the leading causes of data pipeline failures.

## 5. VALIDATION CRITERIA

- [ ] Returns correct dictionary structure for a parsed line.
- [ ] Correctly casts `status_code` and `bytes_sent` to integers, not strings.
- [ ] Correctly tallies up the status codes.
- [ ] Processes multiple lines cleanly without leaving trailing newline strings `\n` in the output data.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Safety):** Assume some log lines might be corrupted or incomplete. Add a `try/except` block to `parse_log_line` to handle `IndexError` or `ValueError` and return `None`. Skip `None` results in `analyze_logs`.
2. **Extension 2 (Time Filtering):** Add `start_time` and `end_time` arguments to `analyze_logs` that only count logs occurring within that specific window by parsing the custom string timestamp into `datetime` objects.
3. **Extension 3 (Generators):** Change `analyze_logs` so it doesn't store all the parsed dictionaries in memory at once. Use a generator to yield one parsed dict at a time to keep it memory-efficient.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: None. Standard library only.
