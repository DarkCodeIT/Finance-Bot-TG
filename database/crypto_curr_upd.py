import pymongo, asyncio
from icecream import ic

from API_site import crypto_api

async def update_crypto_curr() -> None:

    client = pymongo.MongoClient("localhost", 27017)
    db = client.financebot
    collection = db.crypto_currency
    collection.delet_many({})

    data = await crypto_api.get_crypto_price()
    ic("Update crypto currency in Mongo")

    upd_data = []
    for item in data['data']:
        upd_data.append({'name': item['name'], 'symbol' : item['symbol'],
                         'price' : item['quote']['USD']['price'],
                         'volume_change_24h' : item['quote']['USD']['volume_change_24h'],
                         'percent_change_24h' : item['quote']['USD']['percent_change_24h']})

    collection.insert_many(upd_data)


