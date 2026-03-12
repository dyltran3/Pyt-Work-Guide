# Exercise B-06: Inverted Index Builder

## 1. EXERCISE BRIEF

**Context**: Inverted Index (Chỉ mục ngược) là lõi cốt lõi của ElasticSearch, giúp việc Search Fulltext Data diễn ra chỉ trong vài nano giây thay vì quét toàn cơ sở dữ liệu.
**Task**: Phân tách một mảng hàng loạt tài liệu text, thực hiện tokenization thô, và thiết kế bảng Inverted Index ánh xạ mỗi từ khóa đến ID các tài liệu.
**Constraints**: Tối ưu hóa dictionary để hỗ trợ truy vấn các toán tử xếp nối kiểu biến thể đơn giản (AND / OR query).
## 2. STARTER CODE

```python
from collections import defaultdict, Counter

class SearchEngine:
    def __init__(self):
        # Format: {'word': [doc_id_1, doc_id_1, doc_id_2]}
        # Or better: {'word': {doc_id_1: count, doc_id_2: count}}
        self.index = defaultdict(Counter)

    def add_document(self, doc_id: int, text: str) -> None:
        """
        TODO:
        1. Tokenize the text (lowercase, split by whitespace).
        2. Count how many times each token appears.
        3. Update self.index so that index[token][doc_id] = frequency
        """
        pass

    def search(self, query: str) -> list[int]:
        """
        TODO:
        1. Tokenize the query (assume single word for now, lowercase).
        2. Lookup the query in self.index.
        3. Return a list of doc_ids sorted descending by how many times the word appeared.
        """
        pass

if __name__ == "__main__":
    engine = SearchEngine()

    engine.add_document(1, "The quick brown fox jumps over the lazy dog")
    engine.add_document(2, "A fast brown fox")
    engine.add_document(3, "The fox fox fox is very sneaky")

    # 'fox' appears in all three, but most frequently in Doc 3 (three times).
    results = engine.search("fox")
    print(f"Results for 'fox': {results}")
    assert results == [3, 1, 2] # Doc 3 has three, Doc 1 has one, Doc 2 has one.

    # 'brown' appears in 1 and 2
    assert set(engine.search("brown")) == {1, 2}

    # 'sneaky' only in 3
    assert engine.search("sneaky") == [3]

    # Unknown word
    assert engine.search("elephant") == []
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
When `add_document` receives `"The fox fox"`, tokenizing it yields `['the', 'fox', 'fox']`. Passing this list to `Counter()` returns `{'the': 1, 'fox': 2}`.

**HINT-2 (Partial)**:
Loop over the `Counter` dictionary results. Update your main index:

```python
counts = Counter(text.lower().split())
for word, freq in counts.items():
    self.index[word][doc_id] = freq
```

Because `self.index` is a `defaultdict(Counter)`, `self.index[word]` is safely auto-instantiated as a dictionary (Counter) inherently.

**HINT-3 (Near-solution)**:

```python
def search(self, query: str) -> list[int]:
    query = query.lower().strip()
    if query not in self.index:
        return []

    doc_freqs = self.index[query] # Returns {doc_id: frequency, ...}

    # We want to sort the keys (doc_ids) based on the values (frequency) descending
    ranked_docs = sorted(doc_freqs.keys(), key=lambda doc_id: doc_freqs[doc_id], reverse=True)
    return list(ranked_docs)
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `Elasticsearch`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] `add_document` safely tokenizes ignoring cases cleanly (Apple == apple).
- [ ] The `self.index` dictionary is structured optimally for fast lookups.
- [ ] Queries missing entirely return empty brackets `[]` without throwing `KeyError`.
- [ ] Document order strictly matches term frequency (TF) highest-to-lowest.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Punctuation Stripping):** Currently, `"dog"` and `"dog."` are treated as different words. Use `string.punctuation` to strip extra characters.
2. **Extension 2 (Multi-Word AND Query):** Allow the `search` function to accept multi-word phrases (e.g., `"brown fox"`). Return ONLY documents that contain BOTH words (set intersection).
3. **Extension 3 (Stop-words):** Words like "the", "a", "is" are noise. Create an initialization list of "stop words" and filter them out during indexing.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`collections`).
