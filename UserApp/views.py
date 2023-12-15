from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import authenticate
from .serializers import ForLoginSerializer
from drf_yasg.utils import swagger_auto_schema
import jwt


class LoginUser(APIView):
    serializer_class = ForLoginSerializer

    @swagger_auto_schema(request_body=ForLoginSerializer)
    def post(self, request):
        seriya = request.data.get('ps_seriya')
        seriya_raqam = request.data.get('ps_seriya_raqam')
        password = request.data.get('password')
        user = UserModel.objects.filter(ps_seriya=seriya, ps_seriya_raqam=seriya_raqam, password=password).first()
        return Response({"Login Success": user.id})


class Register(APIView):
    serializer_class = ForLoginSerializer

    @swagger_auto_schema(request_body=ForLoginSerializer)
    def post(self, request):
        serializer = ForLoginSerializer(data=request.data)
        if serializer.is_valid():
            seriya = request.data.get('ps_seriya')
            seriya_raqam = request.data.get('ps_seriya_raqam')
            password = request.data.get('password')
            login = request.data.get('login')
            tel_raqam = request.data.get('tel_raqam')
            crt = UserModel.objects.create(tel_raqam=tel_raqam, login=login, password=password,
                                           ps_seriya_raqam=seriya_raqam, ps_seriya=seriya)
            user = UserModel.objects.filter(ps_seriya=seriya, ps_seriya_raqam=seriya_raqam, password=password).first()
            if user:
                access_token = AccessToken.for_user(user)
                refresh_token = RefreshToken(user)
                return Response({"Register Access": str(access_token),
                                 })
            else:
                return Response({"error": "User not found with provided credentials"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)