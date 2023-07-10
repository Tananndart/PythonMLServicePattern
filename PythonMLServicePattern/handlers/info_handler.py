import json

from aiohttp import web
from __init__ import __version__, __service_name__


async def handle_info_request(request):
    service_info = {
        'state': f'{__service_name__} is running',
        'version': __version__
    }

    json_info = json.dumps(service_info, ensure_ascii=False, indent=4)
    return web.Response(
        text=json_info,
        headers={'Access-Control-Allow-Origin': '*'},
        content_type='application/json'
    )
