# Exercise Test-04: Snapshot & Mutation Testing

## 1. EXERCISE BRIEF

**Context**: 
1. **Snapshot Testing**: Hữu ích khi response JSON hoặc HTML quá lớn để assert từng trường.
2. **Mutation Testing**: Kiểm tra chất lượng của chính bộ Test (Test the Tests). Nó tự động đổi code logic (e.g., `>` thành `>=`) để xem Test có fail không.

**Task**: 
- Sử dụng `syrupy` cho Snapshot Assert.
- Sử dụng `mutmut` để tính Mutation Score.

## 2. STARTER CODE

```python
# target_code.py
def calculate_discount(price, member=False):
    if price > 100:
        return price * 0.9 if member else price * 0.95
    return price

# test_snapshot.py
def test_complex_response(snapshot):
    response = {
        "status": "success",
        "data": {
            "id": 1,
            "items": [{"name": "A", "price": 10}, {"name": "B", "price": 20}],
            "total": 30
        }
    }
    # snapshot assert
    assert response == snapshot

# mutation_analysis instructions:
# Run: mutmut run
# Check results: mutmut show all
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Snapshot)**:
Khi data thay đổi cố ý (e.g., thêm field), hãy dùng `pytest --snapshot-update`.

**HINT-2 (Mutation)**:
Nếu code đổi từ `>` sang `>=` mà test vẫn Pass, nghĩa là bộ test của bạn đang bỏ lỡ "Boundary value analysis".

## 4. REAL-WORLD CONNECTIONS
- **Tools**: Jest (Javascript), Syrupy (Python), Mutmut (Python), Stryker (Javascript/C#).

## 5. VALIDATION CRITERIA
- [ ] Snapshot file được tạo tự động trong thư mục `__snapshots__`.
- [ ] Mutation score được cải thiện sau khi bổ sung Boundary tests.
