import random
from django.core.cache import cache

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.general.validators import validate_phone_number


# from apps.users.models import UserModel

# class UserRegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserModel
#         fields = ('phone_number', 'first_name', 'last_name', 'user_type')

#     def validate_phone_number(self, phone_number):
#         if not phone_number:
#             raise ValidationError('Phone number required')

#         if phone_number and UserModel.objects.filter(phone_number=phone_number).exists():
#             raise ValidationError('Phone number already exists')
#         return phone_number

#     def create(self, validated_data):
#         return UserModel.objects.create_user(**validated_data)

def send_message(phone_number: str, message: str):
    """ send message to phone number """

    print(f"Message: {message} sent to {phone_number}")
    return "ok"


class SendAuthCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        max_length=13,
        min_length=13,
        required=True,
        allow_null=False,
        validators=[validate_phone_number],
        trim_whitespace=True,
        help_text="please enter only 13 number"
    )

    def validate_phone_number(self, phone_number):
        if not phone_number:
            raise ValidationError('Phone number required')
        return phone_number

    def save(self, *args, **kwargs):
        phone_number = self.validated_data['phone_number']
        auth_code = random.randint(1000, 9999)
        send_message(phone_number=phone_number, message="Your code is {auth_code}")
        cache.set(phone_number, auth_code, 10 * 60)


class AuthCodeConfirmSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        max_length=13,
        min_length=13,
        required=True,
        allow_null=False,
        validators=[validate_phone_number],
        trim_whitespace=True,
        help_text="please enter only 13 number"
    )
    auth_code = serializers.CharField(
        max_length=4,
        min_length=4,
        required=True,
        allow_null=False,
        trim_whitespace=True,
        help_text="please enter only 4 number"
    )

    def validate(self, data):
        phone_number = data.get('phone_number')
        auth_code = data.get('auth_code')

        if not phone_number:
            raise ValidationError('Phone number required')
        if not auth_code:
            raise ValidationError('Auth code required')

        if cache.get(phone_number) != auth_code:
            raise ValidationError('Invalid auth code')

        return data