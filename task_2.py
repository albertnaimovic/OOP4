# Task Nr.2:

# Create a class Currency that has the following properties:

# code: A 3-letter currency code (e.g. "USD", "EUR", "GBP")
# amount
# exchange_rate
# Create the following methods:

# set_code: A method that accepts a 3-letter currency code and sets the code attribute of the object
# set_amount: A method that accepts a float number and sets the amount attribute of the object
# set_exchange_rate: A method that accepts a float number and sets the exchange_rate attribute of the object
# convert: A method that accepts a 3-letter currency code and a float number representing the new exchange rate,
# and calculates the new amount of currency based on the exchange rate.
# str: A method that returns a string representation of the Currency object in the following format "code: amount"
# Each method should return the instance of the class to allow method chaining.


from typing import Union


class Currency:
    def __init__(self) -> None:
        self.code = None
        self.amount = None
        self.exchange_rate = None
        self.prev_code = None

    def set_code(self, code: str) -> "Currency":
        self.code = code
        return self

    def set_amount(self, amount: float) -> "Currency":
        self.amount = amount
        return self

    def set_exchange_rate(self, exchange_rate: float) -> "Currency":
        self.exchange_rate = exchange_rate
        return self

    def convert(self, new_code: str, new_exchange_rate: float) -> Union[str, float]:
        self.amount = self.amount * new_exchange_rate
        self.prev_code = self.code
        self.code = new_code
        self.exchange_rate = new_exchange_rate
        return self.amount, self.code, self.exchange_rate

    def __str__(self) -> str:
        return f"Converted from {self.prev_code} to {self.code}: {self.amount}"


currency = Currency()

currency.set_code("EUR").set_amount(1000.0)
currency.convert(new_code="USD", new_exchange_rate=1.2)
print(currency)
