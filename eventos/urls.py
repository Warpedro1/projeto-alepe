from django.urls import path
from eventos.views import home_eventos

urlpatterns = [
    path('home_eventos', home_eventos, name='home_eventos')
]