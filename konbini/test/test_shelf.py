import unittest
from konbini.helper import create_items
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
        add_result = shelf.add_item(item)
        self.assertFalse(add_result['error'])
        self.assertIsNone(add_result['error_message'])

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

    def test_add_item(self):
        shelf = Shelf('Shelf #1', 'small')

        items = create_items(5, False)
        for i, item in enumerate(items):
            result = shelf.add_item(item)
            if i < 4:
                # valid addition
                self.assertFalse(result['error'])
                self.assertIsNone(result['error_message'])
            else:
                # invalid addition, no slots left
                self.assertTrue(result['error'])
                self.assertEqual(result['error_message'], 'Item cannot be added to Shelf #1, all slots are taken')

        # invalid addition, not a shelf item
        invalid_item = Item('Item 5', 30, 1.99, True)
        result = shelf.add_item(invalid_item)
        self.assertTrue(result['error'])
        self.assertEqual(result['error_message'], 'Item 5 is not a type of item that can be added to Shelf #1')

    def test_replace_item(self):
        shelf = Shelf('Shelf #1', 'small')
        item = Item('pudding', 20, 1.99, False)
        add_result = shelf.add_item(item)
        self.assertFalse(add_result['error'])
        self.assertIsNone(add_result['error_message'])
        
        result = shelf.details()
        self.assertEqual(result['name'], 'Shelf #1')
        self.assertEqual(result['slots'], 3)
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['items'][0]['name'], 'pudding')

        # valid replace
        new_item = Item('chocolate', 25, 1.59, False)
        replace_result = shelf.replace_item(item, new_item)
        self.assertFalse(replace_result['error'])
        self.assertIsNone(replace_result['error_message'])

        result = shelf.details()
        self.assertEqual(result['name'], 'Shelf #1')
        self.assertEqual(result['slots'], 3)
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['items'][0]['name'], 'chocolate')

        # invalid replace, item does not exist
        new_item = Item('cake', 25, 1.59, False)
        replace_result = shelf.replace_item(item, new_item)
        self.assertTrue(replace_result['error'])
        self.assertEqual(replace_result['error_message'], 'Item \'pudding\' does not exist')

        result = shelf.details()
        self.assertEqual(result['name'], 'Shelf #1')
        self.assertEqual(result['slots'], 3)
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['items'][0]['name'], 'chocolate')

    def test_remove_item(self):
        shelf = Shelf('Shelf #1', 'small')
        item = Item('pudding', 20, 1.99, False)
        add_result = shelf.add_item(item)
        self.assertFalse(add_result['error'])
        self.assertIsNone(add_result['error_message'])
        
        result = shelf.details()
        self.assertEqual(result['name'], 'Shelf #1')
        self.assertEqual(result['slots'], 3)
        self.assertEqual(result['items'][0]['name'], 'pudding')

        # valid removal
        remove_result = shelf.remove_item(item)
        self.assertFalse(remove_result['error'])
        self.assertIsNone(remove_result['error_message'])
        
        result = shelf.details()
        self.assertEqual(result['name'], 'Shelf #1')
        self.assertEqual(result['slots'], 4)
        self.assertEqual(len(result['items']), 0)

        # invalid removal
        remove_result = shelf.remove_item(item)
        self.assertTrue(remove_result['error'])
        self.assertEqual(remove_result['error_message'], 'Item \'pudding\' does not exist')
        
        result = shelf.details()
        self.assertEqual(result['name'], 'Shelf #1')
        self.assertEqual(result['slots'], 4)
        self.assertEqual(len(result['items']), 0)

if __name__ == '__main__':
    unittest.main()
