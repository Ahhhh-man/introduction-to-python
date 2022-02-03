from exchange_rate.exchange_rate_paser import ExchangeRateParser
from exchange_rate_new.exchange_rates_parser_new import NewExchangeRateParser

# ExchangeRateParser(input('What currency? ').upper())      # Old static exchange rate
NewExchangeRateParser(input('What currency? '))             # New dynamic exchange rate


