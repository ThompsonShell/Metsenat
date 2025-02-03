from rest_framework import serializers
from apps.appeals.models import Appeal


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = '__all__'
        read_only_fields = ('id',)
