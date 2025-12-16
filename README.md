# 1. Клонировать репозиторий
git clone https://github.com/ваш-логин/Articles.git
# 2. Активировать окружение
# Linux/Mac:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate
# 3. Установить Django, psycopg2 для работы c PostgreSQL:
pip install django
pip install psycopg2-binary
# 4. Запустить сервер
python manage.py runserver
