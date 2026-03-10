# Exercise A-14: Project Scaffold Generator

## 1. EXERCISE BRIEF

**Context**: Việc setup hàng loạt thư mục dự án mới theo chuẩn (Scaffolding), lặp lại, hay kéo theo sai lệch. Công cụ CLI khởi tạo project theo chuẩn boilerplate sẽ loại bỏ vấn đề đó.
**Task**: Viết script tự động nạp json config, từ đó tạo cây thư mục, ghi các tệp `.gitignore`, `requirements.txt` và `README` mặc định vô dự án đích.
**Constraints**: Hỗ trợ flag Dry-run (--dry-run) để in danh sách hành động mà không tạo file thực tế. Chú trọng validation check quyền ghi (write permission).
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

- **Libraries/Tools**: `cookiecutter`` và các framework chuẩn công nghiệp khác.

## 5. VALIDATION CRITERIA

- [ ] Successfully runs without producing `FileExistsError` if executed twice in a row.
- [ ] Outputs a modern `src/` layout format rather than dropping modules into the root (an anti-pattern).
- [ ] Correctly processes string inputs from `argparse`.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (Github Actions):** Add a subdirectory `.github/workflows/` and write a basic YAML template inside it `test.yml` that configures a Python CI matrix to run on GitHub out of the box.
2. **Extension 2 (Automated Initial Installation):** After writing the files, use the `subprocess` module to programmatically execute `python -m venv .venv` inside the new folder, [...].
3. **Extension 3 (Sub-process Git Init):** Immediately trigger `subprocess.run(['git', 'init'])` in the target directory to establish source control tracking inherently upon bootstrap.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`argparse`, `pathlib`).
