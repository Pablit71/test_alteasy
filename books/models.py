from django.core.validators import MaxValueValidator
from django.db import models


class Profile(models.Model):
    column_name = models.CharField(max_length=30, unique=True)
    is_visible = models.BooleanField(default=True)


class Book(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=30, blank=True)
    author = models.CharField(max_length=30)
    description = models.CharField(max_length=512, blank=True)
    price = models.IntegerField(validators=[MaxValueValidator(99999)])
