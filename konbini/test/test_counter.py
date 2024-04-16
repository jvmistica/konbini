import unittest
from konbini.counter import Counter
from konbini.employee import Employee
from konbini.item import Item


class TestCounter(unittest.TestCase):

    def setUp(self):
        self.counter = Counter('Counter #1')

    def tearDown(self):
        self.counter.remove()

    def validate_initial_details(self, result: dict):
        self.assertIsNotNone(result['id'])
        self.assertEqual(result['name'], 'Counter #1')
        self.assertTrue(result['active'])
        self.assertEqual(result['slots'], 8)
        self.assertEqual(len(result['items']), 0)
        self.assertIsNone(result['employee'])

    def test_new_counter(self):
        counter = Counter('Counter #1')
        self.assertIsNotNone(counter.id)
        self.assertEqual(counter.name, 'Counter #1')
        self.assertEqual(counter.slots, 8)

    def test_details(self):
        result = self.counter.details()
        self.validate_initial_details(result)

        item = Item('chocolate kariman', 20, 1.99, True)
        self.counter.items.append(item)
        self.counter.slots -= 1

        result = self.counter.details()
        self.assertEqual(result['name'], 'Counter #1')
        self.assertEqual(result['slots'], 7)
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['items'][0]['name'], 'chocolate kariman')
        self.assertEqual(result['items'][0]['count'], 20)
        self.assertEqual(result['items'][0]['price'], 1.99)
        self.assertTrue(result['items'][0]['counter'])

    def test_remove(self):
        result = self.counter.details()
        self.validate_initial_details(result)

        # valid removal
        result = self.counter.remove()
        self.assertFalse(result['error'])
        self.assertIsNone(result['error_message'])
        self.assertFalse(self.counter.active)

        # invalid removal
        result = self.counter.remove()
        self.assertTrue(result['error'])
        self.assertEqual(result['error_message'], 'Counter #1 is already inactive')
        self.assertFalse(self.counter.active)

    def test_assign_employee(self):
        result = self.counter.details()
        self.validate_initial_details(result)

        employee = Employee('Employee 1', 70000, 80, 100)
        result = self.counter.assign_employee(employee)
        self.assertFalse(result['error'])
        self.assertIsNone(result['error_message'])
        self.assertEqual(self.counter.employee, employee)


if __name__ == '__main__':
    unittest.main()
