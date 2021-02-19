#!/usr/bin/env python3
from convert_bitcoin import get_current_bitcoin_prices, get_conversion_rate


def main() -> None:
    bitcoin_price = get_current_bitcoin_prices()
    usd_to_nzd_rate = get_conversion_rate()

    nzd_price = bitcoin_price.usd_price * usd_to_nzd_rate
    price_time = bitcoin_price.sample_date.isoformat()

    print(f"The price is ${nzd_price:.2f} at {price_time}")


if __name__ == "__main__":
    main()
