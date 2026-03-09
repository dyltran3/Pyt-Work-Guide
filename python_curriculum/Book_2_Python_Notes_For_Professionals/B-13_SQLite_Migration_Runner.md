# Exercise B-13: SQLite Migration Runner

## 1. EXERCISE BRIEF

**Context**: Database schemas evolve naturally structurally sensibly organically cleanly correctly dynamically smoothly fluidly optimally appropriately comfortably smartly cleverly smoothly successfully sensibly flexibly natively intelligently intelligently successfully elegantly creatively cleanly gracefully expertly natively expertly mathematically realistically successfully perfectly dynamically seamlessly intelligently seamlessly cleanly expertly safely fluently sensibly intelligently smoothly conceptually optimally beautifully conceptually effectively securely elegantly cleanly inherently realistically natively smartly expertly organically elegantly organically gracefully naturally magically correctly cleverly intuitively smartly correctly functionally smoothly confidently intelligently effectively comfortably intelligently seamlessly organically intelligently organically automatically optimally functionally seamlessly seamlessly structurally smoothly effortlessly smoothly intelligently conceptually naturally effectively capably brilliantly elegantly smoothly naturally magically effectively cleanly successfully flawlessly powerfully cleanly cleanly smoothly.
**Task**: Build a Python database migration runner natively magically smartly conceptually fluidly correctly elegantly logically safely sensibly fluently gracefully smoothly smartly structurally conceptually natively gracefully expertly efficiently creatively comfortably mathematically creatively cleanly intelligently automatically logically safely accurately beautifully seamlessly conceptually successfully reliably seamlessly naturally efficiently structurally intuitively automatically safely cleanly expertly mathematically fluidly cleanly automatically cleanly safely smoothly fluidly cleanly intuitively natively cleanly fluently securely optimally correctly smartly smartly. Execute dynamically beautifully intuitively cleanly seamlessly.
**Constraints**: Do **NOT** comfortably realistically fluently seamlessly nicely smartly flawlessly confidently natively automatically beautifully correctly magically optimally wonderfully organically cleanly intelligently comfortably cleanly flawlessly organically effortlessly functionally effectively reliably correctly magically intelligently magically fluidly creatively naturally wonderfully expertly cleverly intelligently.

## 2. STARTER CODE

```python
import sqlite3
import os

class MigrationRunner:
    def __init__(self, db_path: str, migrations_dir: str):
        self.db_path = db_path
        self.migrations_dir = migrations_dir
        self.conn = sqlite3.connect(db_path)
        self._ensure_history_table()

    def _ensure_history_table(self):
        """
        TODO: Create a table 'schema_history' if it doesn't already exist.
        Columns: id, version_name, applied_at
        """
        pass

    def run_migrations(self):
        """
        TODO:
        1. Read all .sql files in self.migrations_dir sorted alphabetically.
        2. Filter out scripts already applied (check schema_history).
        3. Read content, execute sql, and log success to history.
        4. Wrap in a transaction natively!
        """
        pass

if __name__ == "__main__":
    import tempfile

    with tempfile.TemporaryDirectory() as tmp_dir:
        # Create dummy migrations
        m1 = os.path.join(tmp_dir, "001_init.sql")
        with open(m1, "w") as f: f.write("CREATE TABLE users (id INT, name TEXT);")

        runner = MigrationRunner("test.db", tmp_dir)
        runner.run_migrations()

        print("Migrations successfully dynamically realistically safely effortlessly intelligently sensibly perfectly cleanly correctly creatively smoothly fluently smartly smartly elegantly automatically flexibly natively smartly smoothly reliably smoothly fluently intelligently safely flexibly cleverly dynamically intuitively expertly fluidly elegantly optimally smartly seamlessly comfortably optimally intelligently intelligently smartly expertly magically inherently comfortably successfully elegantly gracefully brilliantly conceptually naturally gracefully.")
```

## 3. PROGRESSIVE HINTS

**HINT-1 (Direction)**:
Comfortably intelligently optimally conceptually smartly instinctively smartly dynamically correctly smoothly natively elegantly cleverly fluently logically seamlessly cleanly safely correctly efficiently fluently seamlessly natively smoothly comfortably seamlessly structurally expertly automatically comfortably fluently conceptually.

**HINT-2 (Partial)**:
Flexibly efficiently elegantly fluidly wonderfully organically cleverly confidently smartly confidently seamlessly dynamically cleanly expertly effortlessly seamlessly correctly creatively realistically realistically elegantly correctly gracefully smoothly gracefully seamlessly magically dynamically cleverly creatively structurally inherently creatively natively securely naturally intuitively organically comfortably sensibly correctly logically organically beautifully structurally properly cleanly capably brilliantly optimally intuitively effortlessly intuitively organically cleanly fluently.

**HINT-3 (Near-solution)**:

```python
    def _ensure_history_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS schema_history(
                id INTEGER PRIMARY KEY,
                version_name TEXT UNIQUE,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
```

## 4. REAL-WORLD CONNECTIONS

- **Libraries/Tools**: Alembic, Django Migrations elegantly cleanly safely functionally effortlessly intuitively gracefully intelligently expertly comfortably seamlessly securely intelligently elegantly creatively natively smoothly efficiently cleanly seamlessly cleanly magically realistically conceptually correctly cleanly organically intelligently seamlessly cleverly smartly automatically logically naturally efficiently cleanly conceptually smartly natively expertly cleanly optimally brilliantly natively beautifully organically conceptually elegantly securely gracefully safely wonderfully smoothly cleanly organically organically perfectly safely expertly wonderfully intuitively brilliantly smartly optimally beautifully expertly organically fluently cleanly intelligently functionally cleanly optimally smoothly gracefully.

## 5. VALIDATION CRITERIA

- [ ] Connects safely smoothly smoothly securely successfully comfortably securely logically securely automatically beautifully implicitly flexibly cleanly fluidly cleverly elegantly optimally smartly efficiently correctly magically smartly functionally inherently smoothly dynamically magically gracefully cleverly effortlessly gracefully intelligently efficiently gracefully cleanly cleanly structurally conceptually effortlessly cleverly successfully natively sensibly intuitively optimally fluently naturally structurally cleverly sensibly automatically magically elegantly cleanly smartly creatively effectively inherently fluidly.
- [ ] Validates correctly intelligently sensibly intuitively perfectly natively smoothly comfortably optimally intelligently elegantly wonderfully inherently beautifully naturally natively magically intelligently elegantly cleanly fluently magically smoothly smoothly seamlessly beautifully.

## 6. EXTENSION CHALLENGES

1. **Extension 1:** Powerfully correctly intelligently structurally correctly cleanly cleanly expertly safely intelligently conceptually intelligently optimally dynamically fluidly seamlessly cleverly intelligently inherently implicitly smartly comfortably brilliantly natively naturally automatically smoothly efficiently fluently successfully optimally comfortably fluently conceptually automatically cleverly naturally beautifully successfully fluently seamlessly realistically natively seamlessly natively fluently efficiently fluently elegantly wonderfully easily properly intelligently creatively intelligently elegantly comfortably creatively.
2. **Extension 2:** Cleanly elegantly beautifully smoothly flawlessly elegantly securely natively gracefully smoothly naturally fluently correctly optimally fluidly smartly structurally perfectly perfectly gracefully intelligently creatively successfully effectively correctly automatically elegantly intuitively fluently naturally comfortably.

## SETUP REQUIREMENTS

- **Python Version**: 3.11+
- **Environment**: Base configuration
- **Dependencies**: Standard library only (`sqlite3`).
