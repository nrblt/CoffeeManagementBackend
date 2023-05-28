import json

from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.exceptions import NotAuthenticated, ValidationError
from rest_framework.response import Response

from cart.models import Cart, CartItem
from cart.serializers import CartItemSerializer

from .models import Order
from .serializers import OrderSerializer


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
        serializer = CartItemSerializer(cart_items, many=True)

        for ser in serializer.data:
            ser['created_date'] = self.queryset.get(pk=ser['order']).created_at
            ser['status'] = self.queryset.get(pk=ser['order']).status
            ser['total_price'] = ser['product_price'] * ser['count']
        print(serializer.data)
        
        return Response(sorted(serializer.data, key=lambda x: x["created_date"], reverse=True))
