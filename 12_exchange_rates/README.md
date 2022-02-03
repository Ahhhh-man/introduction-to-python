# Exchange Rate Parser

### The functional code
```python
import json


class ExchangeRateParser:
    def __init__(self, currency):
        self.currency = currency
        try:
            json_file = open('./exchange_rate/exchange_rates.json')
            self.data = json.load(json_file)
            self.rates_dict = self.data['rates']
            if not self.valid_currency():
                print('Invalid Currency')
            else:
                self.print_rates()
        except FileNotFoundError:  # If file error execute following
            print("Json file not found")

    def print_rates(self):
        if self.valid_currency():
            print(f'{self.currency} exchange rate is {self.rates_dict[self.currency]}')

    def valid_currency(self):
        return True if self.currency in self.rates_dict.keys() else False
```
### The main.py
```python
from exchange_rate.exchange_rate_paser import ExchangeRateParser

ExchangeRateParser(input('What currency? ').upper())
```
### Json file 
```json
{
  "base": "EUR",
  "date": "2017-07-26",
  "rates": {
	"AUD": 1.4717,
	"BGN": 1.9558,
	"BRL": 3.6806,
	"CAD": 1.4576,
	"CHF": 1.1152,
	"CNY": 7.8646,
	"CZK": 26.047,
	"DKK": 7.4368,
	"GBP": 0.89275,
	"HKD": 9.0959,
	"HRK": 7.4128,
	"HUF": 305.57,
	"IDR": 15507.0,
	"ILS": 4.1569,
	"INR": 74.938,
	"JPY": 130.26,
	"KRW": 1303.9,
	"MXN": 20.664,
	"MYR": 4.9889,
	"NOK": 9.2893,
	"NZD": 1.5678,
	"PHP": 58.948,
	"PLN": 4.2613,
	"RON": 4.5632,
	"RUB": 69.705,
	"SEK": 9.5705,
	"SGD": 1.585,
	"THB": 38.996,
	"TRY": 4.1406,
	"USD": 1.1644,
	"ZAR": 15.2
  }
}
```

The exchange API uses the same code but with the json file overwritten. But in order to maintain old code, I have just created new files, appropriately extended name with new.
