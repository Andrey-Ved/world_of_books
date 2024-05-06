# World of books

### Python v3.10, [Django v4.1](https://docs.djangoproject.com/en/5.0/releases/4.1/), [Bootstrap v5.2](https://getbootstrap.com/docs/5.2/)

Пример простого веб-сайта написанный на Django с использованием Bootstrap.  
По материалам книги **Анатолия Постолита "Python, Django и Bootstrap для начинающих"**

### Установка

- Скопируйте файлы проекта.
- Создайте виртуальное окружение и установите зависимости.
```bash
$ python -m venv venv
$ source env/bin/activate
$ pip install -r requirements.txt
```

### Запуск

Перейдите в каталог джанго проекта
```bash
$ cd WorldOfBooks
```
Запустите сервер для разработки
```bash
$ python manage.py runserver
```

### Суперпользователь

Superuser в приложенной БД уже создан - имя asd, пароль asd

### Интерфейсы

- development - http://127.0.0.1:8000/
- admin site - http://127.0.0.1:8000/admin/
