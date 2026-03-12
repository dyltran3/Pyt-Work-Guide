# Exercise Backend-01: Production FastAPI Boilerplate

## 1. EXERCISE BRIEF

**Context**: Các Team Backend cần khung mẫu (Boilerplate) quy chuẩn hoá cho APIs: Cấu trúc Middleware, Router lỏng. Thói quen tạo source cấu trúc chuẩn giúp onboard members nhanh cực kỳ hiệu quả.
**Task**: Tạo FastAPI Production Ready Setup Template đầy đủ cơ cấu Exception handlers chuẩn Pydantic formating, Database DI session & CORS Policy chuẩn chỉnh.
**Constraints**: Áp dụng Layered Architecture chuẩn (Router - Services - Repositories).
## 2. STARTER CODE

```python
from fastapi import FastAPI, Depends, HTTPException, Request
from pydantic import BaseModel, BaseSettings
import logging
import time

class Settings(BaseSettings):
    app_name: str = "Production API"
    environment: str = "development"
    database_url: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"

settings = Settings()
app = FastAPI(title=settings.app_name)

# --- MIDDLEWARE ---
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """
    Middleware to measure and log request processing time.
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logging.info(f"Path: {request.url.path} | Method: {request.method} | Time: {process_time:.4f}s")
    return response

# --- DEPENDENCIES ---
async def get_db_session():
    """
    Dependency injection for database sessions.
    """
    db = "mock_db_connection"
    try:
        yield db
    finally:
        pass # Close the mock connection here

# --- ROUTES ---
class User(BaseModel):
    id: int
    name: str

@app.get("/health")
async def health_check():
    return {"status": "ok", "env": settings.environment}

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int, db = Depends(get_db_session)):
    """
    Endpoint to retrieve a user by ID.
    """
    mock_users = {1: {"id": 1, "name": "Alice"}}
    user = mock_users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:

```python
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)

    logging.info(f"{{'path': '{request.url.path}', 'method': '{request.method}', 'time': {process_time:.4f}}}")
    return response
```

**HINT-3 (Near-solution)**:

```python
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logging.error(f"Failed cleanly: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error. Please contact support."}
    )
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `FastAPI`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Correctly uses Middleware for cross-cutting concerns like logging.
- [ ] Implements Dependency Injection for database sessions.
- [ ] Provides standard error handling and response formatting.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: `fastapi`, `uvicorn`, `pydantic`, `pydantic-settings`.
