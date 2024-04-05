import uuid

class Item:
    def __init__(self, name: str, count: int, price: float, counter: bool):
        self.id = str(uuid.uuid4())
        self.name = name
        self.count = count
        self.price = price
        self.counter = counter
        self.min_restock = 20

    def details(self) -> str:
        """
        Returns the details of the item.
        """

        return {
            'id': self.id,
            'name': self.name,
            'count': self.count,
            'price': self.price,
            'counter': self.counter
        }

    def sell(self, count: int) -> str:
        """
        Sells an item.
        """

        if self.count < count:
            return {
                'error': True,
                'error_message': f'Cannot sell {count} amount of items, remaining stock: {self.count}'
            }

        self.count -= count
        return {
            'error': False,
            'error_message': None
        }

    def restock(self, count: int) -> str:
        """
        Re-stocks an item.
        """

        if count < self.min_restock:
            return {
                'error': True,
                'error_message': f'Cannot re-stock {count} amount of items, minimum re-stock value: {self.min_restock}'
            }

        self.count += count
        return {
            'error': False,
            'error_message': None
        }

    def update_price(self, new_price: float) -> str:
        """
        Updates the price of an item.
        """

        self.price = new_price
        return {
            'error': False,
            'error_message': None
        }

    def remove(self) -> str:
        """
        Removes an item.
        """

        if self.count == 0:
            return {
                'error': True,
                'error_message': 'Cannot remove item, amount is already zero'
            }

        self.count = 0
        return {
            'error': False,
            'error_message': None
        }
