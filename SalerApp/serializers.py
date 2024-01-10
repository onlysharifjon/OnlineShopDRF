from rest_framework import serializers
from .models import SalerRegister, ProductModel


class ForLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalerRegister
        fields = '__all__'


class SenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"


class FilterByCategorySerializer(serializers.Serializer):
    katalog = serializers.CharField(max_length=255)
