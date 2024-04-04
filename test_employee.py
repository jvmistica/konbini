import json
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def test_new_employee(self):
        employee = Employee('John Wick', 50000, 120, 100)
        self.assertIsNotNone(employee.id)
        self.assertEqual(employee.name, 'John Wick')
        self.assertEqual(employee.salary, 50000)
        self.assertEqual(employee.speed, 120)
        self.assertEqual(employee.stamina, 100)
        self.assertEqual(employee.status, 'active')

    def test_details(self):
        employee = Employee('John Wick', 50000, 120, 100)
        result = json.loads(employee.details())
        self.assertIsNotNone(result['id'])
        self.assertEqual(result['name'], 'John Wick')
        self.assertEqual(result['salary'], 50000)
        self.assertEqual(result['speed'], 120)
        self.assertEqual(result['stamina'], 100)
        self.assertEqual(result['status'], 'active')

    def test_increase_salary(self):
        employee = Employee('John Wick', 50000, 120, 100)
        increase_result = employee.increase_salary(10250)
        self.assertEqual(increase_result, 'John Wick\'s salary has increased to 60250')
        
        result = json.loads(employee.details())
        self.assertEqual(result['name'], 'John Wick')
        self.assertEqual(result['salary'], 60250)

    def test_increase_speed(self):
        employee = Employee('John Wick', 50000, 120, 100)
        increase_result = employee.increase_speed(10)
        self.assertEqual(increase_result, 'John Wick\'s speed has increased to 130')
        
        result = json.loads(employee.details())
        self.assertEqual(result['name'], 'John Wick')
        self.assertEqual(result['speed'], 130)

    def test_increase_stamina(self):
        employee = Employee('John Wick', 50000, 120, 100)
        increase_result = employee.increase_stamina(20)
        self.assertEqual(increase_result, 'John Wick\'s stamina has increased to 120')
        
        result = json.loads(employee.details())
        self.assertEqual(result['name'], 'John Wick')
        self.assertEqual(result['stamina'], 120)

    def test_remove(self):
        employee = Employee('John Wick', 50000, 120, 100)
        remove_result = employee.remove()
        self.assertEqual(remove_result, 'John Wick has been removed from the staff')
        
        result = json.loads(employee.details())
        self.assertEqual(result['name'], 'John Wick')
        self.assertEqual(result['status'], 'inactive')

if __name__ == '__main__':
    unittest.main()
