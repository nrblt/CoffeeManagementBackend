from rest_framework import serializers
from .models import Cart, CartItem
from collections import OrderedDict

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ("__all__")

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    product_price = serializers.SerializerMethodField()
    # product_name = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id',"cart", 'order', 'product', 'count', 'product_name', 'product_price']
        extra_kwargs = {'cart': {'required': 'False'}}
    def get_product_name(self, obj):

        if type(obj) == OrderedDict:
            name = obj['product'].name
            return name
        return obj.product.name
    
    def get_product_price(self, obj):
        if type(obj) == OrderedDict:
            return obj['product'].price
        return obj.product.price

class CartWithCartItemsSerializer(serializers.ModelSerializer):
    cartitem_set = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = "pk", "user", "total_price", "cartitem_set"
