import requests


class UpdateExchangeRateJson:
    def __init__(self):
        self.update()

    def update(self):
        check_response_rates = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur.json")
        new_exchange_rates = check_response_rates.json()
        file_path = "./exchange_rate_new/new_exchange_rates.json"
        try:
            f = open(file_path)
            f.close()
        except FileNotFoundError:
            f = open(file_path, "x")
            f.close()
        finally:
            self.write_file(file_path, str(new_exchange_rates).replace('\'', '"'))

    def write_file(self, file_path, item):
        f = open(file_path, "w")
        f.write(item)
        f.close()

