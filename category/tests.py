from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient
from .models import Category
from .serializers import CategorySerializer


CATEGORIES_URL = reverse('category:category-list')

def create_category(**params):
    defaults = {
        "name":"Coffee category",
        "description":"coffee category"
    }
    category = Category.objects.create(**defaults)
    return category


def detail_url(category_id):
    """Create and return a recipe detail URL."""
    return reverse('category:category-detail', args=[category_id])


class ProductAPITests(TestCase):

    def test_retrieve_category(self):
        """Test retrieving a list of recipes."""
        create_category()

        res = self.client.get(CATEGORIES_URL)

        products = Category.objects.all().order_by('-id')
        serializer = CategorySerializer(products, many=True)
        print(serializer.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
        
    def test_get_category_detail(self):
        """Test get recipe detail."""
        category = create_category()

        url = detail_url(category.id)
        res = self.client.get(url)

        serializer = CategorySerializer(category)
        self.assertEqual(res.data, serializer.data)

    def test_partial_update(self):
        category = create_category()

        payload = {'name': 'NoLatte'}
        url = detail_url(category.id)
        res = self.client.patch(url, payload)

        print(category.name)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        category.refresh_from_db()
        self.assertEqual(category.name, payload['name'])
