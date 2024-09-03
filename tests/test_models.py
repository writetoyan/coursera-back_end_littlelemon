from django.test import TestCase
from restaurant.models import MenuItems

# Create your tests here.
class MenuItemTest(TestCase):
    def test(self):
        item = MenuItems.objects.create(title='Salad', price=2, inventory=5)
        itemstr = item.get_item()

        self.assertEqual(itemstr, "Salad: 2")
