import io
import json

from aiohttp import web
# from PythonMLServicePattern.utils.web_helpers import get_form_data_parameter


async def handle_get_example_request(request):
    # для получения параметров из url запроса
    # например, такого: http://localhost:1111/api/example?param1=123
    # params = request.query
    # param1 = params.get('param1')
    # param2 = params.get('param2', 'default_value')

    # для получения параметров из json тела запроса:
    # data = await request.json()
    # param1 = data.get('param1')

    # для получения параметров и файлов из тела запроса в формате form-data
    # param1 = await get_form_data_parameter('param1', request)
    # file = await get_form_data_parameter('file', request)

    # тут любой код для обработки

    # Для формирования результата достаточно заполнить result в формате json-а
    result = {
        'param1': 'param1',
        'int_item': 34
    }

    result_json = json.dumps(result, ensure_ascii=False, indent=4)
    return web.Response(
        text=result_json,
        headers={'Access-Control-Allow-Origin': '*'},
        content_type='application/json'
    )
