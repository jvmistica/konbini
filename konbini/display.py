import uuid
from konbini.item import Item


class Display:

    def __init__(self, name: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.status = 'active'
        self.items = []

    def remove(self) -> dict:
        """
        Removes a display.
        """

        if self.status == 'inactive':
            return {
                'error': True,
                'error_message': f'{self.name} is already inactive'
            }

        self.status = 'inactive'
        return {
            'error': False,
            'error_message': None
        }
