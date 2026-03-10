# Exercise B-03: Scope Isolation Debugger

## 1. EXERCISE BRIEF

**Context**: Quản lý đóng gói (Encapsulation) và bảo vệ namespace trong runtime là kỹ thuật phòng vệ chính giúp các framework Python như Django cô lập scope chạy ứng dụng nội bộ.
**Task**: Khởi tạo môi trường ảo thu nhỏ (Isolated scope) trên runtime, sử dụng Scope Injection (hàm `exec` và global/local dictionaries lồng nhau) để chạy code an toàn.
**Constraints**: Kiểm soát context manager để đảm bảo các biến ở scope cha không bị block hoặc sửa đổi trái phép.
## 2. STARTER CODE

```python
import sys
import traceback
from functools import wraps

def debug_on_exception(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            """
            TODO:
            1. Grab the current traceback / exception info.
            2. Extract the locals() dictionary from the lowest failing frame.
            3. Print the function name, exception type, and a clean table of the
               local variables and their values before re-raising.
            """
            print(f"--- FATAL CRASH IN {func.__name__} ---")

            # Extract and print variables here

            raise
    return wrapper

@debug_on_exception
def process_user_data(user: dict, admin_mode: bool = False):
    # These variables are created inside the function scope
    processing_id = "PROC-9923"
    api_endpoint = "https://backend/api/v1/update"

    # Bug triggers here because 'age' isn't in the dict
    user_age = user['age']

    return True

if __name__ == "__main__":
    test_user = {"name": "Charlie", "email": "charlie@example.com"}

    try:
        process_user_data(test_user, admin_mode=True)
    except KeyError:
        print("Caught expected crash. Scroll up to verify the local variable dump.")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
When an exception occurs, you can fetch its traceback using `sys.exc_info()`. The third element of the tuple is the traceback object (`tb`).

**HINT-2 (Partial)**:
You can walk the traceback object down to the exact frame where the crash explicitly happened by iterating `while tb.tb_next: tb = tb.tb_next`. Once at the deepest frame layer, access its `.tb_frame.f_locals` dictionary attribute.

**HINT-3 (Near-solution)**:

```python
def wrapper(*args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(f"\n--- FATAL CRASH IN {func.__name__} ---")
        print(f"Error: {type(e).__name__}: {str(e)}")

        # Get traceback
        _, _, tb = sys.exc_info()

        # Drill down to the exact frame where the exception occurred
        while tb.tb_next:
            tb = tb.tb_next

        # Extract locals dictionary
        local_vars = tb.tb_frame.f_locals

        print("\n[Local Variables Dump]")
        for key, val in local_vars.items():
            print(f"{key:<15} = {repr(val)}")
        print("-" * 40 + "\n")

        raise
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `Sentry.io`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Automatically extracts natively born inside-context variables (like `processing_id`).
- [ ] Neatly [...].
- [ ] Safe execution does not leak or alter the original functionality of the wrapped routine. Wait cleanly to intercept failure blocks prior to bubbling.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (PII Masking):** Add [...]. If `key` deeply contains strings like `"password"`, `"token"`, or `"secret"`, redact the `repr(val)` printing to output `"[REDACTED]"` [...]-text systems.
2. **Extension 2 (Class-level Support):** Current configuration fails safely on `self` introspection? Modify the printer to identify if `key == 'self'`, and output a `[Class Instance]` string cleanly, rather than attempting to print the entire multi-GB nested memory object dump.
3. **Extension 3 (Depth Limitations):** If [...] (list of 1,000,000 dicts), `repr(val)` [...]. Apply safe length-[...] 200 characters visually.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`sys`, `traceback`, `functools`).
