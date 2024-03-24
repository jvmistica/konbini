from item import Item

class Shelf:
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
            return f'Item cannot be added to the shelf, all slots are taken.'

        self.items.append(item)
        self.slots -= 1
        return f'Item has been added to the shelf'

    def remove(self):
        self.status = 'Inactive'
        return f'{self.name} has been removed from the display'


# # example: add items to shelf
# shelf = Shelf('Shelf #1', 4)
# 
# item1 = Item('Pudding', 50, 1.99)
# item2 = Item('Ramen', 50, 0.99)
# 
# print(shelf.add(item1))
# print(shelf.add(item1))
# print(shelf.add(item2))
# print(shelf.add(item2))
# print(shelf.add(item2))
# print(shelf.details())
