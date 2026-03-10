# Exercise B-01: Network Packet Flag Inspector

## 1. EXERCISE BRIEF

**Context**: Deep Packet Inspection (DPI) yêu cầu đọc trực tiếp cờ (flags) bitwise trên các network protocols để phát hiện dị thường hoặc scan cổng.
**Task**: Tạo công cụ bitwise operations trích xuất thông tin TCP Flags (SYN, ACK, FIN...) từ một TCP Header giả lập, ứng dụng masking & bit-shifting.
**Constraints**: Thực hiện phân tích Hex hoàn toàn thuần bằng code bitwise (`&`, `|`, `>>`, `<<`). Validate theo chuẩn TCP header format.
## 2. STARTER CODE

```python
def parse_tcp_flags(flags_int: int) -> dict[str, bool]:
    """
    TODO: Use bitwise & to check the status of each flag.
    TCP Flag Bit Positions:
    URG (Urgent) = 0x20 (32)
    ACK (Acknowledgment) = 0x10 (16)
    PSH (Push) = 0x08 (8)
    RST (Reset) = 0x04 (4)
    SYN (Synchronize) = 0x02 (2)
    FIN (Finish) = 0x01 (1)
    """
    return {
        "URG": False, # Replace with bitwise logic
        "ACK": False,
        "PSH": False,
        "RST": False,
        "SYN": False,
        "FIN": False
    }

if __name__ == "__main__":
    # SYN-ACK Packet (Common in TCP 3-way handshake)
    # SYN (2) + ACK (16) = 18
    syn_ack = 0x12  # Hexadecimal for 18

    parsed = parse_tcp_flags(syn_ack)
    print(f"SYN-ACK Flags: {parsed}")

    assert parsed["SYN"] is True
    assert parsed["ACK"] is True
    assert parsed["FIN"] is False
    assert parsed["URG"] is False

    # FIN-ACK Packet (Connection teardown)
    # FIN (1) + ACK (16) = 17
    fin_ack = 17
    assert parse_tcp_flags(fin_ack)["FIN"] is True
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
The bitwise `&` (AND) compares each bit of two numbers. If you `flags_int & 0x02`, it checks if the 2nd bit is `1` in both numbers. If it is, the result is `2`. If it isn't, the result is `0`.

**HINT-2 (Partial)**:
You can wrap the bitwise expression in `bool()` to naturally convert `2` to `True` and `0` to `False`.

```python
is_syn = bool(flags_int & 0x02)
```

**HINT-3 (Near-solution)**:

```python
def parse_tcp_flags(flags: int) -> dict[str, bool]:
    return {
        "URG": bool(flags & 0x20),
        "ACK": bool(flags & 0x10),
        "PSH": bool(flags & 0x08),
        "RST": bool(flags & 0x04),
        "SYN": bool(flags & 0x02),
        "FIN": bool(flags & 0x01)
    }
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `Scapy`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Strictly applies `&` checks.
- [ ] Returns perfectly typed booleans.
- [ ] Accurate assertions for both Handshake (`0x12`) and Teardown (`17`).

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Assembly Byte String):** Doing the reverse. Write a `construct_tcp_flag(flags_dict: dict) -> int` function that accepts a dictionary of True/False settings and outputs the 1-byte integer utilizing the Bitwise OR `|` operator.
2. **Extension 2 (Struct Unpacking):** Import the `struct` module. Parse an entire simulated 20-byte TCP header taking an incoming `bytes` payload. Find specifically where the flags byte lives (usually Byte 13) within the header offset, unpack it, and feed it into your parser.
3. **Extension 3 (Bit-Shifting Permission Matrix):** Assume standard Linux Permissions `chmod 777`. Read an integer like `0o755` (Octal format). Use right-shifts `>>` to break the integer into 3 groups of numbers (Owner, Group, World) and print exactly which permissions each group possesses (Read/Write/Execute).

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
