import requests
from bs4 import BeautifulSoup


class CurrencyConverter:
    def __init__(self):
        self.url = "https://ru.investing.com/central-banks/federal-reserve"

    def convert(self, amount, from_currency, to_currency):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        currency_table = soup.find("table", {"id": "exchangeRates"})

        if currency_table is None:
            return "Не удалось найти таблицу с курсами валют."


        rows = currency_table.find_all("tr")


        currency_rates = {}


        for row in rows:
            cols = row.find_all("td")
            if len(cols) == 2:
                currency = cols[0].text.strip()
                rate = cols[1].text.strip()
                currency_rates[currency] = rate

        if from_currency not in currency_rates or to_currency not in currency_rates:
            return "Не удалось найти курсы для указанных валют."

        from_rate = float(currency_rates[from_currency].replace(",", "."))
        to_rate = float(currency_rates[to_currency].replace(",", "."))
        converted_amount = amount * (to_rate / from_rate)
        return converted_amount



converter = CurrencyConverter()

from_currency = input("Введите код валюты вашей страны: ").strip().upper()
amount = float(input(f"Введите количество {from_currency}: "))

to_currency = "USD"

result = converter.convert(amount, from_currency, to_currency)
print(f"{amount} {from_currency} = {result} {to_currency}")
