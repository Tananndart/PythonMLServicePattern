import json

from aiohttp import web


async def handle_example_request(request):
    # для получения параметров из запроса:
    # params = request.query
    # param1 = params.get('param1')
    # param2 = params.get('param2', 'default_value')

    # тут любой код для обработки

    # Для формирования результата достаточно заполнить result в формате json-а
    result = {
        'item': 'item1',
        'int_item': 34
    }

    result_json = json.dumps(result, ensure_ascii=False, indent=4)
    return web.Response(
        text=result_json,
        headers={'Access-Control-Allow-Origin': '*'},
        content_type='application/json'
    )
