from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


User = get_user_model()


class ResetPasswordConfirm(models.Model):
    username = models.CharField(max_length=100)
    code = models.CharField(max_length=6)


class LastVisit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_visit = models.DateTimeField(auto_now=True)

