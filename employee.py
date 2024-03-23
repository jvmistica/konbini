class Employee:
    def __init__(self, name, salary, speed, stamina):
        self.name = name
        self.salary = salary
        self.speed = speed
        self.stamina = stamina
        self.status = 'Active'

    def details(self):
        return f'Name: {self.name}\nSalary: {self.salary}\nSpeed: {self.speed}\nStamina: {self.stamina}'

    def increase_salary(self, amount):
        self.salary += amount
        return f'{self.name}\'s salary has increased to {self.salary}'

    def increase_speed(self, amount):
        self.speed += amount
        return f'{self.name}\'s speed has increased to {self.speed}'

    def increase_stamina(self, amount):
        self.stamina += amount
        return f'{self.name}\'s stamina has increased to {self.stamina}'

    def remove(self):
        self.status = 'Inactive'
        return f'{self.name} has been removed from the staff'
