from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.exceptions import (ValidationError, NotAuthenticated)
from django.utils import timezone

User = get_user_model()

class Order(models.Model):
    class OrderStatus(models.TextChoices):
        PAID = "PAID"
        DONE = "DONE"

    total_price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices= OrderStatus.choices, default=OrderStatus.PAID)
