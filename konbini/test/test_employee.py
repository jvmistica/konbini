import unittest
from konbini.employee import Employee

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
        result = employee.details()
        self.assertIsNotNone(result['id'])
        self.assertEqual(result['name'], 'John Wick')
        self.assertEqual(result['salary'], 50000)
        self.assertEqual(result['speed'], 120)
        self.assertEqual(result['stamina'], 100)
        self.assertEqual(result['status'], 'active')

    def test_increase_salary(self):
        employee = Employee('John Wick', 50000, 120, 100)

        # valid salary increase
        increase_result = employee.increase_salary(10250)
        self.assertFalse(increase_result['error'])
        self.assertIsNone(increase_result['error_message'])
        
        result = employee.details()
        self.assertEqual(result['name'], 'John Wick')
        self.assertEqual(result['salary'], 60250)

        # invalid salary increase
        increase_result = employee.increase_salary(-5000)
        self.assertTrue(increase_result['error'])
        self.assertEqual(increase_result['error_message'], 'Salary cannot be reduced, please enter a positive number')
        
        result = employee.details()
        self.assertEqual(result['name'], 'John Wick')
        self.assertEqual(result['salary'], 60250)

    def test_increase_speed(self):
        employee = Employee('John Wick', 50000, 120, 100)

        # valid speed increase
        increase_result = employee.increase_speed(10)
        self.assertFalse(increase_result['error'])
        self.assertIsNone(increase_result['error_message'])
        
        result = employee.details()
        self.assertEqual(result['name'], 'John Wick')
        self.assertEqual(result['speed'], 130)

        # invalid speed increase
        increase_result = employee.increase_speed(-10)
        self.assertTrue(increase_result['error'])
        self.assertEqual(increase_result['error_message'], 'Speed cannot be reduced, please enter a positive number')
        
        result = employee.details()
        self.assertEqual(result['name'], 'John Wick')
        self.assertEqual(result['speed'], 130)

    def test_increase_stamina(self):
        employee = Employee('John Wick', 50000, 120, 100)

        # valid stamina increase
        increase_result = employee.increase_stamina(20)
        self.assertFalse(increase_result['error'])
        self.assertIsNone(increase_result['error_message'])
        
        result = employee.details()
        self.assertEqual(result['name'], 'John Wick')
        self.assertEqual(result['stamina'], 120)

        # invalid stamina increase
        increase_result = employee.increase_stamina(-20)
        self.assertTrue(increase_result['error'])
        self.assertEqual(increase_result['error_message'], 'Stamina cannot be reduced, please enter a positive number')
        
        result = employee.details()
        self.assertEqual(result['name'], 'John Wick')
        self.assertEqual(result['stamina'], 120)

    def test_remove(self):
        employee = Employee('John Wick', 50000, 120, 100)

        # valid removal
        remove_result = employee.remove()
        self.assertFalse(remove_result['error'])
        self.assertIsNone(remove_result['error_message'])
        
        result = employee.details()
        self.assertEqual(result['name'], 'John Wick')
        self.assertEqual(result['status'], 'inactive')

        # invalid removal
        remove_result = employee.remove()
        self.assertTrue(remove_result['error'])
        self.assertEqual(remove_result['error_message'], 'Employee is already inactive')
        
        result = employee.details()
        self.assertEqual(result['name'], 'John Wick')
        self.assertEqual(result['status'], 'inactive')

if __name__ == '__main__':
    unittest.main()
