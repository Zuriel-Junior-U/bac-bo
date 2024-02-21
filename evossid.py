import requests

import params


def gerar_evosessionid():
    headers = {
        'authority': 'launch.aleaplay.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'pt-BR,pt;q=0.9',
        'referer': 'https://estrelabet.com/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }

    dados_params = params.gerar_params()

    info_params = {
        'target': dados_params['target'],
        'timestamp': dados_params['timestamp'],
        'signature': dados_params['signature'],
    }

    response = requests.get('https://launch.aleaplay.com/display', params=info_params, headers=headers)

    jsessionid = response.history[2]

    cookies = jsessionid.headers['Set-Cookie'].split()
    evosessionid = cookies[0].replace(';', '')

    return evosessionid
