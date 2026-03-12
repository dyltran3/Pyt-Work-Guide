# Exercise B-20: Conda/venv Manager CLI

## 1. EXERCISE BRIEF

**Context**: Mở rộng và Quản lý Environment linh hoạt cho dự án Machine Learning yêu cầu tự động xử lý các dependencies phức tạp thay vì gõ lệnh bằng tay.
**Task**: Phần mềm CLI Manager đóng gói wrap các câu lệnh môi trường Venv hoặc conda, support create/freeze/audit version package trong 1 lệnh duy nhất.
**Constraints**: Dùng `subprocess` module. Bắt handle và format stdout trả về an toàn.
## 2. STARTER CODE

```python
import os
import subprocess
import sys
import argparse
from pathlib import Path

class EnvManager:
    def __init__(self):
        self.base_dir = Path.cwd() / "envs"
        self.base_dir.mkdir(exist_ok=True)

    def create_venv(self, env_name: str, python_version: str = None):
        """
        Creates a new virtual environment in the 'envs' directory.
        """
        env_path = self.base_dir / env_name
        if env_path.exists():
            print(f"Environment '{env_name}' already exists.")
            return
        print(f"Creating venv '{env_name}'...")
        subprocess.run([sys.executable, "-m", "venv", str(env_path)], check=True)
        print(f"Successfully created: {env_path}")

    def list_envs(self):
        """
        Lists all directories in the 'envs' folder.
        """
        envs = [d.name for d in self.base_dir.iterdir() if d.is_dir()]
        for e in envs:
            print(f"  - {e}")
        return envs

    def freeze_env(self, env_name: str):
        """
        Executes 'pip freeze' for a specific environment.
        """
        env_path = self.base_dir / env_name
        if not env_path.exists():
            print(f"Environment '{env_name}' not found.")
            return ""
        pip_path = env_path / ("Scripts/pip.exe" if os.name == 'nt' else "bin/pip")
        result = subprocess.run([str(pip_path), "freeze"], capture_output=True, text=True)
        print(result.stdout)
        return result.stdout

def main():
    parser = argparse.ArgumentParser(description="Python Environment Manager CLI")
    parser.add_argument("action", choices=["create", "list", "freeze"])
    parser.add_argument("name", nargs="?")
    args = parser.parse_args()
    
    mgr = EnvManager()
    if args.action == "create":
        mgr.create_venv(args.name)
    elif args.action == "list":
        mgr.list_envs()
    elif args.action == "freeze":
        mgr.freeze_env(args.name)

if __name__ == "__main__":
    main()
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:

```python
def create_venv(self, env_name: str, python_version: str = None):
    env_path = self.base_dir / env_name
    if env_path.exists():
        print(f"Environment {env_name} already exists, skipping...")
        return

    cmd = [sys.executable, "-m", "venv", str(env_path)]
    print(f"Creating virtual environment at {env_path}...")
    subprocess.run(cmd, check=True)
    print("Done! Environment ready.")
```

**HINT-3 (Near-solution)**:

```python
def freeze_env(self, env_name: str):
    env_path = self.base_dir / env_name
    if not env_path.exists():
        print("Not Found: Environment doesn't exist.")
        return

    if os.name == 'nt':
        pip_path = env_path / "Scripts" / "pip.exe"
    else:
        pip_path = env_path / "bin" / "pip"

    result = subprocess.run([str(pip_path), "freeze"], capture_output=True, text=True)
    print(result.stdout)
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `venv`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Correctly uses `subprocess` to call external commands.
- [ ] Handles cross-platform paths for `pip` correctly (Windows vs Unix).
- [ ] Provides a clean CLI interface for environment management.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
