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

    def details(self) -> dict:
        """
        Returns the details of a counter.
        """

        item_list = [{'id': i.id, 'name': i.name, 'count': i.count, 'price': i.price, 'counter': i.counter} for i in self.items if len(self.items) > 0]
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'slots': self.slots,
            'items': item_list
        }

    def remove(self) -> dict:
        """
        Removes a counter.
        """

        if self.status == 'inactive':
            return {
                'error': True,
                'error_message': 'Counter is already inactive'
            }

        self.status = 'inactive'
        return {
            'error': False,
            'error_message': None
        }

    def assign_employee(self, employee: Employee) -> dict:
        """
        Assigns an employee to a counter.
        """

        self.employee = employee
        return {
            'error': False,
            'error_message': None
        }

    def add_item(self, item: Item) -> dict:
        """
        Adds an item to a counter.
        """

        if not item.counter:
            return {
                'error': True,
                'error_message': f'{item.name} is not a type of item that can be added to a counter'
            }

        if self.slots == 0:
            return {
                'error': True,
                'error_message': f'Item cannot be added to the counter, all slots are taken'
            }

        self.items.append(item)
        self.slots -= 1
        return {
            'error': False,
            'error_message': None
        }

    def replace_item(self, current_item: Item, new_item: Item) -> dict:
        """
        Replaces an item in a counter.
        """

        if not new_item.counter:
            return {
                'error': True,
                'error_message': f'{new_item.name} is not a type of item that can be added to a counter'
            }

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
        Removes an item from a counter.
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
