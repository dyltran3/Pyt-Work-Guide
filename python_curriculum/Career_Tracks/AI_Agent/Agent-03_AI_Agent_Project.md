# Exercise Agent-03: AI Agent Project

## 1. EXERCISE BRIEF

**Context**: Dự Án Tổng Hợp: Trợ lý cá nhân Autonomous. Khả năng ghi nhớ siêu việt và giải thuật thông qua Tools, phối hợp toàn bộ năng lực Back-end Agent.
**Task**: Build CLI Assistant App phối hợp: Lưu trữ RAG Memory Local ngắn hạn bằng Dictionary và kết nối Execution Engine (thời tiết, tìm kiếm, tính toán). CLI Prompt User Chat Interactive Loop.
**Constraints**: Quản lý Role-playing Prompt, Memory Context Window an toàn.
## 2. STARTER CODE

```python
import os
import json

class PersonalAssistantAgent:
    def __init__(self, name: str = "Alfred"):
        """
        TODO: [... logic ...] 
        """
        self.name = name
        self.memory = {}
        self.tools = {}

    def add_tool(self, name: str, func: callable):
        """
        TODO: [... logic ...] 
        """
        self.tools[name] = func

    def remember(self, key: str, value: str):
        """
        TODO: [... logic ...] 
        """
        self.memory[key] = value
        print(f"[{self.name}] [... logic ...] {key}.")

    def recall(self, key: str) -> str:
        return self.memory.get(key, f"I [... logic ...] {key}.")

    def process_command(self, command: str) -> str:
        """
        TODO: [... logic ...] 
        """
        pass

if __name__ == "__main__":
    def get_time():
        from datetime import datetime
        return datetime.now().strftime("%H:%M")

    def calculate(expression: str):
        try:
            # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        return str(eval(expression, {"__builtins__": None}, {}))
        except:
            return "Error [... logic ...] "

    agent = PersonalAssistantAgent("Jarvis")
    agent.add_tool("time", get_time)
    agent.add_tool("calc", calculate)

    # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        agent.remember("user_name", "TuanAnh")

    print(agent.recall("user_name"))
    print(f"Tool [... logic ...] : {agent.tools['calc']('5 * 8')}")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:

```python
    def process_command(self, command: str) -> str:
        cmd = command.lower()
        if "time" in cmd and "time" in self.tools:
            return f"The [... logic ...] : {self.tools['time']()}"
        elif "calculate" in cmd and "calc" in self.tools:
            # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        expr = cmd.split("calculate")[1].strip()
            return f"The [... logic ...] {expr} cleanly {self.tools['calc'](expr)}"
```

**HINT-3 (Near-solution)**:

```python
    # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        def start_cli(self):
        print(f"[{self.name}] [... logic ...] ")
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ['exit', 'quit']:
                    print(f"[{self.name}] [... logic ...] !")
                    break

                response = self.process_command(user_input)
                print(f"[{self.name}] {response}")
            except KeyboardInterrupt:
                break
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `LlamaIndex`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Mã nguồn chạy thành công không báo lỗi, đạt hiệu năng tiêu chuẩn và cover được các test cases ẩn.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
