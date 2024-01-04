from django.db import models
from django.core.validators import MinValueValidator


class UserModel(models.Model):
    """Таблица для хранения данных о пользователях"""

    _GENDER = [
        ('Man', "Man"),
        ('Woman', "Woman")
    ]

    name = models.CharField(max_length=255, null=False, blank=False)
    surname = models.CharField(max_length=255, null=False, blank=False)
    age = models.IntegerField(blank=False, null=False, validators=[MinValueValidator(18)])
    gender = models.CharField(max_length=5, choices=_GENDER, default="Man")
    phone_number = models.CharField(max_length=11, blank=True)
    blood_type = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return F"{self.surname} {self.name}"
