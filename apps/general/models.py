from django.db import models
from django.core.validators import MinValueValidator

from apps.utils.models.base_model import AbstractBaseModel


class University(models.Model, AbstractBaseModel):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    contract_amount = models.DecimalField(max_digits=50, decimal_places=5, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name

class PaymentMethod(models.Model, AbstractBaseModel):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.name