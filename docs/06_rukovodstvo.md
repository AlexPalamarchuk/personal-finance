# Этап 6. Внедрение. Руководство пользователя

Требуется Python 3.9 или новее. Установка дополнительных библиотек не нужна.

```
git clone <адрес репозитория>
cd personal-finance
python3 -m finance add income Зарплата 85000 --note "ноябрь"
python3 -m finance add expense Продукты 1250.50
python3 -m finance list
python3 -m finance balance
python3 -m finance report
python3 -m finance months
```

Пример с готовыми данными: `python3 demo.py`
