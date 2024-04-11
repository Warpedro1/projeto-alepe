from django.urls import path
from calendario.views import calendario

urlpatterns = [
    path('', calendario, name="calendario")
    #trocar essa url para: calendario
]