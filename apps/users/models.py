from django.contrib.admindocs.utils import ROLES
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import IntegerChoices
from django.template.defaultfilters import default

from apps.utils.models.base_model import AbstractBaseModel


class CustomUser(AbstractUser):
    class Role(IntegerChoices):
        ADMIN = 1
        STUDENT = 2
        SPONSOR = 3

    class UserType(IntegerChoices):
        JISMONIY = 1
        YURIDIK = 2

    # degree = models.
    photo = models.ImageField()
    is_staff = default(False)
    role = models.CharField(choices=Role, default=3)
    user_type = models.CharField(choices=UserType, default=1)
    balance = models.DecimalField(max_digits=10, decimal_places=5)
    university = models.ForeignKey('general.University', models.CASCADE)
    phone_number = models.CharField(max_length=13,  help_text="please enter only 13 number")


    # def clean(self):
    #     if not Role.ADMIN.is_staff == False:
    #         raise