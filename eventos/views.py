from django.shortcuts import render
from eventos.models import Evento

def home_eventos(request):
    eventos = Evento.objects.all()

    # contagem de eventos por status
    quantidade_agendados = eventos.filter(status='AGENDADO').count()
    quantidade_em_progresso = eventos.filter(status='EM PROGRESSO').count()
    quantidade_concluidos = eventos.filter(status='CONCLUIDO').count()

    return render(request, 'eventos/home_eventos.html', {
        #'evento' : evento,
        'quantidade_agendados': quantidade_agendados,
        'quantidade_em_progresso': quantidade_em_progresso,
        'quantidade_concluidos': quantidade_concluidos,
        })

"""
	colocar o card do evento dentro de um for
"""

