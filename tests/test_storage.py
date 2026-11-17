import tempfile
import unittest
from pathlib import Path

from finance import storage
from finance.models import Operation


class StorageTest(unittest.TestCase):
    def test_add_and_load(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "ops.json"
            storage.add(Operation("2026-11-01", "expense", "Продукты", 150000, "магазин"), path)
            storage.add(Operation("2026-11-02", "income", "Подработка", 500000), path)
            loaded = storage.load(path)
            self.assertEqual(len(loaded), 2)
            self.assertEqual(loaded[0].category, "Продукты")

    def test_wrong_amount(self):
        with self.assertRaises(ValueError):
            Operation("2026-11-01", "expense", "Продукты", 0)


if __name__ == "__main__":
    unittest.main()
