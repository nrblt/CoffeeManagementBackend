from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer
from .models import Category
from rest_framework.decorators import action

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
    # @action(methods=['get'], detail=False)
    # def product_categories(self, request):
