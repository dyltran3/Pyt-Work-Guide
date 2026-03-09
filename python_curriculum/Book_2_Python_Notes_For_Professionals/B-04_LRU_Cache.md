# Exercise B-04: LRU Cache từ đầu

## 1. EXERCISE BRIEF

**Context**: Caching is the ultimate optimization. Python provides `@functools.lru_cache`, enforcing a "Least Recently Used" eviction algorithm: if the cache size limit is hit, the oldest, least-accessed object is thrown out. How is this actually stored efficiently?
**Task**: Build a manual LRU cache class using an `OrderedDict`. Implement `get(key)` and `set(key, value)`. If the capacity limit is exceeded during a `set`, automatically evict the least recently utilized entry. Using `get` should refresh the usage order of the accessed item.
**Constraints**: Do **NOT** use `functools`. You must leverage `collections.OrderedDict` efficiently, preventing slow $O(N)$ index-shifting. Both `get` and `set` must execute mathematically close to $O(1)$ constant time operations.

## 2. STARTER CODE

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # TODO: Initialize your storage container
        self.cache = OrderedDict()

    def get(self, key: str):
        """
        TODO: Return the value if exists, else return None.
        CRITICAL: If it exists, you must mark it as 'recently used'
        before returning so it doesn't get evicted!
        """
        pass

    def set(self, key: str, value: any) -> None:
        """
        TODO: Add or update the key-value pair.
        Mark it as recently used.
        If adding pushes the size over self.capacity, evict the OLDEST item.
        """
        pass

if __name__ == "__main__":
    cache = LRUCache(2)

    cache.set("A", 1)
    cache.set("B", 2)

    # Getting A refreshes it
    assert cache.get("A") == 1

    cache.set("C", 3)
    # Capacity is 2. B was least recently used, so B is gone.
    assert cache.get("B") is None
    assert cache.get("C") == 3
    assert cache.get("A") == 1


    print("LRU Cache logic passed cleanly.")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
`OrderedDict` remembers the insertion order of keys. If you want to mark something as "recently used," you don't rebuild the dictionary. You use the built-in `move_to_end(key)` method provided natively by the class object.

**HINT-2 (Partial)**:
To evict the oldest item when over capacity, you remove the first registered item of the ordered dict. `popitem(last=False)` returns and pops the oldest item in exactly $O(1)$ operations natively without looping.

**HINT-3 (Near-solution)**:

```python
def get(self, key: str):
    if key not in self.cache:
        return None
    self.cache.move_to_end(key) # Refresh it!
    return self.cache[key]

def set(self, key: str, value: any) -> None:
    if key in self.cache:
        self.cache.move_to_end(key) # Refresh position
    self.cache[key] = value

    if len(self.cache) > self.capacity:
        self.cache.popitem(last=False) # Evict the oldest (FIFO head)
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: Redis `maxmemory-policy allkeys-lru`, Memcached, HTTP Browser Cache Control behaviors.
- **Why do it manually**: A `@functools.lru_cache` wraps functions cleanly, but is functionally isolated inside the executing scope. By building an explicit object cache layer with custom dictionaries, developers construct network-bound layers (like a hybrid in-memory + Redis fallback pattern) cleanly sharing state actively across classes natively.

## 5. VALIDATION CRITERIA

- [ ] Maintains the strict `capacity` bounded constraints seamlessly.
- [ ] Validates the `move_to_end()` updating refresh mechanism during read-operations.
- [ ] Accomplishes actions safely avoiding looping iterations to execute pop routines ensuring $O(1)$ efficiency requirements remain unviolated.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (TTL Timer):** Absolute eviction ignores time. Add a "Time to Live" (TTL). In the `set` method, store a tuple of `(value, time.time())`. In `get()`, verify against the TTL bound. If the entry's timestamp exceeds the threshold, strictly delete it and return `None` despite it functionally remaining within the capacity block constraints.
2. **Extension 2 (Cache Decorator Injection):** Implement a class-bound wrapper `@memoize_to_LRU(cache_instance_ref)` bridging your manual class back into standard wrapping usage functionality dynamically capturing function execution arguments into localized strings natively.
3. **Extension 3 (Thread Safety Locks):** Dictionaries aren't fundamentally thread-safe mathematically during destructive iterations. Implement `threading.Lock()` inside your explicit cache methods preventing Race Conditions if 5 threads execute a `set()` simultaneously violating eviction counts critically.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`collections`).
