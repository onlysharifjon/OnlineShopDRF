from django.shortcuts import render
from rest_framework.views import APIView

from .paginations import LargeContentPaginate
from .serializers import ForLoginSerializer
from drf_yasg.utils import swagger_auto_schema
from .models import SalerRegister, ProductModel
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from .serializers import FilterByCategorySerializer, SenderSerializer


# Create your views here.
class Register(APIView):
    serializer_class = ForLoginSerializer

    @swagger_auto_schema(request_body=ForLoginSerializer)
    def post(self, request):
        serializer = ForLoginSerializer(data=request.data)
        if serializer.is_valid():
            login = request.data.get('login')
            password = request.data.get('password')
            seriya = request.data.get('PS_seria')
            seriya_num = request.data.get('PS_serial_num')
            phone = request.data.get('phone')
            crt = SalerRegister.objects.create(login=login, phone=phone, password=password,
                                               PS_serial_num=seriya_num, PS_seria=seriya)
            user = SalerRegister.objects.filter(PS_seria=seriya, PS_serial_num=seriya_num, password=password).first()
            if user:
                acsess_token = AccessToken.for_user(user)
                refresh_token = RefreshToken(user)
                # serializer.save()  # Save the serializer after creating the user
                return Response({"Register Success": str(acsess_token),
                                 })
            else:
                return Response({"error": "User not found with provided credentials"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUzum(APIView):
    serializer_class = ForLoginSerializer

    @swagger_auto_schema(request_body=ForLoginSerializer)
    def post(self, request):
        login = request.data.get('login')
        password = request.data.get('password')
        user = SalerRegister.objects.filter(login=login, password=password).first()
        return Response({"Login Success": user.id})


class FiltrByCategory(APIView):
    serializer_class = FilterByCategorySerializer
    queryset = ProductModel.objects.all()
    pagination_class = LargeContentPaginate
    @swagger_auto_schema(request_body=FilterByCategorySerializer)
    def post(self, request):
        katalog = request.data.get('katalog')
        filtr = ProductModel.objects.all().filter(katalog=katalog)
        serializer = SenderSerializer(filtr, many=True)
        if serializer:
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
