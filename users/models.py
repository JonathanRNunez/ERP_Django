from random import choice

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Role(models.Model):
    PERMISSION_CHOICES = [
        (0, 'No access'),
        (1, 'View only'),
        (2, 'Create and modify'),
    ]

    role_name = models.CharField(max_length=50, primary_key=True)
    custormers = models.IntegerField(choices = PERMISSION_CHOICES,defatult=0)
    suppliers = models.IntegerField(choices = PERMISSION_CHOICES,defatult=0)
    materials = models.IntegerField(choices = PERMISSION_CHOICES,defatult=0)
    purchases = models.IntegerField(choices = PERMISSION_CHOICES,defatult=0)
    sales = models.IntegerField(choices = PERMISSION_CHOICES,defatult=0)
    inventory = models.IntegerField(choices = PERMISSION_CHOICES,defatult=0)
    accounting = models.IntegerField(choices = PERMISSION_CHOICES,defatult=0)
    customers = models.IntegerField(choices = PERMISSION_CHOICES,defatult=0)
    reporting = models.IntegerField(choices = PERMISSION_CHOICES,defatult=0)

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.role_name
