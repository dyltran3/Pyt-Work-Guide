# Exercise A-10: Dependency Resolver

## 1. EXERCISE BRIEF

**Context**: Các pipeline khởi tạo ứng dụng thường gồm hàng loạt service phụ thuộc lẫn nhau (DB phải chạy trước Cache, Cache trước Web). Xử lý cấu trúc đồ thị mạng (DAG) là nền tảng của các DevOps Tool.
**Task**: Viết bộ phân tích sự phụ thuộc sử dụng thuật toán Sắp xếp Topo (Topological Sort). Phát hiện chu trình (Circular Dependency) để văng lỗi nếu cấu trúc bị vòng.
**Constraints**: Mã hóa bằng DFS hoặc Kahn's Algorithm. Yêu cầu in ra thứ tự khởi động (Boot order) đúng chuẩn trên Terminal.
## 2. STARTER CODE

```python
def resolve_dependencies(graph: dict[str, list[str]]) -> list[str]:
    """
    TODO: Given a dependency graph dict, perform a topological sort.
    Return the safe installation order.
    Raise ValueError if a circular dependency is detected.
    """
    installation_order = []

    # Write your graph traversal code here

    return installation_order

if __name__ == "__main__":
    # A relies on nothing. B relies on A. C relies on B. D relies on B and C.
    valid_graph = {
        'D': ['B', 'C'],
        'C': ['B'],
        'B': ['A'],
        'A': []
    }

    order = resolve_dependencies(valid_graph)
    print(f"Installation Order: {order}")
    # Expected: ['A', 'B', 'C', 'D']

    circular_graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }

    try:
        resolve_dependencies(circular_graph)
        assert False, "Should have raised ValueError for circular dependency!"
    except ValueError as e:
        print(f"Correctly caught circular dependency: {e}")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
You need Depth-First Search (DFS). For each node in the graph, recursively visit all of its dependencies first. Keep a `visited` set to avoid visiting the same node twice, and a `temp_visiting` set to detect loops safely on the current branch.

**HINT-2 (Partial)**:
Inside your function, define a helper `dfs(node)` that executes the logic.

```python
visited = set()     # Installed packages
temp_path = set()   # Packages currently in the resolution stack (for loop detection)
result = []

def dfs(node):
    if node in temp_path:
        raise ValueError("Circular loop!")
    if node not in visited:
        temp_path.add(node)
        # Recursively call dfs() for all dependencies of this node...
```

**HINT-3 (Near-solution)**:

```python
def dfs(node):
    # Loop detection
    if node in temp_path:
         raise ValueError(f"Circular dependency detected at {node}")
    # Already processed, skip
    if node in visited:
         return

    temp_path.add(node)

    # Resolve children
    for child in graph.get(node, []):
        dfs(child)

    # Mark as completely processed
    temp_path.remove(node)
    visited.add(node)
    installation_order.append(node)
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `pip`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Returns a flattened list of packages representing safe installation order.
- [ ] Order respects hierarchy: packages with no dependencies (`A: []`) always appear earliest in the list before the modules that import them.
- [ ] Explicitly catches cyclical conditions (A -> B -> A) and yields a custom `ValueError` rather than exhausting recursion memory (RecursionError).

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Missing Packages):** Account for dictionary definitions leaning heavily on external packages: If `D` relies on `E`, but `E` does not exist as a key at the master level of the graph, your system must raise a `KeyError("Missing package resolution for E")`.
2. **Extension 2 (Tarjan's strongly connected components):** Standard DFS [...]. Write [...] _which_ loop of packages is broken (e.g., `"Loop found resolving: A -> B -> C -> A"`).
3. **Extension 3 (Parallel Execution Generation):** If `A` needs nothing, and `Z` needs nothing, [...]. Modify [...]: `[['A', 'Z'], ['B'], ['C', 'D']]` [...] DAG stage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
