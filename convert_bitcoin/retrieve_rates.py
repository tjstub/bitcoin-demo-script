import requests
from dataclasses import dataclass
from datetime import datetime
from dateutil.parser import parse


@dataclass
class BitcoinData:
    usd_price: float
    sample_date: datetime


# we could also pass in NZD to get NZD price. But that's not the exercise here
bitcoin_api_url = "https://api.coindesk.com/v1/bpi/currentprice/USD.json"
# Currency conversion Rate API, hosted by EU bank
currency_rate_url = "https://api.exchangeratesapi.io/latest?base=USD"


def get_current_bitcoin_prices() -> BitcoinData:
    """Gets the bitcoin price and date of price."""
    price_result = requests.get(bitcoin_api_url)
    if price_result.status_code != 200:
        raise RuntimeError("Request to API failed!")

    price_json = price_result.json()

    return BitcoinData(
        price_json["bpi"]["USD"]["rate_float"], parse(price_json["time"]["updated"])
    )


def get_conversion_rate() -> float:
    """retrieves the rate of USD-to-NZD"""
    conversion_rates_result = requests.get(currency_rate_url)
    if conversion_rates_result.status_code != 200:
        raise RuntimeError("Failed to get currency exchange!")

    rates_json = conversion_rates_result.json()

    # return the USD-to-NZD rate
    return rates_json["rates"]["NZD"]