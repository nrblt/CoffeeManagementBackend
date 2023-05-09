from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient
from category.models import Category
from .models import Product
from .serializers import ProductSerializer


PRODUCTS_URL = reverse('product:product-list')

def create_category(**params):
    defaults = {
        "name":"Coffee",
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

def detail_url(product_id):
    """Create and return a recipe detail URL."""
    return reverse('product:product-detail', args=[product_id])


class ProductAPITests(TestCase):

    def test_retrieve_products(self):
        """Test retrieving a list of recipes."""
        create_product()

        res = self.client.get(PRODUCTS_URL)

        products = Product.objects.all().order_by('-id')
        serializer = ProductSerializer(products, many=True)
        print(serializer.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_get_product_detail(self):
        """Test get recipe detail."""
        product = create_product()

        url = detail_url(product.id)
        res = self.client.get(url)

        serializer = ProductSerializer(product)
        self.assertEqual(res.data, serializer.data)

    def test_partial_update(self):
        product = create_product()

        payload = {'name': 'NoLatte'}
        url = detail_url(product.id)
        res = self.client.patch(url, payload)

        print(product.name)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        product.refresh_from_db()
        self.assertEqual(product.name, payload['name'])
