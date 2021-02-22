#!/usr/bin/env python3
from prices import get_current_bitcoin_prices, get_conversion_rate, get_tesla_price
import csv


def write_data_to_csv(date, bitcoin_usd, bitcoin_nzd, tesla) -> None:
    with open("bitcoin.csv", "+w", newline="") as csvfile:
        fieldnames = ["date", "bitcoin USD", "bitcoin NZD", "Tesla NZD"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow(
            {
                "date": date,
                "bitcoin USD": f"{bitcoin_usd:.2f}",
                "bitcoin NZD": f"{bitcoin_nzd:.2f}",
                "Tesla NZD": f"{tesla:.2f}",
            }
        )


def main() -> None:
    bitcoin_price = get_current_bitcoin_prices()
    usd_to_nzd_rate = get_conversion_rate()

    nzd_price = bitcoin_price.usd_price * usd_to_nzd_rate
    price_time = bitcoin_price.sample_date.isoformat()
    tesla_price = get_tesla_price() * usd_to_nzd_rate
    write_data_to_csv(price_time, bitcoin_price.usd_price, nzd_price, tesla_price)

    print(
        f"The price of bitcoin is ${nzd_price:.2f} at {price_time}. TLSA is ${tesla_price:.2f}"
    )


if __name__ == "__main__":
    main()
