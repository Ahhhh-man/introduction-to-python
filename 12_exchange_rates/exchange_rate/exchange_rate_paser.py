import json


class ExchangeRateParser:
    def __init__(self, currency):
        self.currency = currency
        try:
            json_file = open('./exchange_rate/exchange_rates.json')
            self.data = json.load(json_file)
            self.rates_dict = self.data['rates']
            if not self.is_valid_currency():
                print('Invalid Currency')
            else:
                self.print_rates()
        except FileNotFoundError:  # If file error execute following
            print("Json file not found")

    def print_rates(self):
        print(f'{self.currency} exchange rate is {self.rates_dict[self.currency]}')

    def is_valid_currency(self):
        return True if self.currency in self.rates_dict.keys() else False

