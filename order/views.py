from django.shortcuts import render
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from cart.models import Cart, CartItem
from cart.serializers import CartItemSerializer
from rest_framework.exceptions import (ValidationError, NotAuthenticated)
from rest_framework import status
from rest_framework.response import Response

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    model = Order

    def create(self, request):
        user = self.request.user
        if  not user:
            raise NotAuthenticated("Not authenticated")

        cart = Cart.objects.get(user=self.request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        order = self.model.objects.create(user = user, total_price = 0)
        order.total_price = cart.total_price
        cart.total_price = 0
        cart.save()
        for cart_item in cart_items:
            cart_item.cart = None 
            cart_item.order = order
            cart_item.save()
        order.save()
        serializer = self.serializer_class(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def list(self, request):
        user = request.user
        if not user:
            raise NotAuthenticated("Not authenticated")

        cart_items = CartItem.objects.filter(order__user = user)
        serilizer = CartItemSerializer(cart_items, many=True)
        return Response(serilizer.data)
