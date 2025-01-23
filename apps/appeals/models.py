from django.db import models

from apps.utils.models.base_model import AbstractBaseModel


class Appeal(models.Model, AbstractBaseModel):
    phone_number = models.CharField(max_length=34, help_text="please enter only 13 number")
    amount = models.DecimalField(max_digits=10, decimal_places=5)
    # available = models
    is_verified = models.BooleanField(default=True)
    sponsor = models.ForeignKey('', on_delete=models.PROTECT)
    payment_method = models.ForeignKey('general.PaymentMethod', on_delete=models.PROTECT)