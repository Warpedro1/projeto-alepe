from django.shortcuts import render
from eventos.models import Evento

def home_eventos(request):
    # contagem de eventos por status
    quantidade_eventos = get_all_status()

    # pegar usuario atual
    current_user = request.user




    return render(request, 'eventos/home_eventos.html', {
        #'evento' : evento,
        'current_user' : current_user,
        'quantidade_eventos' : quantidade_eventos,
        })


def get_all_status():
    eventos = Evento.objects.all()
    quantidade_eventos = {
        "agendados" : eventos.filter(status='AGENDADO').count(),
        "em_progresso" : eventos.filter(status='EM PROGRESSO').count(),
        "concluidos" : eventos.filter(status='CONCLUIDO').count()

    }
    return quantidade_eventos


"""
	colocar o card do evento dentro de um for
    botao de logout funcional
"""

