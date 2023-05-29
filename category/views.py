from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import NotAuthenticated, ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from staff.models import StaffAccount

from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    """Category viewset"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def create(self, request):
        user = request.user.id
        if not user:
            raise NotAuthenticated("Not authenticated")
        
        if "ADMIN" != (get_object_or_404(StaffAccount, user=user)).position:
            raise ValidationError("Not admin account")
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
