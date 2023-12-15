from django.db import models


class UserModel(models.Model):
    login = models.CharField(unique=True)
    tel_raqam = models.IntegerField(unique=True, max_length=13)
    password = models.CharField(max_length=32)
    ps_seriya = models.CharField(max_length=2)
    ps_seriya_raqam = models.IntegerField(unique=True)
    def __str__(self):
        return self.name






