import uuid

class Employee:
    max_speed = 500
    max_stamina = 500

    def __init__(self, name: str, salary: float, speed: int, stamina: int):
        self.id = str(uuid.uuid4())
        self.name = name
        self.salary = salary
        self.speed = speed
        self.stamina = stamina
        self.status = 'active'

    def details(self) -> dict:
        """
        Returns the details of an employee.
        """

        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'salary': self.salary,
            'speed': self.speed,
            'stamina': self.stamina
        }

    def increase_salary(self, amount: float) -> dict:
        """
        Increases the salary of an employee.
        """

        if amount < 0:
            return {
                'error': True,
                'error_message': 'Salary cannot be reduced, please enter a positive number'
            }

        self.salary += amount
        return {
            'error': False,
            'error_message': None
        }

    def increase_speed(self, amount: int) -> dict:
        """
        Increases the speed of an employee.
        """

        if amount < 0:
            return {
                'error': True,
                'error_message': 'Speed cannot be reduced, please enter a positive number'
            }

        self.speed += amount
        return {
            'error': False,
            'error_message': None
        }

    def increase_stamina(self, amount: int) -> dict:
        """
        Increases the stamina of an employee.
        """

        if amount < 0:
            return {
                'error': True,
                'error_message': 'Stamina cannot be reduced, please enter a positive number'
            }

        self.stamina += amount
        return {
            'error': False,
            'error_message': None
        }

    def remove(self) -> dict:
        """
        Removes an employee.
        """

        if self.status == 'inactive':
            return {
                'error': True,
                'error_message': 'Employee is already inactive'
            }

        self.status = 'inactive'
        return {
            'error': False,
            'error_message': None
        }
