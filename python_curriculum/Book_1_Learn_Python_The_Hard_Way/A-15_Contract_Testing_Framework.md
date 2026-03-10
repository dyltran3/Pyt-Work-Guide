# Exercise A-15: Contract Testing Framework

## 1. EXERCISE BRIEF

**Context**: Trong kiến trúc multi-service (Microservices), Front-End hoặc Service A phải đảm bảo Service B không phá vỡ Payload mong muốn. Contract Testing đảm bảo giao thức đó vững chắc.
**Task**: Xây dựng micro-framework phân tích và so sánh API payload hiện tại với Contract Schema (cấu trúc cam kết), báo cáo fail (diff) chính xác những Key/Type bị vi phạm.
**Constraints**: Phần report diff phải hiển thị dưới dạng đường dẫn Key tường minh thay vì chỉ báo lỗi Fail chung chung.
## 2. STARTER CODE

```python
import inspect
import traceback

class TestCase:
    def assert_equals(self, expected, actual):
        if expected != actual:
            raise AssertionError(f"Expected {expected}, but got {actual}")

    def assert_raises(self, exception_type, func, *args, **kwargs):
        """
        TODO: Call the function. If it raises `exception_type`, pass.
        If it does not raise anything, or raises the wrong type, raise an AssertionError.
        """
        pass

class TestRunner:
    @staticmethod
    def run(test_class):
        instance = test_class()

        # 1. Discover all method names on `instance` starting with "test_"
        # 2. Loop through them and execute them
        # 3. Catch AssertionError for failures, Exception for crashes
        # 4. Print results

        passed = 0
        failed = 0

        # Write discovery and execution loop here

        print(f"\nResults: {passed} passed, {failed} failed")

# User writes code like this:
class MathTests(TestCase):
    def test_addition(self):
        self.assert_equals(4, 2 + 2)

    def test_broken_subtraction(self):
        # This will fail
        self.assert_equals(0, 5 - 2)

    def test_divide_zero(self):
        self.assert_raises(ZeroDivisionError, lambda: 1 / 0)

if __name__ == "__main__":
    TestRunner.run(MathTests)
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
To find methods dynamically, use `inspect.getmembers(instance, predicate=inspect.ismethod)`. This returns a list of tuples `(method_name, method_reference)`. Filter this list down where the name `.startswith("test_")`.

**HINT-2 (Partial)**:
For `assert_raises`:

```python
def assert_raises(self, exception_type, callable_func, *args, **kwargs):
    try:
        callable_func(*args, **kwargs)
    except exception_type:
        return # Success, it threw exactly what we wanted
    except Exception as e:
        raise AssertionError(f"Expected {exception_type.__name__}, got {type(e).__name__}")

    raise AssertionError(f"Expected {exception_type.__name__} but no exception was raised at all.")
```

**HINT-3 (Near-solution)**:

```python
class TestRunner:
    @staticmethod
    def run(test_class):
        instance = test_class()
        methods = inspect.getmembers(instance, predicate=inspect.ismethod)

        passed, failed = 0, 0

        for name, method in methods:
            if not name.startswith("test_"):
                continue

            try:
                method()
                print(f"PASSED: {name}")
                passed += 1
            except AssertionError as e:
                print(f"FAILED: {name} -> {e}")
                failed += 1
            except Exception as e:
                print(f"CRASHED: {name} -> Unknown error: {e}")
                traceback.print_exc()
                failed += 1
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `pytest`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Successfully identifies tests [... logic ...] -coding `.add_test()` lines.
- [ ] Exception failures do not crash the `TestRunner` itself; they are isolated per-test.
- [ ] Correctly asserts exceptions being thrown.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Setup and Teardown):** Modify the `TestRunner` to look for a `setUp()` and a `tearDown()` method on the instance. If they exist, guarantee they are executed _before_ and _after_ each individual `test_` method respectfully.
2. **Extension 2 (Auto-discovery Recursion):** Instead of passing `MathTests` directly into `TestRunner.run(MathTests)`, write a script `pytest_clone.py` that imports a python file by its string path name, extracts all classes inheriting from `TestCase`, and runs tests across the entire file organically.
3. **Extension 3 (ANSI Color Formatting):** Include terminal colors natively (using ASCI scape sequences `\033[92m` for green, `\033[91m` for red) to visually distinct outputs based on successful states without printing long verbose blobs.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`inspect`, `traceback`).
