from forex_python.converter import CurrencyRates


class Currency():
    def __init__(self, currency):
        self.currency = currency


    def return_currency_to_USD(self):
        c = CurrencyRates()
        return c.get_rate("USD", self.currency)
