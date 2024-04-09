from employee import Employee
from display import Display
from item import Item

class Counter(Display):
    slots = 8

    def __init__(self, name: str):
        super().__init__(name)
        self.slots = Counter.slots
        self.employee = None

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

    def assign_employee(self, employee: Employee) -> dict:
        """
        Assigns an employee to a counter.
        """

        self.employee = employee
        return {
            'error': False,
            'error_message': None
        }
