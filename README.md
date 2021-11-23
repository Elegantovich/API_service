# api_final
### Описание
APi сервис предоставления информация с проекта 'Yatube'
### Технологии
Python 3.9.6, Django RF 3.12.4
### Запуск проекта dev-режиме
- Установите и запустите виртуальное окружение
```
python -m venv venv 
source venv/Scripts/activate
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- Проведите создание новых миграций
``` 
python manage.py makemigrations
``` 
- Проведите миграции
``` 
python manage.py migrate
``` 
- В папке с файлом manage.py выполните команду:
```
python3 manage.py runserver
