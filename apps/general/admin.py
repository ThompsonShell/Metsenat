from django.contrib import admin

from apps.general.models import University, PaymentMethod


admin.site.register(University)
admin.site.register(PaymentMethod)