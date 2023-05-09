from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient
from .models import Order
from .serializers import OrderSerializer
from category.models import Category
from product.models import Product


def create_order(**params):
    defaults = {
        "name":"Coffee category",
        "description":"coffee category"
    }
    order = Order.objects.create(**defaults)
    return order


ORDER_URL = reverse("cart:cart-item")
def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)

class OrderAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = create_user(email='user@example.com', password='test123')
        self.client.force_authenticate(self.user)

    def test_add_to_order(self):
        cart = Order.objects.create(user=self.user, total_price=0)
        product = create_order()
        cart_item = {
            'count':1
        }
        cart_item(cart=cart, product=product)
        res = self.client.post(ORDER_URL, cart_item, format='json')
