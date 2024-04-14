import unittest
from konbini.counter import Counter
from konbini.employee import Employee
from konbini.item import Item

class TestCounter(unittest.TestCase):

    def test_new_counter(self):
        counter = Counter('Counter #1')
        self.assertIsNotNone(counter.id)
        self.assertEqual(counter.name, 'Counter #1')
        self.assertEqual(counter.slots, 8)

    def test_details(self):
        counter = Counter('Counter #1')
        result = counter.details()
        self.assertEqual(result['name'], 'Counter #1')
        self.assertEqual(result['slots'], 8)
        self.assertEqual(len(result['items']), 0)

        item = Item('chocolate kariman', 20, 1.99, True)
        counter.items.append(item)
        counter.slots -= 1

        result = counter.details()
        self.assertEqual(result['name'], 'Counter #1')
        self.assertEqual(result['slots'], 7)
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['items'][0]['name'], 'chocolate kariman')
        self.assertEqual(result['items'][0]['count'], 20)
        self.assertEqual(result['items'][0]['price'], 1.99)
        self.assertEqual(result['items'][0]['counter'], True)

    def test_remove(self):
        counter = Counter('Counter #1')
        result = counter.details()
        self.assertEqual(result['name'], 'Counter #1')
        self.assertEqual(result['slots'], 8)
        self.assertEqual(result['status'], 'active')
        self.assertEqual(len(result['items']), 0)

        # valid removal
        remove_result = counter.remove()
        self.assertFalse(remove_result['error'])
        self.assertIsNone(remove_result['error_message'])
        self.assertEqual(counter.status, 'inactive')

        # invalid removal
        remove_result = counter.remove()
        self.assertTrue(remove_result['error'])
        self.assertEqual(remove_result['error_message'], 'Counter #1 is already inactive')
        self.assertEqual(counter.status, 'inactive')

    def test_assign_employee(self):
        counter = Counter('Counter #1')
        employee = Employee('Employee 1', 70000, 80, 100)

        # assign employee
        result = counter.assign_employee(employee)
        self.assertFalse(result['error'])
        self.assertIsNone(result['error_message'])
        self.assertEqual(counter.employee, employee)

        # # unassign employee
        # result = counter.assign_employee('')
        # self.assertFalse(result['error'])
        # self.assertIsNone(result['error_message'])
        # self.assertEqual(counter.employee, '')

if __name__ == '__main__':
    unittest.main()
