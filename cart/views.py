from rest_framework.viewsets import ModelViewSet
from .models import CartItem
from .serializers import CartItemSerializer

class CartItemViewSet(ModelViewSet):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()
