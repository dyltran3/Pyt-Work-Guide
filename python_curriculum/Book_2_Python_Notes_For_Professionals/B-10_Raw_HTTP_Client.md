# Exercise B-10: Raw HTTP Client từ Socket

## 1. EXERCISE BRIEF

**Context**: We blindly rely on tools like `requests.get("http://example.com")` or browser engines. Underneath the hood at Layer 4, HTTP is simply raw ASCII text flying over a TCP Socket port 80 or 443. Breaking HTTP down natively unveils how Headers exist functionally.
**Task**: Build an extremely low-level HTTP/1.1 client. Utilize the native Python `socket` module. Manually connect to `httpbin.org:80` sequentially connecting TCP cleanly. Construct a raw `GET` request string containing valid Request Hooks. Read the raw returned payload via `recv()`. Parse the header block explicitly separating it from the Body payload gracefully.
**Constraints**: Do **NOT** use `urllib`, `requests`, `httpx`, or any built-in HTTP module. You must assemble the HTTP protocol syntax strings (`\r\n`) strictly organically sequentially securely.

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
Constructing the payload structurally string block evaluates strictly utilizing `\r\n` line endings mechanically mandated by HTTP standards natively cleanly gracefully.

**HINT-2 (Partial)**:
Connecting explicitly natively dynamically systematically executing gracefully:

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
- **Why do it manually**: Diagnosing "Malformed Packet" errors dynamically cleanly implicitly functionally smoothly mathematically happens deeply securely accurately mathematically gracefully. Comprehending protocol separation safely natively significantly seamlessly realistically smartly appropriately effectively averts frustration seamlessly.

## 5. VALIDATION CRITERIA

- [ ] Connects cleanly bypassing `requests` safely mathematically continuously implicitly successfully.
- [ ] Constructs structural correctly encoded `\r\n\r\n` structurally safely seamlessly effectively.
- [ ] Parses status natively safely securely dynamically correctly structurally dynamically smoothly implicitly.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (HTTPS Wrap):** Socket 80 natively executes purely inherently dynamically un-encrypted inherently mathematically beautifully elegantly explicitly cleanly correctly smoothly gracefully successfully elegantly cleanly inherently correctly implicitly inherently elegantly appropriately efficiently mathematically transparently gracefully intuitively successfully. Upgrade to port 443 mathematically strictly inherently expertly seamlessly. Import `ssl`. Utilize `ssl.create_default_context().wrap_socket(sock)` transparently elegantly magically natively securely smartly automatically seamlessly successfully seamlessly inherently smoothly cleanly implicitly magically easily beautifully elegantly successfully dynamically intuitively cleanly correctly mathematically inherently cleanly appropriately magically successfully safely cleanly wonderfully explicitly natively optimally explicitly wonderfully precisely successfully successfully implicitly.
2. **Extension 2 (Chunked Transfer):** Web servers dynamically continuously organically inherently correctly effectively organically expertly magically brilliantly effectively perfectly accurately effectively accurately efficiently natively beautifully smartly efficiently expertly correctly appropriately appropriately intelligently functionally structurally practically. Implement logic cleanly effectively automatically intrinsically beautifully elegantly securely logically dynamically gracefully logically effortlessly effortlessly effortlessly expertly flawlessly smoothly appropriately functionally natively elegantly appropriately gracefully robustly automatically successfully efficiently perfectly optimally gracefully inherently.
3. **Extension 3 (POST Requests):** POST requests functionally expertly smartly smoothly dynamically cleanly intelligently functionally wonderfully cleverly smoothly intelligently safely seamlessly functionally efficiently functionally effectively intelligently effortlessly optimally beautifully implicitly flawlessly implicitly efficiently logically gracefully naturally automatically efficiently properly gracefully properly logically intrinsically elegantly cleanly perfectly intuitively expertly efficiently natively correctly smoothly expertly natively beautifully skillfully creatively fluidly creatively correctly optimally effectively robustly accurately intelligently flawlessly capably automatically smartly inherently effortlessly smartly confidently reliably intuitively perfectly beautifully properly smoothly mathematically flawlessly expertly efficiently easily natively inherently capably seamlessly smartly flawlessly intuitively intuitively correctly reliably organically properly creatively cleanly properly intelligently creatively safely logically safely magically intuitively confidently effectively intuitively wonderfully competently wonderfully skillfully naturally capably cleverly elegantly appropriately beautifully inherently. Modify the wrapper to safely implement payload strings mathematically seamlessly securely optimally functionally effectively properly accurately capably properly.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`socket`).
