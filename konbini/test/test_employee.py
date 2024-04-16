import unittest
from konbini.employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('John Wick', 50000, 120, 100)

    def tearDown(self):
        self.employee.remove()

    def validate_initial_details(self, result: dict):
        self.assertIsNotNone(result['id'])
        self.assertEqual(result['name'], 'John Wick')
        self.assertTrue(result['active'])
        self.assertEqual(result['salary'], 50000)
        self.assertEqual(result['speed'], 120)
        self.assertEqual(result['stamina'], 100)

    def test_new_employee(self):
        employee = Employee('John Wick', 50000, 120, 100)
        self.assertIsNotNone(employee.id)
        self.assertEqual(employee.name, 'John Wick')
        self.assertEqual(employee.salary, 50000)
        self.assertEqual(employee.speed, 120)
        self.assertEqual(employee.stamina, 100)
        self.assertTrue(employee.active)

    def test_details(self):
        result = self.employee.details()
        self.validate_initial_details(result)

    def test_increase_salary(self):
        result = self.employee.details()
        self.validate_initial_details(result)

        # valid salary increase
        result = self.employee.increase_salary(10250)
        self.assertFalse(result['error'])
        self.assertIsNone(result['error_message'])
        
        result = self.employee.details()
        self.assertEqual(result['name'], 'John Wick')
        self.assertEqual(result['salary'], 60250)

        # invalid salary increase
        result = self.employee.increase_salary(-5000)
        self.assertTrue(result['error'])
        self.assertEqual(result['error_message'], 'Salary cannot be reduced, please enter a positive number')
        
        result = self.employee.details()
        self.assertEqual(result['name'], 'John Wick')
        self.assertEqual(result['salary'], 60250)

    def test_increase_speed(self):
        result = self.employee.details()
        self.validate_initial_details(result)

        # valid speed increase
        result = self.employee.increase_speed(10)
        self.assertFalse(result['error'])
        self.assertIsNone(result['error_message'])
        
        result = self.employee.details()
        self.assertEqual(result['name'], 'John Wick')
        self.assertEqual(result['speed'], 130)

        # invalid speed increase
        result = self.employee.increase_speed(-10)
        self.assertTrue(result['error'])
        self.assertEqual(result['error_message'], 'Speed cannot be reduced, please enter a positive number')
        
        result = self.employee.details()
        self.assertEqual(result['name'], 'John Wick')
        self.assertEqual(result['speed'], 130)

    def test_increase_stamina(self):
        result = self.employee.details()
        self.validate_initial_details(result)

        # valid stamina increase
        result = self.employee.increase_stamina(20)
        self.assertFalse(result['error'])
        self.assertIsNone(result['error_message'])
        
        result = self.employee.details()
        self.assertEqual(result['name'], 'John Wick')
        self.assertEqual(result['stamina'], 120)

        # invalid stamina increase
        result = self.employee.increase_stamina(-20)
        self.assertTrue(result['error'])
        self.assertEqual(result['error_message'], 'Stamina cannot be reduced, please enter a positive number')
        
        result = self.employee.details()
        self.assertEqual(result['name'], 'John Wick')
        self.assertEqual(result['stamina'], 120)

    def test_remove(self):
        result = self.employee.details()
        self.validate_initial_details(result)

        # valid removal
        result = self.employee.remove()
        self.assertFalse(result['error'])
        self.assertIsNone(result['error_message'])
        
        result = self.employee.details()
        self.assertEqual(result['name'], 'John Wick')
        self.assertFalse(result['active'])

        # invalid removal
        result = self.employee.remove()
        self.assertTrue(result['error'])
        self.assertEqual(result['error_message'], 'Employee is already inactive')
        
        result = self.employee.details()
        self.assertEqual(result['name'], 'John Wick')
        self.assertFalse(result['active'])


if __name__ == '__main__':
    unittest.main()
