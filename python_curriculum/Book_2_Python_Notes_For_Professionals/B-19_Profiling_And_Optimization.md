# Exercise B-19: Profiling & Optimization

## 1. EXERCISE BRIEF

**Context**: Software chuyên nghiệp luôn cần tracking Benchmark hiệu suất Memory và Time thay vì profiling thủ công để tránh rò rỉ RAM.
**Task**: Viết Decorators Profiling đa dụng để phân tích Cực Trị CPU time, Bộ nhớ tổng hao hụt, gọi tự động package `cProfile` và xuất báo cáo text.
**Constraints**: Đóng gói kết quả log ra Standard error hoặc file. Không dùng Framework profiling cấp thứ ba.
## 2. STARTER CODE

```python
import time
import random
import cProfile
import pstats
import io

# --- POORLY OPTIMIZED CODE ---
def find_primes(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            primes.append(num)
    return primes

def calculate_stats(data):
    results = []
    for item in data:
        # Simulate an expensive lookup [... logic ...] 
        time.sleep(0.0001)
        if item > 5000:
            results.append(item * 2)
    return sum(results)

def main_unoptimized():
    data = [random.randint(1, 10000) for _ in range(10_000)]
    primes = find_primes(5000)
    stats = calculate_stats(data)
    return len(primes), stats

# --- END POORLY OPTIMIZED CODE ---

def profile(func):
    """
    TODO: [... logic ...] 
    """
    pass

@profile
def main_optimized():
    """
    TODO: [... logic ...] 
    """
    pass

if __name__ == "__main__":
    print("Running Unoptimized [... logic ...] ")
    start = time.time()
    main_unoptimized()
    print(f"Unoptimized took: {time.time() - start:.2f}s")

    print("\nRunning Optimized [... logic ...] ")
    main_optimized()
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:

```python
def profile(func):
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()

        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
        ps.print_stats(10)
        print(s.getvalue())
        return result
    return wrapper
```

**HINT-3 (Near-solution)**:

```python
@profile
def main_optimized():
    data = [random.randint(1, 10000) for _ in range(10_000)]

    # Optimizer 1: [... logic ...] 
    def find_primes_opt(n):
        sieve = [True] * (n + 1)
        for p in range(2, int(n**0.5) + 1):
            if sieve[p]:
                for i in range(p * p, n + 1, p):
                    sieve[i] = False
        return [p for p in range(2, n + 1) if sieve[p]]

    primes = find_primes_opt(5000)

    # Optimizer 2: [... logic ...] 
    stats = sum(item * 2 [...] > 5000) # Removed time.sleep [... logic ...] 

    return len(primes), stats
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `cProfile`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] [... logic ...] 

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
