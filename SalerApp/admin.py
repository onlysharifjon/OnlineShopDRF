
from django.contrib import admin
from .models import *

admin.site.site_header = "Uzum Admin"
admin.site.register(SalerRegister)
# Register your models here.
