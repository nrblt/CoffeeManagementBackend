from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartWithCartItemsSerializer, CartSerializer

class CartItemViewSet(ModelViewSet):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

class CartViewSet(ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    @action(methods=['get'], detail=True)
    def cart_with_items(self, request, pk=None):
        cart = Cart.objects.get(pk=pk)
        serializer = CartWithCartItemsSerializer(cart, many=False)
        return Response(serializer.data)
