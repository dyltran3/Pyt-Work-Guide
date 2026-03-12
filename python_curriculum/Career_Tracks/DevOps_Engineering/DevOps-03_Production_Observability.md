# Exercise DevOps-03: Production Observability (Logging, Metrics, Tracing)

## 1. EXERCISE BRIEF

**Context**: Khi app chạy ở quy mô lớn, việc "biết app đang làm gì" (Observability) quan trọng hơn việc app chạy đúng. Truy vết lỗi (Tracing) và đo lường (Metrics) giúp chúng ta pro-active thay vì re-active.
**Task**: Thiết lập hệ thống observability cơ bản cho một ứng dụng Python:
1. **Logging**: Sử dụng `logging` với Structured JSON format.
2. **Metrics**: Sử dụng `prometheus_client` để track request count và latency.
3. **Tracing**: Giả lập `OpenTelemetry` span để trace một luồng xử lý phức tạp.

## 2. STARTER CODE

```python
import logging
import json
import time
from prometheus_client import start_http_server, Counter, Summary

# 1. Structured Logging
class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "level": record.levelname,
            "message": record.msg,
            "timestamp": self.formatTime(record),
            "service": "order-service"
        }
        return json.dumps(log_entry)

# 2. Metrics Definition
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint'])
REQUEST_LATENCY = Summary('http_request_duration_seconds', 'Latency in seconds')

@REQUEST_LATENCY.time()
def process_request(method, endpoint):
    REQUEST_COUNT.labels(method=method, endpoint=endpoint).inc()
    time.sleep(0.1) # Simulate work
    # 3. Tracing Insight: Simulate a span
    print(f"[Trace] Starting span for {endpoint}...")
    # ... logic ...
    print(f"[Trace] Ending span.")

if __name__ == "__main__":
    # Start Prometheus metrics server
    start_http_server(8000)
    
    # Setup Logger
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setFormatter(JSONFormatter())
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    while True:
        logger.info("Processing custom request queue")
        process_request("GET", "/api/data")
        time.sleep(1)
```

## 3. PROGRESSIVE HINTS

**HINT-1 (JSON Logs)**:
Tại sao lại dùng JSON thay vì Plane Text? (Hint: Để các tool lọc log như ELK, Datadog có thể parse dễ dàng).

**HINT-2 (Counters vs Gauges)**:
Dùng `Counter` cho những thứ chỉ tăng (requests, errors). Dùng `Gauge` cho những thứ tăng/giảm (CPU usage, Memory).

## 4. REAL-WORLD CONNECTIONS
- **Tools**: ELK Stack (Logging), Prometheus/Grafana (Metrics), Jaeger/Zipkin (Tracing).
- **Standards**: OpenTelemetry (OTel).

## 5. VALIDATION CRITERIA
- [ ] Log xuất ra chuẩn JSON với đầy đủ metadata.
- [ ] Truy cập `localhost:8000` thấy các metric `http_requests_total` tăng dần.
- [ ] Giải thích được sự khác biệt giữa Monitoring (biết app chết) và Observability (biết TẠI SAO app chết).

## 6. SETUP REQUIREMENTS
- **Dependencies**: `pip install prometheus_client`
