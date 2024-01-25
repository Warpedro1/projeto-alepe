from django.urls import path
from login.views import index, login_concluido

urlpatterns = [
    path('', index),
    path('login_concluido', login_concluido, name='login_concluido')
]