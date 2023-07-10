Очень простой шаблон для экспериментов.

# Как добавить какой-нибудь предикт для модели?
1. Создаем обработчик в `handlers` по образу и подобию `example_handler.py`
2. Идем в `main.py` и привязываем новый обработчик к маршруту.
3. В обработчике пишем нашу реализацию, на выходе должен быть json, который будет ответом на запрос.

В помощь есть `logger` и `config_manager`, которые используются в `main.py` можно по аналогии и у себя использовать.

# Структура проекта

## handlers
- содержит пакеты с методом обработчиком входящего запроса;
- сам обработчик должен быть стандартной сигнатуры, имя можно любое;
- на вход принимает объект `request` их которого можно вытащить параметры (пример в комментах к `you_super_handler`)
- можно создавать свои обработчики, делать в них что угодно, главное изолировать их по `.py` файлам, чтобы потом не путаться
- при создании обработчика надо не забыть в `main.py` привязать его к API запросу.

## utils
- содержит `config_manager` и `logger`;
- можно добавлять еще дополнительные служебные вещи и хэлперы

## __init__.py
- хранит версию и имя сервиса, можно менять по своему усмотрению
- все это подхватывается в `info_handler.py`

## app.log
- создает `logger` из `utils`
- пишет туда логи
- находится в корне проекта

## config.ini
- конфиг сервиса, содержит общие параметры
- можно добавлять что захочется, получать их можно через `config_manager`

## main.py
- содержит запуск сервиса с установкой порта из конфига;
- содержит все API маршруты с привязанными обработчиками;
- подключен логгер, который сигнализирует об успешном запуске сервиса.