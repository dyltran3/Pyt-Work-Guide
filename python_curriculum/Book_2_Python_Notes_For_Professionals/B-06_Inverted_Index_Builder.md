# Exercise B-06: Inverted Index Builder

## 1. EXERCISE BRIEF

**Context**: A standard SQL database `LIKE '%query%'` search becomes unbearably slow when scanning millions of text documents. Search engines (like Google, Wikipedia, or Elasticsearch) solve this fundamentally using an "Inverted Index"—mapping every unique word in a corpus to the exact documents (and positions) where it appears, making lookups nearly instant.
**Task**: Build a basic Inverted Index system. Accept a dictionary where keys are document IDs and values are pure text strings. Tokenize the text (split by space, lowercase). Build an index using python `collections.defaultdict(list)`. Create a `search(query)` method that accepts a single word, looks it up in $O(1)$ time, and ranks the matching document IDs by their "Term Frequency" (TF—how many times the word appeared in that document).
**Constraints**: Do **NOT** use `nltk`, `elasticsearch`, or other NLP packages. Rely strictly on `collections.defaultdict` and `collections.Counter` to natively parse the strings blocks into dictionaries cleanly.

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

- **Libraries/Tools**: `Elasticsearch`, `Apache Lucene`, `Whoosh`, `Meilisearch`.
- **Why do it manually**: Production search engines utilize exactly this logic under the hood. Understanding how tokens physically map to integer IDs demystifies "Relevance Scoring". It explains why searching for "Python" heavily ranks a document where "Python" appears 50 times versus a document where it appears once.

## 5. VALIDATION CRITERIA

- [ ] `add_document` safely tokenizes ignoring cases cleanly (Apple == apple).
- [ ] The `self.index` efficiently stores occurrences mapped per document naturally avoiding large array arrays dynamically.
- [ ] Queries missing entirely return empty brackets `[]` without throwing `KeyError`.
- [ ] Document order strictly matches term frequency (TF) highest-to-lowest natively globally.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Punctuation Stripping):** Currently, `"dog"` and `"dog."` evaluate differently due to punctuation sticking to the string natively. Use the `string.punctuation` module to strip natively breaking characters universally during tokenization strictly parsing pure characters continuously.
2. **Extension 2 (Multi-Word AND Query):** Allow the `search` function natively to accept multi-word phrases (e.g., `"brown fox"`). Evaluate both tokens natively. Return ONLY documents that contain BOTH words (set intersection of their `doc_ids`), then rank the sum of their combined frequencies gracefully.
3. **Extension 3 (Stop-words):** Words like "the", "a", "is" are noise functionally. Create an initialization list of "stop words", and natively ignore them during index counting saving massive memory chunks parsing aggressively dynamically.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`collections`).
