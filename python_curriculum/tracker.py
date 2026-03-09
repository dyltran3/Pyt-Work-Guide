import json
import os
import sys
import argparse
from datetime import datetime
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# Path settings
HOME_DIR = Path.home()
DB_DIR = HOME_DIR / ".python-curriculum"
DB_FILE = DB_DIR / "progress.json"
CONFIG_FILE = Path(__file__).parent / "config.json"

console = Console()

def load_config():
    if not CONFIG_FILE.exists():
        console.print(f"[red]Error: config.json not found at {CONFIG_FILE}[/red]")
        sys.exit(1)
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def load_db():
    if not DB_FILE.exists():
        return {"exercises": {}, "last_activity": None, "streak": 0}
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_db(db):
    os.makedirs(DB_DIR, exist_ok=True)
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=4)

def update_streak(db):
    today = datetime.now().date().isoformat()
    last = db.get("last_activity")
    if last == today:
        return # already updated today
    
    if last:
        last_date = datetime.fromisoformat(last).date()
        delta = (datetime.now().date() - last_date).days
        if delta == 1:
            db["streak"] = db.get("streak", 0) + 1
        else:
            db["streak"] = 1
    else:
        db["streak"] = 1
        
    db["last_activity"] = today

def init_tracker():
    db = load_db()
    os.makedirs(DB_DIR, exist_ok=True)
    save_db(db)
    console.print(f"[green]Tracker initialized at {DB_FILE}[/green]")

def set_status(ex_id, status):
    status = status.upper()
    valid = ["TODO", "IN_PROGRESS", "DONE", "SKIPPED"]
    if status not in valid:
        console.print(f"[red]Invalid status. Must be one of: {', '.join(valid)}[/red]")
        return
        
    config = load_config()
    all_ex = {item["id"]: item for item in config.get("exercises", [])}
    if ex_id not in all_ex:
        console.print(f"[red]Exercise ID '{ex_id}' not found in config.[/red]")
        return
        
    db = load_db()
    
    if "exercises" not in db:
        db["exercises"] = {}
        
    if ex_id not in db["exercises"]:
        db["exercises"][ex_id] = {}
        
    db["exercises"][ex_id]["status"] = status
    db["exercises"][ex_id]["updated_at"] = datetime.now().isoformat()
    
    update_streak(db)
    save_db(db)
    console.print(f"[green]Successfully updated {ex_id} to {status}[/green]")

def show_dashboard():
    config = load_config()
    db = load_db()
    exercises = config.get("exercises", [])
    
    # Calculate stats
    total = len(exercises)
    done_count = sum(1 for e in exercises if db.get("exercises", {}).get(e["id"], {}).get("status") == "DONE")
    skipped_count = sum(1 for e in exercises if db.get("exercises", {}).get(e["id"], {}).get("status") == "SKIPPED")
    in_progress_count = sum(1 for e in exercises if db.get("exercises", {}).get(e["id"], {}).get("status") == "IN_PROGRESS")
    
    streak = db.get("streak", 0)
    
    # Header
    console.print(Panel(f"[bold blue]🐍 PYTHON MASTERY CURRICULUM[/bold blue]\n🔥 Streak: {streak} days | 🚀 Total: {total} | ✅ Done: {done_count} | 🏃 In Progress: {in_progress_count} | ⏭️ Skipped: {skipped_count}", expand=False))
    
    # Group by module/track
    modules = {}
    for ex in exercises:
        mod = ex.get("track", "General")
        if mod not in modules:
            modules[mod] = []
        modules[mod].append(ex)
        
    for mod, mod_exercises in modules.items():
        mod_total = len(mod_exercises)
        mod_done = sum(1 for e in mod_exercises if db.get("exercises", {}).get(e["id"], {}).get("status") == "DONE")
        
        console.print(f"\n[bold]{mod}[/bold] ({mod_done}/{mod_total})")
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=12)
        table.add_column("Title", min_width=30)
        table.add_column("Status", justify="center")
        
        for ex in mod_exercises:
            st = db.get("exercises", {}).get(ex["id"], {}).get("status", "TODO")
            status_str = {
                "TODO": "[dim]TODO[/dim]",
                "IN_PROGRESS": "[yellow]IN PROGRESS[/yellow]",
                "DONE": "[green]DONE[/green]",
                "SKIPPED": "[magenta]SKIPPED[/magenta]"
            }.get(st, st)
            
            table.add_row(ex["id"], ex["title"], status_str)
            
        console.print(table)

def export_report():
    config = load_config()
    db = load_db()
    exercises = config.get("exercises", [])
    
    report_path = DB_DIR / "progress_report.md"
    
    lines = [
        "# Python Mastery Curriculum - Progress Report",
        f"**Date Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Current Streak:** {db.get('streak', 0)} days",
        "",
        "## Summary",
        f"- Total Exercises: {len(exercises)}",
        f"- Completed: {sum(1 for e in exercises if db.get('exercises', {}).get(e['id'], {}).get('status') == 'DONE')}",
        "",
        "## Details",
        "| ID | Title | Track | Status | Updated At |",
        "|---|---|---|---|---|"
    ]
    
    for ex in exercises:
        ex_db = db.get("exercises", {}).get(ex["id"], {})
        st = ex_db.get("status", "TODO")
        updated = ex_db.get("updated_at", "-")
        if updated != "-":
            updated = updated[:10] # just date
        lines.append(f"| {ex['id']} | {ex['title']} | {ex.get('track', '')} | {st} | {updated} |")
        
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
        
    console.print(f"[green]Report exported to {report_path}[/green]")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python Curriculum Tracker")
    parser.add_argument("--init", action="store_true", help="Initialize tracker")
    parser.add_argument("--export", action="store_true", help="Export markdown report")
    parser.add_argument("action", nargs="?", choices=["done", "skip", "start", "reset"], help="Action to perform")
    parser.add_argument("exercise_id", nargs="?", help="Exercise ID")
    
    args = parser.parse_args()
    
    if args.init:
        init_tracker()
    elif args.export:
        export_report()
    elif args.action and args.exercise_id:
        status_map = {
            "done": "DONE",
            "skip": "SKIPPED",
            "start": "IN_PROGRESS",
            "reset": "TODO"
        }
        set_status(args.exercise_id, status_map[args.action])
    else:
        show_dashboard()
