import json
import uuid

class Employee:
    def __init__(self, name, salary, speed, stamina):
        self.id = str(uuid.uuid4())
        self.name = name
        self.salary = salary
        self.speed = speed
        self.stamina = stamina
        self.status = 'active'

    def details(self):
        """
        Returns the details of an employee.
        """

        details = {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'salary': self.salary,
            'speed': self.speed,
            'stamina': self.stamina
        }
        return json.dumps(details)

    def increase_salary(self, amount):
        """
        Increases the salary of an employee.
        """

        self.salary += amount
        return f'{self.name}\'s salary has increased to {self.salary}'

    def increase_speed(self, amount):
        """
        Increases the speed of an employee.
        """

        self.speed += amount
        return f'{self.name}\'s speed has increased to {self.speed}'

    def increase_stamina(self, amount):
        """
        Increases the stamina of an employee.
        """

        self.stamina += amount
        return f'{self.name}\'s stamina has increased to {self.stamina}'

    def remove(self):
        """
        Removes an employee.
        """

        self.status = 'inactive'
        return f'{self.name} has been removed from the staff'
