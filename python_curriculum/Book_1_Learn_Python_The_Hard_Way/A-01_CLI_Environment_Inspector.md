# Exercise A-01: CLI Environment Inspector

## 1. EXERCISE BRIEF

**Context**: Môi trường dòng lệnh (CLI) là giao diện đầu vào quan trọng cho các công cụ CI/CD, script tự động hóa. Việc tự động hóa lấy và kiểm thử thông tin hệ thống giúp đảm bảo tính nhất quán giữa các môi trường (Dev, Staging, Prod).
**Task**: Xây dựng công cụ CLI (Command-Line Interface) từ đầu để thu thập Metadata của hệ điều hành, biến môi trường (Environment Variables) và kiểm tra phân quyền thư mục, sau đó xuất kết quả dưới dạng JSON.
**Constraints**: Tuyệt đối không sử dụng thư viện bên thứ ba như `click` hay `typer`. Giới hạn chỉ dùng các module tích hợp sẵn (`os`, `sys`, `json`). Must handle graceful fallback nếu không có quyền truy cập root/admin.
## 2. STARTER CODE

```python
import os
import sys

def get_filtered_env_vars() -> dict[str, str]:
    """
    TODO: Return a dictionary of environment variables where the key
    contains 'PATH', 'HOME', or 'VIRTUAL_ENV'.
    """
    pass

def print_env_table(env_vars: dict[str, str]) -> None:
    """
    TODO: Print the dictionary as a formatted ASCII table.
    The table should have headers: "VARIABLE" and "VALUE".
    Align the Variable column to the left with a fixed width.
    Truncate values that are longer than 80 characters.
    """
    pass

if __name__ == "__main__":
    # Test your functions
    filtered_vars = get_filtered_env_vars()

    # Simple assertion checks
    assert isinstance(filtered_vars, dict), "Should return a dictionary"

    print_env_table(filtered_vars)
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Use `os.environ` to get a dictionary-like object of all environment variables. To filter them, a dictionary comprehension with an `if` condition checking the key works best.

**HINT-2 (Partial)**:
For alignment in the table, Python's f-strings allow specifying a width. For example, `f"{key:<30}"` forces the string to take up at least 30 characters, padding with spaces on the right.

**HINT-3 (Near-solution)**:

```python
env = {k: v for k, v in os.environ.items() if 'PATH' in k or 'HOME' in k or 'VIRTUAL_ENV' in k}

# Printing the header
print(f"{'VARIABLE':<30} | {'VALUE'}")
print("-" * 30 + "-+-" + "-" * 40)
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: The `python-dotenv` library is universally used to load these variables from `.env` files into `os.environ` during application startup.
- **Why do it manually**: Understanding how environment strings are strictly keyed helps prevent painful debugging sessions when deploying to AWS/GCP or inside Docker containers where a typo in a variable key breaks the app.
- **Architectural Pattern**: Directly related to the **Config pattern** in application development, where settings are kept separate from code.

## 5. VALIDATION CRITERIA

- [ ] Script successfully runs without any `ModuleNotFoundError` for external packages.
- [ ] Output table clearly separates the VARIABLE and VALUE columns with a pipe `|` or similar delimiter.
- [ ] Variables longer than 80 characters (like long `PATH` strings) are elegantly truncated (e.g., appended with `...`) so the table does not break wrap on standard terminal sizes.
- [ ] The `PATH` variable is successfully identified and printed.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Sorting):** Sort the environment variables alphabetically by key before printing the table.
2. **Extension 2 (Dotenv Exporter):** Add a feature to write the filtered variables out to a new file named `.env.backup` in key=value format.
3. **Extension 3 (Reverse Verification):** Write a companion function that reads `.env.backup`, parses it back into a dictionary manually (handling empty lines and comments), and compares it against `os.environ` to detect if the system environment has changed.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Standard Python installation (no virtual environment required yet, though setting one up via `python -m venv .venv` is good practice).
- **Dependencies**: None. Only standard library `os` and `sys`.
