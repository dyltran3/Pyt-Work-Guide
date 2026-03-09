# Exercise A-12: ORM-lite Table Mapper

## 1. EXERCISE BRIEF

**Context**: Object-Relational Mappers (ORMs) like SQLAlchemy or Django's ORM translate raw SQL database tables into Python objects, allowing developers to query databases using Python constructs instead of handwriting SQL text.
**Task**: Build a mini-ORM structure in pure Python mapping to an in-memory database (a list of dictionaries). You will create a generic `Table` class with `insert()`, `select(where={})`, `update(where={}, set_data={})`, and `delete(where={})` operations.
**Constraints**: Do **NOT** connect to SQLite or use any database libraries. The internal data store must be a `list of dicts` attached to the class instance. The `where` clause is a simple exact-match dictionary.

## 2. STARTER CODE

```python
class Table:
    def __init__(self, name: str):
        self.name = name
        self.columns = []
        self._data: list[dict] = []
        self._next_id = 1

    def insert(self, record: dict) -> int:
        """
        TODO: Add an 'id' integer key automatically. Append to _data.
        Return the inserted id.
        """
        pass

    def select(self, where: dict = None) -> list[dict]:
        """
        TODO: Return all records where the dict values match the 'where' dict.
        If where is None, return all records.
        """
        pass

    def update(self, where: dict, set_data: dict) -> int:
        """
        TODO: Find matching records, update them with set_data.
        Return number of records updated.
        """
        pass

    def delete(self, where: dict) -> int:
        """
        TODO: Find matching records, remove them from _data.
        Return number of records deleted.
        """
        pass

if __name__ == "__main__":
    users = Table("users")

    # Test Insert
    id1 = users.insert({"name": "Alice", "age": 30})
    id2 = users.insert({"name": "Bob", "age": 25})
    id3 = users.insert({"name": "Charlie", "age": 30})
    assert len(users.select()) == 3

    # Test Select
    thirty_year_olds = users.select(where={"age": 30})
    assert len(thirty_year_olds) == 2

    # Test Update
    updated_count = users.update(where={"name": "Alice"}, set_data={"age": 31})
    assert updated_count == 1
    assert users.select(where={"name": "Alice"})[0]["age"] == 31

    # Test Delete
    users.delete(where={"age": 25})
    assert len(users.select()) == 2

    print("All ORM functions passed!")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Selecting involves iterating over `self._data` and checking if a specific dictionary matches all key/value conditions.
`update` and `delete` fundamentally reuse finding the objects first, so write a strong match condition logic to use universally.

**HINT-2 (Partial)**:
For matching checking:

```python
def is_match(row: dict, conditions: dict) -> bool:
    if not conditions:
        return True
    return all(row.get(k) == v for k, v in conditions.items())
```

**HINT-3 (Near-solution)**:

```python
def select(self, where: dict = None) -> list[dict]:
    return [row for row in self._data if is_match(row, where)]

def delete(self, where: dict) -> int:
    before_count = len(self._data)
    # Retain only those that DO NOT match
    self._data = [row for row in self._data if not is_match(row, where)]
    return before_count - len(self._data)
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `SQLAlchemy`, `Django ORM`, `Peewee`, `Tortoise ORM`.
- **Why do it manually**: ORMs often act as a mysterious layer that developers fight against when queries become slow. Understanding how conditions translate to iteration/matching demystifies concepts like table scans versus indexed lookups, and prepares you for NoSQL databases which inherently use this exact `{key: value}` finding syntax (like MongoDB).

## 5. VALIDATION CRITERIA

- [ ] Successfully injects an auto-incrementing integer `id` key to newly inserted records.
- [ ] Updates multiple records at once if the `where` dictionary matches multiple elements.
- [ ] Safely deletes objects from the internal list without encountering `"index out of bounds"` errors (typically mitigated by rebuilding the list using comprehensions).
- [ ] Returns mathematically clean integer representations of row-counts modified.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Complex Operators):** Exact matching is standard. Introduce an operator syntax. If `where={"age__gt": 25}` is passed, intercept the `__gt` parser and evaluate if the row's age is greater than 25 (rather than exactly matching the string `"age__gt"`). Implement `__gt`, `__lt`, and `__contains`.
2. **Extension 2 (Lookup Dictionary Index):** A table scan (`for row in self._data`) takes $O(N)$ time. Implement a primary key Index. When `id` is created, store a reference in a dictionary `self._index_id = {1: row_dict, 2: row_dict...}`. Modify `.select()` so if `where` _only_ contains an `id`, it bypasses the massive loop and returns the record instantly in $O(1)$ time.
3. **Extension 3 (Dataclass Injection):** In Python, true ORMs return Objects, not Dictionaries. Accept a `dataclass` type in the `Table` initialization, and cast all dictionaries returned by `.select()` into those python Objects respectively.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
