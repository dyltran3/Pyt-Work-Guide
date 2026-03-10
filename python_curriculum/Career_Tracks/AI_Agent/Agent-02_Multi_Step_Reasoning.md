# Exercise Agent-02: Multi-Step Reasoning Agent

## 1. EXERCISE BRIEF

**Context**: Mô hình ReAct (Reasoning and Acting) Agent cho phép AI duy trì Thought Process logic qua nhiều Step, suy luận trước khi Search và ra lệnh. Là hạt nhân cốt lõi LangChain / AutoGPT.
**Task**: Sử dụng String Parser Loop Workflow điều hướng Agent (Thought - Action - Observation Loop). Duy trì Conversation History vòng lặp đệ quy tới khi LLM trả về Final Answer.
**Constraints**: Regex Parser format Action chính xác. Giới hạn Depth recursion (tối đa 5 lượt gọi) ngăn vòng lặp vĩnh viễn (Infinite loop).
## 2. STARTER CODE

```python
import json

class ReActAgent:
    def __init__(self):
        """
        TODO: [... logic ...] 
        """
        self.history = []

    def log_thought(self, thought: str):
        print(f"\n[THOUGHT] {thought}")
        self.history.append({"role": "assistant", "content": f"Thought: {thought}"})

    def log_action(self, action_name: str, action_input: str):
        print(f"[ACTION ] {action_name}({action_input})")
        self.history.append({"role": "assistant", "content": f"Action: {action_name}\nAction Input: {action_input}"})

    def log_observation(self, observation: str):
        print(f"[OBSERVE] {observation}")
        self.history.append({"role": "user", "content": f"Observation: {observation}"})

    def run_step(self, question: str):
        """
        TODO: [... logic ...] 
        Implement [... logic ...] 
        """
        pass

# --- MOCK TOOLS ---
def search_wiki(query: str) -> str:
    # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        data = {
        "Python": "Python [... logic ...] ",
        "Guido van Rossum": "Guido [... logic ...] "
    }
    return data.get(query, f"No [... logic ...] {query}")

if __name__ == "__main__":
    agent = ReActAgent()

    # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        agent.log_thought("I [... logic ...] ")
    agent.log_action("search", "Python")
    agent.log_observation(search_wiki("Python"))

    agent.log_thought("Python [... logic ...] ")
    agent.log_action("search", "Guido van Rossum")
    agent.log_observation(search_wiki("Guido van Rossum"))

    agent.log_thought("I [... logic ...] ")
    print("\n[ANSWER ] Guido [... logic ...] ")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Phân tích kỹ lưỡng các cấu trúc dữ liệu cần thiết (Dictionary, Queue, Set) trước khi bắt tay vào code. Chia nhỏ bài toán thành các hàm độc lập.

**HINT-2 (Partial)**:

```python
    def __init__(self):
        self.history = []
        self.tools = {"search": search_wiki}
        self.system_prompt = """
        You [... logic ...] 
        Action: <tool_name>
        Action Input: <input>
        """
```

**HINT-3 (Near-solution)**:

```python
    def parse_llm_response(self, response: str):
        # TODO: Thay thế bằng code xử lý logic thực tế tại đây.
        if "Action:" in response and "Action Input:" in response:
            lines = response.split('\n')
            action = [l for l in lines if l.startswith("Action:")][0].replace("Action:", "").strip()
            action_input = [l for l in lines if l.startswith("Action Input:")][0].replace("Action Input:", "").strip()
            return "action", action, action_input
        elif "Answer:" in response:
            answer = response.split("Answer:")[1].strip()
            return "answer", answer, None
        return "error", None, None
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `LangChain [... logic ...] `` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Mã nguồn chạy thành công không báo lỗi, đạt hiệu năng tiêu chuẩn và cover được các test cases ẩn.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Thiết kế kiến trúc để hỗ trợ xử lý đồng thời (concurrency/asyncio) nhằm tăng tốc độ xử lý lên gấp nhiều lần.
2. **Extension 2**: Đóng gói ứng dụng bằng Docker Compose, thiết lập self-healing và viết Unit Test đạt tối thiểu 90% coverage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
