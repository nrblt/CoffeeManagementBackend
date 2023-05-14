from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth import authenticate, get_user_model

from order.models import Order
from product.models import Product

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()

    @property
    def get_product_name(self):
        return "product_name"


@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
    print(sender)
    if created:
        Cart.objects.create(user = instance, total_price = 0)

@receiver(pre_delete, sender=CartItem)
def minus_total_price(sender, instance, **kwargs):
    print(sender)
    cart = instance.cart
    cart.total_price = cart.total_price - instance.count * instance.product.price
    cart.save()
