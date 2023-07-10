""" Функции для получения данных из конфигурационного файла. """
import inspect
import os

from dynaconf import Dynaconf

_file_name = inspect.getfile(inspect.currentframe())

config = os.path.join(os.path.dirname(__file__), '../config.ini')
settings = Dynaconf(settings_files=['config.ini'])


def get_param(param_name):
    return settings.get(param_name)


def get_param_or_default(param_name, default_value=None):
    return settings.get(param_name, default=default_value)
