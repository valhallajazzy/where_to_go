# Куда пойти — Москва

Фронтенд для будущего сайта о самых интересных местах в Москве.

![Screenshot](https://github.com/valhallajazzy/where_to_go/blob/main/pictures_guide/site.png)

[Демка сайта](https://valhallajazzy.pythonanywhere.com/)  
[Админ-панель сайта](https://valhallajazzy.pythonanywhere.com/admin/)

## Как запустить
* Скачайте код
* Установите зависимости в корневой директории проекта и активируйте их
```console
$ poetry install
$ poetry shell
```
* Создайте файл .env в корневой директории проекта и укажите переменные окружения
![Screenshot](./pictures_guide/env_файл_where_to_go.png)
![Screenshot](./pictures_guide/vatiables.png)

* Проведите миграции
```console
$ python manage.py makemigrations
$ python manage.py migrate
```
* Запустите сервер
```console
$ python manage.py runserver
```

## Добавить локации
* В терминале пропишите команду
```console
$ python manage.py load_place "Ваш url к json файлу"
```

Пример JSON-файла
![Screenshot](./pictures_guide/Снимок экрана от 2023-11-01 01-03-08.png)
