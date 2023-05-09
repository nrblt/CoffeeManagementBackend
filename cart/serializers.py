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
        fields = ["cart", 'order', 'product', 'count', 'product_name', 'product_price']
        extra_kwargs = {'cart': {'required': 'False'}}
    def get_product_name(self, obj):
        # return obj.product['name']
        # return obj.product
        # print(obj['product'].name)
        if type(obj) == OrderedDict:
            # print(obj['product'].name)
            name = obj['product'].name
            return name
        return obj.product.name
        # return obj['product'].name
    
    def get_product_price(self, obj):
        if type(obj) == OrderedDict:
            return obj['product'].price
        return obj.product.price
# cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     count = models.IntegerField()
class CartWithCartItemsSerializer(serializers.ModelSerializer):
    cartitem_set = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = "pk", "user", "total_price", "cartitem_set"

    # def insert_items(self, cart_items, cart):
    #     items = CartItem.objects.filter(cart=cart)
    #     for item in items:
    #         cart_items.add(item)
            