import unittest
from konbini.item import Item
from konbini.shelf import Shelf

class TestShelf(unittest.TestCase):

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
        shelf = Shelf('Shelf #1', 'small')
        result = shelf.details()
        self.assertEqual(result['name'], 'Shelf #1')
        self.assertEqual(result['slots'], 4)
        self.assertEqual(len(result['items']), 0)

        item = Item('pudding', 20, 1.99, False)
        shelf.items.append(item)
        shelf.slots -= 1

        result = shelf.details()
        self.assertEqual(result['name'], 'Shelf #1')
        self.assertEqual(result['slots'], 3)
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['items'][0]['name'], 'pudding')
        self.assertEqual(result['items'][0]['count'], 20)
        self.assertEqual(result['items'][0]['price'], 1.99)
        self.assertEqual(result['items'][0]['counter'], False)

    def test_remove(self):
        shelf = Shelf('Shelf #1', 'small')
        result = shelf.details()
        self.assertEqual(result['name'], 'Shelf #1')
        self.assertEqual(result['status'], 'active')

        # valid removal
        remove_result = shelf.remove()
        self.assertFalse(remove_result['error'])
        self.assertIsNone(remove_result['error_message'])
        self.assertEqual(shelf.status, 'inactive')

        # invalid removal
        remove_result = shelf.remove()
        self.assertTrue(remove_result['error'])
        self.assertEqual(remove_result['error_message'], 'Shelf #1 is already inactive')
        self.assertEqual(shelf.status, 'inactive')


if __name__ == '__main__':
    unittest.main()
