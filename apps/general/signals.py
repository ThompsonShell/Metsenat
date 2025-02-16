from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from apps.general.models import University
from apps.users.models import UserModel


@receiver((post_save, post_delete), sender=University)
def post_save_post_delete_appeal(instance: University, **kwargs):
    # ======== set related student balance and available ==============
    students = UserModel.objects.filter(role=UserModel.Role.STUDENT)

    for student in students:
        student.set_balance_available()

    UserModel.objects.bulk_update(students, fields=['balance', 'available'])
