import json
import uuid
from item import Item

class Shelf:
    sizes = {'small': 4, 'medium': 8, 'large': 12}

    def __init__(self, name, size):
        self.id = str(uuid.uuid4())
        self.name = name
        self.status = 'active'
        self.items = []

        if size in Shelf.sizes.keys():
            self.size = size
            self.slots = Shelf.sizes[size]
        else:
            raise ValueError('Invalid size. Valid sizes: small, medium, large')

    def details(self):
        """
        Returns the details of the shelf.
        """

        item_list = [{'id': i.id, 'name': i.name, 'count': i.count, 'price': i.price, 'counter': i.counter} for i in self.items if len(self.items) > 0]
        details = {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'size': self.size,
            'slots': self.slots,
            'items': item_list
        }
        return json.dumps(details)

    def remove(self):
        """
        Removes a shelf.
        """

        self.status = 'inactive'
        return f'{self.name} has been removed from the display'

    def add_item(self, item):
        """
        Adds an item to a shelf.
        """

        if item.counter:
            return f'{item.name} is not a type of item that can be added to a shelf'

        if self.slots == 0:
            return 'Item cannot be added to the shelf, all slots are taken'

        self.items.append(item)
        self.slots -= 1
        return 'Item has been added to the shelf'

    def replace_item(self, current_item, new_item):
        """
        Replaces an item in a shelf.
        """

        for n, item in enumerate(self.items):
            if item == current_item:
                self.items[n] = new_item
                return f'Discarded: {current_item.name}\nAdded: {new_item.name}'
        raise ValueError(f'Item \'{current_item.name}\' does not exist')

    def remove_item(self, item):
        """
        Removes an item from a shelf.
        """

        # TODO: add check if removal is successful
        self.items.remove(item)
        self.slots += 1
        return f'Item "{item.name}" has been removed from the shelf'
