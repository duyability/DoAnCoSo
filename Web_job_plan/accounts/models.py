from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager
from vlance.models import ThanhPho

GENDER_CHOICES = (
    ('male', 'Nam'),
    ('female', 'Nữ'))


class User(AbstractUser):
    username = None
    role = models.CharField(max_length=12, error_messages={
        'required': "Role must be provided"
    })
    gender = models.CharField(max_length=10, blank=True, null=True, default="")
    hotline = models.CharField(max_length=15,null=False,default='')
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "Email của bạn đã tồn tại.",
                              })

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManager()
