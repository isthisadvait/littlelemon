from django.test import TestCase, RequestFactory
from restaurant.models import MenuItem
from restaurant.views import MenuItemsView
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        MenuItem.objects.create(title = "Soup", price = 4, inventory = 20)
        MenuItem.objects.create(title = "Salad", price = 3, inventory = 25)
        MenuItem.objects.create(title = "Burger", price = 9, inventory = 8)
    
    def test_getall(self):
        menu_items = MenuItem.objects.all()
        serialized_menu_items = MenuItemSerializer(menu_items, many = True)
        retrieved_menu = MenuItemsView.as_view()(self.factory.get("restaurant/menu/"))
        self.assertEqual(serialized_menu_items.data, retrieved_menu.data)