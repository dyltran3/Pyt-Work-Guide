# Exercise A-06: HTTP Status Code Decision Tree

## 1. EXERCISE BRIEF

**Context**: HTTP client thường phức tạp vì các rẽ nhánh logic phức tạp (200 OK, 301 Redirect, 403 Auth, 50x Server Error). Xử lý State Machine là mô hình tối ưu nhất cho bài toán này.
**Task**: Thiết kế một Decision Tree siêu nhỏ dạng OOP. Khi nhận được một HTTP Status Code và Metadata của Response, hệ thống sẽ đi theo luồng logic đã định để trả về kết luận: 'Retry', 'Abort', 'Refresh Token' hay 'Success'.
**Constraints**: Không dùng `if/elif` lồng nhau quá 3 tầng. Bắt buộc dùng Pattern Matching, Dictionary Dispatch, hoặc Chain of Responsibility.
## 2. STARTER CODE

```python
def determine_status_code(
    authenticated: bool,
    authorized: bool,
    resource_exists: bool,
    rate_limited: bool,
    server_ok: bool
) -> int:
    """
    TODO: Return corresponding HTTP Status Integer.
    Rules Priority (Highest to Lowest):
    1. If the server is NOT ok, it's a 500 (Internal Server Error) regardless of user.
    2. If the user is rate limited, it's a 429 (Too Many Requests).
    3. If the user is NOT authenticated, it's 401 (Unauthorized - usually meaning Unauthenticated).
    4. If the user IS authenticated but NOT authorized for the resource, it's 403 (Forbidden).
    5. If the user checks out, but the resource DOES NOT exist, it's 404 (Not Found).
    6. If all checks pass cleanly, it's 200 (OK).
    """
    pass

if __name__ == "__main__":
    # Test cases

    # Perfect success
    assert determine_status_code(True, True, True, False, True) == 200

    # Server broken takes priority over everything
    assert determine_status_code(False, False, False, True, False) == 500

    # Rate limit takes priority over unauthenticated
    assert determine_status_code(False, True, True, True, True) == 429

    # Unauthorized vs Unauthenticated
    assert determine_status_code(False, False, True, False, True) == 401
    assert determine_status_code(True, False, True, False, True) == 403

    print("All status assertions passed!")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
The "Rules Priority" in the Brief essentially dictates the order your `if` conditions should flow. By [...] `return` statements, you can completely avoid `elif` and `else` nesting.

**HINT-2 (Partial)**:
Instead of:

```python
if server_ok:
    if not rate_limited:
         # ... nested nightmare
else:
    return 500
```

Use the Guard Clause pattern:

```python
if not server_ok:
    return 500
if rate_limited:
    # ...
```

**HINT-3 (Near-solution)**:

```python
def determine_status_code(authenticated, authorized, resource_exists, rate_limited, server_ok) -> int:
    if not server_ok:
        return 500
    if rate_limited:
        return 429

    # Check Auth next...
    if not authenticated:
        return 401
    # Check permissions...
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: Django Middleware, Express/FastAPI Router logic.
- **Why do it manually**: Understanding how HTTP specifications expect endpoints to resolve failures avoids sending 500s when a user just typo'd a URL (404), or leaking whether a secure file exists to an unauthenticated hacker (by returning a 404 before you check a 401).

## 5. VALIDATION CRITERIA

- [ ] Code avoids nesting deeper than the outer functional block constraint. Use Guard Clauses.
- [ ] Returns the raw integers strictly (200, 401, 403, 404, 429, 500).
- [ ] Passes all test assertions representing edge-case combinations.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Security Masking):** In highly secure environments, you might not want to tell an unauthorized user whether a file even exists. Modify the rules so that if the user is `authenticated == True` but `authorized == False`, and the resource is secret, it masks the true `403` status by returning a `404` to feign ignorance. Update the function signature or logic to accommodate.
2. **Extension 2 (List-Based Checks):** Instead of boolean flags, assume you have a list of validator functions (e.g. `[check_server, check_rate, check_auth]`). Rewrite the decision engine to loop through the validators and break at the first failed assertion, yielding the code.
3. **Extension 3 (Truth Table Documentation):** Build a small script that automatically generates a Markdown truth truth for all $2^5 = 32$ possible permutations of your function to verify coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
