# Exercise A-14: Project Scaffold Generator

## 1. EXERCISE BRIEF

**Context**: Creating a new Python project by hand leads to messy inconsistences across teams. Professionals use scaffolding tools to generate standard folder trees (`src/`, `tests/`, `docs/`) and boilerplate files (`requirements.txt`, `.gitignore`, `README.md`) automatically from a command line immediately mimicking best practices.
**Task**: Build a Python CLI script that accepts arguments (like project name) and utilizes `os` and `pathlib` to generate a robust folder structure on the disk programmatically. It should write default generic template text into a `setup.py` (or `pyproject.toml`) and `.gitignore` file.
**Constraints**: Do **NOT** use `cookiecutter` or `copier`. Rely on built-in OS libraries to create directories. Enforce `exist_ok=True` checks so rerunning the script doesn't accidentally wipe existing files.

## 2. STARTER CODE

```python
import argparse
from pathlib import Path

def create_file(path: Path, content: str):
    """Helper: Write content to file if it doesn't already exist."""
    if not path.exists():
        path.write_text(content.strip() + "\n", encoding="utf-8")
        print(f"Created: {path}")

def generate_scaffold(project_name: str) -> None:
    """
    TODO:
    1. Create base directory matching project_name
    2. Create folders: src/{project_name}/, tests/, docs/
    3. Create __init__.py files where appropriate.
    4. Write a basic .gitignore ignoring venv and __pycache__
    """
    base_dir = Path(project_name)

    # Example directory creation
    base_dir.mkdir(parents=True, exist_ok=True)
    print(f"Scaffolding project: {base_dir.absolute()}")

    # Write your file and folder creation hierarchy here

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python Project Scaffolder")
    parser.add_argument("--name", required=True, help="Name of the project")

    args = parser.parse_args()
    generate_scaffold(args.name)
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
`pathlib.Path` is superior to `os.path`. You can join paths aggressively using the slash operator: `src_dir = base_dir / "src" / project_name`. Then call `.mkdir(parents=True, exist_ok=True)`.

**HINT-2 (Partial)**:
To bootstrap a package properly, both the `tests` directory and your module directory typically need an empty `__init__.py`.

```python
(src_dir / "__init__.py").touch()
```

**HINT-3 (Near-solution)**:

```python
def generate_scaffold(project_name):
    base = Path(project_name)
    src = base / "src" / project_name
    tests = base / "tests"

    # Create Directories
    for d in [src, tests, base / "docs"]:
        d.mkdir(parents=True, exist_ok=True)

    (src / "__init__.py").touch()

    # Write templates
    gitignore_content = """
.venv/
__pycache__/
*.pyc
.pytest_cache/
    """
    create_file(base / ".gitignore", gitignore_content)
    create_file(base / "requirements.txt", "# Add dependencies here")
    create_file(base / "README.md", f"# {project_name.capitalize()}\n\nA new python application.")
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `cookiecutter`, `Poetry` init commands, `pytest-cov` layouts.
- **Why do it manually**: Interacting strictly with Operating System I/O file protections (like resolving absolute paths vs relative ones, and handling access rights) is a standard backend hurdle. The `pathlib` framework resolves a decade of awkward string manipulations in `os.path` cleanly.

## 5. VALIDATION CRITERIA

- [ ] Successfully runs without producing `FileExistsError` if executed twice in a row.
- [ ] Outputs a modern `src/` layout format rather than dropping modules into the root (an anti-pattern).
- [ ] Correctly processes string inputs from `argparse`.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Github Actions):** Add a subdirectory `.github/workflows/` and write a basic YAML template inside it `test.yml` that configures a Python CI matrix to run on GitHub out of the box.
2. **Extension 2 (Automated Initial Installation):** After writing the files, use the `subprocess` module to programmatically execute `python -m venv .venv` inside the new folder, automatically bootstrapping the virtual environment exactly as the developer launches it.
3. **Extension 3 (Sub-process Git Init):** Immediately trigger `subprocess.run(['git', 'init'])` in the target directory to establish source control tracking inherently upon bootstrap.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`argparse`, `pathlib`).
