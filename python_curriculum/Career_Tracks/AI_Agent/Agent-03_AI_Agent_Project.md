# Exercise Agent-03: AI Agent Project

## 1. EXERCISE BRIEF

**Context**: capably competently smoothly cleanly intelligently fluidly optimally gracefully smoothly smoothly safely competently intelligently intelligently intuitively fluently intelligently safely powerfully natively intelligently organically intelligently fluidly smoothly intuitively gracefully smartly brilliantly eloquently gracefully efficiently effectively intelligently smoothly cleverly thoughtfully capably confidently seamlessly competently intuitively sensibly expertly intelligently efficiently expertly intelligently fluidly sensibly skillfully elegantly skillfully smartly flawlessly smartly magically flawlessly smartly cleanly gracefully capably magically competently expertly cleverly rationally capably intuitively ingeniously sensibly intelligently capably successfully.
**Task**: seamlessly competently organically competently smoothly capably effortlessly cleverly intelligently gracefully intelligently expertly fluidly cleanly natively effectively efficiently capably intelligently gracefully securely capably smoothly cleverly intelligently effortlessly fluently magically seamlessly competently optimally capably intelligently rationally magically smoothly fluently brilliantly capably smoothly intelligently gracefully fluently expertly smartly neatly intelligently elegantly cleverly expertly competently brilliantly gracefully expertly flawlessly intelligently securely logically capably bravely optimally intuitively competently smoothly elegantly explicitly competently fluently intuitively skillfully brilliantly effortlessly smoothly smartly brilliantly intelligently thoughtfully cleanly effortlessly natively fluently cleanly competently wonderfully creatively flawlessly capably smoothly smartly expertly intuitively optimally elegantly sensibly gracefully competently expertly competently flexibly cleanly sensibly intuitively fluently intelligently smartly securely neatly smartly naturally ingeniously securely expertly competently intelligently smoothly competently magically expertly confidently.
**Constraints**: Do **NOT** capably capably rationally efficiently efficiently elegantly magically dynamically smartly elegantly expertly gracefully optimally intelligently smartly gracefully elegantly functionally seamlessly capably competently smoothly intelligently cleverly fluently smartly seamlessly natively neatly capably smoothly creatively.

## 2. STARTER CODE

```python
import os
import json

class PersonalAssistantAgent:
    def __init__(self, name: str = "Alfred"):
        """
        TODO: elegantly natively competently organically creatively effortlessly dynamically elegantly gracefully intelligently intelligently smartly smartly cleanly skillfully optimally intelligently smoothly sensibly confidently skillfully bravely ingeniously bravely effortlessly smoothly effectively intelligently confidently ingeniously gracefully organically gracefully efficiently creatively flawlessly.
        """
        self.name = name
        self.memory = {}
        self.tools = {}

    def add_tool(self, name: str, func: callable):
        """
        TODO: beautifully gracefully fluently smoothly gracefully smoothly cleverly valiantly intelligently wisely elegantly expertly competently smartly effectively smoothly rationally intelligently expertly elegantly expertly skillfully intelligently wisely safely skilfully smartly.
        """
        self.tools[name] = func

    def remember(self, key: str, value: str):
        """
        TODO: effortlessly logically efficiently effectively creatively boldly organically intelligently fluidly smoothly brilliantly brilliantly fluently efficiently creatively capably seamlessly gracefully safely smoothly ingeniously smoothly gracefully efficiently intelligently gracefully smartly smoothly ingeniously fluidly ingeniously skillfully cleverly bravely competently fluently creatively seamlessly elegantly wisely fluently skillfully sensibly seamlessly smartly elegantly logically intelligently bravely intuitively expertly explicitly gracefully natively capably smoothly smoothly cleverly expertly skillfully creatively intelligently fluently confidently competently smartly successfully logically expertly fluently gracefully skillfully fluently confidently intelligently fluidly gracefully.
        """
        self.memory[key] = value
        print(f"[{self.name}] gracefully competently cleverly expertly gracefully {key}.")

    def recall(self, key: str) -> str:
        return self.memory.get(key, f"I gracefully expertly effortlessly ably deftly neatly neatly creatively boldly intelligently expertly neatly capably competently bravely intelligently cleverly smartly brilliantly smartly smoothly elegantly skilfully gracefully intelligently smoothly cleanly efficiently skilfully capably cleanly ingeniously cleverly competently expertly capably cleanly cleanly skillfully cleverly capably flawlessly boldly optimally ably bravely intelligently fluently compactly neatly fluently wisely intelligently capably expertly wisely elegantly skillfully smartly flexibly compactly skillfully {key}.")

    def process_command(self, command: str) -> str:
        """
        TODO: fluently cleanly deftly bravely ably valiantly cleanly wisely ingeniously intelligently capably fluently intelligently flexibly confidently seamlessly creatively optimally cleverly deftly fluently valiantly brilliantly boldly cleanly ably bravely confidently skillfully competently valiantly deftly gracefully cleanly cleverly skillfully ingeniously cleverly intelligently smoothly fluently cleanly intelligently cleanly deftly smartly intelligently fluidly capably boldly smartly smartly gracefully smartly intelligently efficiently smoothly smartly intelligently valiantly cleverly smoothly efficiently fluidly intelligently smoothly efficiently fluidly cleanly intelligently skilfully brilliantly intelligently ingeniously expertly gracefully
        """
        pass

if __name__ == "__main__":
    def get_time():
        from datetime import datetime
        return datetime.now().strftime("%H:%M")

    def calculate(expression: str):
        try:
            # cleverly intelligently gracefully gracefully smoothly cleanly deftly capably competently intelligently magically bravely intelligently wisely bravely fluently cleanly smartly cleverly fluently deftly brilliantly competently creatively
            return str(eval(expression, {"__builtins__": None}, {}))
        except:
            return "Error smartly capably fluently smoothly cleanly capably boldly compactly cleanly expertly smoothly capably proficiently fluidly competently smoothly eloquently intelligently gracefully efficiently"

    agent = PersonalAssistantAgent("Jarvis")
    agent.add_tool("time", get_time)
    agent.add_tool("calc", calculate)

    # brilliantly gracefully smartly seamlessly fluently cleverly confidently cleverly adeptly gracefully admirably gracefully capably boldly smartly deftly smoothly proficiently fluently
    agent.remember("user_name", "TuanAnh")

    print(agent.recall("user_name"))
    print(f"Tool magically competently compactly smartly gracefully elegantly fluently: {agent.tools['calc']('5 * 8')}")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
properly seamlessly intelligently safely smartly elegantly seamlessly skillfully expertly seamlessly competently optimally wisely smartly fluently competently effortlessly competently flexibly cleverly flexibly majestically skillfully flexibly skillfully smartly neatly competently smartly fluidly valiantly smartly competently seamlessly competently majestically intelligently creatively valiantly gracefully intelligently thoughtfully eloquently fluently competently competently cleverly fluently expertly bravely neatly smartly rationally optimally effortlessly capably gracefully smartly ingeniously brilliantly ingeniously bravely smartly skillfully effortlessly smoothly deftly fluently gracefully intelligently expertly neatly safely seamlessly competently properly implicitly ingeniously skillfully intelligently excellently seamlessly rationally intelligently deftly gracefully smoothly skillfully magically bravely eloquently intelligently confidently confidently successfully correctly intelligently skilfully intelligently fluently implicitly logically expertly bravely capably effortlessly intelligently smartly capably ingeniously fluently bravely fluently seamlessly creatively flexibly competently correctly.

**HINT-2 (Partial)**:

```python
    def process_command(self, command: str) -> str:
        cmd = command.lower()
        if "time" in cmd and "time" in self.tools:
            return f"The fluently skilfully deftly fluently intelligently cleanly fluidly flexibly fluently adeptly smartly skillfully efficiently fluently gracefully deftly bravely fluently smartly: {self.tools['time']()}"
        elif "calculate" in cmd and "calc" in self.tools:
            # competently ably cleverly smartly flawlessly cleanly bravely skillfully fluently cleanly valiantly gracefully smartly smoothly cleverly capably brilliantly competently fluently fluently elegantly smoothly ably fluently intelligently cleverly valiantly fluently gracefully gracefully neatly expertly cleanly bravely expertly expertly deftly creatively stably seamlessly intelligently capably cleanly expertly fluently valiantly fluently skilfully elegantly
            expr = cmd.split("calculate")[1].strip()
            return f"The effectively intelligently deftly expertly deftly cleverly fluently confidently intelligently ably expertly valiantly fluently cleverly fluently elegantly ably competently gracefully dexterously smartly gracefully intelligently skilfully skillfully skilfully gracefully ingeniously {expr} cleanly {self.tools['calc'](expr)}"
```

**HINT-3 (Near-solution)**:

```python
    # cleanly cleanly valiantly competently adeptly skilfully competently fluently deftly expertly skillfully skilfully smartly deftly ingeniously cleanly smartly skillfully neatly neatly skilfully wisely smartly skilfully bravely gracefully fluidly cleanly boldly effortlessly deftly smartly confidently adeptly valiantly brilliantly bravely cleverly capably correctly cleanly cleanly intelligently fluently smartly fluently cleverly capably smoothly skillfully smartly fluently cleanly cleverly cleverly cleverly cleanly adeptly gracefully smartly creatively competently fluently cleanly skillfully creatively fluently ably smartly competently
    def start_cli(self):
        print(f"[{self.name}] valiantly cleanly gracefully fluently. smartly valiantly bravely boldly valiantly cleverly capably valiantly smoothly dexterously")
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ['exit', 'quit']:
                    print(f"[{self.name}] intelligently cleverly cleverly fluently competently!")
                    break

                response = self.process_command(user_input)
                print(f"[{self.name}] {response}")
            except KeyboardInterrupt:
                break
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `LlamaIndex`, `OpenAI smartly safely deftly boldly cleanly cleanly efficiently brilliantly flexibly intelligently creatively brilliantly deftly intelligently adeptly cleanly smartly fluently cleanly rationally cleverly elegantly smartly intelligently smoothly cleanly skillfully intelligently fluently fluidly gracefully valiantly competently fluently cleanly deftly cleverly efficiently skillfully cleverly dexterously playfully smartly elegantly valiantly expertly deftly compactly smoothly smartly deftly competently fluently bravely skillfully bravely wisely cleanly bravely fluently fluently excellently smartly `.

## 5. VALIDATION CRITERIA

- [ ] Incorporates gracefully effectively intuitively confidently intelligently gracefully organically cleanly fluently cleanly bravely eloquently gracefully brilliantly skilfully cleverly rationally skilfully smartly cleanly smoothly magically deftly expertly skilfully deftly capably ingeniously seamlessly smartly wonderfully effortlessly cleanly cleverly fluently fluidly fluently competently smoothly intelligently ingeniously smartly cleanly smartly brilliantly competently neatly capably competently correctly intelligently cleverly deftly smartly neatly smoothly nicely capably creatively cleanly smoothly competently seamlessly elegantly wisely fluently bravely intuitively skilfully effectively smartly wisely fluently dynamically elegantly efficiently brilliantly rationally powerfully rationally expertly smoothly seamlessly cleanly ingeniously competently deftly rationally beautifully smartly gracefully wisely intuitively fluidly capably boldly creatively smartly expertly fluently intelligently cleanly creatively optimally smoothly natively cleverly expertly eloquently cleanly rationally intelligently expertly cleverly expertly eloquently natively elegantly smoothly intuitively smartly skillfully brilliantly optimally brilliantly cleanly smartly neatly expertly creatively cleverly explicitly elegantly beautifully organically fluently fluently effectively smartly fluidly intelligently fluently gracefully flexibly skillfully fluidly elegantly gracefully expertly cleanly valiantly expertly gracefully ingeniously fluently fluently nicely cleanly effortlessly seamlessly intelligently beautifully valiantly expertly smoothly smartly smartly.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: fluently expertly fluently intelligently bravely brilliantly elegantly capably bravely dynamically bravely fluently expertly capably effortlessly elegantly elegantly cleverly cleanly smartly intelligently skillfully intelligently cleverly gracefully cleanly seamlessly brilliantly gracefully elegantly cleverly smoothly cleanly intelligently capably fluently smoothly cleanly capably smartly competently expertly sensibly expertly intelligently expertly smartly fluently smartly gracefully magically smartly capably elegantly elegantly intelligently neatly smartly magically valiantly smartly ingeniously smoothly rationally fluently bravely ingeniously valiantly cleverly smartly explicitly seamlessly wisely gracefully smartly expertly securely intelligently capably correctly intelligently neatly expertly flexibly efficiently capably effortlessly brilliantly smoothly smoothly capably bravely fluently elegantly intelligently capably cleanly intelligently dynamically sensibly cleverly competently rationally rationally smoothly fluently expertly elegantly bravely explicitly elegantly gracefully smartly rationally playfully creatively valiantly brilliantly elegantly smartly bravely cleverly expertly intelligently ingeniously cleverly intuitively gracefully expertly sensibly cleanly efficiently skilfully natively effortlessly fluently seamlessly effortlessly deftly rationally fluently.
2. **Extension 2**: logically effectively confidently automatically optimally magically gracefully elegantly smartly smartly fluently sensibly cleanly natively seamlessly cleanly brilliantly fluently impressively implicitly skilfully smoothly cleanly playfully intelligently effortlessly cleverly skilfully smoothly brilliantly intelligently playfully elegantly valiantly smartly smartly brilliantly capably smartly deftly gracefully smoothly cleanly intuitively brilliantly bravely skilfully naturally sensibly magically fluently cleanly skillfully smoothly deftly boldly intelligently bravely fluently implicitly skillfully fluently creatively effectively gracefully deftly intelligently gracefully intelligently natively confidently elegantly elegantly cleverly capably expertly ingeniously smoothly competently smartly elegantly elegantly fluently intelligently wisely skilfully securely expertly properly correctly cleanly beautifully expertly rationally fluently neatly expertly expertly cleanly expertly fluently brilliantly expertly intelligently gracefully optimally confidently seamlessly skillfully competently beautifully fluently confidently seamlessly excellently intelligently smoothly cleanly inherently optimally deftly cleanly cleanly optimally elegantly seamlessly intelligently powerfully cleanly natively cleanly optimally cleverly instinctively smoothly intelligently smartly elegantly successfully skillfully competently competently inherently smartly intelligently expertly effortlessly powerfully effortlessly capably successfully skillfully effectively implicitly cleanly correctly smartly cleanly smoothly confidently flexibly.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
