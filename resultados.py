import asyncio
import json

import websockets

import evossid


async def entrar_wss_bacbo(evosessionid):
    url = f'wss://aleaplay.evo-games.com/public/bacbo/player/game/BacBo00000000001/socket?messageFormat=json&{evosessionid}'

    async with websockets.connect(url, extra_headers={
        'Pragma': 'no-cache',
        'Origin': 'https://aleaplay.evo-games.com',
        'Accept-Language': 'pt-BR,pt;q=0.9',
        'Sec-WebSocket-Key': 'ttIer1T0J1u6LR+X/xqLkg==',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Upgrade': 'websocket',
        'Cache-Control': 'no-cache',
        'Connection': 'Upgrade',
        'Sec-WebSocket-Version': '13',
        'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits'
    }) as websocket:
        while True:
            try:
                mensagem = json.loads(await websocket.recv())
                if mensagem['type'] == 'bacbo.road':
                    resultado = mensagem['args']['history'][-1]
                    print('-' *20)
                    print(f'Player: {resultado['playerScore']} - Banker: {resultado['bankerScore']}')
                    print(f'Vencedor: {resultado['winner']}')
                    print('-' * 20)
            except Exception as error:
                print(error)


async def main():
    evosessionid = evossid.gerar_evosessionid()
    await entrar_wss_bacbo(evosessionid)

if __name__ == '__main__':
    asyncio.run(main())
