# Exercise B-11: REST API Wrapper Generator

## 1. EXERCISE BRIEF

**Context**: Các công ty SDK phân phối các wrapper giao tiếp API cho khách hàng nội bộ. Pattern phổ biến là Object Factory + Descriptor thay vì lặp code hardcoded.
**Task**: Phác hoạ một Meta-class tự động sinh các methods call API GET/POST tự dựa vào attribute parameters định nghĩa class trên class rỗng.
**Constraints**: Viết Descriptor tự động inject parameters, header cho API requests bằng các attribute khai báo trước (như Pydantic model).
## 2. STARTER CODE

```python
import functools

class MockRequestSession:
    """A fake networking layer returning mocked responses"""
    def request(self, method: str, url: str, **kwargs):
        return {"status": "success", "executed": f"{method} {url}", "args": kwargs}

class APIClient:
    def __init__(self, base_url: str, spec: dict):
        self.base_url = base_url
        self.session = MockRequestSession()
        self._build_dynamic_methods(spec)

    def _core_request(self, method: str, path: str, **kwargs):
        """Internal universal requesting endpoint"""
        return self.session.request(method, self.base_url + path, **kwargs)

    def _build_dynamic_methods(self, spec: dict):
        """
        TODO:
        Loop through the dictionary.
        For each 'endpoint_name', utilize `functools.partial` dynamically natively attaching
        a callable that binds the `self` context.
        """
        pass

if __name__ == "__main__":
    dummy_schema = {
        "get_users": {"method": "GET", "path": "/users"},
        "create_user": {"method": "POST", "path": "/users"},
        "delete_user": {"method": "DELETE", "path": "/users/1"}
    }

    # Notice we haven't written `def get_users()` anywhere.
    client = APIClient("https://api.example.com", dummy_schema)

    res1 = client.get_users(params={"limit": 10})
    res2 = client.create_user(json={"name": "Alice"})

    print(res1)
    print(res2)

    assert res1['executed'] == "GET https://api.example.com/users"
    assert res2['args']['json']['name'] == "Alice"
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:
Using partial to bind methods:

```python
# Inside _build_dynamic_methods:
for func_name, route_info in spec.items():
    method = route_info['method']
    path = route_info['path']
    # Bind _core_request to the new function name.
```

**HINT-3 (Near-solution)**:

```python
def _build_dynamic_methods(self, spec: dict):
    for func_name, route_info in spec.items():
        partial_func = functools.partial(self._core_request, method=route_info['method'], path=route_info['path'])
        # Bind it to the instance dynamically.
        setattr(self, func_name, partial_func)
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `requests-toolbelt`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Successfully binds dynamic methods.
- [ ] Passes kwargs to the session request.

## 6. EXTENSION CHALLENGES

1. **Extension 1:** Add response status code validation.
2. **Extension 2:** Implement a timeout default.
3. **Extension 3:** Support path parameters.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
