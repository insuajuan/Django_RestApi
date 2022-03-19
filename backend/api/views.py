from urllib import request
from django.http import JsonResponse
import json


def api_home(req, *args, **kwargs):
    body = req.body # byte string of JSON data  
    data = dict()
    try:
        data = json.loads(body)
    except:
        pass
    data['headers'] = dict(req.headers)
    data['params'] = dict(req.GET)
    return JsonResponse(data)
