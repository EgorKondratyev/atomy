# Atomy telegram bot
![aiogram](https://img.shields.io/badge/telegram-aiogram-blue)
![aiogram](https://img.shields.io/badge/license-MIT-green)
![aiogram](https://img.shields.io/badge/python-3.7|3.8|3.9|3.10-blue)
![aiogram](https://img.shields.io/badge/TelegramBotApi-6.4-blue)
![aiogram](https://img.shields.io/badge/languge-RUS/EN-yellow)

## О боте
Данный бот разработан для компании продвижения продуктов Atomy, а также вовлечения большего числа людей в данную компанию.
Однако данный бот является полностью динамическим (за исключением расширяемости кнопок), за счет этого его можно использовать в любых целях.
В данном боте можно изменить любой текст будь то кнопка или какое-то предложение, но при этом расширить данного бота нельзя. Также к любому, абсолютно любому предложению в данном боте возможно прикрепить фотографию.
Данный бот обладает админ-панелью фреймворка Django. Данный бот доступен в двух языках RUS/EN

## Первый запуск
Установим для начала все необходимые пакеты:
```
pip install Django
pip install Pillow
pip install PyYAML
pip install aiogram
pip install python-dotenv
```
Настроим переменные окружения (.env)
```
TOKEN='Токен бота телеграм'
PATH_SQLITE3 = 'Путь, где будет лежать SQLite'
ADMIN=Ваш ID телеграм (если ID несколько, то записываем через запятую)
```
Настроить пути также log - create_logger

Выполним миграцию (cmd):
```commandline
cd /Путь/До/Бота
<source venv/bin/activate> linux | <venv\Scripts\activate> windows
cd beget_tech
python manage.py makemigrations
python manage.py migrate
```
После этого запускаем бота.

Вся инициализация предложений/кнопок происходит при старте бота.
