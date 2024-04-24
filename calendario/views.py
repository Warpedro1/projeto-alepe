from django.shortcuts import render
from setup.src import *

def calendario(request):
    usuario = get_user(request)
   
    return render(request, 'calendario/calendario.html', {
        'usuario' : usuario,
    })
