from item import Item

# TODO:
# Counter and shelf are very similar, perhaps define a class and have these two act as subclasses
class Counter:
    slots = 8

    def __init__(self, name):
        self.name = name
        self.status = 'Active'
        self.slots = Counter.slots
        self.items = []
        self.employee = ''

    def details(self):
        """
        Returns the details of a counter.
        """

        item_list = [{'name': i.name, 'count': i.count, 'price': i.price} for i in self.items if len(self.items) > 0]
        return f'Name: {self.name}\nSlots: {self.slots}\nItems: {item_list}'

    def remove(self):
        """
        Removes a counter.
        """

        self.status = 'Inactive'
        return f'{self.name} has been removed from the display'

    def assign_employee(self, employee):
        """
        Assigns an employee to a counter.
        """

        self.employee = employee
        if employee == '':
            return f'Counter {self.name} has no employee assigned'
        
        return f'{employee.name} has been assigned to counter {self.name}'


    def add_item(self, item):
        """
        Adds an item to a counter.
        """

        if not item.counter:
            return f'{item.name} is not a type of item that can be added to a counter'

        if self.slots == 0:
            return f'{item.name} cannot be added to the counter, all slots are taken'

        self.items.append(item)
        self.slots -= 1
        return f'{item.name} has been added to the counter'

    def replace(self, current_item, new_item):
        """
        Replaces an item in a counter.
        """

        if not new_item.counter:
            return f'{new_item.name} is not a type of item that can be added to a counter'

        for n, item in enumerate(self.items):
            if item == current_item:
                self.items[n] = new_item
                return f'Discarded: {current_item.name}\nAdded: {new_item.name}'
        raise ValueError(f'Item \'{current_item.name}\' does not exist')
