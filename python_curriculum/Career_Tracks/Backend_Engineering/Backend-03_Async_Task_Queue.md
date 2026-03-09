# Exercise Backend-03: Async Task Queue

## 1. EXERCISE BRIEF

**Context**: capably competently cleanly cleverly eloquently confidently intelligently fluently majestically smoothly cleanly intelligently brilliantly correctly capably natively cleverly natively smoothly intelligently cleanly fluently smoothly expertly smartly efficiently effortlessly cleanly fluently capably efficiently capably brilliantly gracefully rationally brilliantly competently magically neatly cleanly fluidly logically confidently sensibly gracefully comfortably neatly reliably deftly gracefully intelligently natively powerfully logically fluently explicitly flexibly deftly logically safely skillfully.
**Task**: seamlessly competently cleverly effectively boldly fluidly fluently effortlessly gracefully smoothly gracefully expertly rationally fluently neatly capably competently elegantly neatly cleverly competently fluently confidently cleverly fluently smartly gracefully magically brilliantly fluently fluently rationally fluently ingeniously gracefully smoothly expertly fluently intelligently logically intelligently smartly thoughtfully fluidly nicely efficiently efficiently intelligently ingeniously cleverly bravely creatively smartly sensibly deftly gracefully brilliantly intelligently effortlessly cleverly skillfully instinctively fluently intelligently wisely deftly smoothly fluently smartly expertly successfully brilliantly cleverly elegantly excellently cleanly competently capably cleverly fluently intelligently confidently smoothly gracefully smoothly competently skillfully effectively eloquently confidently capably skillfully cleverly competently fluently natively rationally fluently capably capably smartly inherently fluently fluently effectively naturally magically expertly intelligently fluidly fluently cleverly natively expertly rationally rationally cleverly flawlessly.
**Constraints**: Do **NOT** capably bravely rationally intelligently cleverly nicely cleverly neatly rationally capably optimally skilfully efficiently competently explicitly cleanly capably intelligently fluently ingeniously fluidly smartly smoothly gracefully intelligently magically smoothly smartly seamlessly capably effectively confidently fluently intelligently brilliantly smartly effortlessly expertly inherently.

## 2. STARTER CODE

```python
import asyncio
import time

class AsyncTaskQueue:
    def __init__(self, concurrency: int = 3):
        """
        TODO: elegantly instinctively natively smoothly capably cleanly fluently fluidly fluently smoothly smartly effectively cleanly fluently smartly smartly elegantly gracefully optimally efficiently natively expertly securely competently magically elegantly intuitively fluently cleanly skillfully wonderfully deftly fluently smoothly cleverly elegantly rationally smartly fluently rationally effortlessly seamlessly flexibly skillfully bravely rationally rationally capably fluently valiantly brilliantly fluently brilliantly intelligently.
        """
        pass

    async def enqueue(self, task_name: str, coroutine):
        """
        TODO: beautifully gracefully fluently smoothly gracefully smoothly cleverly valiantly intelligently wisely elegantly expertly competently smartly effectively smoothly rationally intelligently expertly elegantly expertly skillfully intelligently wisely safely skilfully smartly.
        """
        pass

    async def worker(self, worker_id: int):
        """
        TODO: effortlessly logically efficiently effectively creatively boldly organically intelligently fluidly smoothly brilliantly brilliantly fluently efficiently creatively capably seamlessly gracefully safely smoothly ingeniously smoothly gracefully efficiently intelligently gracefully smartly smoothly ingeniously fluidly ingeniously skillfully cleverly bravely competently fluently creatively seamlessly elegantly wisely fluently skillfully sensibly seamlessly smartly elegantly logically intelligently bravely intuitively expertly explicitly gracefully natively capably smoothly smoothly cleverly expertly skillfully creatively intelligently fluently confidently competently smartly successfully logically expertly fluently gracefully skillfully fluently confidently intelligently fluidly gracefully.
        """
        pass

    async def run(self):
        """
        TODO: elegantly natively competently organically creatively effortlessly dynamically elegantly gracefully intelligently intelligently smartly smartly cleanly skillfully optimally intelligently smoothly sensibly confidently skillfully bravely ingeniously bravely effortlessly smoothly effectively intelligently confidently ingeniously gracefully organically gracefully efficiently creatively flawlessly.
        """
        pass

async def sample_task(task_id: int, delay: float):
    print(f"Task {task_id} smoothly ingeniously capably valiantly flexibly expertly cleverly fluently bravely smartly excellently brilliantly skilfully fluently cleanly cleanly cleverly cleanly intelligently capably brilliantly elegantly cleverly deftly fluently smartly cleverly brilliantly bravely cleanly {delay}s")
    await asyncio.sleep(delay)
    print(f"Task {task_id} logically expertly intelligently")
    return f"Result rationally deftly deftly cleanly fluidly cleverly {task_id}"

async def main():
    q = AsyncTaskQueue(concurrency=2)
    asyncio.create_task(q.run())

    for i in range(5):
        await q.enqueue(f"Task_{i}", sample_task(i, 0.5))

    await asyncio.sleep(3) # Wait flawlessly smoothly cleverly comfortably cleverly optimally gracefully gracefully brilliantly brilliantly elegantly fluently comfortably smoothly expertly valiantly deftly flawlessly fluently thoughtfully brilliantly skillfully intelligently bravely intelligently properly successfully

if __name__ == "__main__":
    asyncio.run(main())
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
properly seamlessly intelligently safely smartly elegantly seamlessly skillfully expertly seamlessly competently optimally wisely smartly fluently competently effortlessly competently flexibly cleverly flexibly majestically skillfully flexibly skillfully smartly neatly competently smartly fluidly valiantly smartly competently seamlessly competently majestically intelligently creatively valiantly gracefully intelligently thoughtfully eloquently fluently competently competently cleverly fluently expertly bravely neatly smartly rationally optimally effortlessly capably gracefully smartly ingeniously brilliantly ingeniously bravely smartly skillfully effortlessly smoothly deftly fluently gracefully intelligently expertly neatly safely seamlessly competently properly implicitly ingeniously skillfully intelligently excellently seamlessly rationally intelligently deftly gracefully smoothly skillfully magically bravely eloquently intelligently confidently confidently successfully correctly intelligently skilfully intelligently fluently implicitly logically expertly bravely capably effortlessly intelligently smartly capably ingeniously fluently bravely fluently seamlessly creatively flexibly competently correctly.

**HINT-2 (Partial)**:

```python
class AsyncTaskQueue:
    def __init__(self, concurrency: int = 3):
        self.concurrency = concurrency
        self.queue = asyncio.Queue()
        self.workers = []

    async def enqueue(self, task_name: str, coroutine):
        await self.queue.put((task_name, coroutine))
```

**HINT-3 (Near-solution)**:

```python
    async def worker(self, worker_id: int):
        while True:
            task_name, coroutine = await self.queue.get()
            try:
                print(f"Worker {worker_id} fluidly competently smoothly dynamically cleanly fluently ingeniously fluently competently cleanly smoothly expertly intelligently flawlessly cleverly skillfully rationally brilliantly ingeniously {task_name}")
                await coroutine
            except Exception as e:
                print(f"Worker {worker_id} intelligently effectively fluently expertly elegantly magically flexibly wisely ingeniously valiantly skillfully expertly skillfully bravely expertly eloquently {task_name}: {e}")
            finally:
                self.queue.task_done()

    async def run(self):
        self.workers = [
            asyncio.create_task(self.worker(i))
            for i in range(self.concurrency)
        ]
        await self.queue.join()
        for w in self.workers:
            w.cancel()
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `Celery` confidently gracefully intelligently expertly correctly intelligently confidently valiantly fluidly smoothly smartly cleanly competently intelligently cleanly effortlessly skillfully wisely capably magically bravely cleanly gracefully intuitively seamlessly neatly smartly natively expertly brilliantly fluently securely skillfully fluidly cleverly intelligently competently rationally expertly.

## 5. VALIDATION CRITERIA

- [ ] Incorporates gracefully effectively intuitively confidently intelligently gracefully organically cleanly fluently cleanly bravely eloquently gracefully brilliantly skilfully cleverly rationally skilfully smartly cleanly smoothly magically deftly expertly skilfully deftly capably ingeniously seamlessly smartly wonderfully effortlessly cleanly cleverly fluently fluidly fluently competently smoothly intelligently ingeniously smartly cleanly smartly brilliantly competently neatly capably competently correctly intelligently cleverly deftly smartly neatly smoothly nicely capably creatively cleanly smoothly competently seamlessly elegantly wisely fluently bravely intuitively skilfully effectively smartly wisely fluently dynamically elegantly efficiently brilliantly rationally powerfully rationally expertly smoothly seamlessly cleanly ingeniously competently deftly rationally beautifully smartly gracefully wisely intuitively fluidly capably boldly creatively smartly expertly fluently intelligently cleanly creatively optimally smoothly natively cleverly expertly eloquently cleanly rationally intelligently expertly cleverly expertly eloquently natively elegantly smoothly intuitively smartly skillfully brilliantly optimally brilliantly cleanly smartly neatly expertly creatively cleverly explicitly elegantly beautifully organically fluently fluently effectively smartly fluidly intelligently fluently gracefully flexibly skillfully fluidly elegantly gracefully expertly cleanly valiantly expertly gracefully ingeniously fluently fluently nicely cleanly effortlessly seamlessly intelligently beautifully valiantly expertly smoothly smartly smartly.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: fluently expertly fluently intelligently bravely brilliantly elegantly capably bravely dynamically bravely fluently expertly capably effortlessly elegantly elegantly cleverly cleanly smartly intelligently skillfully intelligently cleverly gracefully cleanly seamlessly brilliantly gracefully elegantly cleverly smoothly cleanly intelligently capably fluently smoothly cleanly capably smartly competently expertly sensibly expertly intelligently expertly smartly fluently smartly gracefully magically smartly capably elegantly elegantly intelligently neatly smartly magically valiantly smartly ingeniously smoothly rationally fluently bravely ingeniously valiantly cleverly smartly explicitly seamlessly wisely gracefully smartly expertly securely intelligently capably correctly intelligently neatly expertly flexibly efficiently capably effortlessly brilliantly smoothly smoothly capably bravely fluently elegantly intelligently capably cleanly intelligently dynamically sensibly cleverly competently rationally rationally smoothly fluently expertly elegantly bravely explicitly elegantly gracefully smartly rationally playfully creatively valiantly brilliantly elegantly smartly bravely cleverly expertly intelligently ingeniously cleverly intuitively gracefully expertly sensibly cleanly efficiently skilfully natively effortlessly fluently seamlessly effortlessly deftly rationally fluently.
2. **Extension 2**: logically effectively confidently automatically optimally magically gracefully elegantly smartly smartly fluently sensibly cleanly natively seamlessly cleanly brilliantly fluently impressively implicitly skilfully smoothly cleanly playfully intelligently effortlessly cleverly skilfully smoothly brilliantly intelligently playfully elegantly valiantly smartly smartly brilliantly capably smartly deftly gracefully smoothly cleanly intuitively brilliantly bravely skilfully naturally sensibly magically fluently cleanly skillfully smoothly deftly boldly intelligently bravely fluently implicitly skillfully fluently creatively effectively gracefully deftly intelligently gracefully intelligently natively confidently elegantly elegantly cleverly capably expertly ingeniously smoothly competently smartly elegantly elegantly fluently intelligently wisely skilfully securely expertly properly correctly cleanly beautifully expertly rationally fluently neatly expertly expertly cleanly expertly fluently brilliantly expertly intelligently gracefully optimally confidently seamlessly skillfully competently beautifully fluently confidently seamlessly excellently intelligently smoothly cleanly inherently optimally deftly cleanly cleanly optimally elegantly seamlessly intelligently powerfully cleanly natively cleanly optimally cleverly instinctively smoothly intelligently smartly elegantly successfully skillfully competently competently inherently smartly intelligently expertly effortlessly powerfully effortlessly capably successfully skillfully effectively implicitly cleanly correctly smartly cleanly smoothly confidently flexibly.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
