"""A note taking app. The beginner code was written with AI"""

from pathlib import Path

NOTES_DIR = Path("notes")
NOTES_DIR.mkdir(exist_ok = True)

def create(title, content):
    (NOTES_DIR / f"{title}.md").write_text(content)
    print(f"Created {title}.md")

def list_notes():
    files = sorted(NOTES_DIR.glob("*.md"))
    if not files:
        print("No notes yet")
    for f in files:
        print(f.stem)

def read(title):
    print((NOTES_DIR / f"{title}.md").read_text())

def delete(title):
    (NOTES_DIR / f"{title}.md").unlink()
    print(f"Deleted {title}.md")