"""Модель данных: одна финансовая операция."""
from dataclasses import dataclass, asdict

INCOME = "income"
EXPENSE = "expense"


@dataclass
class Operation:
    date: str        # ГГГГ-ММ-ДД
    kind: str        # income или expense
    category: str
    amount: int      # сумма в копейках
    note: str = ""

    def __post_init__(self):
        if self.kind not in (INCOME, EXPENSE):
            raise ValueError("тип операции: income или expense")
        if self.amount <= 0:
            raise ValueError("сумма должна быть больше нуля")

    def to_dict(self):
        return asdict(self)
