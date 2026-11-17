"""Хранение операций в файле JSON."""
import json
from pathlib import Path

from .models import Operation

DEFAULT_PATH = Path("data") / "operations.json"


def load(path=DEFAULT_PATH):
    path = Path(path)
    if not path.exists():
        return []
    rows = json.loads(path.read_text(encoding="utf-8"))
    return [Operation(**row) for row in rows]


def save(operations, path=DEFAULT_PATH):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = [op.to_dict() for op in operations]
    path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")


def add(operation, path=DEFAULT_PATH):
    operations = load(path)
    operations.append(operation)
    save(operations, path)
    return operations
