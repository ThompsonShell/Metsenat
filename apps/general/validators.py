from django.core.validators import RegexValidator

validate_phone_number = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="The phone must be 9 numbers and start with +998"
)