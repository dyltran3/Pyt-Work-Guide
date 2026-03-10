# Exercise A-11: Plugin Architecture

## 1. EXERCISE BRIEF

**Context**: Framework Python thường được thiết kế để dễ dàng mở rộng từ cộng đồng (qua các Addon, Plugin) mà không cần can thiệp source code trực tiếp.
**Task**: Xây dựng Plugin Manager nhỏ gọn, tự động quét thư mục `plugins/`, load động (dynamically load) tất cả các module có implement một abstract base class nhất định và lưu vào registry.
**Constraints**: Sử dụng module `importlib`. Kiểm soát lỗi (sandbox cơ bản) trong quá trình import.
## 2. STARTER CODE

```python
# 1. Base Class representing the Plugin interface
class TextPlugin:
    def process(self, text: str) -> str:
        raise NotImplementedError("Plugins must implement the process method.")

# 2. Pipeline engine controlling execution
class Pipeline:
    def __init__(self):
        self._plugins: list[TextPlugin] = []

    def register(self, plugin: TextPlugin) -> None:
        """TODO: Add the plugin to the list."""
        pass

    def run(self, text: str) -> str:
        """TODO: Pass text through every registered plugin sequentially and return the final text."""
        pass

# 3. Create your Concrete Plugins here
class StripSpacesPlugin(TextPlugin):
    pass
    # TODO: implement process() to remove leading/trailing whitespace

class LowercasePlugin(TextPlugin):
    pass
    # TODO: implement process() to lower the text

class CensorPlugin(TextPlugin):
    def __init__(self, bad_word: str):
        self.bad_word = bad_word

    # TODO: implement process() to replace bad_word with "***"

if __name__ == "__main__":
    pipeline = Pipeline()

    # Registering behavior injected at runtime
    pipeline.register(StripSpacesPlugin())
    pipeline.register(LowercasePlugin())
    pipeline.register(CensorPlugin(bad_word="heck"))

    dirty_text = "   What the HECK is this?   "
    clean_text = pipeline.run(dirty_text)

    print(f"Result: '{clean_text}'")
    assert clean_text == "what the *** is this?"
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Inheriting from `TextPlugin` mandates that subclasses override `.process(text)`. Inside the pipeline's `.run(text)` string, assign the passed `text` variable, then loop through `self._plugins:` reassigning `text = plugin.process(text)`.

**HINT-2 (Partial)**:
For the implementations:

```python
class StripSpacesPlugin(TextPlugin):
    def process(self, text: str) -> str:
        return text.strip()
```

**HINT-3 (Near-solution)**:

```python
class CensorPlugin(TextPlugin):
    def __init__(self, bad_word: str):
        self.bad_word = bad_word.lower() # Case insensitive for matching

    def process(self, text: str) -> str:
        # Relies on LowercasePlugin firing FIRST, or you need slightly more complex logic
        return text.replace(self.bad_word, "***")

class Pipeline:
    def run(self, text: str) -> str:
        current_text = text
        for p in self._plugins:
            current_text = p.process(current_text)
        return current_text
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: Transformers (`HuggingFace pipelines`), Pytest hooks, requests `Sessions`, Webpack loaders.
- **Why do it manually**: Relying strictly on "Composition over Inheritance" makes applications infinitely scalable. If you hardcoded 5 `if` [...], [...]. Plugins decouple rules into isolate, testable classes securely.

## 5. VALIDATION CRITERIA

- [ ] Implementations enforce the interface class method override seamlessly.
- [ ] The `Pipeline` class has absolutely bare-minimum code (no knowledge of what `StripSpaces` is natively).
- [ ] Passes tests handling state via `CensorPlugin` taking constructor arguments effectively at runtime.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Dynamic Loading):** Modify your system to load plugin objects dynamically from a mock `.json` configuration file, avoiding hard-wiring `pipeline.register(X)` manually in the start script.
2. **Extension 2 (Error Handling Constraints):** What if `CensorPlugin` crashes internally during `.run()`? Update the Pipeline loop with `try/except Exception` logic. If a plugin crashes, [...] _which_ plugin class crashed (using `plugin.__class__.__name__`), [...], [...].
3. **Extension 3 (Timing Analytics):** Add Python `time.monotonic()` hooks inside the pipeline loop, calculating how many milliseconds each individual plugin requires. Have `Pipeline` print an analytics table ranking plugins by operational latency after completion.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
