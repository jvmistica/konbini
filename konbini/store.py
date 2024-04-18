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

    def is_item_valid(self, display: any, item: Item) -> bool:
        if (item.counter and type(display).__name__ == 'Shelf') or (not item.counter and type(display).__name__ == 'Counter'):
            return False

    def add_item(self, display: any, item: Item) -> dict:
        """
        Adds an item to a display.
        """

        if self.is_item_valid(display, item) is False:
            return {
                'error': True,
                'error_message': f'{item.name} is not a type of item that can be added to {display.name}'
            }

        if display.slots == 0:
            return {
                'error': True,
                'error_message': f'Item cannot be added to {display.name}, all slots are taken'
            }

        display.items.append(item)
        display.slots -= 1
        self.money -= item.count * item.price

        return {
            'error': False,
            'error_message': None
        }

    def replace_item(self, display: any, current_item: Item, new_item: Item) -> dict:
        """
        Replaces an item in a display.
        """

        if self.is_item_valid(display, new_item) is False:
            return {
                'error': True,
                'error_message': f'{new_item.name} is not a type of item that can be added to {display.name}'
            }

        for n, item in enumerate(display.items):
            if item == current_item:
                display.items[n] = new_item
                self.money -= new_item.count * new_item.price
                return {
                    'error': False,
                    'error_message': None
                }
        return {
            'error': True,
            'error_message': f'Item \'{current_item.name}\' does not exist'
        }

    def remove_item(self, display: any, item: Item) -> dict:
        """
        Removes an item from a display.
        """

        try:
            display.items.remove(item)
        except ValueError:
            return {
                'error': True,
                'error_message': f'Item \'{item.name}\' does not exist'
            }

        display.slots += 1
        return {
            'error': False,
            'error_message': None
        }
