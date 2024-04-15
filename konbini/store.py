import uuid
from konbini.counter import Counter
from konbini.employee import Employee
from konbini.item import Item
from konbini.shelf import Shelf


class Store:
    capital = 100000
    currency = 'Gold'

    def __init__(self, name: str, location: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.location = location
        self.money = Store.capital

        employees = []
        employees.append(Employee('Employee #1', 20000, 80, 80))
        self.employees = employees

        displays = []
        displays.append(Shelf('Shelf #1', 'small'))
        displays.append(Counter('Counter #1'))
        self.displays = displays

    def details(self) -> dict:
        """
        Returns the details of the store.
        """

        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'money': self.money,
            'currency': Store.currency,
            'employees': self.employees,
            'displays': self.displays
        }

    def add_shelf(self, shelf: Shelf) -> dict:
        """
        Adds a shelf to the store.
        """

        self.displays.append(shelf)
        self.money -= Shelf.cost

        return {
            'error': False,
            'error_message': None
        }

    def add_counter(self, counter: Counter) -> dict:
        """
        Adds a counter to the store.
        """

        self.displays.append(counter)
        self.money -= Counter.cost

        return {
            'error': False,
            'error_message': None
        }

    def add_employee(self, employee: Employee) -> dict:
        """
        Adds an employee to the store.
        """

        self.employees.append(employee)
        return {
            'error': False,
            'error_message': None
        }

    def add_item_shelf(self, shelf: Shelf, item: Item) -> dict:
        """
        Adds an item to a shelf.
        """

        if item.counter:
            return {
                'error': True,
                'error_message': f'{item.name} is not a type of item that can be added to {shelf.name}'
            }

        if shelf.slots == 0:
            return {
                'error': True,
                'error_message': f'Item cannot be added to {shelf.name}, all slots are taken'
            }

        shelf.items.append(item)
        shelf.slots -= 1
        self.money -= item.count * item.price

        return {
            'error': False,
            'error_message': None
        }

    def replace_item_shelf(self, shelf: Shelf, current_item: Item, new_item: Item) -> dict:
        """
        Replaces an item in a shelf.
        """

        for n, item in enumerate(shelf.items):
            if item == current_item:
                shelf.items[n] = new_item
                self.money -= new_item.count * new_item.price
                return {
                    'error': False,
                    'error_message': None
                }
        return {
            'error': True,
            'error_message': f'Item \'{current_item.name}\' does not exist'
        }

    def remove_item_shelf(self, shelf: Shelf, item: Item) -> dict:
        """
        Removes an item from a shelf.
        """

        try:
            shelf.items.remove(item)
        except ValueError:
            return {
                'error': True,
                'error_message': f'Item \'{item.name}\' does not exist'
            }

        shelf.slots += 1
        return {
            'error': False,
            'error_message': None
        }

    def add_item_counter(self, counter: Counter, item: Item) -> dict:
        """
        Adds an item to a counter.
        """

        if not item.counter:
            return {
                'error': True,
                'error_message': f'{item.name} is not a type of item that can be added to {counter.name}'
            }

        if counter.slots == 0:
            return {
                'error': True,
                'error_message': f'Item cannot be added to {counter.name}, all slots are taken'
            }

        counter.items.append(item)
        counter.slots -= 1
        self.money -= item.count * item.price

        return {
            'error': False,
            'error_message': None
        }

    def replace_item_counter(self, counter: Counter, current_item: Item, new_item: Item) -> dict:
        """
        Replaces an item in a counter.
        """

        for n, item in enumerate(counter.items):
            if item == current_item:
                counter.items[n] = new_item
                self.money -= new_item.count * new_item.price
                return {
                    'error': False,
                    'error_message': None
                }
        return {
            'error': True,
            'error_message': f'Item \'{current_item.name}\' does not exist'
        }

    def remove_item_counter(self, counter: Counter, item: Item) -> dict:
        """
        Removes an item from a counter.
        """

        try:
            counter.items.remove(item)
        except ValueError:
            return {
                'error': True,
                'error_message': f'Item \'{item.name}\' does not exist'
            }

        counter.slots += 1
        return {
            'error': False,
            'error_message': None
        }
