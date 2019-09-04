from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="full name")
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    birth_date = models.DateField()
