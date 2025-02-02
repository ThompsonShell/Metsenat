from rest_framework import serializers

from apps.users.models import UserModel


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        read_only_fields = ('id',)
