from django.contrib import admin
from .models import SalerRegister, ProductModel, CategoryPartModel, ProductPartModel

admin.site.site_header = "Uzum Admin"

admin.site.register(ProductModel, list_display=['katalog', 'kategoriya'])

admin.site.register(CategoryPartModel, list_display=['category_name', 'sub_category'])

admin.site.register(ProductPartModel)

# Register your models here.
