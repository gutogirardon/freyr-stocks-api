"""
Indexes Common Model
"""


class Indexes:
    """
    Indexes Definition
    """
    def __init__(self, ticker=None, name=None, last_price=None, change=None, per_cent_change=None, volume=None):
        """
        Only relevant world indices information

        :param ticker: 
        :param name: 
        :param last_price: 
        :param change: 
        :param per_cent_change: 
        :param volume:
        """
        self.ticker = ticker
        self.name = name
        self.last_price = last_price
        self.change = change
        self.per_cent_change = per_cent_change
        self.volume = volume

    def to_json(self):
        """
        :return: data class in a json
        """
        return {
            'ticker': self.ticker, 'name': self.name, 'last_price': self.last_price,
            'change': self.change, 'per_cent_change': self.per_cent_change, 'volume': self.volume
        }


