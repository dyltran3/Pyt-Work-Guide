# Exercise DevOps-01: Dockerized Microservices

## 1. EXERCISE BRIEF

**Context**: Software chỉ thành công khi triển khai (Deploy) chạy mượt trên mọi OS. Containerization cực tiểu hoá size Image, bảo chứng High Availability Web App.
**Task**: Xây Dockerfile Multi-stage build chia Layer tối ưu venv builder và Minimal Container thu nhỏ size base bằng Python-slim. Cấu hình Docker-compose.yml khởi tạo kèm Cache Redis Network internal.
**Constraints**: Không chứa hardcoded credentials trong Git. Giảm Base size Image sau khi đóng gói Build cuối cùng càng nhẹ càng tốt.
## 2. STARTER CODE

# Builder stage
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Final stage
FROM python:3.11-slim
WORKDIR /app
# Copy installed dependencies from builder
COPY --from=builder /root/.local /root/.local
COPY src/ .

ENV PATH=/root/.local/bin:$PATH
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

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
Modularize your Dockerfile into stages:

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

- **Libraries/Tools**: `Docker Desktop`, `Kubernetes`, `Podman`, `Terraform`.

## 5. VALIDATION CRITERIA

- [ ] Dockerfile uses multi-stage build to reduce image size.
- [ ] Image uses a non-root user or minimal base (slim/alpine).
- [ ] Docker-compose correctly links web service to redis.
- [ ] Application starts successfully within the container environment.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Docker
- **Dependencies**: None.
