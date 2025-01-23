from django.db import models

from apps.utils.models.base_model import AbstractBaseModel


class StudentSponsor(models.Model, AbstractBaseModel):
    sponsor = models.ForeignKey('', on_delete=models.PROTECT)
    student = models.ForeignKey('', on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=5)