import json
import uuid

class Item:
    def __init__(self, name, count, price, counter):
        self.id = str(uuid.uuid4())
        self.name = name
        self.count = count
        self.price = price
        self.counter = counter

    def details(self):
        """
        Returns the details of the item.
        """

        details = {
            'id': self.id,
            'name': self.name,
            'count': self.count,
            'price': self.price,
            'counter': self.counter
        }
        return json.dumps(details)

    def sell(self, count):
        """
        Sells an item.
        """

        self.count -= count
        return f'{self.name}\'s count has decreased to {self.count}'

    def restock(self, count):
        """
        Re-stocks an item.
        """

        self.count += count
        return f'{self.name}\'s count has increased to {self.count}'

    def update_price(self, new_price):
        """
        Updates the price of an item.
        """

        self.price = new_price
        return f'{self.name}\'s price is now {self.price}'

    def remove(self):
        """
        Removes an item.
        """

        self.count = 0
        return f'{self.name} has been removed from the inventory'
