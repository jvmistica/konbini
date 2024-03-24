from item import Item

class Shelf:
    sizes = {'small': 4, 'medium': 8, 'large': 12}

    def __init__(self, name, size):
        self.name = name
        self.status = 'Active'
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

        item_list = [{'name': i.name, 'count': i.count, 'price': i.price} for i in self.items if len(self.items) > 0]
        return f'Name: {self.name}\nSlots: {self.slots}\nItems: {item_list}'

    def remove(self):
        """
        Removes a shelf.
        """

        self.status = 'Inactive'
        return f'{self.name} has been removed from the display'

    def add_item(self, item):
        """
        Adds an item to a shelf.
        """

        if self.slots == 0:
            return 'Item cannot be added to the shelf, all slots are taken'

        self.items.append(item)
        self.slots -= 1
        return 'Item has been added to the shelf'

    def replace(self, current_item, new_item):
        """
        Replaces an item in a shelf.
        """

        for n, item in enumerate(self.items):
            if item == current_item:
                self.items[n] = new_item
                return f'Discarded: {current_item.name}\nAdded: {new_item.name}'
        raise ValueError(f'Item \'{current_item.name}\' does not exist')
