import logging

from __init__ import __service_name__


# Создание и конфигурация глобального логгера
logger = logging.getLogger(__service_name__)
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи в файл
file_handler = logging.FileHandler('../app.log')
file_handler.setLevel(logging.DEBUG)

# Создание форматировщика
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавление обработчика
logger.addHandler(file_handler)
