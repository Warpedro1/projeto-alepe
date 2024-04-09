from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from eventos.models import Evento
from datetime import datetime, timedelta
from django.contrib.auth import logout
from login.views import index

dias_da_semana = {
    0: "Segunda",
    1: "Terça",
    2: "Quarta",
    3: "Quinta",
    4: "Sexta",
    5: "Sábado",
    6: "Domingo"
}

meses = {
    0: "Janeiro",
    1: "Fevereiro",
    2: "Março",
    3: "Abril",
    4: "Maio",
    5: "Junho",
    6: "Julho",
    7: "Agosto",
    8: "Setembro",
    9: "Outubro",
    10: "Novembro",
    11: "Dezembro",
}

# @login_required(login_url='index.html')
def home_eventos(request):
    dia_de_hoje = datetime.now().date()
    dia_de_amanha = (dia_de_hoje + timedelta(days=1))
    
    user = request.user # Clayton Aguiar 

    eventos = {
        'quantidade': {
            'status': {
                'total': get_all_status_total(),
                'hoje': get_all_status_hoje(dia_de_hoje)
            },
            'mensal': get_eventos_mes_atual(dia_de_hoje).count()
        },
        'total': get_all_eventos(),
        'hoje': get_eventos_hoje(dia_de_hoje),
        'amanha': get_eventos_amanha(dia_de_amanha)
    }

    data = {        
        'hoje': {
            'formatada': {
                'DM': dia_de_hoje.strftime("%d/%m"), # 31/01
                'DMA':  dia_de_hoje.strftime("%d/%m/%Y"), # 31/01/2023
                'string': dia_de_hoje # 31 de Janeiro de 2023
            },
            'dia': {
                'numerico': dia_de_hoje.strftime("%d"), # 31
                'string': dias_da_semana[dia_de_hoje.weekday()] # Terça
            }, 
            'mes': {
                'numerico': dia_de_hoje.strftime("%m"), # 01
                'string': meses[dia_de_hoje.month] # Janeiro
            },
            'ano': dia_de_hoje.strftime("%Y") # 2023
        },
        'amanha': {
            'formatada': {
                'DM': dia_de_amanha.strftime("%d/%m"), # 01/02
                'DMA':  dia_de_amanha.strftime("%d/%m/Y"), # 01/02/2023
                'string': dia_de_amanha # 1 de Fevereiro de 2023 
            },
            'dia': {
                'numerico': dia_de_amanha.strftime("%d"), # 01
                'string': dias_da_semana[dia_de_amanha.weekday()] # Quarta
            }, 
            'mes': {
                'numerico': dia_de_amanha.strftime("%m"), # 02
                'string':  meses[dia_de_amanha.month] # Fevereiro
            },
            'ano': dia_de_amanha.strftime("%Y") # 2023
        }
    }

    return render(request, 'eventos/home_eventos.html', {
        'user' : user,
        'eventos': eventos,
        'data': data
    })

def get_all_eventos():
    return Evento.objects.all()

def get_eventos_hoje(dia):
    eventos = Evento.objects.filter(tempo__date=dia).order_by('tempo')

    for evento in eventos:
        evento.tempo = evento.tempo.strftime("%H:%M")

    return eventos

def get_eventos_amanha(dia):
    return Evento.objects.filter(tempo__date=dia)

def get_all_status_hoje(dia):
    return status_count(get_eventos_hoje(dia))

def get_all_status_total():
    return status_count(get_all_eventos())

def status_count(eventos):
    status = {
        'agendados': sum(1 for evento in eventos if evento.status == 'AGENDADO'),
        'em_progresso': sum(1 for evento in eventos if evento.status == 'EM PROGRESSO'),
        'concluidos': sum(1 for evento in eventos if evento.status == 'CONCLUIDO')
    }

    return status

def get_eventos_mes_atual(dia):
    return Evento.objects.filter(tempo__month=dia.month)
    
def logout_view(request):
    logout(request)
    return render(request, 'eventos/home_eventos.html')