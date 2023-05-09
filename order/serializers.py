from rest_framework import serializers
from .models import Order
from cart.serializers import  CartItemSerializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
class OrderWithItemsSerializer(serializers.ModelSerializer):
    item_set = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ("total_price", 'item_set')
