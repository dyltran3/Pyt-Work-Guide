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
        Initializes the assistant with a name, empty memory, and tool registry.
        """
        self.name = name
        self.memory = {}
        self.tools = {}

    def add_tool(self, name: str, func: callable):
        """
        Registers a tool function to be used by the agent.
        """
        self.tools[name] = func

    def remember(self, key: str, value: str):
        """
        Stores information in the local dictionary memory.
        """
        self.memory[key] = value
        print(f"[{self.name}] I've remembered that {key} is {value}.")

    def recall(self, key: str) -> str:
        """
        Retrieves information from memory.
        """
        return self.memory.get(key, f"I don't have any information about {key}.")

    def process_command(self, command: str) -> str:
        """
        Routes the command to either a tool or a memory recall.
        """
        cmd = command.lower()
        if "time" in cmd and "time" in self.tools:
            return f"The current time is {self.tools['time']()}"
        elif "calculate" in cmd and "calc" in self.tools:
            expr = cmd.split("calculate")[-1].strip()
            return f"The result of {expr} is {self.tools['calc'](expr)}"
        elif "recall" in cmd or "what is" in cmd:
            key = cmd.split()[-1]
            return self.recall(key)
        return "I'm not sure how to handle that command yet."

if __name__ == "__main__":
    def get_time():
        from datetime import datetime
        return datetime.now().strftime("%H:%M")

    def calculate(expression: str):
        try:
            return str(eval(expression, {"__builtins__": None}, {}))
        except:
            return "Error: calculation failed"

    agent = PersonalAssistantAgent("Jarvis")
    agent.add_tool("time", get_time)
    agent.add_tool("calc", calculate)

    agent.remember("user_name", "TuanAnh")
    print(agent.recall("user_name"))
    print(f"Assistant: {agent.process_command('calculate 10 * 10')}")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:
Sử dụng `eval()` một cách an toàn bằng cách giới hạn `__builtins__` như trong ví dụ trên.

**HINT-3 (Near-solution)**:
Có thể mở rộng thêm tính năng `Persistent Memory` bằng cách lưu `self.memory` vào một file JSON khi agent tắt.

**HINT-3 (Near-solution)**:

```python
        def start_cli(self):
        print(f"[{self.name}] Assistant is online.")
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ['exit', 'quit']:
                    print(f"[{self.name}] Goodbye!")
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
