import asyncio, aiohttp
from datetime import date, timedelta

from tool_data.all_data import headers


async def get_cur(from_: str, to_: str) -> str:
    date_now = date.today()
    date_yesterday = date.today() - timedelta(days=1)

    async with aiohttp.ClientSession() as session:
        async with session.get(url=f"https://fxds-public-exchange-rates-api.oanda.com/cc-api/currencies?base={from_}&quote={to_}&data_type=general_currency_pair&start_date={date_yesterday}&end_date={date_now}",
                               headers=headers) as response:

            row_data = await response.json()
            data = row_data['response'][0]
            text = f"Currency from {data['base_currency']} to {data['quote_currency']}\nAVG={data['average_bid']}\nHigh={data['high_bid']}\nLow={data['low_bid']}"

            return text
