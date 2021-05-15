Приложение для учета доходов/расходов в рамках курса ПВП в МИФИ
Инструкция по запуску
```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py compilemessages
python manage.py runserver
```