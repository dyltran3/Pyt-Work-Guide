# Exercise Test-02: Property-Based Testing (Hypothesis)

## 1. EXERCISE BRIEF

**Context**: Unit Test truyền thống thường chỉ cover các "Happy Path" hoặc một vài Edge case do con người nghĩ ra. Property-based Testing tự động sinh ra hàng nghìn bộ data để tìm điểm gãy của logic.
**Task**: Sử dụng thư viện `Hypothesis` để viết test cho hàm `process_list(items, limit)`. Hàm này phải filter các số lớn hơn limit, sort chúng, và trả về list.
**Constraints**: Phải tìm ra bug tiềm ẩn khi items chứa NaN, Infinity, hoặc list cực lớn (Memory Exhaustion).

## 2. STARTER CODE

```python
from hypothesis import given, strategies as st

def process_list(items: list[float], limit: float) -> list[float]:
    """
    Business Logic: 
    1. Filter items <= limit.
    2. Sort ascending.
    3. Return result.
    """
    # Truncated logic - Student must implement and fix bugs found by Hypothesis
    filtered = [x for x in items if x <= limit]
    filtered.sort()
    return filtered

# --- TESTS ---

@given(st.lists(st.floats()), st.floats())
def test_process_list_properties(items, limit):
    result = process_list(items, limit)
    
    # Property 1: All items in result must be <= limit
    assert all(x <= limit for x in result)
    
    # Property 2: Result must be sorted
    assert result == sorted(result)
    
    # Property 3: Result length <= input length
    assert len(result) <= len(items)
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Chuẩn bị tâm lý: Hypothesis sẽ tìm ra những giá trị mà bạn không bao giờ ngờ tới (như `float('nan')`).

**HINT-2 (The Trap)**:
`x <= limit` sẽ trả về `False` nếu `x` là `NaN`. Điều này có đúng yêu cầu nghiệp vụ không? Ngoài ra, `sort()` xử lý `NaN` như thế nào?

## 4. REAL-WORLD CONNECTIONS
- **Libraries**: Hypothesis (Python), QuickCheck (Haskell), jqwik (Java).
- **Use cases**: Kiểm thử parser, financial calculations, complex state machines.

## 5. VALIDATION CRITERIA
- [ ] Test suite chạy và tìm ra ít nhất 1 failing case với `NaN` hoặc `Inf`.
- [ ] Code được fix để handle các giá trị đặc biệt này một cách nhất quán.

## 6. SETUP REQUIREMENTS
- **Dependencies**: `pip install hypothesis`
