import asyncio
from proxybroker import Broker


def show(proxies):
    while True:
        proxy = proxies.get()
        if proxy is None: break
        print('Found proxy: %s'% proxy)

asyncio.set_event_loop(asyncio.new_event_loop())
proxies = asyncio.Queue()
broker = Broker(proxies)
tasks = asyncio.gather(broker.find(types=['HTTP', 'HTTPS'], limit=10), show(proxies))

loop = asyncio.get_event_loop()
loop.run_until_complete(tasks)
