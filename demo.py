"""Заполняет файл данных примером и показывает отчёты."""
from finance import storage
from finance.cli import main
from finance.models import Operation

PATH = "data/demo.json"
ROWS = [
    ("2026-10-05", "income", "Зарплата", 85000, "октябрь"),
    ("2026-10-06", "expense", "Жильё", 28000, "аренда"),
    ("2026-10-12", "expense", "Продукты", 14350.50, ""),
    ("2026-10-20", "expense", "Транспорт", 3200, "проездной"),
    ("2026-11-05", "income", "Зарплата", 85000, "ноябрь"),
    ("2026-11-06", "expense", "Жильё", 28000, "аренда"),
    ("2026-11-10", "expense", "Продукты", 12870, ""),
    ("2026-11-15", "expense", "Досуг", 4500, "кино, кафе"),
]
storage.save([Operation(d, k, c, round(a * 100), n) for d, k, c, a, n in ROWS], PATH)
for command in ("balance", "report", "months"):
    print(f"--- {command} ---")
    main(["--file", PATH, command])
