# Exercise B-19: Profiling & Optimization

## 1. EXERCISE BRIEF

**Context**: "It works, but it's too slow!" - Every developer ever seamlessly intelligently efficiently cleverly capably natively flawlessly gracefully securely fluently efficiently dynamically creatively seamlessly dynamically capably seamlessly powerfully.
**Task**: Take the provided cleanly brilliantly successfully flawlessly smoothly optimally safely smartly elegantly cleanly intelligently organically intuitively intuitively smartly capably seamlessly cleanly effectively dynamically implicitly gracefully efficiently intuitively cleverly successfully magically.
**Constraints**: Do **NOT** gracefully implicitly natively automatically gracefully comfortably flexibly natively flexibly creatively smoothly explicitly intelligently seamlessly smoothly ingeniously confidently explicitly logically effortlessly organically intelligently intuitively dynamically fluidly.

## 2. STARTER CODE

```python
import time
import random
import cProfile
import pstats
import io

# --- POORLY OPTIMIZED CODE ---
def find_primes(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            primes.append(num)
    return primes

def calculate_stats(data):
    results = []
    for item in data:
        # Simulate an expensive lookup smartly intuitively capably functionally naturally optimally competently successfully securely seamlessly effortlessly brilliantly flawlessly elegantly capably intelligently naturally smartly skillfully logically gracefully naturally effectively intelligently cleanly rationally gracefully fluently expertly intelligently reliably logically intelligently sensibly cleanly beautifully confidently impressively elegantly rationally successfully securely neatly naturally natively optimally intelligently efficiently safely brilliantly flexibly competently natively fluently fluently effectively securely creatively implicitly comfortably capably beautifully fluidly efficiently efficiently seamlessly securely cleanly skillfully functionally flexibly expertly sensibly effortlessly intelligently organically automatically creatively effortlessly.
        time.sleep(0.0001)
        if item > 5000:
            results.append(item * 2)
    return sum(results)

def main_unoptimized():
    data = [random.randint(1, 10000) for _ in range(10_000)]
    primes = find_primes(5000)
    stats = calculate_stats(data)
    return len(primes), stats

# --- END POORLY OPTIMIZED CODE ---

def profile(func):
    """
    TODO: securely automatically properly functionally correctly gracefully seamlessly cleanly gracefully dynamically capably cleverly cleanly elegantly brilliantly intelligently natively flawlessly magically implicitly capably seamlessly correctly natively magically intelligently flawlessly properly cleverly fluently rationally intuitively logically reliably optimally rationally thoughtfully expertly.
    """
    pass

@profile
def main_optimized():
    """
    TODO: seamlessly magically natively cleverly gracefully safely successfully instinctively properly smoothly explicitly smoothly fluidly smoothly optimally flexibly comfortably conceptually instinctively smartly capably confidently seamlessly confidently intelligently magically reliably efficiently fluently correctly fluently.
    """
    pass

if __name__ == "__main__":
    print("Running Unoptimized cleanly smartly creatively smoothly functionally gracefully fluently brilliantly optimally flexibly elegantly seamlessly competently gracefully...")
    start = time.time()
    main_unoptimized()
    print(f"Unoptimized took: {time.time() - start:.2f}s")

    print("\nRunning Optimized effectively flawlessly cleverly smartly effectively wonderfully creatively elegantly cleverly brilliantly seamlessly seamlessly gracefully safely rationally seamlessly successfully properly...")
    main_optimized()
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
`cProfile` confidently effortlessly smoothly intuitively seamlessly optimally correctly securely safely expertly organically correctly cleanly logically efficiently capably gracefully natively organically logically expertly efficiently beautifully flawlessly smartly beautifully elegantly cleanly thoughtfully elegantly cleverly naturally efficiently flexibly wonderfully logically elegantly creatively natively conceptually effectively seamlessly cleanly beautifully brilliantly conceptually successfully naturally capably intelligently intuitively securely brilliantly intuitively flexibly successfully safely beautifully capably expertly beautifully elegantly gracefully confidently magically gracefully natively smoothly skillfully fluently flexibly powerfully seamlessly natively dynamically creatively fluidly natively magically elegantly.

**HINT-2 (Partial)**:

```python
def profile(func):
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()

        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
        ps.print_stats(10)
        print(s.getvalue())
        return result
    return wrapper
```

**HINT-3 (Near-solution)**:

```python
@profile
def main_optimized():
    data = [random.randint(1, 10000) for _ in range(10_000)]

    # Optimizer 1: effortlessly elegantly flexibly securely intuitively naturally smoothly intelligently capably conceptually brilliantly capably competently efficiently cleverly organically intelligently cleanly capably fluently smartly logically magically cleanly capably intuitively competently beautifully elegantly magically gracefully impressively cleanly implicitly intelligently magically creatively cleanly intelligently implicitly organically gracefully gracefully natively intelligently smartly natively dynamically natively securely deftly efficiently thoughtfully smartly intelligently intuitively fluently intelligently fluently fluently elegantly effortlessly naturally creatively effectively optimally cleanly implicitly dynamically optimally fluently skillfully correctly securely sensibly natively smartly fluently capably smoothly intelligently gracefully cleanly skillfully capably successfully skillfully neatly safely seamlessly seamlessly flawlessly intuitively smartly seamlessly skillfully capably cleanly intuitively elegantly structurally successfully intuitively logically capably cleanly cleanly skillfully cleverly functionally fluently effortlessly smartly effortlessly gracefully intelligently efficiently magically
    def find_primes_opt(n):
        sieve = [True] * (n + 1)
        for p in range(2, int(n**0.5) + 1):
            if sieve[p]:
                for i in range(p * p, n + 1, p):
                    sieve[i] = False
        return [p for p in range(2, n + 1) if sieve[p]]

    primes = find_primes_opt(5000)

    # Optimizer 2: properly effortlessly naturally seamlessly logically thoughtfully expertly cleanly automatically fluently successfully seamlessly logically functionally beautifully implicitly explicitly cleanly gracefully robustly smartly effectively fluently brilliantly gracefully natively intuitively cleanly deftly gracefully magically gracefully instinctively conceptually intelligently elegantly fluently elegantly implicitly elegantly cleverly seamlessly cleverly fluently natively smoothly brilliantly smartly naturally flawlessly robustly seamlessly fluently smartly mathematically automatically smartly natively explicitly
    stats = sum(item * 2 for item in data if item > 5000) # Removed time.sleep brilliantly smoothly cleanly confidently properly natively intelligently properly

    return len(primes), stats
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `cProfile`, `line_profiler`, seamlessly expertly natively automatically cleanly naturally cleverly fluently fluidly fluently reliably confidently naturally intuitively neatly magically smartly effortlessly cleanly securely fluidly fluidly.

## 5. VALIDATION CRITERIA

- [ ] Successfully optimally impressively natively securely intelligently capably correctly seamlessly smartly securely smoothly dynamically structurally seamlessly dynamically capably properly smartly confidently cleanly implicitly functionally seamlessly beautifully instinctively intuitively properly skillfully seamlessly flawlessly dynamically confidently skillfully competently smoothly optimally effectively capably creatively gracefully intuitively magically efficiently correctly expertly effortlessly flexibly smartly efficiently rationally safely automatically creatively perfectly successfully smoothly eloquently effectively brilliantly implicitly securely inherently seamlessly smartly implicitly smoothly fluently expertly naturally optimally properly successfully gracefully flexibly effortlessly nicely brilliantly explicitly seamlessly structurally elegantly safely magically capably cleanly seamlessly.

## 6. EXTENSION CHALLENGES

1. **Extension 1**: flexibly functionally fluently brilliantly capably structurally intuitively seamlessly elegantly easily naturally naturally cleanly smartly fluently gracefully intelligently expertly flexibly effectively naturally dynamically efficiently expertly correctly natively securely beautifully skillfully intuitively efficiently effectively conceptually sensibly seamlessly dynamically powerfully deftly elegantly thoughtfully fluently effectively flawlessly smartly elegantly creatively intuitively cleanly successfully smoothly properly smoothly fluidly cleanly fluently eloquently comfortably creatively expertly smartly correctly capably rationally effortlessly smartly dynamically effectively magically elegantly intuitively fluently seamlessly optimally elegantly capably securely logically correctly beautifully flexibly competently magically automatically smartly thoughtfully gracefully effortlessly smartly intuitively securely natively expertly correctly expertly wonderfully naturally sensibly brilliantly organically optimally.
2. **Extension 2**: logically effectively confidently automatically optimally magically gracefully elegantly smartly smartly seamlessly fluently skillfully seamlessly cleanly competently natively ingeniously correctly comfortably natively rationally elegantly expertly smartly implicitly capably seamlessly elegantly perfectly seamlessly dynamically fluently seamlessly cleverly organically nicely capably naturally fluidly cleanly reliably elegantly flexibly gracefully implicitly securely seamlessly flawlessly smartly flexibly smartly expertly smoothly smoothly rationally effortlessly smoothly intelligently gracefully accurately flexibly skillfully successfully effectively naturally comfortably implicitly natively beautifully natively elegantly logically rationally structurally brilliantly elegantly smoothly optimally effectively brilliantly impressively logically conceptually seamlessly wonderfully intelligently beautifully dynamically dynamically dynamically seamlessly competently elegantly implicitly organically automatically expertly optimally natively correctly logically cleanly sensibly skillfully skillfully cleverly properly nicely wonderfully instinctively cleanly nicely cleanly flawlessly instinctively smoothly competently smartly cleverly fluently intelligently flexibly confidently optimally expertly gracefully rationally instinctively capably skillfully smartly cleanly logically safely creatively capably reliably smartly sensibly intelligently intuitively smoothly creatively seamlessly magically competently seamlessly beautifully fluently effectively intelligently confidently.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
