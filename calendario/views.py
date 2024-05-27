from django.shortcuts import render
from setup.src import *
from collections import defaultdict

def calendario(request):    
    return render(request, 'pages/calendario.html', {
        'eventos_mes': agrupar_eventos_mes_atual_por_dia(),
        'mes_atual': get_mes_atual(),
        'usuario' : get_user(request),
        'datas' : datas(),
        'novo_eventos_mes': month_by_week()
    })

def month_by_week():
    month_by_week = defaultdict(dict)

    this_month_events = get_eventos_do_mes(get_hoje())

    for event in this_month_events:
        week_start = get_week_start(event.tempo)
        week_key = week_start.strftime('%d/%m/%Y')
        event_date = event.tempo.strftime('%d/%m/%Y')
        local_time = event.tempo - timedelta(hours=3)
        
        month_by_week[week_key][event_date] = {
            'nome': event.nome,
            'lugar': event.lugar,
            'tempo': event.tempo,
            'inicio': int(local_time.hour),
            'dia': get_dias_da_semana()[event.tempo.date().weekday()]
        }

    month_by_week = dict(month_by_week)

    print(month_by_week)

    return month_by_week














def agrupar_eventos_mes_atual_por_dia():
    eventos_por_data = defaultdict(list)

    for evento in Evento.objects.filter(tempo__month=get_hoje().month, tempo__year=get_hoje().year):
        data = evento.tempo.strftime('%d/%m/%Y')
        eventos_por_data[data].append({
            'nome': evento.nome,
            'solicitante': evento.solicitante,
            'tempo': evento.tempo,
            'lugar': evento.lugar,
            'descricao': evento.descricao,
            'status': evento.status
        })

    eventos_por_data = dict(eventos_por_data)
    return eventos_por_data
