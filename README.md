# Куда пойти — Москва

Фронтенд для будущего сайта о самых интересных местах в Москве.

![&#x41A;&#x443;&#x434;&#x430; &#x43F;&#x43E;&#x439;&#x442;&#x438;](.gitbook/assets/site.png)

[Демка сайта](./pictures_guide/site.png).

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
