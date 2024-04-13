import uuid
from konbini.counter import Counter
from konbini.employee import Employee
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
