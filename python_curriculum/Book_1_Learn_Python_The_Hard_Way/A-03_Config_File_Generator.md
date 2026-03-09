# Exercise A-03: Config File Generator

## 1. EXERCISE BRIEF

**Context**: Every application needs configuration (databases, APIs, internal settings). These are often written in formats like `.ini`, `.env`, or `.yaml`. Teams frequently build CLI tools to bootstrap these configuration files for new environments or developers.
**Task**: Write a Python script that prompts the user for 5 inputs (host, port, db_name, username, password). Using these inputs, dynamically generate three different configuration files: a `.env` file, a `.ini` file, and a `.yml` file. Validate that critical fields (like host and db_name) are not left entirely empty.
**Constraints**: You **CANNOT** use the `yaml` or `configparser` libraries for generation. You must assemble the files purely using Python's multi-line strings (`"""`) and `f-strings`.

## 2. STARTER CODE

```python
def get_user_input() -> dict:
    """
    TODO: Use input() to ask the user for:
    DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS.
    Ensure HOST and NAME are not empty strings. Re-prompt if they are empty.
    Return a dictionary of the answers.
    """
    pass

def generate_env(config: dict) -> str:
    """
    TODO: Return a multi-line string in .env format (KEY=VALUE).
    """
    pass

def generate_ini(config: dict) -> str:
    """
    TODO: Return a multi-line string in .ini format under a [database] section.
    """
    pass

def generate_yaml(config: dict) -> str:
    """
    TODO: Return a multi-line string in YAML format.
    Ensure proper indentation and that numbers (like port) aren't quoted.
    """
    pass

if __name__ == "__main__":
    # Remove the mock config and call get_user_input() once your input function handles reprompting
    mock_config = {
        'host': 'localhost',
        'port': '5432',
        'name': 'myapp_db',
        'user': 'admin',
        'password': 'supersecret'
    }

    print("=== ENV ===")
    print(generate_env(mock_config))
    print("=== INI ===")
    print(generate_ini(mock_config))
    print("=== YAML ===")
    print(generate_yaml(mock_config))
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
For the user input, use a `while True` loop to ask for the host. If the length of the answered string is `0` or purely spaces, print an error and let the loop restart. Wait to `break` until validation passes.

**HINT-2 (Partial)**:
For formatting the files, multi-line `f-strings` keep the logic incredibly clean:

```python
def generate_env(config: dict) -> str:
    return f"""DATABASE_HOST={config['host']}
DATABASE_PORT={config['port']}
"""
```

**HINT-3 (Near-solution)**:

```python
def generate_yaml(config: dict) -> str:
    # Notice the 2-space indentation, critical for valid YAML
    return f"""database:
  host: "{config['host']}"
  port: {int(config['port'])}
  name: "{config['name']}"
  user: "{config['user']}"
  password: "{config['password']}"
"""
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: `configparser`, `PyYAML`, `pydantic-settings`, 12-factor CLI bootstrap tools (like `vue-cli` or `create-react-app`).
- **Why do it manually**: Relying heavily on package generation tools masks how the files are physically written. By writing raw string templates, you start to understand exactly where syntax constraints like YAML whitespace strictness kick in.

## 5. VALIDATION CRITERIA

- [ ] Validation loop re-prompts the user if an invalid/empty input is provided for `host`.
- [ ] `.env` file does not contain quotes or spaces around the `=` signs.
- [ ] `.ini` file correctly declares the `[database]` head section.
- [ ] `.yaml` file contains valid spacing (e.g., 2 spaces for properties nested under `database:`).
- [ ] Port is cast correctly to an integer in the yaml output.

## 6. EXTENSION CHALLENGES

1. **Extension 1 (File Saving):** Modify the script to actually save the strings into 3 separate files on disk: `config.env`, `config.ini`, and `config.yml`.
2. **Extension 2 (Base64 Encode):** The password is in raw text. Write logic to apply `base64` encoding to the password solely for the `.env` output, so the raw password isn't immediately readable by shoulder-surfers.
3. **Extension 3 (Template System):** Refactor the functions out completely. Store the string templates in a `templates/` folder as `.tpl` files with placeholders like `{{DB_HOST}}`. Read the file, use the `.replace()` method loops on the dictionary to inject the config, and spit it back out.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only.
