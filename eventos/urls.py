from django.urls import path
from eventos.views import home_eventos
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('home_eventos', home_eventos, name='home_eventos'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]