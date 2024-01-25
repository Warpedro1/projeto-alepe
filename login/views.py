from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from login.forms import LoginForms


def index(request):
    form = LoginForms()

    if request.method=='POST':
        form = LoginForms(request.POST)

        if form.is_valid():
             
            nome=form['nome_login'].value()
            senha=form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                return redirect('login_concluido')
            else:
                return render(request, 'login/index.html', {'form': form})

    return render(request, 'login/index.html', {'form': form})

def login_concluido(request):
    return render(request, 'login/login_concluido.html')
