"""Интерфейс командной строки программы «Личные финансы»."""
import argparse
from datetime import date

from . import analytics, storage
from .models import Operation, INCOME


def rub(kopecks):
    return f"{kopecks / 100:,.2f}".replace(",", " ") + " руб."


def main(argv=None):
    parser = argparse.ArgumentParser(prog="finance", description="Учёт и анализ личных финансов")
    parser.add_argument("--file", default=str(storage.DEFAULT_PATH), help="файл с данными")
    sub = parser.add_subparsers(dest="command", required=True)
    add = sub.add_parser("add", help="добавить операцию")
    add.add_argument("kind", choices=["income", "expense"])
    add.add_argument("category")
    add.add_argument("amount", type=float, help="сумма в рублях")
    add.add_argument("--date", default=date.today().isoformat())
    add.add_argument("--note", default="")
    for name, text in (("list", "список операций"), ("balance", "баланс"),
                       ("report", "расходы по категориям"), ("months", "итоги по месяцам")):
        sub.add_parser(name, help=text)
    args = parser.parse_args(argv)

    if args.command == "add":
        op = Operation(args.date, args.kind, args.category, round(args.amount * 100), args.note)
        storage.add(op, args.file)
        print("Операция добавлена:", op.date, op.category, rub(op.amount))
        return
    operations = storage.load(args.file)
    if args.command == "list":
        for op in operations:
            sign = "+" if op.kind == INCOME else "-"
            print(f"{op.date}  {sign}{rub(op.amount):>16}  {op.category:<12} {op.note}")
    elif args.command == "balance":
        print("Доходы: ", rub(analytics.total(operations, "income")))
        print("Расходы:", rub(analytics.total(operations, "expense")))
        print("Баланс: ", rub(analytics.balance(operations)))
    elif args.command == "report":
        for category, value, share in analytics.expenses_by_category(operations):
            print(f"{category:<12} {rub(value):>16}  {share:>5}%")
    elif args.command == "months":
        for month, (inc, exp, rest) in analytics.by_month(operations).items():
            print(f"{month}  доходы {rub(inc)}  расходы {rub(exp)}  остаток {rub(rest)}")
