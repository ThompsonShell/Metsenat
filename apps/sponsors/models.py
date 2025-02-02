from django.conf import settings
from django.db import models
from rest_framework.exceptions import ValidationError

from apps.users.models import UserModel
from apps.utils.models.base_model import AbstractBaseModel


class StudentSponsor(AbstractBaseModel):
    sponsor = models.ForeignKey( 
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='sponsor',
        limit_choices_to={'available__gt': 0,
                          'role': UserModel.Role.SPONSOR}
                          )

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='student',)
    amount = models.DecimalField(max_digits =10, decimal_places=5)

    def clean(self):
        if self.amount > self.sponsor.available:
            raise ValidationError({'amount': "amount must be greater than sponsor available"})
        if self.amount > self.student.university.contract_amount - self.student.balance:
            raise ValidationError({'amount':"amount must be greater than student contrat amount"})
        


    def __str__(self):
        return f'sponsor{self.sponsor_id} student:{self.student_id}'