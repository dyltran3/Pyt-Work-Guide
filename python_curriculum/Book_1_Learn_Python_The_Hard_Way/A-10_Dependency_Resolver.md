# Exercise A-10: Dependency Resolver

## 1. EXERCISE BRIEF

**Context**: Applications rely on dependency managers (`pip`, `npm`, Dockerfiles) to install packages. Many packages depend on other packages. A resolver must determine the correct order to install packages so that no package is installed before its prerequisites exist. This is a classic Computer Science graph traversal problem: "Topological Sorting".
**Task**: Build a resolver in Python. Accept a dictionary where the keys are package names, and the values are lists of packages they depend on. Resolve this graph into a flat 1D list showing the correct installation order. You must also successfully detect "Circular Dependencies" (e.g., A needs B, B needs A) and raise an explicit `ValueError`.
**Constraints**: Do **NOT** import the `graphlib` module or any third-party graph network libraries. Rely purely on Python lists, sets, and basic algorithms using recursion or iterative stacks.

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

- **Libraries/Tools**: `pip`, `npm`, Dockerfile layer caching, Makefiles executing commands.
- **Why do it manually**: Resolving dependency graphs isn't just for installing libraries. Build-automation tools (like Webpack parsing JS imports), task schedulers (Apache Airflow running DAGs), and Terraform deploying cloud infrastructure universally utilize this algorithm to safely process steps that rely on past steps.

## 5. VALIDATION CRITERIA

- [ ] Returns a flattened list of packages representing safe installation order.
- [ ] Order respects hierarchy: packages with no dependencies (`A: []`) always appear earliest in the list before the modules that import them.
- [ ] Explicitly catches cyclical conditions (A -> B -> A) and yields a custom `ValueError` rather than exhausting recursion memory (RecursionError).

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Missing Packages):** Account for dictionary definitions leaning heavily on external packages: If `D` relies on `E`, but `E` does not exist as a key at the master level of the graph, your system must raise a `KeyError("Missing package resolution for E")`.
2. **Extension 2 (Tarjan's strongly connected components):** Standard DFS throws a simple error on hitting a loop. Write an implementation that accurately outputs exactly _which_ loop of packages is broken (e.g., `"Loop found resolving: A -> B -> C -> A"`).
3. **Extension 3 (Parallel Execution Generation):** If `A` needs nothing, and `Z` needs nothing, they could technically be installed simultaneously in production threading. Modify the output to return a list of lists: `[['A', 'Z'], ['B'], ['C', 'D']]` grouping packages that can be installed concurrently at each DAG stage.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
