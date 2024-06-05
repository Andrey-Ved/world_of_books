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

### Суперпользователь

Superuser в приложенной БД уже создан - имя asd, пароль asd


### Запуск

Перейдите в каталог джанго проекта
```bash
$ cd WorldOfBooks
```
Запустите сервер для разработки
```bash
$ python manage.py runserver
```

### Запуск в Докере

Создание и запуск контейнеров:
```bash
$ docker-compose up
```
Остановка запущенных контейнеров:
```bash
$ docker-compose stop
```
Запуск остановленных контейнеров:
```bash
$ docker-compose start
```
