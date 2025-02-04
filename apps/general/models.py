from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify
from rest_framework.exceptions import ValidationError

from apps.utils.models.base_model import AbstractBaseModel


class University(AbstractBaseModel):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    contract_amount = models.DecimalField(max_digits=50, decimal_places=5, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name

    def clean(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if University.objects.filter(slug=self.slug).exists():
            raise ValidationError("This University already exists")

        old_contract = University.objects.get(pk=self.pk)
        if self.contract_amount != old_contract.contract_amount:
            raise ValidationError("You can't change the amount of your contract.")


class PaymentMethod(AbstractBaseModel):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, editable=False)

    def clean(self):
        self.slug = slugify(self.name)
        if PaymentMethod.objects.filter(slug=self.slug).exists():
            raise ValidationError("This Payment Method already exists")

    def __str__(self):
        return self.name