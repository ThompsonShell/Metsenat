from django.core.validators import RegexValidator

def validate_phone_number(phone_number: str):
    RegexValidator(
        regex=r'^\+998\d{9}$',
        message="The phone must be 9 number and start with +998"
    )