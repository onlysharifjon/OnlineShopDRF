from django.urls import path, include

from .views import LoginUzum, Register
urlpatterns = [
    path('login/', LoginUzum.as_view()),
    path('register/', Register.as_view()),

]