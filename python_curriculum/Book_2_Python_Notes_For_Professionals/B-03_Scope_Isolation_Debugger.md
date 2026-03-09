# Exercise B-03: Scope Isolation Debugger

## 1. EXERCISE BRIEF

**Context**: Replicating a bug in production is a nightmare if the logs only say `KeyError: 'user_id'`. A good crash tracker (like Sentry) doesn't just record the error name; it records the exact local variables present inside the function _at the moment of the crash_.
**Task**: Build an advanced Python decorator `@debug_on_exception`. If the wrapped function crashes, the decorator must intercept the exception, use Python's `inspect` or `traceback` library to dump all local variables (their names and stringified values) actively living in that function's scope, log them to the terminal clearly, and then re-raise the exception.
**Constraints**: Do **NOT** rely purely on passing `**kwargs`. The function may have local variables instantiated _during_ execution mid-way through. You must capture the function's internal state frame natively using introspection.

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

- **Libraries/Tools**: `Sentry.io`, `Rollbar`, `Loguru` exceptions, Werkzeug Flask Debugger interface.
- **Why do it manually**: Relying strictly on basic python `logging.error(e)` leaves enormous context holes. Automatically dumping the active frame object converts a generic `"Failed to process HTTP"` error into explicitly exposing `"Failed... because user_id=None and auth_token='expired'"`. Frame introspection is the black magic powering the entire observability industry.

## 5. VALIDATION CRITERIA

- [ ] Automatically extracts natively born inside-context variables (like `processing_id`).
- [ ] Neatly maps out parameter arguments dynamically alongside newly born variables.
- [ ] Safe execution does not leak or alter the original functionality of the wrapped routine. Wait cleanly to intercept failure blocks prior to bubbling.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (PII Masking):** Add logic that obfuscates potentially sensitive keys. If `key` deeply contains strings like `"password"`, `"token"`, or `"secret"`, redact the `repr(val)` printing to output `"[REDACTED]"` explicitly avoiding logging credentials to plain-text systems.
2. **Extension 2 (Class-level Support):** Current configuration fails safely on `self` introspection? Modify the printer to identify if `key == 'self'`, and output a `[Class Instance]` string cleanly, rather than attempting to print the entire multi-GB nested memory object dump.
3. **Extension 3 (Depth Limitations):** If a variable contains an absolutely gigantic database dump (list of 1,000,000 dicts), `repr(val)` will lock up the terminal attempting to render it. Apply safe length-bound string truncation so no individual variable trace consumes more than 200 characters visually.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`sys`, `traceback`, `functools`).
