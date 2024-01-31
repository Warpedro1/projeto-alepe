from django.urls import path
from login.views import index, home_eventos

urlpatterns = [
    path('', index),
    path('home_eventos', home_eventos, name='home_eventos')
]