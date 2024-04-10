from django.urls import path
from calendario.views import calendario

urlpatterns = [
    path('calendario', calendario, name="calendario")
]