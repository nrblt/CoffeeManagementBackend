from rest_framework import serializers
from .models import Category
from product.serializers import ProductSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("__all__")
class CategoryProductSerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = "name", "description", "product_set"
