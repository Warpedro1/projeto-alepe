from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from login.forms import LoginForms


def login(request):
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
                #messages.success(request, f'{nome} logado com sucesso!')
                if 'manter-conectado' in request.POST:
                    request.session.set_expiry(9999999)
                    return redirect('home_eventos')
                else:
                    request.session.set_expiry(0)  # desloga quando fechar browser
                    return redirect('home_eventos')
            else:
                messages.error(request, 'Usuário ou senha incorretos.')
                return render(request, 'pages/login.html', {'form': form})

    return render(request, 'pages/login.html', {'form': form})