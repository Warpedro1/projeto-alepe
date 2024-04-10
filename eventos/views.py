from django.shortcuts import render
from eventos import admin
from eventos.models import Evento
from datetime import datetime, timedelta
from django.contrib.auth import logout

# from django.shortcuts import redirect
# from django.contrib.auth.decorators import login_required
# from login.views import index

# @login_required(login_url='index.html')

def home_eventos(request):
    # Variáveis
    dia_de_hoje = datetime.now().date()
    dia_de_amanha = (dia_de_hoje + timedelta(days=1))
    
    dias_da_semana = {i: dia for i, dia in enumerate(
        ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    )}

    meses = {i: mes for i, mes in enumerate(
        ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    )}

    usuario = request.user # Clayton Aguiar 

    eventos = {
        'status': { 
            'hoje': get_count(get_eventos_de_hoje(dia_de_hoje)), 
            'amanha': get_count(get_eventos_de_amanha(dia_de_amanha)), 
            'mensal': get_count(get_eventos_do_mes(dia_de_hoje)), 
            'todos': get_count(get_eventos())
        },
        'hoje': get_eventos_de_hoje(dia_de_hoje), 
        'amanha': get_eventos_de_amanha(dia_de_amanha), 
        'mensal': get_eventos_do_mes(dia_de_hoje), 
        'todos': get_eventos() 
    }

    datas = {        
        'hoje': {
            'formatada': {
                'DM': dia_de_hoje.strftime("%d/%m"), # 31/12
                'DMA':  dia_de_hoje.strftime("%d/%m/%Y"), # 31/12/2023
                'string': dia_de_hoje # 31 de Dezembro de 2023
            },
            'dia': {
                'numerico': dia_de_hoje.strftime("%d"), # 31
                'string': dias_da_semana[dia_de_hoje.weekday()] # Domingo
            }, 
            'mes': {
                'numerico': dia_de_hoje.strftime("%m"), # 01
                'string': meses[dia_de_hoje.month] # Janeiro
            },
            'ano': dia_de_hoje.strftime("%Y") # 2023
        },
        'amanha': {
            'formatada': {
                'DM': dia_de_amanha.strftime("%d/%m"), # 01/01
                'DMA':  dia_de_amanha.strftime("%d/%m/Y"), # 01/01/2024
                'string': dia_de_amanha # 1 de Janeiro de 2024
            },
            'dia': {
                'numerico': dia_de_amanha.strftime("%d"), # 01
                'string': dias_da_semana[dia_de_amanha.weekday()] # Segunda-feira
            }, 
            'mes': {
                'numerico': dia_de_amanha.strftime("%m"), # 01
                'string':  meses[dia_de_amanha.month] # Janeiro
            },
            'ano': dia_de_amanha.strftime("%Y") # 2024
        }
    }

    return render(request, 'eventos/home_eventos.html', {
        'usuario' : usuario,
        'eventos': eventos,
        'datas': datas
    })

def logout_view(request):
    logout(request)
    return render(request, 'eventos/home_eventos.html')

def admin_view(request):
    usuario = request.user # Clayton Aguiar

    if usuario.is_superuser:
        return render(request, 'admin/', admin.site.urls)

def get_eventos():
    return Evento.objects.all()

def get_eventos_de_hoje(dia):
    return formatar_horário(Evento.objects.filter(tempo__date=dia).order_by('tempo'))

def get_eventos_de_amanha(dia):
    return Evento.objects.filter(tempo__date=dia).order_by('tempo')

def get_eventos_do_mes(dia):
    return Evento.objects.filter(tempo__month=dia.month)

def get_count(eventos):
    tipo_do_status = {i: status for i, status in enumerate(
        ["AGENDADO", "EM PROGRESSO", "CONCLUIDO"]
    )}

    count = {
        'total': len(eventos),
        'agendados': sum(1 for evento in eventos if evento.status == tipo_do_status[0]),
        'em_progresso': sum(1 for evento in eventos if evento.status == tipo_do_status[1]),
        'concluidos': sum(1 for evento in eventos if evento.status == tipo_do_status[2])
    }

    return count

def formatar_horário(eventos):
    fuso_horario = timedelta(hours=-3)

    for evento in eventos:
        evento.tempo = (evento.tempo + fuso_horario).strftime("%H:%M")
    
    return eventos