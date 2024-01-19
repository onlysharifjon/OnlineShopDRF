from django.db import models


class SalerRegister(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    PS_serial_num = models.IntegerField(unique=True)
    PS_seria = models.CharField(max_length=2)
    phone = models.IntegerField(unique=True)

    def __str__(self):
        return self.login


class ProductModel(models.Model):
    choise_katalog = (
        ("Muddatli To'lov", "Muddatli To'lov"),
        ("Yangi yil sovg'alari", "Yangi yil sovg'alari"),
        ("Elektronika", "Elektronika"),
        ("Maishiy Texnika", "Maishiy Texnika"),
        ("Kiyim", "Kiyim"),
        ("Poyabzallar", "Poyabzallar"),
        ("Aksessuarlar", "Aksessuarlar"),
        ("Go'zallik va Parvarish", "Go'zallik va Parvarish"),
        ("Salomatlik", "Salomatlik"),
        ("Uy-ro'zg'or buyumlari", "Uy-ro'zg'or buyumlari"),
        ("Qurilish va Ta'mirlash", "Qurilish va Ta'mirlash"),
        ("Avtotovarlar", "Avtotovarlar"),
        ("Bolalar tovarlari", "Bolalar tovarlari"),
        ("Xobbi va ijod", "Xobbi va ijod"),
        ("Sport va Xordiq", "Sport va Xordiq"),
        ("Oziq-Ovqat mahsulotlari", "Oziq-Ovqat mahsulotlari"),
        ("Maishiy kimyoviy moddalar", "Maishiy kimyoviy moddalar"),
        ("Kanselariya tovarlari", "Kanselariya tovarlari"),
        ("Hayvonlar uchun tovarlar", "Hayvonlar uchun tovarlar"),
        ("Kitoblar", "Kitoblar"),
        ("Dacha, Bog' va tomorqa", "Dacha, Bog' va tomorqa")
    )
    katalog = models.CharField(choices=choise_katalog, max_length=255)
    kategoriya = models.CharField(max_length=255)

    def __str__(self):
        return self.kategoriya


class CategoryPartModel(models.Model):
    category_name = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=255, primary_key=True, unique=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.sub_category)




class ProductPartModel(models.Model):
    product_name = models.CharField(max_length=255)
    last_category = models.ForeignKey(CategoryPartModel, on_delete=models.CASCADE)

    product_price = models.IntegerField()
    product_image1 = models.ImageField(upload_to='images/', null=True, blank=True)
    product_image2 = models.ImageField(upload_to='images/', null=True, blank=True)
    product_image3 = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.product_name
