from django.db import models
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


#0 - admin of coffee
#1 - barista
#2 - waiter

class StaffAccount(models.Model):
    class Position(models.TextChoices):
        ADMIN = "ADMIN"
        BARISTA = "BARISTA"
        WAITER = "WAITER"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(choices= Position.choices, default=Position.WAITER)
