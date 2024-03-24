from item import Item

class Counter:
    def __init__(self, name, slots):
        self.name = name
        self.slots = slots
        self.status = 'Active'
        self.items = []

    def details(self):
        item_list = [{'name': i.name, 'count': i.count, 'price': i.price} for i in self.items if len(self.items) > 0]
        return f'Name: {self.name}\nSlots: {self.slots}\nItems: {item_list}'

    def add(self, item):
        if self.slots == 0:
            return f'{self.name} cannot be added to the counter, all slots are taken.'

        self.items.append(item)
        self.slots -= 1
        return f'{self.name} has been added to the counter'

    def remove(self):
        self.status = 'Inactive'
        return f'{self.name} has been removed from the display'
