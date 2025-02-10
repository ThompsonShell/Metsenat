from django.db import models
from django.db.models import IntegerChoices
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from datetime import timedelta

from apps.general.validators import validate_phone_number


class UserManager(BaseUserManager):

    def create_user(self, phone_number, email=None, password=None, **extra_fields):
            if not phone_number:
                raise ValueError("The phone number is require")
            extra_fields.setdefault("is_staff", False)
            extra_fields.setdefault("is_superuser", False)
            user = self.model(phone_number=phone_number, **extra_fields)
            if password:
                user.set_password(password)
            user.save(using=self._db)
            return user

    def create_superuser(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        user = self.create_user(phone_number, email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    class Role(IntegerChoices):
        ADMIN = (1, "admin")
        STUDENT = (2, "student")
        SPONSOR = (3, "sponsor")

    class UserType(IntegerChoices):
        PERSONAL = 1
        LEGAL = 2
        EMPTY = 3


    class StudentDegree(IntegerChoices):
        BACHELOR = 1
        MASTERS = 2
        EMPTY = 3


    username = None
    photo = models.ImageField(upload_to="users/%Y/%m/%d", blank=True, null=True)
    degree = models.IntegerField(choices=StudentDegree, default=3)
    role = models.IntegerField(choices=Role, default=3)
    user_type = models.IntegerField(choices=UserType, default=3)
    balance = models.DecimalField(max_digits=50, decimal_places=5, default=1, validators=[MinValueValidator(1)])
    available = models.DecimalField(max_digits=50, decimal_places=5, default=1, validators=[MinValueValidator(1)])
    last_updated = models.DateTimeField(auto_now=True)
    university = models.ForeignKey('general.University', on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=13,  help_text="please enter only 13 number", validators=[validate_phone_number], unique=True)
    date_joined = models.DateTimeField(default=now)

    objects = UserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        if self.role == self.Role.STUDENT and self.balance is None:
            self.balance = self.university.contract_amount
        super().save(*args, **kwargs)

    def clean(self):
        if self.role == self.Role.STUDENT and self.degree not in [self.StudentDegree.BACHELOR, self.StudentDegree.MASTERS]:
            raise ValidationError({"degree": "Student must be 1 {BACHELOR} or 2 {MASTERS}"})

        if self.role == self.Role.STUDENT and not self.university:
                raise ValidationError({"university": "this field must not be blank"})

        if self.role == self.Role.STUDENT:
            if self.last_updated and now() - self.last_updated > timedelta(days=2) and (
                    self.available is not None and self.available > 0):
                raise ValidationError({"available": "The sponsor's balance must not remain 0 for more than 2 days."})


UserModel = CustomUser


# CustomUser = UserManager



    # def clean(self):
    #     if not Role.ADMIN.is_staff == False:
    #         raise