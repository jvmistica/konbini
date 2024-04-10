import uuid
from konbini.item import Item

class Display:
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.status = 'active'
        self.items = []

    def remove(self) -> dict:
        """
        Removes a display.
        """

        if self.status == 'inactive':
            return {
                'error': True,
                'error_message': f'{self.name} is already inactive'
            }

        self.status = 'inactive'
        return {
            'error': False,
            'error_message': None
        }

    def add_item(self, item: Item) -> dict:
        """
        Adds an item to a display.
        """

        # make sure that only counter type items are added to counters and non-counter types to shelves
        if (item.counter and type(self).__name__ == 'Shelf') or (not item.counter and type(self).__name__ == 'Counter'):
            return {
                'error': True,
                'error_message': f'{item.name} is not a type of item that can be added to {self.name}'
            }

        if self.slots == 0:
            return {
                'error': True,
                'error_message': f'Item cannot be added to {self.name}, all slots are taken'
            }

        self.items.append(item)
        self.slots -= 1
        return {
            'error': False,
            'error_message': None
        }

    def replace_item(self, current_item: Item, new_item: Item) -> dict:
        """
        Replaces an item in a display.
        """

        for n, item in enumerate(self.items):
            if item == current_item:
                self.items[n] = new_item
                return {
                    'error': False,
                    'error_message': None
                }
        return {
            'error': True,
            'error_message': f'Item \'{current_item.name}\' does not exist'
        }

    def remove_item(self, item: Item) -> dict:
        """
        Removes an item from a display.
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
