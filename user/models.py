from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    class Meta:
        db_table = "User"

    # username = models.CharField(max_length=20, null=False)
    # password = models.CharField(max_length=256, null=False)
    bio = models.CharField(max_length=256, default='')
    phone_numbers = models.IntegerField(max_length=256, null=False)
    adress = models.CharField(max_length=256, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


