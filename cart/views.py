from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.http import Http404
from rest_framework.exceptions import (ValidationError, NotAuthenticated)
from rest_framework import status
from django.http import HttpResponse, JsonResponse

from product.models import Product
from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartWithCartItemsSerializer, CartSerializer

class CartItemViewSet(ModelViewSet):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()
    model = CartItem

    def create(self, request):
        user = request.user.pk
        if  not user:
            raise NotAuthenticated("Not authenticated")

        cart = Cart.objects.get(user = user)
        request.data['cart'] = cart.pk
        # print(request.data)
        serializer = self.serializer_class( data=request.data)
        if serializer.is_valid():
            if serializer.data['count'] <= 0:
                raise ValidationError("Quantity must be greater than 0")
            if self.queryset.filter(product=serializer.data['product']).exists():
                cart_item = self.queryset.get(product = serializer.data['product'])
                
                cart.total_price -= cart_item.count * cart_item.product.price
                
                cart.total_price -= cart_item.count * cart_item.product.price
                cart_item.count = cart_item.count + serializer.data['count']
                cart_item.save()
                cart.total_price += cart_item.count * cart_item.product.price
                cart.save()
                return Response(serializer.data)
            
            cart_item = self.model.objects.create(cart = cart, order = None, product_id = serializer.data['product'], count = serializer.data['count'])
            cart_item.save()
            cart.total_price = cart.total_price + cart_item.product.price * cart_item.count
            cart.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartViewSet(ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    def list(self, request):
        user = request.user.pk
        print(user)
        if user:
            cart = Cart.objects.get(user=user)
            serializer = CartWithCartItemsSerializer(cart, many=False)

            return Response(serializer.data)
        else:
            raise NotAuthenticated("Not authenticated")
