from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from apps.sponsors.models import StudentSponsor


@receiver((post_save, post_delete), sender=StudentSponsor)
def post_save_post_delete_student_sponsor(instance: StudentSponsor, **kwargs):
    instance.sponsor.set_balance_available()
    instance.student.set_balance_available()