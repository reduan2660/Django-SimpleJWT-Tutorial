from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator

from .manager import UserManager

phone_validator = RegexValidator(r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$", "The phone number provided is invalid")

class zilla(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=16, unique=True, validators=[phone_validator])
    email = models.EmailField(blank=True)
    name = models.CharField(max_length=200, blank=True)

    SexChoices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    sex = models.CharField(max_length=10, choices=SexChoices, blank=True)
    address = models.CharField(max_length=400, blank=True)
    zilla = models.ForeignKey(zilla, on_delete=models.SET_NULL, null=True)

    active = models.BooleanField(default=True)
    verified = models.BooleanField(default=False)
    restricted = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []