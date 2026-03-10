# Exercise Agent-01: Tool-Use Foundation

## 1. EXERCISE BRIEF

**Context**: Nền tảng của LLM Agent (Trí tuệ nhân tạo Tự Trị) là kỹ năng Mapping Hàm (Function Calling). Trình giả lập Tool-Use là linh hồn của hệ thống tự ra quyết định.
**Task**: Triển khai Simple Core Agent: Tạo JSON Tool Schema Decorator. Nhận Input Model, Parser JSON call mapping trả về kết quả local functions Execution an toàn.
**Constraints**: Cơ chế bảo mật sandbox error handling, Mock JSON prompt output LLm function calls không break Core App nếu params LLM trả bị thiếu.
## 2. STARTER CODE

```python
import json
import requests

class SimpleAgentCore:
    def __init__(self, api_key: str):
        """
        TODO: [... logic ...] 
        """
        self.api_key = api_key
        self.tools = []

    def register_tool(self, name: str, description: str, parameters: dict, func: callable):
        """
        TODO: [... logic ...] 
        """
        pass

    def call_llm(self, prompt: str) -> dict:
        """
        TODO: [... logic ...] 
        (Mock this [... logic ...] )
        """
        pass

    def execute_tool(self, tool_name: str, arguments: dict):
        """
        TODO: [... logic ...] 
        """
        pass

# --- MOCK TOOLS [... logic ...] ---
def get_weather(location: str) -> str:
    return f"The [... logic ...] {location} [... logic ...] "

def calculate_sum(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    agent = SimpleAgentCore(api_key="mock_key")

    agent.register_tool(
        name="get_weather",
        description="Get [... logic ...] ",
        parameters={"type": "object", "properties": {"location": {"type": "string"}}, "required": ["location"]},
        func=get_weather
    )

    agent.register_tool(
        name="calculate_sum",
        description="Add [... logic ...] ",
        parameters={"type": "object", "properties": {"a": {"type": "integer"}, "b": {"type": "integer"}}, "required": ["a", "b"]},
        func=calculate_sum
    )

    # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        tool_calls = [
        {"name": "get_weather", "arguments": {"location": "Hanoi"}},
        {"name": "calculate_sum", "arguments": {"a": 5, "b": 7}}
    ]

    for call in tool_calls:
        print(f"Executing [... logic ...] {call['name']}...")
        result = agent.execute_tool(call["name"], call["arguments"])
        print(f"Result [... logic ...] : {result}")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:

```python
    def register_tool(self, name: str, description: str, parameters: dict, func: callable):
        self.tools.append({
            "type": "function",
            "function": {
                "name": name,
                "description": description,
                "parameters": parameters
            },
            "callable": func
        })
```

**HINT-3 (Near-solution)**:

```python
    def execute_tool(self, tool_name: str, arguments: dict):
        tool = next((t for t in self.tools if t["function"]["name"] == tool_name), None)
        if not tool:
            return f"Error: [... logic ...] {tool_name} [... logic ...] "

        try:
            # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        result = tool["callable"](**arguments)
            return str(result)
        except Exception as e:
            return f"Error [... logic ...] {e}"
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `LangChain`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Mã nguồn chạy thành công không báo lỗi, đạt hiệu năng tiêu chuẩn và cover được các test cases ẩn.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
