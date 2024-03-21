from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from eventos.models import Evento
from datetime import datetime, timedelta
from django.contrib.auth import logout
from login.views import index



def logout_view(request):
    logout(request)
    
    return render(request, 'eventos/home_eventos.html')

#@login_required(login_url='index.html')
def home_eventos(request):
    # contagem de eventos por status
    quantidade_eventos = {
        'hoje': get_all_status_hoje(),
        'total': get_all_status_total()
    }
    #get_all_status()
    # pegar usuario atual
    current_user = request.user

    # pegar todos os eventos
    eventos = get_all_eventos()

    eventos_hoje = get_eventos_hoje()
    for evento in eventos_hoje:
        evento.tempo = evento.tempo.strftime("%H:%M")

    # pegar eventos amanha
    eventos_amanha = get_eventos_amanha()

    # quantidade de eventos neste mes
    quantidade_eventos_mes_atual = get_eventos_mes_atual().count()

    string_dias_da_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]

    datas_em_string = {
        'dia_da_semana': string_dias_da_semana[datetime.now().date().weekday()],
        'hoje': datetime.now().date(),
        'amanha': string_dias_da_semana[(datetime.now() + timedelta(days=1)).date().weekday()]
    }

    datas_formatadas = {
        'hoje' : datetime.now().date().strftime("%d/%m"),
        'amanha' : (datetime.now() + timedelta(days=1)).date().strftime("%d/%m"),
    }


    return render(request, 'eventos/home_eventos.html', {
        'datas_em_string' : datas_em_string,
        'datas_formatadas' : datas_formatadas,
        'eventos_hoje': eventos_hoje,
        'eventos_amanha' : eventos_amanha,
        'eventos' : eventos,
        'current_user' : current_user,
        'quantidade_eventos' : quantidade_eventos,
        'quantidade_eventos_mes_atual' : quantidade_eventos_mes_atual,
        })


def get_all_status_total():
    eventos = get_all_eventos()
    quantidade_eventos = {
        "agendados" : eventos.filter(status='AGENDADO').count(),
        "em_progresso" : eventos.filter(status='EM PROGRESSO').count(),
        "concluidos" : eventos.filter(status='CONCLUIDO').count()

    }
    return quantidade_eventos

def get_all_status_hoje():
    eventos = get_eventos_hoje()
    quantidade_eventos = {
        "agendados" : eventos.filter(status='AGENDADO').count(),
        "em_progresso" : eventos.filter(status='EM PROGRESSO').count(),
        "concluidos" : eventos.filter(status='CONCLUIDO').count()

    }
    return quantidade_eventos

def get_all_eventos():
    # retorna uma query
    return Evento.objects.all()

def get_eventos_hoje():
    data_hoje = datetime.now().date()
    eventos_hoje = Evento.objects.filter(tempo__date=data_hoje).order_by('tempo')

    return eventos_hoje #querry

def get_eventos_amanha():
    # Obtenha a data de amanhã
    data_amanha = (datetime.now() + timedelta(days=1)).date()

    # Filtrar os eventos de amanhã
    eventos_amanha = Evento.objects.filter(tempo__date=data_amanha)
    return eventos_amanha

def get_eventos_mes_atual():
    # Obtém o mês atual
    mes_atual = datetime.now().month

    # Filtra os eventos que ocorrem no mês atual
    eventos_mes_atual = Evento.objects.filter(tempo__month=mes_atual)
    return eventos_mes_atual


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