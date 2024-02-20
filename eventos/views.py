from django.shortcuts import render
from eventos.models import Evento

def home_eventos(request):
    
    eventos = Evento.objects.all()

    return render(request, 'eventos/home_eventos.html', {'eventos' : eventos})

