import urllib.parse
import json

import requests

import login


def gerar_params():
    params = {
        'gameSymbol': 'alea_evl7617', # codigo do bac-bo
        'language': 'pt',
    }

    response = requests.get(
        'https://service.estrelabet.com//ajax/launcher/getRealGames',
        params=params,
        cookies=login.logar(),
    )

    url = urllib.parse.urlparse(json.loads(response.content)['gameDetails']['url'])
    params = urllib.parse.parse_qs(url.query)

    target = params.get('target')[0]
    timestamp = params.get('timestamp')[0]
    signature = params.get('signature')[0]

    return {'target': target, 'timestamp': timestamp, 'signature': signature}

