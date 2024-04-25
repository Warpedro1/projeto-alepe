from datetime import datetime, timedelta

from eventos.models import Evento


def get_user(request):
    return request.user

def get_hoje():
    return datetime.now().date()

def get_amanha():
    return get_hoje() + timedelta(days=1)

def get_dias_da_semana():
    return {i: dia for i, dia in enumerate(
        ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    )}

def get_mes_atual():
    return get_meses()[get_hoje().month]

def get_meses():
    return {i+1: mes for i, mes in enumerate(
        ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    )}

def eventos():
    return {
        'status': { 
            'hoje': get_count(get_eventos_de_hoje(get_hoje())), 
            'amanha': get_count(get_eventos_de_amanha(get_amanha())), 
            'mensal': get_count(get_eventos_do_mes(get_hoje())), 
            'todos': get_count(get_eventos())
        },
        'hoje': get_eventos_de_hoje(get_hoje()), 
        'amanha': get_eventos_de_amanha(get_amanha()), 
        'mensal': get_eventos_do_mes(get_hoje()),
        'todos': get_eventos() 
    }

def datas():
    return {        
        'hoje': {
            'formatada': {
                'DM': get_hoje().strftime("%d/%m"), # 31/12
                'DMA':  get_hoje().strftime("%d/%m/%Y"), # 31/12/2023
                'string': get_hoje() # 31 de Dezembro de 2023
            },
            'dia': {
                'numerico': get_hoje().strftime("%d"), # 31
                'string': get_dias_da_semana()[get_hoje().weekday()] # Domingo
            }, 
            'mes': {
                'numerico': get_hoje().strftime("%m"), # 01
                'string': get_meses()[get_hoje().month] # Janeiro
            },
            'ano': get_hoje().strftime("%Y") # 2023
        },
        'amanha': {
            'formatada': {
                'DM': get_amanha().strftime("%d/%m"), # 01/01
                'DMA':  get_amanha().strftime("%d/%m/Y"), # 01/01/2024
                'string': get_amanha() # 1 de Janeiro de 2024
            },
            'dia': {
                'numerico': get_amanha().strftime("%d"), # 01
                'string': get_dias_da_semana()[get_amanha().weekday()] # Segunda-feira
            }, 
            'mes': {
                'numerico': get_amanha().strftime("%m"), # 01
                'string':  get_meses()[get_amanha().month] # Janeiro
            },
            'ano': get_amanha().strftime("%Y") # 2024
        }
    }

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


