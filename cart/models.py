from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from product.models import Product


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()


@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
    print(sender)
    if created:
        Cart.objects.create(user = instance, total_price = 0)
