from django.shortcuts import render
from eventos import admin
from django.contrib.auth.decorators import login_required
from setup.src import *

@login_required(login_url='/login')
def home_eventos(request):
    return render(request, 'pages/home_eventos.html', {
        'usuario' : get_user(request),
        'eventos': eventos(),
        'datas': datas()
    })

def admin_view(request):
    if get_user(request).is_superuser:
        return render(request, 'admin/', admin.site.urls)
