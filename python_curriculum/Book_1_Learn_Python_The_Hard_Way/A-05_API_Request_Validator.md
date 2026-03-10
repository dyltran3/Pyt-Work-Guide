# Exercise A-05: API Request Validator

## 1. EXERCISE BRIEF

**Context**: Tại các hệ thống Gateway, mọi payload nhận từ người dùng đều là 'untrusted'. Việc validate cấu trúc JSON payload sâu trước khi cho đi tiếp là bước cực kỳ trọng yếu chống lại Injection & crash hệ thống.
**Task**: Viết một bộ Decorator/Hàm kiểm duyệt JSON payload dựa trên một schema tuỳ chỉnh do bạn thiết kế. Cần báo đúng đường dẫn key bị thiếu hoặc sai type (vd: 'user.address.street must be string').
**Constraints**: Không sử dụng `pydantic` hay `jsonschema`. Cần bắt recursive depth validation để quét payload lồng nhau đa tầng.
## 2. STARTER CODE

```python
def validate_payload(payload: dict, schema: dict) -> list[str]:
    """
    TODO: Validate payload against the schema.
    Rules:
    1. If a key is in the schema but missing in the payload, add exception string.
    2. If a key is present but wrong type, add exception string.
    3. If an integer is present, and min/max are defined in schema, enforce bounds.
    4. Any extranous keys in the payload NOT in the schema should ideally be ignored (or optionally yield a warning).
    Return a list of error explanation strings. Return an empty list if valid.
    """
    errors = []

    # Write your looping validation logic here

    return errors

if __name__ == "__main__":
    user_schema = {
        'username': {'type': str, 'required': True},
        'age': {'type': int, 'required': True, 'min': 0, 'max': 150},
        'email_opt_in': {'type': bool, 'required': False}
    }

    good_payload = {'username': 'johndoe', 'age': 30}
    bad_payload = {'username': 123, 'age': 200, 'extra_key': 'exploiting_database'}

    assert len(validate_payload(good_payload, user_schema)) == 0

    bad_errors = validate_payload(bad_payload, user_schema)
    print(bad_errors)
    # Expected errors:
    # "username must be of type <class 'str'>"
    # "age value 200 exceeds maximum of 150"
    assert len(bad_errors) == 2
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
You need to loop through the `schema.items()` because the schema defines what is expected. For each field, first check `if field in payload`. If it isn't, and `'required': True` is in the schema rules, add an error to your list.

**HINT-2 (Partial)**:
For type checking, you can use Python's built-in `type(value)`.

```python
expected_type = rules['type']
actual_value = payload[field]
if type(actual_value) != expected_type:
    errors.append(f"Field '{field}' expected {expected_type}, got {type(actual_value)}")
```

**HINT-3 (Near-solution)**:
For range bounds, check if the expected type was an integer first, then look up the limits.

```python
# Assuming actual_value is validated as an int
if 'min' in rules and actual_value < rules['min']:
    errors.append(f"Value too low")
if 'max' in rules and actual_value > rules['max']:
    errors.append(f"Value too high")
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `Pydantic`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Detects missing `required` keys completely safely, without throwing `KeyError`.
- [ ] Confirms the payload type matches exactly what the schema asks for.
- [ ] Handles correctly validating `min` and `max` limitations.
- [ ] Gathers **all** errors in a list. If a bad payload has 3 wrong fields, the returned error list must have 3 items. It does not stop on the first error.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (String Length Boundaries):** Add support to the engine to respect `min_length` and `max_length` rules in the schema specifically for `type: str`.
2. **Extension 2 (List Validation):** Add functionality to support `type: list`, but specifically, ensure the engine can enforce that all items _inside_ the array match a specified internal subtype (e.g., array of integers only).
3. **Extension 3 (Nested Object Validation):** Expand your schema processor to support recursive looping. If a user has a key `address`, the `type` for address can be `dict`, and it should have a nested `properties` key that recursively passes that sub-dictionary back through the `validate_payload` mechanism.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
