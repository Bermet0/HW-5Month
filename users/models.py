from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User


class ConfirmCode(models.Model):
    code = models.IntegerField(max_length=6)

