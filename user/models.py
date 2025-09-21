from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    paid_member = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=True)  # Set to True by default