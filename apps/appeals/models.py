from django.db import models
from django.conf import settings
from django.db.models import IntegerChoices

from apps.users import UserModel 
from apps.utils.models.base_model import AbstractBaseModel
from apps.general.validators import validate_phone_number

class Status(IntegerChoices):
    YANGI = ('yangi', 1)
    MODERATSIYA = ('moderatsiya', 2)
    TASDIQLANGAN = ('tasdiqlangan', 3)
    BEKOR_QILINGAN = ('bekor qilingan', 4)



class Appeal(models.Model, AbstractBaseModel):
    phone_number = models.CharField(max_length=34, help_text="please enter only 13 number", validators=[validate_phone_number])
    amount = models.DecimalField(max_digits=50, decimal_places=5, default=1)
    available = models.DecimalField(max_digits=50, decimal_places=5, default=1)
    status = models.IntegerField(choices=Status, default=2)
    sponsor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, limit_choices_to={"role": UserModel.Role.SPONSOR})
    payment_method = models.ForeignKey('general.PaymentMethod', on_delete=models.PROTECT)