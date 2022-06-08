import aiohttp
import asyncio


async def get_url(url):
    print(f'read {url}')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            with open(f'{url[-1:]}.txt', "w", encoding='utf-8') as file:
                file.write(data)
                print(f'write {url}')


URLS = ['http://127.0.0.1:8001/category/3', 'http://127.0.0.1:8001/category/5']

future_urls = [get_url(url) for url in URLS]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(future_urls))
