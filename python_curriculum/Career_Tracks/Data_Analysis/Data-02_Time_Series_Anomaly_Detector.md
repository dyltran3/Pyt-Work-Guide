# Exercise Data-02: Time Series Anomaly Detector

## 1. EXERCISE BRIEF

**Context**: Dòng Time-Series metrics server (RAM, CPU, Nhiệt độ) tăng trưởng liên miên. Việc scan tìm Peak (Outlier Anomalies) báo lỗi tức thì là bài toán cốt cán AI Observability.
**Task**: Triển khai Anomaly Detector theo thuật toán IQR (Interquartile Range) cơ bản, hoặc Moving Window Average xử lý dòng dữ liệu Time Series mượt chèn streaming logs metrics.
**Constraints**: Duyệt Stream qua Ring Buffer để bảo vệ RAM cực độ không crash do quá lớn.
## 2. STARTER CODE

```python
import pandas as pd
import numpy as np

class TimeSeriesAnomalyDetector:
    def __init__(self, window_size: int = 5, threshold: float = 2.0):
        """
        TODO: [... logic ...] 
        """
        self.window_size = window_size
        self.threshold = threshold

    def detect_zscore(self, series: pd.Series) -> pd.Series:
        """
        TODO: [... logic ...] 
        """
        pass

    def detect_rolling_mean(self, series: pd.Series) -> pd.Series:
        """
        TODO: [... logic ...] 
        """
        pass

if __name__ == "__main__":
    dates = pd.date_range("20230101", periods=100)
    data = np.random.normal(loc=100, scale=10, size=100)

    # Inject [... logic ...] 
    data[20] = 500
    data[75] = -200

    ts = pd.Series(data, index=dates)

    detector = TimeSeriesAnomalyDetector(window_size=10, threshold=3.0)

    anomalies_z = detector.detect_zscore(ts)
    anomalies_rolling = detector.detect_rolling_mean(ts)

    print("Z-Score [... logic ...] :")
    print(ts[anomalies_z])
    print("\nRolling [... logic ...] :")
    print(ts[anomalies_rolling])
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:

```python
    def detect_zscore(self, series: pd.Series) -> pd.Series:
        mean = series.mean()
        std = series.std()
        z_scores = np.abs((series - mean) / std)
        return z_scores > self.threshold
```

**HINT-3 (Near-solution)**:

```python
    def detect_rolling_mean(self, series: pd.Series) -> pd.Series:
        rolling_mean = series.rolling(window=self.window_size, min_periods=1).mean()
        rolling_std = series.rolling(window=self.window_size, min_periods=1).std()

        # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        rolling_std = rolling_std.fillna(method='bfill')

        z_scores = np.abs((series - rolling_mean) / rolling_std)
        return z_scores > self.threshold
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `sktime`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Mã nguồn chạy thành công không báo lỗi, đạt hiệu năng tiêu chuẩn và cover được các test cases ẩn.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: `pandas`, `numpy`.
