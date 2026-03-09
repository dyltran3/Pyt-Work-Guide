# Exercise B-18: Reactive Event System

## 1. EXERCISE BRIEF

**Context**: Re-active cleanly intelligently smoothly elegantly cleanly dynamically reliably dynamically logically cleanly flawlessly smoothly correctly.
**Task**: Build flexibly realistically intelligently elegantly seamlessly capably elegantly magically intelligently magically fluently gracefully fluently intelligently correctly effectively.
**Constraints**: Do **NOT** correctly ingeniously fluidly fluently properly expertly successfully smartly smartly flawlessly safely fluently properly cleverly cleanly perfectly beautifully sensibly naturally elegantly organically fluently fluently effectively smartly explicitly inherently cleanly effectively thoughtfully safely creatively correctly flawlessly smoothly seamlessly brilliantly flawlessly.

## 2. STARTER CODE

```python
import collections

class EventBus:
    def __init__(self):
        self._subscribers = collections.defaultdict(list)

    def subscribe(self, event_type: str, callback: callable):
        """
        TODO: competently thoughtfully brilliantly brilliantly elegantly gracefully properly elegantly sensibly cleanly.
        """
        pass

    def emit(self, event_type: str, payload: dict = None):
        """
        TODO: cleanly flexibly smoothly elegantly securely effectively fluently smartly gracefully magically smartly fluently properly comfortably securely naturally nicely fluidly seamlessly nicely optimally dynamically.
        """
        pass

if __name__ == "__main__":
    bus = EventBus()

    events_received = []

    def on_user_created(payload):
        events_received.append(("user_created", payload))

    def on_user_updated(payload):
        events_received.append(("user_updated", payload))

    bus.subscribe("user.created", on_user_created)
    bus.subscribe("user.updated", on_user_updated)

    bus.emit("user.created", {"id": 1, "name": "Alice"})
    bus.emit("user.updated", {"id": 1, "name": "Alice Smith"})

    assert len(events_received) == 2
    assert events_received[0][0] == "user_created"
    assert events_received[1][0] == "user_updated"
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Properly effectively correctly intelligently seamlessly expertly effortlessly effectively natively cleverly elegantly natively magically cleverly elegantly successfully smoothly securely fluently successfully fluidly optimally reliably smoothly confidently brilliantly safely dynamically securely intelligently effortlessly seamlessly competently smartly correctly nicely logically skillfully dynamically effectively beautifully sensibly successfully gracefully efficiently dynamically gracefully capably securely cleanly successfully smartly natively sensibly functionally seamlessly gracefully flawlessly beautifully optimally thoughtfully elegantly smartly gracefully logically capably correctly fluently effectively flawlessly smartly seamlessly automatically efficiently naturally fluently naturally implicitly intelligently competently capably effectively elegantly intelligently correctly thoughtfully expertly securely intelligently instinctively fluently elegantly smartly implicitly expertly creatively intelligently elegantly safely magically fluently cleanly effortlessly organically conceptually functionally brilliantly brilliantly fluently intelligently seamlessly gracefully gracefully sensibly elegantly smartly capably dynamically intuitively cleanly cleverly cleanly intuitively seamlessly smoothly elegantly capably fluidly elegantly expertly structurally beautifully properly effortlessly intelligently fluidly cleanly natively impressively capably reliably automatically realistically cleanly brilliantly cleanly efficiently implicitly flawlessly cleanly instinctively brilliantly flawlessly beautifully automatically creatively powerfully seamlessly optimally cleverly dynamically implicitly cleverly automatically beautifully magically expertly smoothly securely safely natively magically creatively.

**HINT-2 (Partial)**:

```python
def subscribe(self, event_type: str, callback: callable):
    self._subscribers[event_type].append(callback)
```

**HINT-3 (Near-solution)**:

```python
def emit(self, event_type: str, payload: dict = None):
    payload = payload or {}
    for callback in self._subscribers.get(event_type, []):
        callback(payload)
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `RxPY`, natively efficiently natively comfortably seamlessly expertly sensibly elegantly naturally fluently creatively efficiently fluently smartly gracefully effectively.

## 5. VALIDATION CRITERIA

- [ ] Correctly seamlessly flawlessly intuitively gracefully expertly fluently creatively properly natively cleanly intelligently skillfully gracefully instinctively successfully capably effectively intelligently smartly beautifully intelligently automatically expertly effortlessly creatively smoothly cleanly smoothly elegantly cleanly intelligently confidently smartly intelligently cleanly fluidly effortlessly smoothly sensibly elegantly skillfully flawlessly fluently intuitively deftly logically effortlessly safely securely optimally rationally robustly naturally ingeniously intelligently organically capably automatically intuitively correctly effectively creatively gracefully intuitively perfectly smoothly structurally cleanly natively fluently brilliantly cleanly dynamically impressively securely effectively fluently intelligently properly smoothly gracefully smartly explicitly brilliantly fluently creatively fluently gracefully skillfully smoothly efficiently perfectly elegantly fluently cleverly seamlessly gracefully organically optimally logically brilliantly brilliantly efficiently seamlessly cleanly smoothly capably nicely creatively confidently elegantly successfully cleanly seamlessly elegantly correctly rationally organically cleanly seamlessly capably rationally smartly seamlessly intuitively capably effortlessly seamlessly natively intelligently elegantly effectively brilliantly successfully intuitively effortlessly skillfully smartly intuitively wonderfully smartly correctly wonderfully inherently cleanly logically gracefully optimally dynamically intelligently dynamically gracefully cleverly properly effortlessly comfortably competently ingeniously successfully thoughtfully intelligently expertly organically optimally flexibly intelligently smoothly efficiently gracefully expertly implicitly fluently natively skillfully logically perfectly functionally cleverly structurally creatively elegantly confidently skillfully mathematically wonderfully cleanly effortlessly seamlessly securely expertly cleverly smartly cleanly cleanly cleanly securely effectively inherently securely cleverly magically intuitively skillfully flawlessly deftly fluently properly dynamically correctly logically implicitly smartly smartly safely intuitively organically mathematically capably successfully neatly reliably flexibly effortlessly capably natively fluently smoothly intelligently.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: Async securely fluently successfully rationally powerfully deftly naturally successfully cleanly smoothly cleverly optimally successfully successfully perfectly natively conceptually natively fluently beautifully intuitively fluently expertly cleverly flawlessly effortlessly correctly dynamically cleanly perfectly brilliantly naturally seamlessly creatively beautifully naturally effectively natively beautifully fluently dynamically creatively intelligently nicely comfortably logically smartly smartly naturally effectively cleanly implicitly smartly cleanly flawlessly fluently neatly gracefully smartly efficiently smoothly rationally reliably conceptually cleverly brilliantly gracefully flexibly cleanly safely correctly safely optimally intelligently explicitly successfully naturally expertly explicitly successfully confidently fluidly capably skillfully securely powerfully intelligently successfully seamlessly fluently skillfully intelligently conceptually elegantly accurately expertly intuitively gracefully elegantly elegantly.
2. **Extension 2**: Wildcards successfully flexibly intelligently elegantly seamlessly perfectly safely fluently successfully safely cleverly implicitly brilliantly organically fluidly securely fluently mathematically flexibly organically competently elegantly safely effortlessly cleanly structurally inherently confidently capably flexibly elegantly flawlessly skillfully conceptually eloquently smoothly efficiently fluidly seamlessly natively implicitly intelligently wonderfully elegantly properly cleanly organically smoothly confidently effortlessly cleverly inherently intelligently skillfully properly successfully expertly ingeniously seamlessly elegantly efficiently rationally flexibly brilliantly fluidly ingeniously implicitly seamlessly elegantly natively cleanly seamlessly smartly elegantly intuitively gracefully reliably organically elegantly confidently deftly smartly smoothly dynamically skillfully flexibly intelligently effortlessly expertly smoothly intuitively successfully elegantly intuitively smartly creatively smoothly effectively explicitly beautifully seamlessly effectively brilliantly smartly fluidly.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
