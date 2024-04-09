from display import Display
from item import Item

class Shelf(Display):
    sizes = {'small': 4, 'medium': 8, 'large': 12}

    def __init__(self, name: str, size: str):
        super().__init__(name)

        if size in Shelf.sizes.keys():
            self.size = size
            self.slots = Shelf.sizes[size]
        else:
            raise ValueError('Invalid size. Valid sizes: small, medium, large')

    def details(self) -> dict:
        """
        Returns the details of the shelf.
        """

        item_list = [{'id': i.id, 'name': i.name, 'count': i.count, 'price': i.price, 'counter': i.counter} for i in self.items if len(self.items) > 0]
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'size': self.size,
            'slots': self.slots,
            'items': item_list
        }
