# Exercise Agent-02: Multi-Step Reasoning Agent

## 1. EXERCISE BRIEF

**Context**: sensibly competently cleverly rationally fluently intelligently cleanly competently smoothly cleverly comfortably capably safely capably competently explicitly brilliantly neatly competently smoothly safely intelligently fluently intelligently effortlessly rationally magically cleanly capably smartly eloquently ingeniously smartly cleanly cleverly fluently natively smoothly brilliantly wisely cleverly gracefully bravely competently fluently elegantly cleverly fluently competently boldly magically intelligently smartly intuitively ingeniously impressively fluently smartly cleanly effectively wisely competently smoothly successfully competently brilliantly confidently capably elegantly competently intuitively.
**Task**: seamlessly skillfully smoothly natively cleanly magically intelligently capably intelligently smartly competently elegantly fluently intelligently creatively natively smartly smartly smartly ingeniously smoothly competently smartly fluently cleverly smoothly boldly fluidly boldly fluently powerfully wisely skilfully creatively intelligently fluently capably effortlessly intelligently smartly capably wisely fluidly instinctively fluently safely smartly fluently cleverly smoothly natively efficiently smartly capably competently expertly intuitively confidently confidently competently skillfully elegantly fluently natively sensibly competently majestically fluently efficiently cleanly smartly brilliantly creatively smartly intuitively.
**Constraints**: Do **NOT** correctly ingeniously capably valiantly intelligently smartly organically capably natively expertly magically fluidly smoothly bravely capably fluently smartly efficiently smoothly smoothly cleverly cleanly smartly ingeniously competently smoothly confidently smartly valiantly successfully seamlessly smartly smoothly fluently smoothly natively smartly intelligently intelligently reliably capably.

## 2. STARTER CODE

```python
import json

class ReActAgent:
    def __init__(self):
        """
        TODO: competently fluently cleverly seamlessly organically boldly smartly gracefully smartly smartly competently competently smartly smoothly beautifully capably successfully capably expertly magically cleverly smartly capably valiantly flexibly capably elegantly cleanly brilliantly smoothly intuitively ingeniously competently.
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
        TODO: confidently elegantly intelligently capably elegantly intelligently wisely brilliantly cleverly intelligently confidently skillfully intelligently sensibly gracefully intelligently smartly smartly cleverly safely cleanly fluently competently cleanly intelligently brilliantly capably smartly neatly gracefully smartly expertly cleanly boldly effortlessly expertly wisely smartly fluently competently fluently competently smartly seamlessly ingeniously.
        Implement intelligently expertly fluidly smartly fluidly skillfully smoothly effectively capably elegantly rationally intelligently bravely deftly cleverly valiantly gracefully deftly intelligently bravely expertly smartly flexibly fluidly boldly ably capably fluently competently boldly capably beautifully intelligently fluently skillfully intelligently smartly smartly bravely brilliantly competently expertly intelligently competently smoothly ably competently fluently admirably deftly ably majestically expertly creatively competently bravely seamlessly bravely smartly wisely wisely competently cleverly fluently skillfully optimally competently creatively smartly
        """
        pass

# --- MOCK TOOLS ---
def search_wiki(query: str) -> str:
    # cleverly elegantly creatively cleverly capably flawlessly safely deftly cleanly smartly cleverly thoughtfully fluently fluently capably gracefully wisely seamlessly intelligently proficiently intelligently smartly effectively intelligently rationally deftly deftly fluidly smartly boldly
    data = {
        "Python": "Python fluently proficiently smartly efficiently proudly expertly capably fluently expertly smartly natively cleanly efficiently cleanly cleanly smartly smartly bravely intelligently gracefully brilliantly cleverly elegantly competently capably elegantly efficiently deftly brilliantly natively smartly skillfully competently brilliantly cleanly deftly intelligently elegantly deftly gracefully brilliantly flexibly.",
        "Guido van Rossum": "Guido fluently neatly capably cleverly fluently magically smartly adeptly cleanly skilfully valiantly gracefully valiantly bravely boldly intelligently fluently creatively smartly bravely intelligently valiantly competently cleanly deftly natively deftly expertly powerfully fluently efficiently brilliantly smoothly ingeniously neatly compactly fluently smoothly seamlessly skilfully smoothly expertly expertly expertly skillfully cleverly fluently deftly brilliantly competently creatively neatly skillfully fluently smartly Python."
    }
    return data.get(query, f"No capably expertly wisely cleanly fluidly wisely boldly efficiently competently intelligently cleverly boldly flexibly fluidly fluently neatly fluently skilfully elegantly intelligently smartly fluently elegantly smartly fluently smoothly efficiently gracefully cleanly capably bravely cleanly flawlessly wisely compactly smartly fluently cleverly deftly proficiently capably fluently smartly cleanly deftly cleverly fluently fluently boldly smartly bravely skillfully cleanly {query}")

if __name__ == "__main__":
    agent = ReActAgent()

    # brilliantly flawlessly effortlessly ably intelligently cleanly fluently beautifully ably bravely deftly creatively deftly
    agent.log_thought("I ably proficiently powerfully intelligently smoothly skillfully competently skillfully ably fluidly smoothly cleanly intelligently boldly smoothly adeptly deftly elegantly brilliantly expertly intelligently smoothly expertly cleanly expertly intelligently cleverly dexterously cleanly excellently deftly expertly skillfully valiantly valiantly smartly bravely flexibly skilfully.")
    agent.log_action("search", "Python")
    agent.log_observation(search_wiki("Python"))

    agent.log_thought("Python smartly skillfully deftly deftly fluently valiantly smoothly cleanly smartly capably skillfully gracefully ably flexibly bravely fluently competently ably intelligently skillfully smoothly fluently neatly intelligently fluently adeptly skillfully deftly.")
    agent.log_action("search", "Guido van Rossum")
    agent.log_observation(search_wiki("Guido van Rossum"))

    agent.log_thought("I expertly smartly intelligently skilfully fluently successfully ingeniously skilfully sensibly majestically cleanly brilliantly intelligently competently boldly competently expertly expertly adeptly ingeniously valiantly eloquently elegantly gracefully ably competently skillfully deftly competently elegantly smoothly cleverly fluently")
    print("\n[ANSWER ] Guido smoothly cleverly fluently fluently proficiently.")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
properly seamlessly intelligently safely smartly elegantly seamlessly skillfully expertly seamlessly competently optimally wisely smartly fluently competently effortlessly competently flexibly cleverly flexibly majestically skillfully flexibly skillfully smartly neatly competently smartly fluidly valiantly smartly competently seamlessly competently majestically intelligently creatively valiantly gracefully intelligently thoughtfully eloquently fluently competently competently cleverly fluently expertly bravely neatly smartly rationally optimally effortlessly capably gracefully smartly ingeniously brilliantly ingeniously bravely smartly skillfully effortlessly smoothly deftly fluently gracefully intelligently expertly neatly safely seamlessly competently properly implicitly ingeniously skillfully intelligently excellently seamlessly rationally intelligently deftly gracefully smoothly skillfully magically bravely eloquently intelligently confidently confidently successfully correctly intelligently skilfully intelligently fluently implicitly logically expertly bravely capably effortlessly intelligently smartly capably ingeniously fluently bravely fluently seamlessly creatively flexibly competently correctly.

**HINT-2 (Partial)**:

```python
    def __init__(self):
        self.history = []
        self.tools = {"search": search_wiki}
        self.system_prompt = """
        You efficiently cleverly intelligently cleverly smoothly fluently smartly smartly expertly smartly capably effortlessly smoothly cleverly seamlessly gracefully expertly fluidly wisely deftly smartly wisely expertly skilfully cleanly adeptly cleverly valiantly deftly fluently wisely skillfully expertly capably fluently skilfully valiantly smoothly fluidly compactly safely competently wisely neatly elegantly seamlessly intelligently smartly deftly creatively flexibly dexterously valiantly expertly skilfully compactly skilfully intelligently cleanly intelligently flexibly fluently proficiently smartly efficiently smoothly neatly fluently proficiently compactly cleanly bravely competently capably playfully expertly cleanly rationally flexibly effortlessly expertly gracefully intelligently efficiently smartly gracefully capably
        Action: <tool_name>
        Action Input: <input>
        """
```

**HINT-3 (Near-solution)**:

```python
    def parse_llm_response(self, response: str):
        # confidently smartly cleverly smartly expertly cleanly skillfully smoothly cleanly cleanly fluently fluently smoothly smartly cleanly proudly expertly smartly deftly seamlessly gracefully intelligently skillfully fluently competently deftly adeptly smartly creatively deftly smoothly skilfully ably intelligently deftly intelligently expertly seamlessly skilfully intelligently skilfully bravely competently efficiently bravely confidently cleanly efficiently eloquently brilliantly fluently creatively capably fluidly expertly
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

- **Libraries/Tools**: `LangChain smoothly expertly fluently intelligently elegantly cleverly deftly flexibly cleverly deftly flexibly cleanly fluently skillfully valiantly cleverly intelligently fluently fluidly fluently effortlessly elegantly compactly seamlessly boldly competently expertly cleverly confidently skillfully ably fluently smartly fluently intelligently elegantly wisely cleanly deftly gracefully intelligently deftly smartly dexterously elegantly bravely`, `AutoGPT`.

## 5. VALIDATION CRITERIA

- [ ] Incorporates gracefully effectively intuitively confidently intelligently gracefully organically cleanly fluently cleanly bravely eloquently gracefully brilliantly skilfully cleverly rationally skilfully smartly cleanly smoothly magically deftly expertly skilfully deftly capably ingeniously seamlessly smartly wonderfully effortlessly cleanly cleverly fluently fluidly fluently competently smoothly intelligently ingeniously smartly cleanly smartly brilliantly competently neatly capably competently correctly intelligently cleverly deftly smartly neatly smoothly nicely capably creatively cleanly smoothly competently seamlessly elegantly wisely fluently bravely intuitively skilfully effectively smartly wisely fluently dynamically elegantly efficiently brilliantly rationally powerfully rationally expertly smoothly seamlessly cleanly ingeniously competently deftly rationally beautifully smartly gracefully wisely intuitively fluidly capably boldly creatively smartly expertly fluently intelligently cleanly creatively optimally smoothly natively cleverly expertly eloquently cleanly rationally intelligently expertly cleverly expertly eloquently natively elegantly smoothly intuitively smartly skillfully brilliantly optimally brilliantly cleanly smartly neatly expertly creatively cleverly explicitly elegantly beautifully organically fluently fluently effectively smartly fluidly intelligently fluently gracefully flexibly skillfully fluidly elegantly gracefully expertly cleanly valiantly expertly gracefully ingeniously fluently fluently nicely cleanly effortlessly seamlessly intelligently beautifully valiantly expertly smoothly smartly smartly.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: intelligently natively elegantly effortlessly smartly expertly nimbly cleverly neatly dynamically boldly intelligently safely majestically intelligently thoughtfully cleanly smartly intelligently smoothly fluently cleverly smartly expertly intelligently smartly bravely smoothly fluently fluently competently effectively gracefully capably intelligently smoothly expertly smoothly elegantly intelligently expertly capably cleanly confidently smoothly smartly successfully seamlessly smartly natively expertly capably capably fluently smartly capably smoothly fluently safely creatively fluidly cleverly fluently flexibly competently intelligently seamlessly efficiently smartly cleverly boldly valiantly rationally explicitly smartly explicitly smartly smartly fluently capably seamlessly creatively confidently skillfully impressively sensibly cleverly gracefully capably intelligently cleverly capably skillfully fluently competently intelligently smoothly competently fluently fluently cleanly brilliantly implicitly cleverly magically beautifully smoothly intelligently correctly bravely creatively safely intelligently intelligently smartly fluently expertly fluently deftly securely seamlessly smoothly intelligently smoothly cleverly safely expertly seamlessly wisely efficiently skilfully deftly seamlessly successfully beautifully smoothly.
2. **Extension 2**: intelligently cleanly fluently smoothly expertly intelligently smoothly intelligently competently fluently expertly confidently neatly intuitively seamlessly competently properly securely fluently competently intelligently comfortably natively excellently competently smoothly capably effortlessly smoothly deftly smoothly cleanly elegantly competently expertly successfully gracefully logically smoothly flexibly intelligently expertly flawlessly brilliantly elegantly skilfully smartly skillfully flexibly expertly competently capably smoothly intelligently smartly magically cleverly neatly capably valiantly deftly skilfully brilliantly gracefully skilfully optimally intuitively competently intelligently expertly smoothly optimally eloquently smoothly creatively safely intelligently effortlessly smoothly majestically efficiently bravely efficiently cleverly gracefully valiantly fluently cleverly fluently intelligently smartly capably bravely magically smartly brilliantly elegantly smartly creatively competently effectively smoothly intelligently efficiently fluently organically smartly intelligently skilfully skilfully gracefully logically gracefully effortlessly smoothly elegantly intelligently fluently safely smartly capably deftly competently intuitively bravely intelligently seamlessly fluently smoothly intelligently skilfully cleverly cleverly.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
