from django.shortcuts import render
from setup.src import *
from collections import defaultdict

def calendario(request):
    return render(request, 'calendario/calendario.html', {
        'eventos_mes': agrupar_eventos_mes_atual_por_dia(),
        'mes_atual': get_mes_atual(),
        'usuario' : get_user(request),
    })

def agrupar_eventos_mes_atual_por_dia():
    eventos = Evento.objects.filter(tempo__month=get_hoje().month)
    eventos_por_data = defaultdict(list)

    for evento in eventos:
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
