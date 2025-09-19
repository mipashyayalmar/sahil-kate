from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=50, default='Default')
    phone  = models.CharField(max_length=20, default='8888888888')
    paid_member = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    