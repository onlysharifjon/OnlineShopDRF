from django.db import models

# Create your models here.



class SalerRegister(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    PS_serial_num = models.IntegerField(unique=True)
    PS_seria = models.CharField(max_length=2)
    phone = models.IntegerField(unique=True)

    def __str__(self):
        return self.login