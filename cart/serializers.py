from rest_framework import serializers
from .models import Cart, CartItem


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ("__all__")

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ("__all__")

class CartWithCartItemsSerializer(serializers.ModelSerializer):
    cart_item_set = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = "user", "total_price", "cart_item_set"
