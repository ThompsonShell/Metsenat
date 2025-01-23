from django.db import models

from apps.utils.models.base_model import AbstractBaseModel


class University(models.Model, AbstractBaseModel):
    name = models.CharField(max_length=250)
    contract_amount = models.DecimalField(max_digits=10, decimal_places=5)

class PaymentMethod(models.Model, AbstractBaseModel):
    name = models.CharField(max_length=250)

