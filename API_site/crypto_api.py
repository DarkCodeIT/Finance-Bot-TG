import aiohttp, asyncio
from icecream import ic

from tool_data.all_data import headers_api


async def get_crypto_price():
    ic("Parse crypto currency")
    async with aiohttp.ClientSession() as session:
        async with session.get(url="https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest", headers=headers_api) as response:

            data = await response.json()
            return data