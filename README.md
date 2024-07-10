
Тестовое задание отдел бэкенд Сарафан - веб-сервис на базе Django.

1.	numeric_elements.py - реализован алгоритм, который выводит n первых элементов последовательности 122333444455555… (число повторяется столько раз, чему оно равно).

2.	Реализовать Django проект магазина продуктов со следующим функционалом:
   
•	Ссоздания, редактирования, удаления категорий и подкатегорий товаров в админке.

•	Категории и подкатегории обязательные поля: наименование, slug-имя, изображение.

•	Подкатегории связаны с родительской категорией.

•	Рреализован эндпоинт для просмотра всех категорий с подкатегориями.

•	Реализована возможность добавления, изменения, удаления продуктов в админке.

•	Реализован эндпоинт вывода продуктов. Каждый продукт в выводе имеет поля: наименование, slug, категория, подкатегория, цена, список изображений.

•	Реализован эндпоинт добавления, изменения (изменение количества), удаления продукта в корзине.

•	Реализован эндпоинт вывода состава корзины с подсчетом количества товаров и суммы стоимости товаров в корзине.

•	Реализована возможность полной очистки корзины.

•	Операции по эндпоинтам категорий и продуктов может осуществлять любой пользователь.

•	Операции по эндпоинтам корзины может осуществлять только авторизированный пользователь и только со своей корзиной.

•	Реализована пагинация на уровне проекта.

•	Реализована авторизация по токену.

•	Представлена документация в формате Swagger и Redoc.

## Технологии
Django REST framework, Drf-yasg


## Запуск проекта локально:
Клонировать репозиторий:
```
git clone https://github.com/MochalovaES/test_SARAFAN
```
Создать и активировать виртуальное окружение:
```
python -m venv venv
Linux/macOS: source env/bin/activate
windows: source env/scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
pip install -r backend/requirements.txt
```
Создать и заполнить файл .env:

Выполнить миграции:
```
python manage.py migrate
```
Создать суперпользователя:
```
python manage.py csu
```
Запустить проект:
```
python manage.py runserver
```

Просмотр документации
Swagger
http://localhost:8000/docs/

Redoc
http://localhost:8000/redoc/