from django.db import models
from django.db.models.base import Model


class Register(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=200)
    number = models.IntegerField()
    city = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'registers'
