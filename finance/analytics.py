"""Анализ операций: баланс, категории, месяцы."""
from collections import defaultdict

from .models import INCOME, EXPENSE


def total(operations, kind):
    return sum(op.amount for op in operations if op.kind == kind)


def balance(operations):
    return total(operations, INCOME) - total(operations, EXPENSE)


def expenses_by_category(operations):
    """Список (категория, сумма, доля в процентах) по убыванию суммы."""
    sums = defaultdict(int)
    for op in operations:
        if op.kind == EXPENSE:
            sums[op.category] += op.amount
    whole = sum(sums.values())
    rows = [(cat, value, round(value * 100 / whole, 1)) for cat, value in sums.items()]
    return sorted(rows, key=lambda row: -row[1])


def by_month(operations):
    """Словарь: месяц -> (доходы, расходы, остаток)."""
    months = defaultdict(lambda: [0, 0])
    for op in operations:
        index = 0 if op.kind == INCOME else 1
        months[op.date[:7]][index] += op.amount
    return {m: (inc, exp, inc - exp) for m, (inc, exp) in sorted(months.items())}
