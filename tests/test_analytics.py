import unittest

from finance import analytics
from finance.models import Operation

OPS = [
    Operation("2026-10-05", "income", "Зарплата", 8500000),
    Operation("2026-10-06", "expense", "Жильё", 2800000),
    Operation("2026-10-12", "expense", "Продукты", 1200000),
    Operation("2026-11-05", "income", "Зарплата", 8500000),
    Operation("2026-11-10", "expense", "Продукты", 1000000),
]


class AnalyticsTest(unittest.TestCase):
    def test_balance(self):
        self.assertEqual(analytics.balance(OPS), 12000000)

    def test_expenses_by_category(self):
        rows = analytics.expenses_by_category(OPS)
        self.assertEqual(rows[0], ("Жильё", 2800000, 56.0))
        self.assertEqual(rows[1], ("Продукты", 2200000, 44.0))

    def test_by_month(self):
        months = analytics.by_month(OPS)
        self.assertEqual(months["2026-10"], (8500000, 4000000, 4500000))
        self.assertEqual(months["2026-11"], (8500000, 1000000, 7500000))


if __name__ == "__main__":
    unittest.main()
