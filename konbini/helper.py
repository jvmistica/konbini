from konbini.item import Item

def create_items(count, is_counter_item):
    items = []
    for i in range(count):
        items.append(Item(f'Item {i + 1}', 30, 1.99, is_counter_item))
    return items
