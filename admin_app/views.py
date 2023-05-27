from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
import datetime
from staff.models import StaffAccount
from order.models import Order
from .serializers import PositionSerializer

User = get_user_model()

class AdminViewSet(ViewSet):
    # @action(detail=False, methods=['get'])
    def getPosition(self, request):
        serializer = PositionSerializer( data=request.data)
        serializer.is_valid()
        # return Response({'position': 'customer'})
        print(serializer.data)

        user = User.objects.get(username=serializer.data['username'])
        print(user)
        is_staff = StaffAccount.objects.get(user = user)
        if is_staff:
            return Response({'position': is_staff.position})
        else:
            return Response({'position': 'customer'})
    def todaysIncome(self, request):
        today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        orders = Order.objects.filter(created_at__range=(today_min, today_max))
        today_earning = int(0)
        for order in orders:
            today_earning += order.total_price
        context = {}
        context['today_earning'] = today_earning
        return Response(context)
