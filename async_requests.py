import asyncio
import aiohttp
import aiofiles


async def main(url):
    # for url in urls:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(response.status)
            content = await response.text()
        async with aiofiles.open(f'downloaded_pages/products{url.split("/")[-1]}.txt', mode='w', encoding='UTF-8') as f:
            await f.write(content)
                

URLS = ['http://127.0.0.1:8000/products/','http://127.0.0.1:8000/products/1', 'http://127.0.0.1:8000/products/2', 'http://127.0.0.1:8000/products/3']
# asyncio.run(main(URLS))
futures = [main(url) for url in URLS]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))