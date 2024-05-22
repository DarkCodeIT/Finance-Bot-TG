from dotenv import load_dotenv
import os


load_dotenv()

crypto_news = "https://ru.investing.com/news/cryptocurrency-news/1"
fond_news = "https://ru.investing.com/news/stock-market-news/1"
forex_news = "https://ru.investing.com/analysis/forex/1"
stategy_news = "https://ru.tradingview.com/scripts/page-2/?script_type=strategies" # Need VPN
analytict_news = "https://ru.tradingview.com/news/market-analysis/?section=analysis"


kurs_valut = "https://www.oanda.com/currency-converter/ru/?from=GBP&to=RUB&amount=1" # API not free
kurs_crypto = "https://coinmarketcap.com/ru/" #have API
# kurs_crypto2 = "https://www.coingecko.com/" #have_API not free

# to connect out sites
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
}

headers_api = {
    "Accepts" : "application/json",
    "X-CMC_PRO_API_KEY" : f"{os.getenv('api_crypto')}"
}

# data for pagination
currencys = ["KWD", "BHD", "OMR", "JOD", "GBR", "KYD", "CHF", "EUR", "USD", "CAD",
             "RUB", "KZT", "JPY", "AUD", "CNH", "CNY", "INR", "AED", "EGP", "BMD"]
