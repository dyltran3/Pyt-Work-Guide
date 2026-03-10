# Exercise Test-01: Advanced Pytest & Mocks

## 1. EXERCISE BRIEF

**Context**: Dự án chuyên nghiệp không thể chạy thực tế Unit Test nếu gọi Real Database hay API thanh toán nạp tiền. Pytest Mocks & Patchings cô lập hoàn toàn môi trường an toàn cao độ.
**Task**: Viết Suite Test Mocks kiểm tra Service Thanh Toán (PaymentGateway) bắt Network Response `requests.post`. Test logic Thành công, Timeout Exception, và Invalid Params mà không văng request thật.
**Constraints**: Chặn tuyệt đối HTTP Outbound sử dụng `unittest.mock` (Mock object returned values / Side effects).
## 2. STARTER CODE

```python
import requests

class PaymentGateway:
    def __init__(self, api_key: str):
         self.api_key = api_key
         self.base_url = "https://mock-payment-api.com/v1"

    def charge(self, amount: float, source: str) -> dict:
         """
         TODO: [... logic ...] 
         """
         response = requests.post(
             f"{self.base_url}/charges",
             headers={"Authorization": f"Bearer {self.api_key}"},
             json={"amount": amount, "source": source}
         )
         response.raise_for_status()
         return response.json()

# --- TESTS (to [... logic ...] ) ---
import pytest
from unittest.mock import patch, Mock

def test_charge_success():
    """TODO: [... logic ...] """
    pass

def test_charge_network_error():
    """TODO: [... logic ...] """
    pass
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:

```python
@patch('requests.post')
def test_charge_success(mock_post):
    gateway = PaymentGateway("fake_key")
    mock_response = Mock()
    mock_response.json.return_value = {"id": "ch_123", "status": "succeeded"}
    mock_response.raise_for_status.return_value = None
    mock_post.return_value = mock_response

    result = gateway.charge(100.0, "tok_mastercard")
    assert result["status"] == "succeeded"
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `pytest`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Mã nguồn chạy thành công không báo lỗi, đạt hiệu năng tiêu chuẩn và cover được các test cases ẩn.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: `pytest`, `requests`.
