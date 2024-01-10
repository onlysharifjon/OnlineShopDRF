from django.urls import path

from .views import LoginUzum, Register, FiltrByCategory

urlpatterns = [
    path('login/', LoginUzum.as_view()),
    path('register/', Register.as_view()),
    path('filtr/', FiltrByCategory.as_view()),
]
