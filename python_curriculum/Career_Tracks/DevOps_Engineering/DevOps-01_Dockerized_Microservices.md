# Exercise DevOps-01: Dockerized Microservices

## 1. EXERCISE BRIEF

**Context**: Software chỉ thành công khi triển khai (Deploy) chạy mượt trên mọi OS. Containerization cực tiểu hoá size Image, bảo chứng High Availability Web App.
**Task**: Xây Dockerfile Multi-stage build chia Layer tối ưu venv builder và Minimal Container thu nhỏ size base bằng Python-slim. Cấu hình Docker-compose.yml khởi tạo kèm Cache Redis Network internal.
**Constraints**: Không chứa hardcoded credentials trong Git. Giảm Base size Image sau khi đóng gói Build cuối cùng càng nhẹ càng tốt.
## 2. STARTER CODE

```dockerfile
# TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        FROM python:3.11-slim as base

WORKDIR /app
COPY requirements.txt .

# TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

# TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```yaml
# docker-compose.yml
version: "3.8"

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - redis

  redis:
    image: "redis:alpine"
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:
Modify [... logic ...] 

```dockerfile
FROM python:3.11-slim as builder
WORKDIR /app
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /app
COPY src/ .
CMD ["python", "main.py"]
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `Docker [... logic ...] `` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Mã nguồn chạy thành công không báo lỗi, đạt hiệu năng tiêu chuẩn và cover được các test cases ẩn.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Docker
- **Dependencies**: None.
