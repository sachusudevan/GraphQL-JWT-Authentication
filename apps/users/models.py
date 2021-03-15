from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(blank=False, max_length=255, verbose_name="email")

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    IS_STATUS_FIELD = 'is_staff'
    IS_SUPERUSER_FIELD = 'is_superuser'
    IS_ACTIVE_FIELD = 'is_active'