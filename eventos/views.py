from django.shortcuts import render
from eventos.models import Evento
from datetime import datetime, timedelta

def home_eventos(request):
    # contagem de eventos por status
    quantidade_eventos = get_all_status()

    # pegar usuario atual
    current_user = request.user

    # pegar todos os eventos
    eventos = get_all_eventos()

    # pegar eventos amanha
    eventos_amanha = get_eventos_amanha()



    return render(request, 'eventos/home_eventos.html', {
        'eventos_amanha' : eventos_amanha,
        'eventos' : eventos,
        'current_user' : current_user,
        'quantidade_eventos' : quantidade_eventos,
        })


def get_all_status():
    eventos = get_all_eventos()
    quantidade_eventos = {
        "agendados" : eventos.filter(status='AGENDADO').count(),
        "em_progresso" : eventos.filter(status='EM PROGRESSO').count(),
        "concluidos" : eventos.filter(status='CONCLUIDO').count()

    }
    return quantidade_eventos

def get_all_eventos():
    # retorna uma query
    return Evento.objects.all()

def get_eventos_amanha():
    # Obtenha a data de amanhã
    data_amanha = (datetime.now() + timedelta(days=1)).date()

    # Filtrar os eventos de amanhã
    eventos_amanha = Evento.objects.filter(tempo__date=data_amanha)
    return eventos_amanha

"""
	colocar o card do evento dentro de um for
    botao de logout funcional
"""

"""
sample = Evento.objects.all()
sa = sample.first()
hoje = datetime.date.today()
print(type(hoje))
print(type(sa.tempo))

"""