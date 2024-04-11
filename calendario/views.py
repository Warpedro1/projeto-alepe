from django.shortcuts import render

def calendario(request):
    usuario = request.user
    return render(request, 'calendario/calendario.html', {
        'usuario' : usuario,
    })
