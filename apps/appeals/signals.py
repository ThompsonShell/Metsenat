from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from apps.appeals.models import Appeal


@receiver((post_save, post_delete), sender=Appeal)
def post_save_post_delete_appeal(instance: Appeal, **kwargs):
    # ======== set related sponsor balance and available ==============
    sponsor = instance.sponsor
    sponsor.set_balance_available()
    sponsor.save()
