from django.test import TestCase
from restaurant.views import MenuItemsView
from restaurant.models import MenuItems

class MenuViewTest(TestCase):
    def setUp(self):
        item1 = MenuItems.objects.create(title = 'salad', price = 2, inventory = 10)
        item2 = MenuItems.objects.create(title = 'sandwich', price = 6, inventory = 20)

    def test_getall(self):
        all = list(MenuItems.objects.values_list('title', flat=True))
        self.assertEqual(all, ['salad', 'sandwich'])