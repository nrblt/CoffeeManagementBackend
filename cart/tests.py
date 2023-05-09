from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient
from .models import Cart, CartItem
from .serializers import CartSerializer
from category.models import Category
from product.models import Product


def create_category(**params):
    defaults = {
        "name":"Coffee category",
        "description":"coffee category"
    }
    category = Category.objects.create(**defaults)
    return category

def create_product(**params):
    category = create_category()

    defaults = {
        'name': "Latte",
        'price': 5,
        'description': "latettt"
    }
    product = Product.objects.create(category=category,**defaults)
    return product

CART_ITEM_URL = reverse("cart:cart-item")
def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)

class CartAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = create_user(email='user@example.com', password='test123')
        self.client.force_authenticate(self.user)

    def test_add_to_cart(self):
        cart = Cart.objects.create(user=self.user, total_price=0)
        product = create_product()
        cart_item = {
            'count':1
        }
        cart_item(cart=cart, product=product)
        res = self.client.post(CART_ITEM_URL, cart_item, format='json')
