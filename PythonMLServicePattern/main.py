from handlers.info_handler import handle_info_request
from handlers.example_handler import handle_example_request
from utils import config_manager as config

from aiohttp import web
from utils.logger import logger


if __name__ == '__main__':
    # создание сервиса
    app = web.Application()

    # для добавления нового метода API достаточно указать формат запроса, маршрут и обработчик
    # - формат запроса, это add_get, add_post и т.д. Можно для тестов просто GET пользоваться
    # - маршрут, тут все стандартно. Разве что не забывай, что наличие `/` тоже часть пути. Т.е. /super/ и /super
    #   это разные маршруты. Я обычно всегда в конце `/` не ставлю, чтобы было единообразно
    # - обработчик, это просто асинхронная функция в пакете handlers. Можно создавать свои и делать в них что угодно.
    app.router.add_get('/', handle_info_request)
    app.router.add_get('/api/example', handle_example_request)

    # В конфиге пока только порт, но можно легко добавлять другие параметры и получать их аналогичным способом
    # конфиг можно импортировать в любой пакет аналогично импорту в этом пакете
    port = config.get_param('port')

    # логгер один и универсальный, по умолчанию создает файл прямо в корне app.log
    # можно помимо info использовать warning, error, debug области
    # как импортируется см. выше, в других пакетах можно также
    logger.info('Service started at port %s', port)

    # старт сервиса
    web.run_app(app, port=port)
