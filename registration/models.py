from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Interest(models.Model):
    description = models.CharField(max_length=96)

    def __str__(self):
        return self.description


class CustomUser(AbstractUser):
    interest = models.ForeignKey(
        Interest,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    years = models.PositiveBigIntegerField(
        null=True,
        blank=True
    )
