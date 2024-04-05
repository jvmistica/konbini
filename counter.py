import json
import uuid
from employee import Employee
from item import Item

class Counter:
    slots = 8

    def __init__(self, name: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.status = 'active'
        self.slots = Counter.slots
        self.items = []
        self.employee = ''

    def details(self) -> str:
        """
        Returns the details of a counter.
        """

        item_list = [{'id': i.id, 'name': i.name, 'count': i.count, 'price': i.price, 'counter': i.counter} for i in self.items if len(self.items) > 0]
        details = {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'slots': self.slots,
            'items': item_list
        }
        return json.dumps(details)

    def remove(self) -> str:
        """
        Removes a counter.
        """

        self.status = 'inactive'
        return f'{self.name} has been removed from the display'

    def assign_employee(self, employee: Employee) -> str:
        """
        Assigns an employee to a counter.
        """

        self.employee = employee
        if employee == '':
            return f'Counter {self.name} has no employee assigned'
        
        return f'{employee.name} has been assigned to counter {self.name}'


    def add_item(self, item: Item) -> str:
        """
        Adds an item to a counter.
        """

        if not item.counter:
            return f'{item.name} is not a type of item that can be added to a counter'

        if self.slots == 0:
            return f'Item cannot be added to the counter, all slots are taken'

        self.items.append(item)
        self.slots -= 1
        return f'Item has been added to the counter'

    def replace_item(self, current_item: Item, new_item: Item) -> str:
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

    def remove_item(self, item: Item) -> str:
        """
        Removes an item from a counter.
        """

        # TODO: add check if removal is successful
        self.items.remove(item)
        self.slots += 1
        return f'Item "{item.name}" has been removed from the counter'
