from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.users.models import UserModel


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('phone_number', 'first_name', 'last_name', 'user_type')

    def validate_phone_number(self, phone_number):
        if not phone_number:
            raise ValidationError('Phone number required')

        if phone_number and UserModel.objects.filter(phone_number=phone_number).exists():
            raise ValidationError('Phone number already exists')
        return phone_number

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)