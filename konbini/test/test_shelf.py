import unittest
from konbini.item import Item
from konbini.shelf import Shelf


class TestShelf(unittest.TestCase):

    def setUp(self):
        self.shelf = Shelf('Shelf #1', 'small')

    def tearDown(self):
        self.shelf.remove()

    def validate_initial_details(self, result: dict):
        self.assertIsNotNone(result['id'])
        self.assertEqual(result['name'], 'Shelf #1')
        self.assertEqual(result['status'], 'active')
        self.assertEqual(result['size'], 'small')
        self.assertEqual(result['slots'], 4)
        self.assertEqual(len(result['items']), 0)

    def test_new_shelf(self):
        # small shelf
        shelf = Shelf('Shelf #1', 'small')
        self.assertIsNotNone(shelf.id)
        self.assertEqual(shelf.name, 'Shelf #1')
        self.assertEqual(shelf.slots, 4)
        self.assertEqual(shelf.size, 'small')

        # medium shelf
        shelf = Shelf('Shelf #1', 'medium')
        self.assertEqual(shelf.name, 'Shelf #1')
        self.assertEqual(shelf.slots, 8)
        self.assertEqual(shelf.size, 'medium')

        # medium shelf
        shelf = Shelf('Shelf #1', 'large')
        self.assertEqual(shelf.name, 'Shelf #1')
        self.assertEqual(shelf.slots, 12)
        self.assertEqual(shelf.size, 'large')

        # invalid size shelf
        with self.assertRaises(ValueError):
            Shelf('Shelf #2', 'extra-large')

    def test_details(self):
        result = self.shelf.details()
        self.validate_initial_details(result)

        item = Item('pudding', 20, 1.99, False)
        self.shelf.items.append(item)
        self.shelf.slots -= 1

        result = self.shelf.details()
        self.assertEqual(result['name'], 'Shelf #1')
        self.assertEqual(result['slots'], 3)
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['items'][0]['name'], 'pudding')
        self.assertEqual(result['items'][0]['count'], 20)
        self.assertEqual(result['items'][0]['price'], 1.99)
        self.assertEqual(result['items'][0]['counter'], False)

    def test_remove(self):
        result = self.shelf.details()
        self.validate_initial_details(result)

        # valid removal
        result = self.shelf.remove()
        self.assertFalse(result['error'])
        self.assertIsNone(result['error_message'])
        self.assertEqual(self.shelf.status, 'inactive')

        # invalid removal
        result = self.shelf.remove()
        self.assertTrue(result['error'])
        self.assertEqual(result['error_message'], 'Shelf #1 is already inactive')
        self.assertEqual(self.shelf.status, 'inactive')


if __name__ == '__main__':
    unittest.main()
