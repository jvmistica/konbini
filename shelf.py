import uuid
from item import Item

class Shelf:
    sizes = {'small': 4, 'medium': 8, 'large': 12}

    def __init__(self, name: str, size: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.status = 'active'
        self.items = []

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

    def remove(self) -> dict:
        """
        Removes a shelf.
        """

        if self.status == 'inactive':
            return {
                'error': True,
                'error_message': 'Shelf is already inactive'
            }

        self.status = 'inactive'
        return {
            'error': False,
            'error_message': None
        }

    def add_item(self, item: Item) -> dict:
        """
        Adds an item to a shelf.
        """

        if item.counter:
            return {
                'error': True,
                'error_message': f'{item.name} is not a type of item that can be added to a shelf'
            }

        if self.slots == 0:
            return {
                'error': True,
                'error_message': 'Item cannot be added to the shelf, all slots are taken'
            }

        self.items.append(item)
        self.slots -= 1
        return {
            'error': False,
            'error_message': None
        }

    def replace_item(self, current_item: Item, new_item: Item) -> dict:
        """
        Replaces an item in a shelf.
        """

        for n, item in enumerate(self.items):
            if item == current_item:
                self.items[n] = new_item
                return {
                    'error': False,
                    'error_message': None
                }
                # return f'Discarded: {current_item.name}\nAdded: {new_item.name}'
        return {
            'error': True,
            'error_message': f'Item \'{current_item.name}\' does not exist'
        }

    def remove_item(self, item: Item) -> dict:
        """
        Removes an item from a shelf.
        """

        try:
            self.items.remove(item)
        except ValueError:
            return {
                'error': True,
                'error_message': f'Item \'{item.name}\' does not exist'
            }

        self.slots += 1
        return {
            'error': False,
            'error_message': None
        }
